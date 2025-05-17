# api_key="***REMOVED***"
from composio import ComposioToolSet
import typing as t
from composio_openai import ComposioToolSet, action

toolset = ComposioToolSet()


@action(toolname="github")
def list_repositories(
    owner: str,
    execute_request: t.Callable,
) -> list[str]:
    """
    List repositories for a user.

    :param owner: Name of the owner.
    :return repositories: List of repositories for given user.
    """
    return [
        repo["name"]
        for repo in execute_request(f"/users/{owner}/repos", "get", None, None).get(
            "data", []
        )
    ]


res = toolset.execute_action(entity_id="uday",
    action=list_repositories, params={"owner": "abhishekpatil4"}, 
)
print(res)
# # --- Example Usage ---
# # You would fetch this tool like any other:
# # tools = toolset.get_tools(actions=[get_github_repo_topics])
# result = composio_toolset.execute_action(get_github_repo_topics, params={"owner": "udayusefulagents", "repo": "TestComposio"})
# print(result)
