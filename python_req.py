"""from composio import ComposioToolSet, App
toolset = ComposioToolSet(api_key="yoggllclca096m7ia4oaxq")

integration = toolset.get_integration(id="5fa6df08-0724-4ea5-a82d-56ce29551d20")
# Collect auth params from your users
print(integration.expectedInputFields)

connection_request = toolset.initiate_connection(
    integration_id=integration.id,
    entity_id="testingendpoimts",
)

# Redirect step require for OAuth Flow
print(connection_request.redirectUrl)
print(connection_request.connectedAccountId)
"""

'''from composio import ComposioToolSet, App
toolset = ComposioToolSet(api_key="")

integration = toolset.get_integration(id="c34cb26d-06b6-4331-9fe3-37c24fd7e7b6")
# Collect auth params from your users
print(integration.expectedInputFields)

connection_request = toolset.initiate_connection(
    integration_id=integration.id,
    entity_id="endpointT",
)

# Redirect step require for OAuth Flow
print(connection_request.redirectUrl)
print(connection_request.connectedAccountId)'''


'''# from composio import Composio

# # Initialize the Composio client
# composio = Composio(api_key="")
# app = composio.apps.get(name="notion")
# # Create a new integration
# integration = composio.integrations.create(
#     app_id=app.appId,
#     auth_mode="API_KEY",
#     force_new_integration=True,
#     name="notion_Y3Ci",
#     use_composio_auth=False
# )

from composio import ComposioToolSet, App
toolset = ComposioToolSet(api_key="")

integration = toolset.get_integration(id="3a27633e-e349-4ea5-8d4a-cf38af68c8f3")
# Collect auth params from your users
print(integration.expectedInputFields)

connection_request = toolset.initiate_connection(
    integration_id=integration.id,
    connected_account_params={
  "api_key": ""
  },
    entity_id="notionTestT3",
)

# Redirect step require for OAuth Flow
print(connection_request.redirectUrl)
print(connection_request.connectedAccountId)

'''

# from composio import Composio

# # Initialize the Composio client
# composio = Composio(api_key="")
# app = composio.apps.get(name="github")
# # Create a new integration
# integration = composio.integrations.create(
#     app_id=app.appId,
#     auth_config = {"scopes":"public_repo,user"},
#     auth_mode="OAUTH2",
#     force_new_integration=True,
#     name="github_iaBH",
#     use_composio_auth=True
# )

# from composio import ComposioToolSet, App
# toolset = ComposioToolSet(api_key="")

# integration = toolset.get_integration(id="158c9d01-2022-4c7a-a230-7430d1debee9")
# # Collect auth params from your users
# print(integration.expectedInputFields)

# connection_request = toolset.initiate_connection(
#     integration_id=integration.id,
#     entity_id="githubT1",
# )

# # Redirect step require for OAuth Flow
# print(connection_request.redirectUrl)
# print(connection_request.connectedAccountId)


from composio import Composio

# Initialize the Composio client
composio = Composio(api_key="")
app = composio.apps.get(name="github")
# Create a new integration
integration = composio.integrations.create(
    app_id=app.appId,
    auth_config = {"scopes":"public_repo,user"},
    auth_mode="OAUTH2",
    force_new_integration=True,
    name="github_vGb_",
    use_composio_auth=True
)

