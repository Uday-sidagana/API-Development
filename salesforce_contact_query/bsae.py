from abc import ABC
from typing import Any, ClassVar

from composio_langchain import Action
from pydantic import BaseModel, ConfigDict

from artifact.base_artifact import BasePatternToolArtifact
from tools.base_pattern_tool import BasePatternTool
from tools.composio_utils import get_composio_tool, execute_composio_tool
from tools.tool_model import AIMessage, BasePatternToolMessage


def allow_extra_fields(schema_cls: type[BaseModel]) -> type[BaseModel]:
    """Dynamically create a subclass of a Pydantic model that allows extra fields."""

    class DynamicSchema(schema_cls):
        model_config = ConfigDict(extra="allow")  # Used for passing user_id param to tool

    return DynamicSchema


class BaseComposioTool(BasePatternTool, ABC):
    action: ClassVar[Action]
    name: str = "Will be replaced in Constructor"
    description: str = "Will be replaced in Constructor"

    def __init__(self, **kwargs: Any):
        composio_tool = get_composio_tool(self.action)
        kwargs["name"] = composio_tool.name
        kwargs["description"] = composio_tool.description
        kwargs["args_schema"] = (
            allow_extra_fields(composio_tool.args_schema) if composio_tool.args_schema.model_fields else {}
        )
        super().__init__(**kwargs)

    def _run(self, user_id: str, **kwargs: Any) -> BasePatternToolMessage:  # pylint: disable=arguments-differ
        return self._execute(user_id, kwargs)

    def _execute(self, user_id: str, params: dict[str, Any]):
        try:
            response = self._run_tool(user_id, params)
            if "error" in response and response["error"]:
                return self._handle_error(response["error"])

            return self._create_result(response["data"])
        except Exception as e:
            if "No connected account found for app" in str(e):
                app_name = str(e).split("`")[1]
                return AIMessage(
                    message=(
                        f"It seems you haven't authorized the {app_name} integration yet. "
                        f"Please open the integrations menu and authorize {app_name} "
                        "to continue with this step."
                    )
                )
            raise Exception(f"An error occurred: {e}") from e

    def _run_tool(self, user_id: str, params: dict[str, Any]) -> Any:
        return execute_composio_tool(self.action, user_id, params)

    def _handle_error(self, error_message: str) -> BasePatternToolMessage:
        return AIMessage(
            message=self._get_error_message(error_message),
        )

    def _parse_artifact(self, response_data: dict) -> BasePatternToolArtifact:
        return BasePatternToolArtifact(value=response_data, type=self.output_artifact_type)

    def _create_result(self, response_data: dict) -> BasePatternToolMessage:
        return AIMessage(
            message=self._get_success_message(response_data),
            artifact=self._parse_artifact(response_data),
        )

    def _get_error_message(self, error_message: str):
        return f"Action failed: {error_message}"

    def _get_success_message(self, response: dict):  # pylint: disable=unused-argument
        return "Action finished successfully"