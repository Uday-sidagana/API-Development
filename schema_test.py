from composio import ComposioToolSet, Action, App # Use base ComposioToolSet for schema inspection
# Initialize base ToolSet
base_toolset = ComposioToolSet()
# Get the raw schema for a specific Google Calendar action
# Bypass the check for an active Google Calendar connection
calendar_schemas = base_toolset.get_action_schemas(
    actions=[Action.GOOGLEDRIVE_DOWNLOAD_FILE],
    check_connected_accounts=False
)
if calendar_schemas:
    import json
    print("Raw Schema for GOOGLECALENDAR_LIST_CALENDARS:")
    # calendar_schemas is a list, access the first element
    print(json.dumps(calendar_schemas[0].model_dump(), indent=2))
else:
    print("Schema not found.")