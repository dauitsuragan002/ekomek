import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve API key from environment variables
API_KEY = os.environ.get('API_RESPONSE')
# Set the Assistant ID (replace 'ASSISTANT_ID' with your actual ID)
ASSISTANT_ID = 'ASSISTANT_ID'  # Example: '1234'

# Base URL for the KazLLM API
URL_KAZLLM = "https://apikazllm.nu.edu.kz/assistant/"

# Define headers for the API request
HEADERS = {
    "Authorization": f"Api-Key {API_KEY}",
    "accept": "application/json"
}

# Function to retrieve the current context of the assistant
def get_assistant_context(assistant_id):
    """
    Fetches the combined context of the specified assistant from KazLLM API.

    Parameters:
    - assistant_id (str): The ID of the assistant.

    Returns:
    - str: The combined context of the assistant if successful.
    - None: If there was an error during the request.
    """
    # Construct the URL for retrieving assistant context
    url = f"{URL_KAZLLM}{assistant_id}/"

    # Send a GET request to the API to retrieve the context
    response = requests.get(url, headers=HEADERS)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the combined context from the JSON response
        return response.json().get("combined_context", "")
    else:
        # Print an error message if the request failed
        print(f"Error fetching assistant context: {response.status_code} - {response.text}")
        return None

# Retrieve and print the current context of the assistant
context = get_assistant_context(ASSISTANT_ID)
print("Current context:", context)