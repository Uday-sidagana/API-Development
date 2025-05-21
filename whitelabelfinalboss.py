# 3k3bebbvojhg7fp-eoc1z2nm2uearm7  C_id-Secret 

# from composio import Composio

# # Initialize the Composio client
# composio = Composio(api_key="")
# app = composio.apps.get(name="dropbox")
# # Create a new integration
# integration = composio.integrations.create(
#     app_id=app.appId,
#     auth_config = {"client_id":"","client_secret":"","oauth_redirect_uri":"https://backend.composio.dev/api/v1/auth-apps/add","scopes":"email,profile,account_info.write,account_info.read,files.metadata.write,files.metadata.read,files.content.write,files.content.read,openid,file_requests.write,file_requests.read,sharing.write,sharing.read,contacts.write,contacts.read","base_url":"https://api.dropboxapi.com"},
#     auth_mode="OAUTH2",
#     force_new_integration=True,
#     name="White Label",
#     use_composio_auth=False
# )

from composio import ComposioToolSet, App
toolset = ComposioToolSet(api_key="")

integration = toolset.get_integration(id="82029d52-7952-401e-98c5-ca3b0b371eec")
# Collect auth params from your users
print(integration.expectedInputFields)

connection_request = toolset.initiate_connection(
    integration_id=integration.id,
    entity_id="label2",
)

# Redirect step require for OAuth Flow
print(connection_request.redirectUrl)
print(connection_request.connectedAccountId)
