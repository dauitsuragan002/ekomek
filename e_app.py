# import libs and functions
import os
from aiogram import  types
import asyncio
from aiogram.filters import Command
from aiogram import F

from modules.bot import *
from modules.callbacks import *
from modules.commands import *

dp.message.register(start_handler, Command('start'))
dp.message.register(more_handler, Command('more'))
dp.message.register(info_handler, Command('info'))
dp.message.register(help_handler, Command('help'))

# text handler 
@dp.message(F.text)
async def text_handler(message: types.Message):
    user_id = message.from_user.id
    try:
        await bot.send_chat_action(message.chat.id, "typing")
        user_input = message.text
        bot_response = await gpt_bot_response(user_input)
        await message.answer(bot_response, parse_mode='Markdown')
    except Exception as e:
        print(f"Error Text Handler: {e}")

# audio handler 
@dp.message(F.voice)
async def voice_handler(message: types.Message):
    await synthesize_speech('text')

async def main():
    try:
        print('Update succesfully!')
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка on main:  {e}")

if __name__ == "__main__":
    folder_path = 'tmp\\voice'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    asyncio.run(main())