import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file (API key, Assistant ID, etc.)
load_dotenv()

# Retrieve API key from environment variables
API_KEY = os.environ.get('API_RESPONSE')
# Set the Assistant ID (#https://kazllm.nu.edu.kz/assistant/'ASSISTANT_ID', replace 'ASSISTANT_ID' with your actual ID )
ASSISTANT_ID = 'ASSISTANT_ID'  # Example: '12'

# Base URL for the KazLLM API
URL_KAZLLM = "https://apikazllm.nu.edu.kz/assistant/"

# Define headers for the API request
HEADERS = {
    "Authorization": f"Api-Key {API_KEY}",
    "accept": "application/json"
}

# Function to upload a DOCX file as context to KazLLM API
def upload_docx_context(assistant_id, file_path):
    """
    Uploads a DOCX file to the KazLLM API as context.

    Parameters:
    - assistant_id (str): The ID of the assistant for which the context is being uploaded.
    - file_path (str): The path to the DOCX file to be uploaded.

    Returns:
    - dict: JSON response from the API if successful.
    - None: If there was an error during the upload process.
    """
    # Construct the full URL for the DOCX upload endpoint
    url = f"{URL_KAZLLM}{assistant_id}/upload-docx/"

    # Check if the specified file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found — {file_path}")
        return None

    try:
        # Open the DOCX file in binary read mode
        with open(file_path, "rb") as docx_file:
            # Prepare the file payload for the API request
            files = {
                "files": (os.path.basename(file_path), docx_file, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            }
            # Send a POST request to the API with headers and the file
            response = requests.post(url, headers=HEADERS, files=files)

        # Check the status code of the response
        if response.status_code == 200:
            # If successful, print a success message and return the JSON response
            print("DOCX file uploaded successfully!")
            return response.json()
        else:
            # If the response indicates an error, print the status code and error message
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        # Handle any exceptions that occur during the process
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Get the absolute path to the DOCX file
    file_path = os.path.abspath('modules/path/context.docx')

    # Print the file path for debugging purposes
    print(f"File path: {file_path}")

    # Call the function to upload the DOCX context
    result = upload_docx_context(ASSISTANT_ID, file_path)
    
    # Check if the result was successful
    if result:
        # Print the combined context from the API response
        print("Uploaded context:", result.get("combined_context", "Context is empty"))
    else:
        # Print an error message if the upload failed
        print("An error occurred while uploading the context.")
