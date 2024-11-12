import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import json 

#importing routers
from handlers.personal_actions import router as personal_router

logging.basicConfig(level=logging.INFO)
bot = Bot(token = json.load(open("config.json"))["token"] )

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("free video downloader ")

async def main():
    #registering routers
    dp.include_routers( personal_router )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
