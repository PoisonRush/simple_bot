from aiogram import Router, types, F
from aiogram.filters import Command
from keyboard import *
from config import logger

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Добро пожаловать в Pytorial!\nВыберите раздел, который хотели бы изучить:",
        reply_markup=get_start_kb()
        )

@router.message(Command("info"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Вот кратвкая справка для работы с Pytorial:",
        reply_markup=get_start_kb()
        )
    
@router.callback_query(F.data == 'easy')
async def show_base_level(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Выберите тему: ",
        reply_markup=get_base_level_kb(),
    )
    await callback.answer()

@router.callback_query(F.data == 'medium')
async def show_medium_level(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Выберите тему: ",
        reply_markup=get_medium_level_kb(),
    )
    await callback.answer()

@router.callback_query(F.data == 'back')
async def back_to_main_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(reply_markup=get_start_kb())