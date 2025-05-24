# import requests

# API_KEY = "yoggllclca096m7ia4oaxq"
# BASE_URL = "https://backend.composio.dev/api/v3"
# HEADERS = {"x-api-key": API_KEY}

# def get_paginated_tools(toolkit_slug):
#     params = {"toolkit_slug": toolkit_slug}
#     next_cursor = None
#     while True:
#         if next_cursor:
#             params['cursor'] = next_cursor
#         resp = requests.get(f"{BASE_URL}/tools", headers=HEADERS, params=params)
#         data = resp.json()
#         for item in data.get("items", []):
#             yield item
#         next_cursor = data.get("next_cursor")
#         if not next_cursor:
#             break

# # Fetch toolkits without pagination
# resp = requests.get(f"{BASE_URL}/toolkits", headers=HEADERS)
# toolkit_data = resp.json()
# toolkit_slugs = [item["slug"] for item in toolkit_data.get("items", []) if "slug" in item]

# long_tool_slugs = []

# for toolkit_slug in toolkit_slugs:
#     for tool in get_paginated_tools(toolkit_slug):
#         slug = tool.get("slug")
#         if slug and len(slug) > 64:
#             long_tool_slugs.append(slug)

# for slug in long_tool_slugs:
#     print(slug)



# import requests

# API_KEY = "yoggllclca096m7ia4oaxq"
# BASE_URL = "https://backend.composio.dev/api/v3"
# HEADERS = {"x-api-key": API_KEY}

# def get_paginated_tools(toolkit_slug):
#     next_cursor = None
#     page = 1
#     while True:
#         params = {"toolkit_slug": toolkit_slug}
#         if next_cursor:
#             params['cursor'] = next_cursor
#         print(f"Requesting tools page {page} for toolkit '{toolkit_slug}'...")
#         resp = requests.get(f"{BASE_URL}/tools", headers=HEADERS, params=params)
#         data = resp.json()
#         items = data.get("items", [])
#         print(f"Received {len(items)} tools on page {page}.")
#         for item in items:
#             yield item
#         next_cursor = data.get("next_cursor", None)
#         # Defensive exit: if next_cursor is empty or no items, stop
#         if not next_cursor or not items:
#             print("No more pages left for tools.")
#             break
#         page += 1

# slack_toolkit_slug = "slack"

# print("Starting to check tools in 'slack' toolkit...")
# long_slack_tool_slugs = []

# for tool in get_paginated_tools(slack_toolkit_slug):
#     slug = tool.get("slug")
#     print(f"Checking tool slug: {slug}")
#     if slug and len(slug) > 63:
#         print(f"Found long slug (>64): {slug}")
#         long_slack_tool_slugs.append(slug)

# print("\nFinished. Tool slugs longer than 64 characters in 'slack' toolkit:")
# for slug in long_slack_tool_slugs:
#     print(slug)



import requests

API_KEY = "yoggllclca096m7ia4oaxq"
BASE_URL = "https://backend.composio.dev/api/v3"
HEADERS = {"x-api-key": API_KEY}

def get_paginated_tools(toolkit_slug):
    next_cursor = None
    while True:
        params = {"toolkit_slug": toolkit_slug}
        if next_cursor:
            params['cursor'] = next_cursor
        resp = requests.get(f"{BASE_URL}/tools", headers=HEADERS, params=params)
        data = resp.json()
        items = data.get("items", [])
        for item in items:
            yield item
        next_cursor = data.get("next_cursor", None)
        if not next_cursor or not items:
            break

toolkit_slug = "slack"  # change as needed
long_tool_slugs = []

for tool in get_paginated_tools(toolkit_slug):
    slug = tool.get("slug")
    if slug and len(slug) >= 64:
        long_tool_slugs.append(slug)

for slug in long_tool_slugs:
    print(slug)
