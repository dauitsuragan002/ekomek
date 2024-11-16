# 
import os
import speech_recognition as sr
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

load_dotenv()

token = os.environ.get('TOKEN')
API_KEY = os.environ.get('API_RESPONSE')
API_SOYLE = os.environ.get("API_SOYLE")
# Set the Assistant ID (#https://kazllm.nu.edu.kz/assistant/'ASSISTANT_ID', replace 'ASSISTANT_ID' with your actual ID )
ASSISTANT_ID = 'ASSISTANT_ID'  # Example: '12'

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
recognizer = sr.Recognizer()

# KazLLM, Soyle App API endpoint base urls
URL_KAZLLM = "https://apikazllm.nu.edu.kz/assistant/"
URL_SOYLE = "https://soyle.nu.edu.kz/external-api/v1/translate/text/"

# 
class config():
    character_storage = {}
    first_time_users = {}
    user_languages = {}
    first_time_audio ={}
    message_info = {}
    user_lang = {}
    assistant_id = {}

