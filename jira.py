# api_key="***REMOVED***"

from composio import ComposioToolSet
from composio import Action, App

composio_toolset = ComposioToolSet()

response = composio_toolset.execute_action(action=Action.JIRA_GET_PROJECT, params={'projectIdOrKey':'CPG'})
print(response)