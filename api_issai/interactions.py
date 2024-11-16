import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key from environment variables
API_KEY = os.environ.get('API_RESPONSE')
# Set the Assistant ID (replace 'ASSISTANT_ID' with your actual ID)
ASSISTANT_ID = 'ASSISTANT_ID'  # Example: '12'
URL_KAZLLM = f"https://apikazllm.nu.edu.kz/assistant/{ASSISTANT_ID}/interactions/"

# Configuration for the request headers
HEADERS = {
    "Authorization": f"Api-Key {API_KEY}",
    "accept": "application/json"
}

# Function to test file upload
def test_file_upload(file_path):
    """
    Uploads a file to the assistant's interaction endpoint.

    :param file_path: Path to the file to be uploaded
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, 'rb') as file:
        files = {
            "file_prompt": (os.path.basename(file_path), file)
        }
        response = requests.post(URL_KAZLLM, headers=HEADERS, files=files)
        print(f"Response: {response.status_code}, Text: {response.text}")

# Example usage
test_file_upload("contexts/context.docx")