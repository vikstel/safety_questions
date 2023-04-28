import random
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command
from config import TOKEN

token = TOKEN
bot = Bot(token, parse_mode='HTML')
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_commands(message: Message):
    random_number = random.choices([i for i in range(1, 89)], k=10)
    for num in random_number:
        with sqlite3.connect('questions.db') as con:
            cur = con.cursor()
            cur.execute("""SELECT question, answer FROM question WHERE id = (?)""", (num,))
            text_fetchall = cur.fetchall()
            text_to_answer = f'<b>{text_fetchall[0][0]}</b>\n' \
                             f'{text_fetchall[0][1]}'
            await message.answer(text_to_answer)


if __name__ == '__main__':
    dp.run_polling(bot)
