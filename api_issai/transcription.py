import base64
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from a .env file into the environment
load_dotenv()

# Retrieve the API key for the Soyle API from environment variables
API_SOYLE = os.environ.get("API_SOYLE")

# Function to convert an audio file to base64
def convert_audio_to_base64(audio_file_path):
    """
    Converts an audio file to a base64 string.
    
    :param audio_file_path: Path to the audio file
    :return: Base64 string representing the audio file
    """
    with open(audio_file_path, "rb") as audio_file:
        audio_base64 = base64.b64encode(audio_file.read()).decode('utf-8')
    return audio_base64

# Function to send a request to translate audio
def translate_audio(audio_base64, target_language, output_format="text", output_voice=None):
    """
    Sends a request to translate audio using the API.

    :param audio_base64: Audio file in base64 format
    :param target_language: Target language for translation
    :param output_format: Output format (text or audio)
    :param output_voice: Voice for audio (male or female), if output is audio
    :return: Translated text or audio (in base64 format)
    """
    url = "https://soyle.nu.edu.kz/external-api/v1/translate/audio/"

    # Prepare data for the request
    data = {
        "target_language": target_language,
        "audio": audio_base64,
        "output_format": output_format
    }
    
    # If a voice is specified for audio
    if output_voice:
        data["output_voice"] = output_voice

    # Headers for the request with API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_SOYLE}"  # Add API key to the header
    }

    # Send POST request to the API
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Check the API response
    if response.status_code == 200:
        result = response.json()
        if output_format == "text":
            return result.get("text")  # Translated text
        elif output_format == "audio":
            return result.get("audio")  # Translated audio in base64
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage:
if __name__ == "__main__":
    # 1. Convert the audio file to base64
    audio_file_path = "kaz_tts_output.wav"  # Specify the path to your audio file
    audio_base64 = convert_audio_to_base64(audio_file_path)

    # 2. Define the target language for translation and parameters
    target_language = "kaz"  # Target language for translation (e.g., "kaz", "eng", "tur", "rus")
    output_format = "text"  # Output format ("text" or "audio")
    output_voice = "male"  # Optional: "male" or "female", if output is audio

    # 3. Translate the audio
    translated_result = translate_audio(audio_base64, target_language, output_format, output_voice)

    # 4. Print the result
    if output_format == "text":
        print("Translated text:", translated_result)
    elif output_format == "audio":
        print("Translated audio in base64:", translated_result)