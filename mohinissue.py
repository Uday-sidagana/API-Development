from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, Action, App
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()



def setup_agent(user_id: str):
    """Create a LangChain agent with specified tools for a user"""
    composio_toolset = ComposioToolSet(entity_id=user_id)

    # Get tools for this specific user
    tools = composio_toolset.get_tools(
        # apps=[App.JIRA],
        # tags=[Tag.JIRA_ISSUES,Tag.JIRA_PROJECTS],
        actions=[Action.JIRA_GET_ALL_PROJECTS],
    )

    # Initialize the LLM
    llm = ChatOpenAI(
        model="gpt-4.1"
    )

    # Get the prompt template
    prompt = hub.pull("hwchase17/openai-functions-agent")

    print("Final tools: ",tools)
    print("project tags: ",Action.JIRA_GET_ALL_PROJECTS.tags)

    # Create the agent
    agent = create_openai_functions_agent(llm, tools, prompt)

    # Create the executor
    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True
    )


if __name__ == "__main__":
    user_id = "your-entity-id"  # Replace with your actual Composio entity ID

    # Step 1: Setup the agent with Composio Jira tools
    agent_executor = setup_agent(user_id="")

    if agent_executor:
        # Step 2: Define a task in plain English
        task = "List all Jira projects"

        # Step 3: Run the agent
        result = agent_executor.run(task)

        # Step 4: Print the output
        print("\nAgent response:")
        print(result)

