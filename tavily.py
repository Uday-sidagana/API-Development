# from langchain.agents import create_openai_functions_agent, AgentExecutor
# from langchain import hub
# from langchain_openai import ChatOpenAI
# from composio_langchain import ComposioToolSet, Action, App
# from dotenv import load_dotenv
# import os



# load_dotenv()


# llm = ChatOpenAI()
# prompt = hub.pull("hwchase17/openai-functions-agent")


# composio_toolset = ComposioToolSet(api_key= os.getenv("COMPSIO_API_KEY"))



# tools = composio_toolset.get_tools(actions=['TAVILY_TAVILY_SEARCH'])

# agent = create_openai_functions_agent(llm, tools, prompt)
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# task = " would like to know about the current events and news happening in Milano. Please provide the latest updates."
# result = agent_executor.invoke({"input": task})
# print(result)


from composio_livekit import Action, ComposioToolSet
from livekit import agents
from livekit.agents.voice import Agent, AgentSession, room_io
from livekit.plugins import (
    cartesia,
    deepgram,
    openai,
    silero,
)
from dotenv import load_dotenv
import os



load_dotenv()


toolset = ComposioToolSet(api_key= os.getenv("COMPSIO_API_KEY"))


tools = toolset.get_tools(
    actions=[Action.TAVILY_TAVILY_SEARCH],
    
)


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="You are a helpful voice AI assistant.", tools=tools
        )

async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
        stt=deepgram.STT(),
        llm=openai.LLM(model="gpt-4o"),
        tts=cartesia.TTS(),
        vad=silero.VAD.load(),
        
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=room_io.RoomInputOptions(),
    )

    await session.generate_reply()

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
