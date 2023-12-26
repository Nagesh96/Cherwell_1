import requests

# Set the Cherwell REST API endpoint URL
url = "https://<your_cherwell_instance>/CherwellAPI/token"

# Set the client credentials
username = "<your_username>"
password = "<your_password>"
client_id = "<your_client_id>"
grant_type = "password"

# Set the request headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

# Set the request body
data = {
    "username": username,
    "password": password,
    "client_id": client_id,
    "grant_type": grant_type
}

# Send the POST request to the Cherwell authentication server
response = requests.post(url, headers=headers, data=data)

# Extract the access token from the JSON response
access_token = response.json()["access_token"]
