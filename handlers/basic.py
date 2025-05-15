from aiogram import Router, types
from aiogram.filters import Command
from keyboard import main_keyboard

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет, я простой бот! Нажми <code>/id</code>, что бы увидеть свой ID",
        parse_mode='HTML',
        reply_markup=main_keyboard(),
    )

@router.message(Command('id'))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Твой ID: <code>{message.from_user.id}</code>",
        parse_mode='HTML',
        reply_markup=main_keyboard(),
    )