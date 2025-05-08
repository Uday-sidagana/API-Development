from composio import action
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
print(result)

