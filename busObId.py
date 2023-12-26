import requests
from requests.auth import HTTPBasicAuth

url = "https://cherwell_instance/api/V1/getbusinessobject/busobname/Release"
username = "your_username"
password = "your_password"

response = requests.get(url, auth=HTTPBasicAuth(username, password))

if response.status_code == 200:
    try:
        release_data = response.json()
        bus_ob_id = release_data.get("busObId", "")
        print(f"BusObId of Release: {bus_ob_id}")
    except ValueError as e:
        print(f"Error decoding JSON: {e}")
        print("Response content:", response.content)
else:
    print(f"Error: {response.status_code} - {response.text}")
    print("Response content:", response.content)
