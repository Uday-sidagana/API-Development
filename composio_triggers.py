from composio_openai import ComposioToolSet, Action, App, Trigger
import openai

# Initialize
toolset = ComposioToolSet()
client = openai.OpenAI()  # Your OpenAI client

entity = toolset.get_entity()
entity.enable_trigger(
    app=App.GITHUB, 
    trigger_name="GITHUB_COMMIT_EVENT",
    config={"owner": "Uday-sidagana", "repo": "API-Development"}
)

# Set up listener
listener = toolset.create_trigger_listener()

@listener.callback(filters={"trigger_name": "GITHUB_COMMIT_EVENT"})
def handle_pr(event):

    # title = event.payload.get("pull_request", {}).get("title", "")
    # body = event.payload.get("pull_request", {}).get("body", "")
    # number = event.payload.get("commit", {}).get("number")
    
    # Generate a code review comment using OpenAI
    review = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful code reviewer."},
            {"role": "user", "content": f"Review this commit: repo-API-Development"}
        ]
    )
    
    # Post the review back to GitHub
    toolset.execute_action(
        action=Action.GITHUB_CREATE_AN_ISSUE_COMMENT,
        params={
            "owner": "Uday-sidagana",
            "repo": "API-Development",
            "body": review.choices[0].message.content
        }
    )

# Start listening
listener.wait_forever()


'''# Using same imports as above
trigger = toolset.get_trigger("GITHUB_COMMIT_EVENT")
print(trigger.config.model_dump_json(indent=4))
'''