import requests
import base64

def check_cherwell_connection(api_url, username, password):
    # ... (existing connection check code)

def create_new_release(api_url, username, password):
    if not check_cherwell_connection(api_url, username, password):
        print("Connection to Cherwell failed. Cannot create a new release.")
        return

    # Set the Cherwell business object properties for the new release
    new_release = {
        "busObId": "your_busObId",
        "fields": [
            {
                "dirty": True,
                "fieldId": "your_fieldId",
                "value": "your_value"
            },
            {
                "dirty": True,
                "fieldId": "your_fieldId",
                "value": "your_value"
            },
            {
                "dirty": True,
                "fieldId": "your_fieldId",
                "value": "your_value"
            }
        ]
    }

    # Endpoint for creating a new release (adjust based on Cherwell's API)
    create_endpoint = f"{api_url}/api/V1/your_create_release_endpoint"

    # Set up headers with content type and authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": get_authorization_header(username, password)
    }

    # Make a request to create a new release
    create_response = requests.post(create_endpoint, json=new_release, headers=headers)

    # Check if the release creation was successful (status code 201 for created)
    if create_response.status_code == 201:
        print("New release created successfully!")

        # Retrieve busObPublicId and busObRecId from the response
        response_json = create_response.json()
        busObPublicId = response_json.get("busObPublicId")
        busObRecId = response_json.get("busObRecId")

        print(f"busObPublicId: {busObPublicId}")
        print(f"busObRecId: {busObRecId}")

    else:
        print(f"Failed to create new release. Status code: {create_response.status_code}")

# Example usage
api_url = ""  # Adjust the URL
username = ""
password = ""

create_new_release(api_url, username, password)￼Enter
