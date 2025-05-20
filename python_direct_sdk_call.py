# export COMPOSIO_LOGGING_LEVEL=debug
# COMPOSIO_LOG_VERBOSITY=3
# ***REMOVED***
from composio import ComposioToolSet
from composio import Action, App

composio_toolset = ComposioToolSet()
'''
response = composio_toolset.execute_action(entity_id="EndPointTest",
                                           action="SNOWFLAKE_DESCRIBE_TABLE",
                                            params={"database":"TESTCOMPOSIO", "schema_name":"TESTCOMPOSIO", "table_name":"USERS"})'''
# Direct Execution targeting a specific connection
# response= composio_toolset.execute_action(connected_account_id="ca_j876qdxfdUuN",
#                                           action=Action.GMAIL_SEND_EMAIL,
#                                           params={"recipient_email":"uday.sidgana@gmail.com", "body":"Hell there, this is a test"},
#   
# 
#                                         )

# tools = composio_toolset.get_action(action=Action.SNOWFLAKE_DESCRIBE_TABLE)
# tools.description = "New Description"

# print(tools)

response = composio_toolset.execute_action(action="SALESFORCE_RETRIEVE_SPECIFIC_CONTACT_BY_ID", params={"id": "003Wd000004ApjkIAC"})

print(response)


# integrationID= composio_toolset.get_integration("19acc862-dd9d-4572-983f-cdc8cee5c33e")
# print(integrationID)

# AccountID = composio_toolset.get
# print(AccountID)

# entity = composio_toolset.get_entity("customapptest")
# response = composio_toolset.execute_action(entity_id=entity, )
# integration = composio_toolset.get_integration("5fa6df08-0724-4ea5-a82d-56ce29551d20")
# # print(entity.id)
# print(integration)
