import typing as t
from typing import Any, ClassVar, List, Optional

import requests
from composio import action
from composio_langchain import Action
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from artifact.artifact_type import ArtifactType
from tools.base_pattern_tool import BasePatternToolSchema
from tools.salesforce.base_salesforce_tool import BaseSalesforceTool


class QueryContactInput(BasePatternToolSchema):
    user_id: str = Field(description="The Salesforce user id")
    name: str = Field(description="Name to search for in contacts")


class QueryContactByNameResponse(BaseModel):
    topics: Optional[List[str]] = Field(default=None, description="List of contact names or relevant topics found.")
    error: Optional[str] = Field(default=None, description="Error message if the query failed.")
    raw_response: Optional[Any] = Field(
        default=None, description="The raw response data if parsing failed or for additional details."
    )


@action(
    toolname="salesforce",
)
def query_contact_by_name(
    name: Annotated[str, "Contact Name"],
    execute_request: t.Callable,
) -> QueryContactByNameResponse:
    """
    Queries Salesforce for contacts by name.

    :param name: The name of the contact to search for.
    :param execute_request: A callable to execute the Salesforce API request.
    :return dict: A dictionary containing the contact information (e.g., names)
                  if successful, or an error message if an issue occurs.
    """
    try:
        query = f"SELECT Id, Name, Email, Phone FROM Contact WHERE Name LIKE '%{name}%'"
        encoded_query = requests.utils.quote(query)

        response_data = execute_request(
            endpoint=f"/services/data/v61.0/query?q={encoded_query}",
            method="GET",
        )

        if isinstance(response_data, dict):
            return QueryContactByNameResponse(topics=response_data.get("names", []))

        return QueryContactByNameResponse(error="Failed to parse topics", raw_response=response_data)
    except Exception as e:
        print(f"Error executing request for topics: {e}")
        return {"error": str(e)}


class QueryContact(BaseSalesforceTool):
    action: ClassVar[Action] = query_contact_by_name
    output_artifact_type: Optional[ArtifactType] = ArtifactType.SALESFORCE_CONTACT

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)