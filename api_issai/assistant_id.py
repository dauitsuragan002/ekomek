import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve API key from environment variables
API_KEY = os.environ.get('API_RESPONSE')
# Set the Assistant ID (replace 'ASSISTANT_ID' with your actual ID)
ASSISTANT_ID = 'ASSISTANT_ID'  # Example: '12'

# Base URL for the KazLLM API
URL_KAZLLM = "https://apikazllm.nu.edu.kz/assistant/"

# Function to check existing assistants or create a new one
async def check_or_create_assistant():
    """
    Checks for existing assistants via the KazLLM API.
    If no assistants are found, creates a new assistant.

    Returns:
    - str: The ID of the found or newly created assistant.
    - None: If there was an error during the request.
    """

    # Define request headers with authorization
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "accept": "application/json"
    }

    # Send a GET request to fetch existing assistants
    response = requests.get(URL_KAZLLM, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        assistants = response.json()
        
        # If assistants exist, return the ID of the first one
        if assistants:
            assistant_id = assistants[0]["id"]
            print(f"Assistant found with ID: {assistant_id}")
            return assistant_id
        else:
            # If no assistants found, create a new one
            data = {
                "name": "eKömek",
                "description": "eKömek Telegram Bot Assistant",
                "temperature": 0.7,
                "max_tokens": 500,
                "model": "KazLLM",
                "system_instructions": "KazLLM bot assistant",
                "context": ""
            }
            
            # Send a POST request to create a new assistant
            create_response = requests.post(URL_KAZLLM, headers=headers, json=data)
            
            # Check if the assistant was created successfully
            if create_response.status_code == 201:
                new_assistant = create_response.json()
                assistant_id = new_assistant["id"]
                print(f"New Assistant created with ID: {assistant_id}")
                return assistant_id
            else:
                # Print an error message if assistant creation failed
                print(f"Error creating assistant: {create_response.status_code}")
                return None
    else:
        # Print an error message if fetching assistants failed
        print(f"Error fetching assistants: {response.status_code}")
        return None

# Main function execution
if __name__ == "__main__":
    # Run the function to check or create an assistant
    response = check_or_create_assistant()
    print(f"ASSISTANT ID: {response}")
