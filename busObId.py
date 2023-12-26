import requests
import json

# Cherwell API endpoint URL
url = "https://charter.cherwellondemand.com/CherwellClient/CherwellAPI/api/V1/savebusinessobject"
# Cherwell API key
api_key = "<api_key>"

# Cherwell username and password
username = "<username>"
password = "<password>"

# Set the Release properties
release = {
    "busObId": "Release",
    "fields": [
        {"name": "Short Description", "value": "Providing Dummy Data for Testing purpose"},
        {"name": "Requestor", "value": "annem, nageswara (P3214461)"},
        {"name": "Request Group", "value": "Spectrum Mobile App Support"},
        {"name": "Program", "value": "Spectrum Mobile 2.0"},
        {"name": "Environment", "value": "QA"},
        {"name": "Primary Application (CI)", "value": "SPECTRUM MOBILE 2.0 BACKOFFICE (SMBO M2) QA2"},
        {"name": "Release Type", "value": "Code"},
        {"name": "Type Of Testing- Required", "value": "Smoke Test only"},
        {"name": "Deployment Description Summary", "value": "Defect Fixes"},
        {"name": "Build", "value": "1.0.1"},
        {"name": "Urgency", "value": "Low"},
        {"name": "Urgency Reason", "value": "Defect Fixes"},
        {"name": "Service Impact", "value": "Yes - Continuous"},
        {"name": "Impacts to Orders in Procress", "value": "Yes"}
    ],
    "persist": True
}

# Set the headers for the Cherwell API request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer " + api_key
}

# Authenticate with the Cherwell API
auth_data = {
    "grant_type": "password",
    "client_id": "api_client",
    "username": username,
    "password": password
}
auth_url = "https://<base_uri>/CherwellAPI/token"
auth_response = requests.post(auth_url, data=auth_data)
auth_response.raise_for_status()
auth_json = auth_response.json()
api_key = auth_json["access_token"]

# Set the headers for the Cherwell API request with the new API key
headers["Authorization"] = "Bearer " + api_key

# Create the new Release in Cherwell
response = requests.post(url, headers=headers, data=json.dumps(release))
response.raise_for_status()

# Show the new business object record id
print("RecId for new Release: {}".format(response.json()["busObRecId"]))
print("PublicId for new Release: {}".format(response.json()["busObPublicId"]))
