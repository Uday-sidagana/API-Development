from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, Action, App
from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatOpenAI()
prompt = hub.pull("hwchase17/openai-functions-agent")


composio_toolset = ComposioToolSet(api_key= os.getenv("COMPSIO_API_KEY"))# Recommended for descriptions


composio_toolset = ComposioToolSet(api_key="***REMOVED***")
tools = composio_toolset.get_tools(actions=['SUPABASE_LIST_ALL_PROJECTS','SUPABASE_BETA_RUN_SQL_QUERY'])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
task = "Get all the rows of 'commit_reviews' table"
# task ="List all organizations"
result = agent_executor.invoke({"input": task})
print(result)