from composio_openai import App, ComposioToolSet

toolset = ComposioToolSet()
integration = toolset.create_integration(
    app=App.GITHUB,
    auth_mode="OAUTH2",
    use_composio_oauth_app=False,
    auth_config={
      "client_id": "",
      "client_secret": "",
      "redirect_uri": "https://backend.composio.dev/api/v1/auth-apps/add"
    }
)

entity = toolset.get_entity("Whitelabel2")

connection_request = entity.initiate_connection(
    app_name=App.GITHUB, integration=integration
)
print(connection_request.redirectUrl)



user_id = "Whitelabel"
entity = toolset.get_entity(user_id)

# entity = toolset.get_entity("Whitelabel2")

# thread_id = "12345678"
redirect_url = "https://uday.com/thread/59U1DpBj" # Example redirect URL

conn_req = entity.initiate_connection(
    app_name=App.GITHUB,
    auth_mode="OAUTH2",
    use_composio_auth=False,
    redirect_url=redirect_url
)

print(conn_req.redirect_url)

