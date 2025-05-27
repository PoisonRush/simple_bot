from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_start_kb():
    """Кнопки для главного меню"""
    buttons = [
        [InlineKeyboardButton(text='1. Базовый уровень', callback_data='easy')],
        [InlineKeyboardButton(text='2. Средний уровень', callback_data='medium')],
        [InlineKeyboardButton(text='3. Продвинутый уровень', callback_data='hard')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_base_level_kb():
    """Кнопки для базового уровня"""
    buttons = [
        [InlineKeyboardButton(text='1. Объявление переменных', callback_data='variables')],
        [InlineKeyboardButton(text='2. Типы данных', callback_data='datatypes')],
        [InlineKeyboardButton(text='3. Операторы', callback_data='operators')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_medium_level_kb():
    """Кнопки для среднего уровня"""
    buttons = [
        [InlineKeyboardButton(text='1. Функции', callback_data='functions')],
        [InlineKeyboardButton(text='2. Файлы', callback_data='files')],
        [InlineKeyboardButton(text='3. Модули', callback_data='modules')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)