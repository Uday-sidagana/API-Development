from composio_livekit import ComposioToolSet, App
# from composio_livekit import Action


# from composio import Action
from livekit import agents
from livekit.agents.voice import Agent, AgentSession, room_io
from livekit.plugins import (
    cartesia,
    deepgram,
    openai,
    silero,
)

composio_toolset = ComposioToolSet()

# tools = composio_toolset.get_tools(actions=['GMAIL_FETCH_EMAILS'])
# tools =composio_toolset.get_tools(apps=[App.GMAIL])
tools = composio_toolset.get_app([App.GMAIL])

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
