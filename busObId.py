import requests
import json

# Set the Cherwell API endpoint URL
url = "https://<your_cherwell_instance>/CherwellAPI/api/V1/getbusinessobject/busobname/release"

# Set the Cherwell API credentials
username = "<your_cherwell_username>"
password = "<your_cherwell_password>"
client_id = "<your_cherwell_client_id>"
client_secret = "<your_cherwell_client_secret>"

# Set the headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer <your_access_token>"
}

# Get the access token
auth_url = "https://<your_cherwell_instance>/CherwellAPI/token"
auth_data = {
    "grant_type": "password",
    "username": username,
    "password": password,
    "client_id": client_id,
    "client_secret": client_secret
}
auth_response = requests.post(auth_url, data=auth_data)
access_token = auth_response.json()["access_token"]
headers["Authorization"] = f"Bearer {access_token}"

# Fetch the Release busObId
response = requests.get(url, headers=headers)
busObId = response.json()["busObId"]

print(f"The busObId for Release is {busObId}")
