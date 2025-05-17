# ***REMOVED***
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, Action, App
from dotenv import load_dotenv
import os




load_dotenv()


llm = ChatOpenAI()
prompt = hub.pull("hwchase17/openai-functions-agent")


composio_toolset = ComposioToolSet(api_key= os.getenv("COMPSIO_API_KEY"))

composio_toolset = ComposioToolSet(api_key="")
tools = composio_toolset.get_tools(entity_id="usefulagents",actions=['SALESFORCE_RETRIEVE_SPECIFIC_CONTACT_BY_ID','SALESFORCE_RETRIEVE_CONTACT_INFO_WITH_STANDARD_RESPONSES'])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
task = "Retreive Contact details"
result = agent_executor.invoke({"input": task})
print(result)


# from composio import ComposioToolSet, Action, App # Use base ComposioToolSet for schema inspection
# # Initialize base ToolSet
# base_toolset = ComposioToolSet()
# # Get the raw schema for a specific Google Calendar action
# # Bypass the check for an active Google Calendar connection
# notion_schemas = base_toolset.get_action_schemas(
#     actions=[Action.NOTION_QUERY_DATABASE],
#     check_connected_accounts=False
# )
# if notion_schemas:
#     import json
#     print("Raw Schema for NOTION_QUERY_DATABASE:")
#     # notion_schemas is a list, access the first element
#     print(json.dumps(notion_schemas[0].model_dump(), indent=2))
# else:
#     print("Schema not found.")






