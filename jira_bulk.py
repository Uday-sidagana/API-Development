from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, Action, App
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

now_local = datetime.now()
today= now_local.date()

llm = ChatOpenAI()
prompt = hub.pull("hwchase17/openai-functions-agent")


composio_toolset = ComposioToolSet(entity_id="test",api_key= os.getenv("COMPSIO_API_KEY"))
tools = composio_toolset.get_tools(actions=['JIRA_BULK_CREATE_ISSUE'])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# task = f"Fetch Title, Subject and Time of my mails that i received on 11th May 2025 and structure them in a readable format. For reference Today is {today}"
# task = " Fetch Gmails"
task = "Create 3 Issues with Random names. Parameters to take a note of "
result = agent_executor.invoke({"input": task})
print(result)