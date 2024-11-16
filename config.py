import os
import speech_recognition as sr
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

# Load environment variables from the .env file (API key, Assistant ID, etc.)
load_dotenv()
token = os.environ.get('TOKEN') # Token telegram @BotFather
API_KEY = os.environ.get('API_RESPONSE') #KazLLM API-KEY

# Set the Assistant ID (#https://kazllm.nu.edu.kz/assistant/'ASSISTANT_ID', replace 'ASSISTANT_ID' with your actual ID )
ASSISTANT_ID = 'ASSISTANT_ID'  # Example: '12'

# initialiation telegram bot 
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
recognizer = sr.Recognizer()

# KazLLM API endpoint base_url
URL_KAZLLM = "https://apikazllm.nu.edu.kz/assistant/"

# class for storage
class config():
    first_time_users = {}
    user_languages = {}
    first_time_audio ={}
    user_lang = {}
    assistant_id = {}
