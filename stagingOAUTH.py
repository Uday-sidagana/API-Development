# wv6rkjbru4a!kztvfxwpl1s  -------added !





# from composio import Composio

# # Initialize the Composio client
# composio = Composio(api_key="", base_url="https://staging-backend.composio.dev/api")
# app = composio.apps.get(name="notion")
# # Create a new integration
# integration = composio.integrations.create(
#     app_id=app.appId,
#     auth_config = {"scopes":""},
#     auth_mode="OAUTH2",
#     force_new_integration=True,
#     name="notion_9",
#     use_composio_auth=True
# )


from composio import ComposioToolSet, App
toolset = ComposioToolSet(api_key="", base_url="https://staging-backend.composio.dev/api")

integration = toolset.get_integration(id="e634b054-aa55-44d7-a0ac-0f69f83a670e")
# Collect auth params from your users
print(integration.expectedInputFields)

connection_request = toolset.initiate_connection(
    integration_id=integration.id,
    entity_id="2.8",
)

# Redirect step require for OAuth Flow
print(connection_request.redirectUrl)
print(connection_request.connectedAccountId)



# from composio import Composio

# # Initialize the Composio client
# composio = Composio(api_key="",  base_url="https://staging-backend.composio.dev/api")
# app = composio.apps.get(name="notion")
# # Create a new integration
# integration = composio.integrations.create(
#     app_id=app.appId,
#     auth_mode="API_KEY",
#     force_new_integration=True,
#     name="notion_8",
#     use_composio_auth=False
# )




# from composio import ComposioToolSet, App
# toolset = ComposioToolSet(api_key="", base_url="https://staging-backend.composio.dev/api")

# integration = toolset.get_integration(id="ca46c3e3-91bd-4fce-a2cb-7883bd0bb588")
# # Collect auth params from your users
# print(integration.expectedInputFields)

# connection_request = toolset.initiate_connection(
#     integration_id=integration.id,
#     connected_account_params={
#   "api_key": "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"
#   },
#     entity_id="2.6",
# )

# # Redirect step require for OAuth Flow
# print(connection_request.redirectUrl)
# print(connection_request.connectedAccountId)


