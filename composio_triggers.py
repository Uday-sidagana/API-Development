'''from composio_openai import ComposioToolSet, App, Action
from fastapi import FastAPI, Request
from openai import OpenAI
from dotenv import load_dotenv
import uvicorn
import json

load_dotenv()

app = FastAPI(debug=True)
toolset = ComposioToolSet()
client = OpenAI()

# 1. Enable the GitHub Trigger for commit events
entity = toolset.get_entity()
entity.enable_trigger(
    app=App.SLACKBOT,
    trigger_name="SLACKBOT_RECEIVE_DIRECT_MESSAGE",
    config={
        
        "owner": "Uday-sidagana",
        "repo": "API-Development"
    },
)



# 2. Webhook endpoint to receive trigger events
@app.post("/webhook/github-commit")
async def github_commit_webhook(request: Request):
    payload = await request.json()

    data = payload.get("data", {})
    commit_message = data.get("message", "")
    commit_sha = data.get("id", "")
    # Call OpenAI to generate a comment
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful code reviewer."},
            {"role": "user", "content": f"Review this commit: {commit_message}"}
        ]
    )

    comment_body = response.choices[0].message.content
    print(comment_body)


    # Post review comment as GitHub issue comment
    toolset.execute_action(
        action=Action.GITHUB_CREATE_A_COMMIT_COMMENT,
        params={
            "owner": "Uday-sidagana",
            "repo": "API-Development",
            "commit_sha": commit_sha,
            "body": comment_body
        }
    )

    return {"status": "success"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  
    '''



from composio_openai import ComposioToolSet, App, Action
from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os

import uvicorn
import json


from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, App


load_dotenv()


app = FastAPI(debug=True)

llm = ChatOpenAI()
prompt = hub.pull("hwchase17/openai-functions-agent")# Using same imports as above
# trigger = toolset.get_trigger("SLACKBOT_RECEIVE_DIRECT_MESSAGE")
# print(trigger.config.model_dump_json(indent=4))

toolset = ComposioToolSet(api_key=os.getenv("COMPOSIO_API_KEY"))# Recommended for descriptions
user_id = "default" # User ID referencing an entity retrieved from application logic
entity = toolset.get_entity(id=user_id)
triggers = toolset.get_trigger("SLACKBOT_RECEIVE_DIRECT_MESSAGE")

entity = toolset.get_entity()
response = entity.enable_trigger(
    app=App.SLACKBOT,
    trigger_name="SLACKBOT_RECEIVE_DIRECT_MESSAGE",
    config={},
)

print(response["status"])

listener = toolset.create_trigger_listener()

@listener.callback(
    filters={
        "trigger_name": "SLACK_RECEIVE_MESSAGE",
    }
)
def handle_slack_message(event):
    print(event)

listener.wait_forever()




