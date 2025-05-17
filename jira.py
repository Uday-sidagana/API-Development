# api_key="***REMOVED***"

from composio import ComposioToolSet
from composio import Action, App

composio_toolset = ComposioToolSet()

response = composio_toolset.execute_action(entity_id="apitest",action=Action.JIRA_CREATE_PROJECT, params={'name':'CPG'})
print(response)