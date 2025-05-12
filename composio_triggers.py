from composio_openai import ComposioToolSet, App, Action
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
    app=App.GITHUB,
    trigger_name="GITHUB_COMMIT_EVENT",
    config={
        
        "owner": "Uday-sidagana",
        "repo": "API-Development"
    },
)



# 2. Webhook endpoint to receive trigger events
@app.post("/webhook/github-commit")
async def github_commit_webhook(request: Request):
    event = await request.json()

    commit_message = event.payload.get("head_commit", {}).get("message", "")
    repo_name = event.payload.get("repository", {}).get("name", "")
    commit_sha = event.payload.get("head_commit", {}).get("id", "")

    # Debugging prints
    print(f"Repository Name: {repo_name}")
    print(f"Commit SHA: {commit_sha}")
    print(f"Commit Message: {commit_message}")

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
            "repo": repo_name,
            "commit_sha": commit_sha,
            "body": comment_body
        }
    )

    return {"status": "success"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
#@@@