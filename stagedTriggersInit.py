# wv6rkjbru4!akztvfxwpl1s ----added !
from composio_openai import ComposioToolSet,App

toolset = ComposioToolSet(api_key="", base_url="https://staging-backend.composio.dev/api")

user_id = "2" # User ID referencing an entity retrieved from application logic
entity = toolset.get_entity(id=user_id)
triggers = toolset.get_trigger("GMAIL_NEW_GMAIL_MESSAGE")

res = entity.enable_trigger(
    app=App.GMAIL,
    trigger_name="GMAIL_NEW_GMAIL_MESSAGE",
    config={
        
    }
)

print(res["status"])