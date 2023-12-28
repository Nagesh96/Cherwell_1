import requests
import json
import base64

# Set the Cherwell REST API endpoint
url = "<base_uri>/api/V1/savebusinessobject"

# Set the Cherwell REST API headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic {}".format(base64.b64encode("<username>:<password>".encode()).decode())
}

# Set the Cherwell REST API payload
payload = {
    "busObId": "<busObId>",
    "fields": [
        {
            "dirty": True,
            "fieldId": "<fieldId>",
            "value": "New Release Ticket"
        },
        {
            "dirty": True,
            "fieldId": "<fieldId>",
            "value": "Open"
        },
        {
            "dirty": True,
            "fieldId": "<fieldId>",
            "value": 5
        },
        {
            "dirty": True,
            "fieldId": "<fieldId>",
            "value": "IT Service Desk"
        },
        {
            "dirty": True,
            "fieldId": "<fieldId>",
            "value": "Report Outage or Error"
        },
        {
            "dirty": True,
            "fieldId": "<fieldId>",
            "value": "Submit Incident"
        },
        {
            "dirty": True,
            "fieldId": "<fieldId>",
            "value": "Event"
        }
    ]
}

# Send the Cherwell REST API request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Show the response status code and content
print("Response Status Code: {}".format(response.status_code))
print("Response Content: {}".format(response.content))
