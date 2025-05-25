# export COMPOSIO_LOGGING_LEVEL=debug
# COMPOSIO_LOG_VERBOSITY=3
# ***REMOVED***
from composio import ComposioToolSet
from composio import Action, App

composio_toolset = ComposioToolSet()
for i in range(100):
    response = composio_toolset.execute_action(action="GMAIL_FETCH_EMAILS", params={'max_results': 1})
    print(f"{i} Times done")

print("Completed 100 times!")
