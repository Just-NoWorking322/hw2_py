import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import token 

bot = Bot(token=token)
dp = Dispatcher()

random_number = random.randint(1, 3)

@dp.message(CommandStart())
async def start(message: types.Message):
    global random_number
    random_number = random.randint(1, 3)  
    await message.answer("угадайте число от 1 до 3")

@dp.message()
async def guess_number(message: types.Message):
    global random_number
    try:
        user_guess = int(message.text)
        if 1 <= user_guess <= 3: 
            if user_guess == random_number:
                await message.answer("Вы Ванга")
                random_number = random.randint(1, 3) 
            else:
                await message.answer("Пробйте еще раз!")
        else:
            await message.answer("Введите число от 1 до 3")
    except ValueError:
        await message.answer("Введите число от 1 до 3")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
