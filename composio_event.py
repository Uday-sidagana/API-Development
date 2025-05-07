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
# tools = composio_toolset.get_tools(actions=['GOOGLECALENDAR_CREATE_EVENT'])
tools = composio_toolset.get_tools(apps=[App.GOOGLECALENDAR])
# prompt = hub.pull("hwchase17/openai-functions-agent")

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# task = "Create an event on Wed 7th May 2025 11PM. Title is 'Ai Agent Test' and Description is 'Test"
task = "Give me details of Events scheduled today, just give me title and time"
result = agent_executor.invoke({"input": task})
print(result)
