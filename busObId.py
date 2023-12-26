import requests

# Replace these values with your Cherwell instance details
cherwell_url = "https://your-cherwell-instance/api/V1"
cherwell_username = "your_username"
cherwell_password = "your_password"

# Authentication
auth_endpoint = f"{cherwell_url}/auth/token"
auth_data = {"username": cherwell_username, "password": cherwell_password}
auth_response = requests.post(auth_endpoint, json=auth_data)
auth_token = auth_response.json().get("access_token")

# Get the busObId for the "Release" business object type
bus_obj_endpoint = f"{cherwell_url}/busobinfo"
bus_obj_query = {"busObName": "Release"}

headers = {"Authorization": f"Bearer {auth_token}"}
bus_obj_response = requests.get(bus_obj_endpoint, params=bus_obj_query, headers=headers)
bus_obj_info = bus_obj_response.json()

# Extract the busObId
busObId = bus_obj_info.get("busObId")

print(f"busObId for 'Release': {busObId}")
