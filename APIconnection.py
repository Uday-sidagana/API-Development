#Set for Default project

from composio import Composio

# Initialize the Composio client
composio = Composio(api_key="")
app = composio.apps.get(name="notion")
# Create a new integration
integration = composio.integrations.create(
    app_id=app.appId,
    auth_mode="API_KEY",
    force_new_integration=True,
    name="notion_11",
    use_composio_auth=False
)




# from composio import ComposioToolSet, App
# toolset = ComposioToolSet(api_key="")

# # integration = toolset.get_integration(id="72946d15-5a5d-4ede-9064-90f32ea7dbbc")
# integration = toolset.get_integration(id="3ae4aa5e-406c-4d49-95b2-24eafc96af95")

# # Collect auth params from your users
# print(integration.expectedInputFields)

# connection_request = toolset.initiate_connection(
#     integration_id=integration.id,
#     connected_account_params={
#   "api_key": ""
#   },
#     entity_id="3.7",
# )

# # Redirect step require for OAuth Flow
# print(connection_request.redirectUrl)
# print(connection_request.connectedAccountId)

