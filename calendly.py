# from langchain.agents import create_openai_functions_agent, AgentExecutor
# from langchain import hub
# from langchain_openai import ChatOpenAI
# from composio_langchain import ComposioToolSet, Action, App
# from dotenv import load_dotenv
# import os
# from datetime import datetime

# load_dotenv()

# now_local = datetime.now()
# today= now_local.date()

# llm = ChatOpenAI()
# prompt = hub.pull("hwchase17/openai-functions-agent")


# composio_toolset = ComposioToolSet(entity_id="scopesTest",api_key= os.getenv("COMPSIO_API_KEY"))
# tools = composio_toolset.get_tools(actions=['CALENDLY_CREATE_ONE_OFF_EVENT_TYPE'])

# agent = create_openai_functions_agent(llm, tools, prompt)
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# # task = f"Fetch Title, Subject and Time of my mails that i received on 11th May 2025 and structure them in a readable format. For reference Today is {today}"
# # task = " Fetch Gmails"
# # task= f"Create an off Event of 30 mins at 9:00PM a named 'Test' user_uri: 'uday-usefulagents'. Use the Time zone named exactly 'India Standard Time' This is a test Event so keep everything default and feel free to add details of anything i missed."
# task= f"Create an off Event Timezone there is an option called 'India Standard Time' just choose that optoin, Duration will be 30 minutes and you don't need to specify Host as it is already been selected"
# result = agent_executor.invoke({"input": task})
# print(result)


# export COMPOSIO_LOGGING_LEVEL=debug
# api_key="***REMOVED***"
from composio import ComposioToolSet
from composio import Action, App

composio_toolset = ComposioToolSet()


response= composio_toolset.execute_action(entity_id="scopesTest",
                                          action=Action.CALENDLY_CREATE_ONE_OFF_EVENT_TYPE,
                                          params={"date_setting": { "message": "India Standard Time"  },"duration":30, "host":"https://calendly.com/uday-usefulagents", "name":"Test"},
                                          )

print(response)




