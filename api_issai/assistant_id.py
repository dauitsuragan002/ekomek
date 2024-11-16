import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key from environment variables
API_KEY = os.environ.get('API_RESPONSE')
URL_KAZLLM = "https://apikazllm.nu.edu.kz/assistant/"

# Function to check for existing assistants or create a new one
def check_or_create_assistant():
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "accept": "application/json"
    }

    # Fetch existing assistants
    response = requests.get(URL_KAZLLM, headers=headers)
    if response.status_code == 200:
        assistants = response.json()
        if assistants:
            assistant_id = assistants[0]["id"]
            print(f"Assistant found with ID: {assistant_id}")
            return assistant_id
        else:
            # If no assistants exist, create a new one
            data = {
                "name": "eKömek-0.0.2",
                "description": "eKömek Telegram Bot Assistant",
                "temperature": 1,
                "max_tokens": 1000,
                "model": "KazLLM",
                "system_instructions": "You are eKömek, a virtual expert on the legislation of the Republic of Kazakhstan.",
                "context": ""
            }
            create_response = requests.post(URL_KAZLLM, headers=headers, json=data)
            if create_response.status_code == 201:
                new_assistant = create_response.json()
                assistant_id = new_assistant["id"]
                print(f"New Assistant created with ID: {assistant_id}")
                return assistant_id
            else:
                # Print error status and response content for diagnostics
                print(f"Error creating assistant: {create_response.status_code}")
                print(f"Response content: {create_response.text}")
                return None
    else:
        # Print error status if unable to fetch assistants
        print(f"Error fetching assistants: {response.status_code}")
        print(f"Response content: {response.text}")
        return None

if __name__ == "__main__":
    response = check_or_create_assistant()
    print(f"ASSISTANT ID's: {response}")