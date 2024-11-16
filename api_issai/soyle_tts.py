import requests
import base64
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_SOYLE = os.environ.get("API_SOYLE")
URL_SOYLE = "https://soyle.nu.edu.kz/external-api/v1/translate/text/"

# Define headers for the API request
HEADERS = {
    "Authorization": f"Api-Key {API_SOYLE}",
    "accept": "application/json",
    "Content-Type": "application/json"
}

def auto_kaz_tts(text):
    """
    Function to automatically generate Text-to-Speech (TTS) in the Kazakh language.

    Parameters:
    - text (str): The input text to be converted to speech.
    """
    # Define the payload for the API request
    data = {
        "source_language": "kaz",
        "target_language": "kaz",
        "text": text,
        "output_format": "audio",
        "output_voice": "female"
    }

    try:
        # Send a POST request to the TTS API
        response = requests.post(URL_SOYLE, headers=HEADERS, json=data)

        # Check the response status
        if response.status_code == 200:
            # Extract the audio content from the response
            audio_base64 = response.json().get("audio")
            if audio_base64:
                # Decode the base64 audio data
                audio_data = base64.b64decode(audio_base64)
                output_filename = "kaz_tts_output.wav"
                
                # Save the decoded audio data to a file
                with open(output_filename, "wb") as audio_file:
                    audio_file.write(audio_data)
                
                print(f"Audio file successfully saved: {output_filename}")
            else:
                print("Error: No audio content received.")
        else:
            # Print an error message if the request failed
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        # Handle any exceptions that occur during the process
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Predefined input text
    text = "Сәлем, бұл қазақ тілінде жасалған TTS мысалы."
    auto_kaz_tts(text)
