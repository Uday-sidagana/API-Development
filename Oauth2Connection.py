#  qnjc3y6yzap!v86mbwu0ws ------ added ! in the middle


# from composio import Composio

# # Initialize the Composio client
# composio = Composio(api_key="")
# app = composio.apps.get(name="notion")
# # Create a new integration
# integration = composio.integrations.create(
#     app_id=app.appId,
#     auth_config = {"scopes":""},
#     auth_mode="OAUTH2",
#     force_new_integration=True,
#     name="notion_4",
#     use_composio_auth=True
# )



#############


from composio import ComposioToolSet, App
toolset = ComposioToolSet(api_key="")

integration = toolset.get_integration(id="b6a2dd03-8293-4806-bb25-a410dd5ea854")
# Collect auth params from your users
print(integration.expectedInputFields)

connection_request = toolset.initiate_connection(
    integration_id=integration.id,
    entity_id="4.7",
)

# Redirect step require for OAuth Flow
print(connection_request.redirectUrl)
print(connection_request.connectedAccountId)

