import logging
import requests
import base64
import json

from config import *

# Function to synthesize speech
async def synthesize_speech(text, output_file, language):
    try:
        # Parameters for the API request
        data = {
            "source_language": language,
            "target_language": language,
            "text": text,
            "output_format": "audio",
            "output_voice": "female"
        }

        HEADERS = {
            "Authorization": f"Api-Key {API_SOYLE}",
            "accept": "application/json",
            "Content-Type": "application/json"
        }

        # Send request to Soyle API
        response = requests.post(URL_SOYLE, headers=HEADERS, json=data)

        # Check response status
        if response.status_code == 200:
            response_data = response.json()
            audio_hex = response_data.get("audio")

            if audio_hex:
                # Convert hex to Base64 and decode to audio file
                audio_base64 = hex_to_base64(audio_hex)
                audio_data = base64.b64decode(audio_base64)

                # Write audio data directly to BytesIO
                output_file.write(audio_data)
                output_file.seek(0)  # Move pointer to the start of the file

                logging.info("Audio successfully generated and written to BytesIO.")
            else:
                logging.error("Error: No audio content received.")
        else:
            logging.error(f"API error: {response.status_code} - {response.text}")

    except Exception as e:
        logging.error(f"An error occurred during speech synthesis: {e}")

# Function to convert hex string to Base64
def hex_to_base64(hex_string: str) -> str:
    """
    Convert a hex string to Base64.
    """
    byte_data = bytes.fromhex(hex_string)
    base64_data = base64.b64encode(byte_data)
    return base64_data.decode('utf-8')

# Function to recognize speech
async def recognize_speech(user_id, audio_base64):
    output_format = "text"
    change_user_languages = config.user_languages.get(user_id, ('kaz', 'Қазақ тілі'))
    target_language, user_language = change_user_languages

    url = "https://soyle.nu.edu.kz/external-api/v1/translate/audio/"

    # Prepare data for the request
    data = {
        "target_language": target_language,
        "audio": audio_base64,
        "output_format": output_format
    }
    
    # Headers for the request with API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_SOYLE}"
    }

    # Send POST request to the API
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Check the API response
    if response.status_code == 200:
        result = response.json()
        return result.get("text"), target_language
    else:
        return f"Ошибка: {response.status_code}, {response.text}"

# Function to convert audio file to Base64
def convert_audio_to_base64(audio_file_path):
    """
    Convert an audio file to a Base64 string.
    
    :param audio_file_path: Path to the audio file
    :return: Base64 string representing the audio file
    """
    with open(audio_file_path, "rb") as audio_file:
        audio_base64 = base64.b64encode(audio_file.read()).decode('utf-8')
    return audio_base64

# Function to handle text responses
def handler_texts(handler_name):
    if handler_name == 'start_handler':
        text = 'Сәлем! Мен eKömek ботымын. ҚР заңнамасы бойынша сұрағыңызды қойыңыз.'
    elif handler_name == 'more_handler':
        text = "Таныс болыңыз!\n\n 1.Ағылшын тілін ЖИ мен бірге үйрену - @englishkaz_bot\n\n2.Мәтінді қазақша тегін сөйлету - @qaztts_bot"
    elif handler_name == 'lang_hanlder':
        text = "Бот интерфейсінде қазақ тілі орнатылған 🇰🇿.\n\nАл, 🗣 дауыстық хабарламаны қандай тілде екенін анықтау үшін, тілді таңдаңыз. 👇"
    elif handler_name == 'help_handler':
        text = "\n/lang - 🗣 Дауыс детекторының тілін таңдау. \n/info - Бот туралы ақпарат. \n/more - Менің басқада бот достарым.\n"
    elif handler_name == 'info_handler':
        text = "Телеграм бот eKömek KazLLM API және Soyle App API қолданылып жасалған."
    return text