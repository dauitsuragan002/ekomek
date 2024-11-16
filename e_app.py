import io, os
from aiogram import types
from pydub import AudioSegment
import asyncio
from aiogram.filters import Command
from aiogram import F
from aiogram.types import BufferedInputFile

# Importing necessary configurations and modules
from config import config
from modules.functions import *
from modules.bot import *
from modules.callbacks import *
from modules.commands import *

# Register command handlers
dp.message.register(start_handler, Command('start'))
dp.message.register(lang_handler, Command('lang'))
dp.message.register(more_handler, Command('more'))
dp.message.register(info_handler, Command('info'))
dp.message.register(help_handler, Command('help'))

# Text message handler
@dp.message(F.text)
async def text_handler(message: types.Message):
    user_id = message.from_user.id
    try:
        # Notify user that bot is typing
        await bot.send_chat_action(message.chat.id, "typing")
        user_input = message.text
        # Get response from GPT bot
        bot_response = await gpt_bot_response(user_input)
        # Send response to user
        await message.answer(bot_response, parse_mode='Markdown')
    except Exception as e:
        print(f"Error Text Handler: {e}")

# Voice message handler
@dp.message(F.voice)
async def voice_handler(message: types.Message):
    try:
        user_id = message.from_user.id

        # Define file paths
        file = await bot.get_file(message.voice.file_id)
        file_name = f"file_{message.voice.file_unique_id}.oga"
        file_path_oga = os.path.join("tmp", "voice", file_name)
        file_path_wav = os.path.splitext(file_path_oga)[0] + ".wav"

        # Ensure the "tmp/voice" directory exists
        os.makedirs(os.path.dirname(file_path_oga), exist_ok=True)
        
        # Download the voice message
        await bot.download_file(file.file_path, destination=file_path_oga)

        # Check if the file was downloaded successfully
        if not os.path.exists(file_path_oga):
            await message.reply("Failed to download the voice message. Please try again.")
            return

        # Convert the OGG file to WAV format
        audio = AudioSegment.from_ogg(file_path_oga)
        audio.export(file_path_wav, format="wav")

        await bot.send_chat_action(message.chat.id, "record_voice")
        # Recognize speech from the WAV file
        audio_base64 = convert_audio_to_base64(file_path_wav)
        recognized_text, language = await recognize_speech(user_id, audio_base64)
        recognized_text = recognized_text.capitalize()

        if not recognized_text:
            await message.answer("Could not recognize your speech.", parse_mode='Markdown')
            return

        # Get the bot response and detect the language
        bot_response = await gpt_bot_response(recognized_text)

        # Synthesize the response and send it as a voice message
        audio_stream = io.BytesIO()
        await synthesize_speech(bot_response, audio_stream, language)
        audio_stream.seek(0)
        voice_file = BufferedInputFile(audio_stream.read(), filename="response.wav")
        await bot.send_voice(
                chat_id=message.chat.id,
                voice=voice_file,
                reply_to_message_id=message.message_id,
                caption = f"You: {recognized_text}\n" + f"\neKömek: " + bot_response,
                parse_mode='Markdown')
    except Exception as e:
        bot_response = None
        if "API error: 500 - Internal Server Error" in str(e):
            print(f"Error in voice handler: {e}")
        else:
            print(f"Unexpected error in voice handler: {e}")
        if bot_response:
            await message.reply(
                f"You: {recognized_text}\n\neKömek: {bot_response}", parse_mode='Markdown'
            )
        else:
            await message.reply(
                f"Unexpected error in voice handler:", parse_mode='Markdown'
            )
    finally:
        # Safely remove the temporary files if they exist
        if os.path.exists(file_path_oga):
            os.remove(file_path_oga)
        if os.path.exists(file_path_wav):
            os.remove(file_path_wav)

# Main function to start the bot
async def main():
    try:
        print('Update successfully!')
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Error in main:  {e}")

# Start the main loop
if __name__ == "__main__":
    folder_path = 'tmp\\voice'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    asyncio.run(main())