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
task = "Get topics for my github repo udayusefulagents/TestComposio"
result = agent_executor.invoke({"input": task})
print(result)



# from composio_openai import ComposioToolSet, Action

# toolset = ComposioToolSet()

'''def simplify_gmail_send_schema(schema: dict) -> dict:
    """Removes recipient_email and attachment params from the schema."""
    params = schema.get("parameters", {}).get("properties", {})
    params.pop("recipient_email", None)
    params.pop("attachment", None)
    # We could also modify descriptions here, e.g.:
    # schema["description"] = "Sends an email using Gmail (recipient managed separately)."
    return schema
def inject_gmail_recipient(inputs: dict) -> dict:
    """Injects a fixed recipient email into the inputs."""
    # Get the recipient from app logic, context, or hardcode it
    inputs["recipient_email"] = "uday.sidgana@gmail.com"
    # Ensure subject exists, providing a default if necessary
    inputs["subject"] = inputs.get("subject", "No Subject Provided")
    return inputs
# Combine schema processing and preprocessing
processed_tools = composio_toolset.get_tools(
    actions=[Action.GMAIL_SEND_EMAIL],
    processors={
        "schema": {Action.GMAIL_SEND_EMAIL: simplify_gmail_send_schema},
        "pre": {Action.GMAIL_SEND_EMAIL: inject_gmail_recipient}
    }
)'''

# import json # For pretty printing example output

# def filter_email_results(result: dict) -> dict:
#     """Filters email list to only include sender and subject."""
#     # Pass through errors or unsuccessful executions unchanged
#     if not result.get("successful") or "data" not in result:
#         return result

#     original_messages = result["data"].get("messages", [])
#     if not isinstance(original_messages, list):
#         return result # Return if data format is unexpected

#     filtered_messages = []
#     for email in original_messages:
#         filtered_messages.append({
#             "sender": email.get("sender"),
#             "subject": email.get("subject"),
#         })

#     # Construct the new result dictionary
#     processed_result = {
#         "successful": True,
#         # Use a clear key for the filtered data
#         "data": {"summary": filtered_messages},
#         "error": None
#     }
#     return processed_result

# # Get tools with the postprocessor
# processed_tools = composio_toolset.get_tools(
#     actions=[Action.GMAIL_FETCH_EMAILS],
#     processors={
#         "post": {Action.GMAIL_FETCH_EMAILS: filter_email_results}
#     }
# )

# # --- Simulate Execution and Postprocessing ---
# # Assume 'raw_execution_result' is the large dictionary returned by
# # executing GMAIL_FETCH_EMAILS without postprocessing.
# # raw_execution_result = toolset.execute_action(Action.GMAIL_FETCH_EMAILS, params={...})

# # Apply the postprocessor manually to see the effect (handle_tool_calls does this automatically)
# # filtered_result = filter_email_results(raw_execution_result)
# # print("Filtered Result (much smaller for LLM):")
# # print(json.dumps(filtered_result, indent=2))



# agent = create_openai_functions_agent(llm, processed_tools, prompt)
# agent_executor = AgentExecutor(agent=agent, tools=processed_tools, verbose=True)

# # task = f'Get My username from Github and run the add_numbers and calculator_mu;tiply tools on a=1,b=2 and give me result'
# # task = "Get my Github Username"

# task = "Fetch Mail information'"
# result = agent_executor.invoke({"input": task})
# print(result)
# # print(json.dumps(result, indent=2))
# # Now, when the LLM calls this tool (without providing recipient_email),
# # the 'inject_gmail_recipient' function will run automatically
# # before Composio executes the action, adding the correct email.
# # result = toolset.handle_tool_calls(llm_response_using_processed_tools)
