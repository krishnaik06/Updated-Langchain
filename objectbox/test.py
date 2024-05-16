import requests

# Create Chat Session
url = "https://gateway-dev.on-demand.io/chat/v1/sessions"
headers = { "apikey": "FSs5SmWWSaqrstpxZ87v1NrACHnT0ozk" }
body = { "pluginIds": [], "externalUserId": "plugin-1713962163" }
response = requests.post(url, headers=headers, json=body)
chatSession = response.json()
print(chatSession)
session_id = chatSession['chatSession']['id']

# Answer Query
url = f"https://gateway-dev.on-demand.io/chat/v1/sessions/{session_id}/query"
headers = { "apikey": "FSs5SmWWSaqrstpxZ87v1NrACHnT0ozk" }
body = { "endpointId": "predefined-openai-gpt4o", "query": "What is the weather in Bangalore", "pluginIds": ["plugin-1713924030"], "responseMode": "sync" }
response = requests.post(url, headers=headers, json=body)
print(response.json())
