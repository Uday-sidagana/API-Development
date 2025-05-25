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
# tools = composio_toolset.get_tools(actions=['GMAIL_LIST_THREADS'])
tools = composio_toolset.get_tools(actions=['GMAIL_FETCH_EMAILS'])


agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
task = f"Fetch Title, Subject and Time of my mails that i received on 25th May 2025 and structure them in a readable format.fetch only 1 mail, For reference Today is {today}"
# task = " Fetch Gmails"
result = agent_executor.invoke({"input": task})
print(result)