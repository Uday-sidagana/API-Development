'''from composio import action
from typing import Annotated 

from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, Action, App



# from composio_openai import ComposioToolSet, App, Tag, Action, action
from dotenv import load_dotenv
import os

load_dotenv()


composio_toolset = ComposioToolSet(api_key=os.getenv("COMPOSIO_API_KEY"))# Recommended for descriptions
llm = ChatOpenAI()
prompt = hub.pull("hwchase17/openai-functions-agent")


# Define a simple function
@action # Decorate it to make it a Composio tool
def add_numbers(
    a: Annotated[int, "The first number to add"],
    b: Annotated[int, "The second number to add"]
) -> int:
    """Adds two integers and returns the result."""
    print(f"Executing add_numbers: Adding {a} and {b}")
    return a + b

# Optionally, provide a custom name for the tool
@action(toolname="calculator_multiply")
def multiply_numbers(
    a: Annotated[int, "The first number to multiply"],
    b: Annotated[int, "The second number to multiply"]
) -> Annotated[int, "The product of the two provided numbers"]:
    """
        Multiplies two integers.
        Returns:
        int: The product of the two provided numbers.
    """
    print(f"Executing multiply_numbers: Multiplying {a} by {b}")
    return a * b


# Fetch custom and built-in tools together
tools = composio_toolset.get_tools(actions=['GITHUB_GET_THE_AUTHENTICATED_USER'])




# prompt = hub.pull("hwchase17/openai-functions-agent")

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

task = f'Get My username from Github and run the add_numbers and calculator_mu;tiply tools on a=1,b=2 and give me result'
# task = "Get my Github Username"
result = agent_executor.invoke({"input": task})
print(result)'''





# from composio_openai import ComposioToolSet, App, Tag, action
from composio import action, Action
from typing import Annotated
import typing as t

from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, App



# from composio_openai import ComposioToolSet, App, Tag, Action, action
from dotenv import load_dotenv
import os

load_dotenv()

composio_toolset = ComposioToolSet(api_key=os.getenv("COMPOSIO_API_KEY"))# Recommended for descriptions
llm = ChatOpenAI()
prompt = hub.pull("hwchase17/openai-functions-agent")


# prompt = hub.pull("hwchase17/openai-functions-agent")


@action # Associate with GitHub app for auth
def get_github_repo_topics(
    owner: Annotated[str, "Repository owner username"],
    repo: Annotated[str, "Repository name"],
    execute_request: t.Callable # Injected by Composio
) -> dict:
    """Gets the topics associated with a specific GitHub repository."""
    print(f"Getting topics for {owner}/{repo} using Composio-managed GitHub auth...")
    try:
        # Call the GitHub API endpoint using the injected function
        response_data = execute_request(
            endpoint=f"/repos/{owner}/{repo}/topics", # API path relative to base URL
            method="GET"
            # Body/parameters usually not needed when relying on managed auth
        )
        # Ensure response_data is a dictionary before accessing 'names'
        if isinstance(response_data, dict):
             return {"topics": response_data.get("names", [])}
        else:
             # Handle unexpected response format
             print(f"Warning: Unexpected response format from execute_request: {type(response_data)}")
             return {"error": "Failed to parse topics", "raw_response": response_data}
    except Exception as e:
        print(f"Error executing request for topics: {e}")
        return {"error": str(e)}
    

tools = composio_toolset.get_tools(actions=[Action.GITHUB_GET_ALL_REPOSITORY_TOPICS,])
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# task = f'Get My username from Github and run the add_numbers and calculator_mu;tiply tools on a=1,b=2 and give me result'
# task = "Get my Github Username"
task = "Get topics for my github repo Uday-sidagana/CU-Placement-Assistant"
result = agent_executor.invoke({"input": task})
print(result)
