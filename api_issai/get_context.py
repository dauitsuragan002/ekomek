import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key from environment variables
API_KEY = os.environ.get('API_RESPONSE')
ASSISTANT_ID = 'ASSISTANT_ID'  # Replace 'ASSISTANT_ID' with your actual assistant ID

# Base URL for the KazLLM API
URL_KAZLLM = "https://apikazllm.nu.edu.kz/assistant/"

# Configuration for the request headers
HEADERS = {
    "Authorization": f"Api-Key {API_KEY}",
    "accept": "application/json"
}

# Function to get the context of an assistant
def get_assistant_context(assistant_id):
    url = f"{URL_KAZLLM}{assistant_id}/"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("combined_context", "")
    else:
        print(f"Error retrieving assistant context: {response.status_code} - {response.text}")
        return None

# Retrieve and print the current context
context = get_assistant_context(ASSISTANT_ID)
print("Current context:", context)