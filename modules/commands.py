from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import *
from modules.functions import *
from modules.bot import *

# Command /start
async def start_handler(message: types.Message):
    try:
        if message.chat.type == 'private':
            builder = InlineKeyboardBuilder()
            wlc_msg = handler_texts('start_handler')
            if ASSISTANT_ID:
                builder.row(InlineKeyboardButton(text='🔽 Мәзір', callback_data='menu'))
                await message.answer(text=wlc_msg,
                    reply_markup=builder.as_markup(),
                    parse_mode='Markdown')
            else:
                await message.reply("Қате: ассистент табылмады және жасалмады.")
    except Exception as e:
        print("Error in start_handler:", e)

# Command /info
async def info_handler(message: types.Message):
    if message.chat.type == 'private':
        info_text = handler_texts('info_handler')
        await message.answer(info_text)
    else:
        print("Not PRIVATE CHAT:", message.chat.type)

# Command /help
async def help_handler(message: types.Message):
    if message.chat.type == 'private':
        help_text = handler_texts('help_handler')
        await message.answer(help_text)
    else:
        print("Not a private chat")

# Command /more
async def more_handler(message: types.Message):
    if message.chat.type == 'private':
        builder = InlineKeyboardBuilder()
        builder.row(InlineKeyboardButton('« Артқа', callback_data='command'))
        more_text = handler_texts('more_handler')
        await message.answer(more_text, reply_markup=builder.as_markup())

# Command /lang
async def lang_handler(message: types.Message):
    try:
        user_id = message.from_user.id
        
        if message.chat.type == 'private':
            language_code = "kaz"
            
            builder = InlineKeyboardBuilder()
            check_mark = "✅"
            text = handler_texts('lang_hanlder')
            change_user_languages = config.user_languages.get(user_id, '')

            if change_user_languages:
                language_code, user_language = change_user_languages
            
            if not config.first_time_users.get(user_id, False):
                builder.row(InlineKeyboardButton(text=f"Қазақ тілі {check_mark}", callback_data="kaz"),)
                builder.row(InlineKeyboardButton(text=f"Русский {check_mark if change_user_languages == 'rus' else ''}", callback_data="rus"),)
                builder.row(InlineKeyboardButton(text=f"English {check_mark if change_user_languages == 'eng' else ''}", callback_data="eng"))
                builder.row(InlineKeyboardButton(text='« Артқа', callback_data='menu'),)
                config.first_time_users[user_id] = True  
                await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=builder.as_markup())
            else:
                keyboard = get_keyboard_markup_lang(config.user_languages.get(user_id, ""))
                await message.answer(text=text, reply_markup=keyboard)
    except Exception as e:
        print("Problem in lang_handler:", e)

def get_keyboard_markup_lang(selected_language: str) -> InlineKeyboardMarkup:
    check_mark = "✅"

    if selected_language:
        language_code, user_language = selected_language
    else:
        language_code = 'kaz'
        user_language = 'Қазақ тілі'

    buttons = [
        InlineKeyboardButton(text="Қазақ тілі", callback_data="kaz"),
        InlineKeyboardButton(text="Русский", callback_data="rus"),
        InlineKeyboardButton(text="English", callback_data="eng"),
        InlineKeyboardButton(text='« Артқа', callback_data='menu')
    ]
    
    for button in buttons:
        if button.callback_data == language_code:
            button.text = f"{user_language} {check_mark}"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons[i:i + 1] for i in range(0, len(buttons), 1)])
    return keyboard