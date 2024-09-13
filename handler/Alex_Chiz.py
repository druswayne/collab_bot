from distutils.text_file import TextFile

from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command, Text
from random import randint, random

A = ['Сейчас я вынесу вердикт. Помогите мне его не поднять, он тяжелый.',
     'Не все мысли материальны, например мысль попить пивка - идеальна.',
     'Кто в пробках постоял,  тот над мопедом не смеётся!',
     'Мама-вампир, Папа-оборотень. Сын не знает, по чьим стопам пойти, то ли в Налоговую, то ли в МВД. ,',
     'не бывает страшных женщин бывают очень пугливые мужчины ,',
     'Врач, который считает, что у Вас все в порядке, работает только в военкомате',
     'Работа это не волк, работа — ворк. А волк — ходить.',
     'Падает компьютер с 16-го этажа и думает: "Вот сейчас бы зависнуть... ',
     'Сидет драконы в баре один другому говорит: - жарко -а ты рот закрой ',
     '150+150=?']


@dp.message(F.text == '300')
async def func_name_1(message: Message):
    """
    обработчик, который реагирует на текст "Привет"
    """
    await message.answer('спроси у тракториста')


@dp.message(F.text == 'триста')
async def func_name_1(message: Message):
    """
    обработчик, который реагирует на текст "Привет"
    """
    await message.answer('спроси у тракториста')


@dp.message(F.text == 'Триста')
async def func_name_1(message: Message):
    """
    обработчик, который реагирует на текст "Привет"
    """
    await message.answer('спроси у тракториста')


@dp.message(F.text == 'анекдот')
async def func_name_2(message: Message):
    a = randint(1, 10)
    await message.answer(text=A[a - 1])


@dp.message(F.photo)
async def func_name_3(message: Message, bot: Bot):
    """
    обработчик, который реагирует на команду отправленные изображения
    """
    await bot.download(message.photo[-1],
                       f'data/image/{message.photo[-1].file_id}.jpg')
    await message.answer(text='Я сохранил твоё изображение')


game = True


@dp.message(Command('ИграВБота'))
async def func_name_4(message: Message):
    """
    обработчик, который реагирует на команду /photo
    """
    image = FSInputFile('data/image/3F3F_Skin-Default.png')

    await message.answer_photo(image, caption='Что это за боец из бабл квас\n начни свой ответ со слова ответ')



@dp.message(Text(startswith='ответ'))
async def func_name_4(message: Message):
    answer = message.text[6:]
    if answer == 'Фэнг':
        await message.answer('бро ты реально бравлер')
    else:
        await message.answer('Партия не довольна тобой')


@dp.message(Command('страшилка'))
async def func_name_2(message: Message):
    image = FSInputFile('data/image/1642598812177585946.png')

    await message.answer_photo(image,caption='БУУУУУУ!!!')
