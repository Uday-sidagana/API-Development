
from composio import Action, action
from typing import Annotated, Any
import typing as t
import requests
from composio import ComposioToolSet




@action(
    toolname="salesforce",
)  # Associate with SalesForce app for auth
def query_contact_by_name(
    name: Annotated[str, "Contact Name"],
    execute_request: t.Callable,  # Injected by Composio
) -> dict:
    """
    Queries Salesforce for contacts by name.

    :param name: The name of the contact to search for.
    :param execute_request: A callable to execute the Salesforce API request.
    :return dict: A dictionary containing the contact information (e.g., names)
                  if successful, or an error message if an issue occurs.
    """
    try:
        # query = f"SELECT Id, Name, Email, Phone FROM Contact WHERE Name LIKE '%Test%'"
        query = f"SELECT Id, Name, Email, Phone FROM Account'"
        encoded_query = requests.utils.quote(query)

        response_data = execute_request(
            endpoint=f"/services/data/v61.0/query?q={encoded_query}",  # API path relative to base URL
            method="GET",
        )


        return {
            "success": True,
            "data": response_data.get("records", [])
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def execute_composio_tool(action: Action, user_id: str, params: dict[str, Any]):
    toolset = ComposioToolSet(api_key="", lock=False)
    entity = toolset.get_entity(id=user_id)
    result = toolset.execute_action(entity_id=entity.id, action=action, params=params)
    return result
    

print(execute_composio_tool(query_contact_by_name, "customapptest", {"name": "Composio"}))