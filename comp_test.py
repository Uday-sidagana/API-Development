'''from google.genai import types
from google import genai
from composio_gemini import Action, ComposioToolSet, App
from dotenv import load_dotenv
import os


from crewai import Agent, Task, Crew
# from langchain_openai import ChatOpenAI
from composio_crewai import ComposioToolSet, Action, App


from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)



client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
toolset = ComposioToolSet(api_key=os.getenv('COMPOSIO_API_KEY'))


#Composio Tools
# tools = toolset.get_tools(actions=[Action.GITHUB_GET_THE_AUTHENTICATED_USER])
tools = toolset.get_tools(actions=[Action.HUBSPOT_CREATE_A_CAMPAIGN])

# config = types.GenerateContentConfig(tools = tools)

#OpenAI workflow
# task = "Get my Github Username"

# message = [
#     {'role': 'system', 'content': 'You are expert in using tools'},
#     {'role': 'client', 'content': task},
# ]

# response = client.chat.completions.create(
#     model='chatgpt-4o-latest',
#     messages= message,
#     tools=tools,
#     tool_choice= 'auto',

# )


# chat = client.chats.create(model='gemini-2.0-flash', config=config)
# response = chat.send_message(
#     "Create a Campaign with default settings"
# )

# print(response.text)

#Use ComposioToolset to handle calls
# result = toolset.handle_tool_calls(response)

# print(result)


crewai_agent = Agent(
    role="Sample Agent",
    goal="""You are an AI agent that is responsible for taking actions based on the tools you have""",
    backstory=(
        "You are AI agent that is responsible for taking actions based on the tools you have"
    ),
    verbose=True,
    tools=tools,
    llm=llm,
)
task = Task(
    description="Create a Campaign with default settings and Values",
    agent=crewai_agent,
    expected_output=""
)


my_crew = Crew(agents=[crewai_agent], tasks=[task])

result = my_crew.kickoff()
print(result)'''

'''# from google.genai import types
# # from google.genai import genai
# import google.genai as genai
# from composio_gemini import Action, ComposioToolSet, App
# from dotenv import load_dotenv
# import os

# from crewai import Agent, Task, Crew
# from composio_crewai import ComposioToolSet, Action, App
# from langchain_google_genai import ChatGoogleGenerativeAI

# # Load environment variables first
# load_dotenv()

# # Initialize API clients after loading env var

# model = genai.GenerativeModel(
#     model_name="gemini-1.5-flash"
# )

# # client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# toolset = ComposioToolSet(api_key=os.getenv('COMPOSIO_API_KEY'))

# # Composio Tools
# tools = toolset.get_tools(actions=[Action.HUBSPOT_CREATE_A_CAMPAIGN])

# # Create CrewAI Agent
# crewai_agent = Agent(
#     role="Sample Agent",
#     goal="""You are an AI agent that is responsible for taking actions based on the tools you have""",
#     backstory="You are an AI agent that is responsible for taking actions based on the tools you have.",
#     verbose=True,
#     tools=tools,
    
# )

# # Create Task
# task = Task(
#     description="Create a Campaign with default settings and Values",
#     agent=crewai_agent,
#     expected_output=""
# )

# # Create Crew and kick off
# my_crew = Crew(agents=[crewai_agent], tasks=[task])

# result = my_crew.kickoff()
# print(result)
'''


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
tools = composio_toolset.get_tools(actions=['HUBSPOT_CREATE_A_CAMPAIGN'])
# prompt = hub.pull("hwchase17/openai-functions-agent")

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

task = "Create a test Campaign with default settings and values"
result = agent_executor.invoke({"input": task})
print(result)

