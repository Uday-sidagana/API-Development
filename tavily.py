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



tools = composio_toolset.get_tools(actions=['TAVILY_TAVILY_SEARCH'])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
task = " would like to know about the current events and news happening in Milano. Please provide the latest updates."
result = agent_executor.invoke({"input": task})
print(result)