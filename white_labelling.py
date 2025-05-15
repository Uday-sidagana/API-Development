from composio_openai import App, ComposioToolSet

# Init Toolset
toolset = ComposioToolSet(api_key="***REMOVED***")

# Create integration
integration = toolset.create_integration(
    app=App.LINEAR,
    auth_mode="OAUTH2",
    use_composio_oauth_app=False,
    auth_config={
        "client_id": "2bf4cde32dfa507c8071cea06ad172a6",
        "client_secret": "***REMOVED***",
        "redirect_uri": "https://apollo.com/redirect"
    }
)

# Create entity for default user (will auto-generate user and thread)
entity = toolset.get_entity("default")

# Initiate connection
connection_request = entity.initiate_connection(
    app_name=App.LINEAR, integration=integration
)
print(connection_request)

user_id = "default"
entity = toolset.get_entity(user_id)

thread_id = "12345678"
redirect_url = "https://apollo.com/thread/{thread_id}" # Example redirect URL

conn_req = entity.initiate_connection(
    app_name=App.LINEAR,
    auth_mode="OAUTH2",
    use_composio_auth=False,
    redirect_url=redirect_url
)

print(conn_req.redirect_url)



