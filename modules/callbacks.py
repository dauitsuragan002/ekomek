import logging

from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import *
from modules.commands import *
from modules.functions import *
from modules.lang.translater import *

@dp.callback_query(lambda query: query.data in ["info_cmd","help_cmd","more_cmd"])
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data
    message = callback_query.message
    builder = InlineKeyboardBuilder()
    text = 'Сәлем, бір қателік кетті( Қазір жөндеймін!'
    builder.row(InlineKeyboardButton(text='« Артқа', callback_data='cmd'))
    if data == "help_cmd":
        text=handler_texts('help_handler')
    elif data == "info_cmd":
        text=handler_texts('info_handler')
    elif data == "more_cmd":
        text=handler_texts('more_handler')
    await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=text, reply_markup=builder.as_markup())

@dp.callback_query(lambda query: query.data in ["menu", "lang_cmd", "close_menu", 'cmd'])
async def process_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data
    builder = InlineKeyboardBuilder()
    
    message = callback_query.message
    if data == "menu":
        buttons = [
            [InlineKeyboardButton(text='🧑‍💻 Командалар', callback_data='cmd')],
            [InlineKeyboardButton(text='🔼 Мәзірді жабу', callback_data='close_menu')]
            ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        text = "Сәлем! Мен KazLLM тілдік моделінің көмегімен жұмыс жасаймын.\n\nМаған орнатылған негізгі командалар осы белгі '/' арқылы немесе \"Меню\" батырмасы арқылы орындылады." + "\n\nТөменде боттың мәзірі көрсетілген👇"
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id, 
            message_id=callback_query.message.message_id,  
            text=text,
            reply_markup=keyboard,
            parse_mode='Markdown')
    elif data == "close_menu":
        builder = InlineKeyboardBuilder()
        builder.row(InlineKeyboardButton(text='🔽 Мәзір', callback_data='menu'))
        text='Дисклеймер: бот оқу-танысу үшін жасалынған.\n\n Мен KazLLM тілдік моделінің көмегімен жұмыс жасаймын'
        await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=text, reply_markup=builder.as_markup())
    elif data == "lang_cmd":
        text = handler_texts('lang_hanlder')
        change_user_languages = config.user_languages.get(user_id, '')
        # print("call change_user_languages :",change_user_languages )
        if change_user_languages:
            language_code, user_language = change_user_languages
            user_id = message.from_user.id

            builder = InlineKeyboardBuilder()
            check_mark = "✅"
            if not config.first_time_users.get(user_id, False):
                builder.row(InlineKeyboardButton(text=f"Қазақ тілі {check_mark}", callback_data="kk-KZ"),),
                builder.row(InlineKeyboardButton(text=f"Русский {check_mark if change_user_languages == 'ru-RU' else ''}", callback_data="ru-RU"),),
                builder.row(InlineKeyboardButton(text=f"English {check_mark if change_user_languages == 'en-US' else ''}", callback_data="en-US")),
                builder.row (InlineKeyboardButton(text='« Артқа', callback_data='menu'),),
                config.first_time_users[user_id] = True
            else:
                builder.row(InlineKeyboardButton(text=f"Қазақ тілі {check_mark if language_code == 'kk-KZ' else ''}", callback_data="kk-KZ"),),
                builder.row(InlineKeyboardButton(text=f"Русский {check_mark if language_code == 'ru-RU' else ''}", callback_data="ru-RU"),),
                builder.row(InlineKeyboardButton(text=f"English {check_mark if language_code == 'en-US' else ''}", callback_data="en-US"))
                builder.row (InlineKeyboardButton(text='« Артқа', callback_data='menu'),),
            await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=text, reply_markup=builder.as_markup())
        else:
            keyboard = get_keyboard_markup_lang(config.user_languages.get(user_id, ""))
            await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=text, reply_markup=keyboard)
    elif data == "cmd":
        builder = InlineKeyboardBuilder()
        text = "Ботта орналасқан командалар тізімі 👇"
        builder.row (
            InlineKeyboardButton(text=f"➕ Көмек", callback_data="help_cmd"),)
        # builder.row(InlineKeyboardButton(text='🗣 Детектор - тілі', callback_data='lang_cmd'))
        builder.row(InlineKeyboardButton(text=f"ℹ️ Ақпарат", callback_data="info_cmd"),)
        builder.row(InlineKeyboardButton(text=f"Басқа", callback_data="more_cmd"),)
        builder.row(InlineKeyboardButton(text='« Мәзір', callback_data='menu'))
        await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=text, reply_markup=builder.as_markup())

@dp.callback_query(lambda query: query.data in ["kk-KZ", "ru-RU", "en-US"])
async def handle_language_callback(callback_query: types.CallbackQuery):
    
    callback_data = callback_query.data

    check_mark = "✅"

    language_code = "kk-KZ"
    user_language = "Қазақ тілі"

    # Проверяем, какая кнопка была нажата
    if callback_data == "kk-KZ":
        # Обработка выбора языка казахский
        await callback_query.answer(f"{check_mark} Қазақ тілі орнатылды.")
        language_code = "kk-KZ"
        user_language = "Қазақ тілі"

    elif callback_data == "ru-RU":
        # Обработка выбора языка русский
        await callback_query.answer(f"{check_mark} Язык установлен на русский.")
        language_code = "ru-RU"
        user_language = "Русский"

    elif callback_data == "en-US":
        # Обработка выбора языка английский
        await callback_query.answer(f"{check_mark} The language has been set to English.")
        language_code = "en-US"
        user_language = "English"

    # Сохраняем выбор пользователя в словаре
    user_id = callback_query.from_user.id
    save_language = (language_code, user_language)
    config.user_languages[user_id] = save_language
    config.first_time_users[user_id] = True

    # Обновляем текст кнопки с добавлением галочки
    keyboard = get_keyboard_markup_lang(config.user_languages.get(user_id, ""))
    await callback_query.message.edit_text(
        f"{callback_query.message.text}",
        reply_markup=keyboard,
    )