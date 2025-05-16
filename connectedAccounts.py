# export COMPOSIO_LOGGING_LEVEL=debug
from composio import ComposioToolSet
from composio import Action, App
from dotenv import load_dotenv
import os



load_dotenv()

composio_toolset = ComposioToolSet(api_key= os.getenv("COMPSIO_API_KEY"))

# response = composio_toolset.execute_action(action="SALESFORCE_RETRIEVE_SPECIFIC_CONTACT_BY_ID", params={"id":"5a1abc5c-94b2-4501-9e6d-324187aba6b9"})
# Direct Execution targeting a specific connection
try:
    composio_toolset.check_connected_account(entity_id="ticketTest", action=Action.SLACK_FETCH_BOT_USER_INFORMATION)  
    print("Success")

except:
    print("Unsuccessful")

# accounts = composio_toolset.get_connected_account('10d8c21b-ec01-4bcon    e4-b3e2-176ec5949d2b')

# accounts = composio_toolset.get_connected_accounts()
connection_id ="52209aa7-14c3-4d29-86f8-f4c3cc466f1c"
accounts = composio_toolset.get_connected_account(id=connection_id) 


#52209aa7-14c3-4d29-86f8-f4c3cc466f1c
print(accounts)
# 1d0bf959-21cd-4bfc-b122-84fed31b93bc(Google Analytics)