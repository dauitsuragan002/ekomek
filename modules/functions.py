from config import recognizer, config

import speech_recognition as sr
import edge_tts, re, tempfile, logging

# Func Text To SOILE TTS
async def synthesize_speech(text):
    pass

# Func recognize_speech
async def recognize_speech(file_path_wav, message, user_id):
    change_user_languages = config.user_languages.get(user_id, ('kk-KZ', 'Қазақ тілі'))
    with sr.AudioFile(file_path_wav) as source:
        try:
            audio_data = recognizer.record(source)
            if change_user_languages:
                language_code, user_language = change_user_languages
            text = recognizer.recognize_google(audio_data, language = language_code)
            return text
        except sr.UnknownValueError:
            print("Речь не распознана")
            return None
        except sr.RequestError as e:
            print(f"Ошибка запроса к Google Web Speech API: {e}")
            return None   

#Function return bot command  handler texts 
def handler_texts(handler_name):
    if handler_name == 'start_handler':
        text = 'Сәлем! Мен eKömek ботымын. Сұрағыңызды жазыңыз.'
    elif handler_name == 'more_handler':
        text = "\tМенің басқа да боттарым. Таныс болыңыз!\n\n 1.Ағылшын тілін ЖИ мен бірге үйрену - @englishkaz_bot\n\n2.Мәтінді қазақша тегін сөйлету - @qaztts_bot"
    elif handler_name == 'lang_hanlder':
        text = "Бот интерфейсінде қазақ тілі орнатылған 🇰🇿.\n\nАл, 🗣 дауыстық хабарламаны қандай тілде екенін анықтау үшін, тілді таңдаңыз. 👇"
    elif handler_name == 'help_handler':
        text = "\n/lang - 🗣 Дауыс детекторының тілін таңдау. \n/info - ЖИ Бот туралы ақпарат. \n/more - Менің басқада бот достарым.\n"
    elif handler_name == 'info_handler':
        text = "Телеграм бот eKömek KazLLM API қолданып жасалынған"
    return text
