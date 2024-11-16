import requests

from config import *  # Import all configurations like API_KEY, URL_KAZLLM, ASSISTANT_ID

# Function to get a response from the bot
async def gpt_bot_response(user_prompt):
    # Set up the headers for the API request
    headers = {
        "Authorization": f"Api-Key {API_KEY}",  # API key for authentication
        "accept": "application/json",           # Accept JSON response
        "Content-Type": "application/json"      # Send data as JSON
    }
    
    # Prepare the data payload with the user's prompt
    data = {
        "text_prompt": user_prompt
    }

    # Construct the URL for the API endpoint
    url = f"{URL_KAZLLM}{ASSISTANT_ID}/interactions/"
    
    # Make a POST request to the API
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 201:
        # Extract the bot's response from the JSON data
        bot_response = response.json()["vllm_response"]["content"]
        return bot_response
    else:
        # Print an error message if the request failed
        print(f"Error fetching response: {response.status_code}")
        return "Error: Unable to fetch response."