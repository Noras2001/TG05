import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from datetime import datetime
import requests
import random

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


def get_random_movie():
    url = "https://imdb-top-100-movies.p.rapidapi.com/"
    headers = {
        "x-rapidapi-key": "9f01634ab6msh8678df376b20c2ap1876edjsn997e60a027b9",
        "x-rapidapi-host": "imdb-top-100-movies.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nЯ бот для получения рандомного фильма!")


@dp.message(Command("movie"))
async def get_movie(message: Message):
    movies = get_random_movie()
    if movies:
        random_movie = random.choice(movies)
        title = random_movie.get('title', 'Нет информации')
        year = random_movie.get('year', 'Нет информации')
        description = random_movie.get('description', 'Нет описания')
        image_url = random_movie.get('image', None)  # Assuming 'image' is the key for image URL

        response_message = f"{title} - {year}\n\n{description}"
        if image_url:
            await message.answer_photo(photo=image_url, caption=response_message)
        else:
            await message.answer(response_message)
    else:
        await message.answer("Не удалось получить данные о фильмах. Попробуйте позже.")

async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())