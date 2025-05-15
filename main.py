import asyncio
import os

from config import logger
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from handlers import basic

load_dotenv()

async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()

    dp.include_router(basic.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())