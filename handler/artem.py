import logging
import asyncio
import requests
import aiogram
from PIL.ImagePalette import random
import random
from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile, Update
from aiogram.filters import Command
from aiogram import types
import urllib
import urllib.request



def get_random_meme():
    url = 'https://api.imgflip.com/get_memes'
    response = requests.get(url)
    memes = response.json()['data']['memes']
    # Возвращаем случайный мем
    return memes[random.randint(0, 105)]  # Здесь можно добавить случайный выбор

def download_image(url, file_name):
    # Отправляем GET-запрос на указанный URL
    response = requests.get(url)

    # Проверяем, что запрос был успешным
    if response.status_code == 200:
        # Открываем файл для записи в бинарном режиме
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Изображение сохранено как {file_name}")
    else:
        print("Не удалось загрузить изображение. Статус код:", response.status_code)

@dp.message(Command('daily_shablon_memas'))
async def func_name_2(message: Message):
    url = get_random_meme()['url']
    response = requests.get(url)
    file_name = 'data/image/23434.jpg'
    if response.status_code == 200:
        # Открываем файл для записи в бинарном режиме
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Изображение сохранено как {file_name}")
    else:
        print("Не удалось загрузить изображение. Статус код:", response.status_code)

    image = FSInputFile('data/image/23434.jpg')
    await message.answer_photo(image, caption='держи рандомный шаблон для мема')