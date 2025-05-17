from typing import Any

from composio_langchain import Action, ComposioToolSet

from cloud.ssm_client import COMPOSIO_API_KEY, get_ssm_param


def get_composio_tool(action: Action):
    toolset = ComposioToolSet(api_key=get_composio_api_key(), lock=False)
    return toolset.get_tools(actions=[action])[0]


def execute_composio_tool(action: Action, user_id: str, params: dict[str, Any]):
    toolset = ComposioToolSet(api_key=get_composio_api_key(), entity_id=user_id, lock=False)
    result = toolset.execute_action(action=action, params=params)
    return result


def get_composio_api_key():
    return get_ssm_param(COMPOSIO_API_KEY)