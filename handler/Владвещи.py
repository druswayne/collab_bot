from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command

@dp.message(F.text == 'Vпомоги мне с дз')
async def func_name_1(message: Message):
    await message.answer(text='нет, делай сам')

@dp.message(F.text == 'Vну пж мне очень надо')
async def func_name_1(message: Message):
    await message.answer(text='нет, можешь даже не мечтать')


@dp.message(F.text == 'Vах ты неблагодарны')
async def func_name_1(message: Message):
    await message.answer(text='ах я не благодарны')

@dp.message(F.text == 'Vну хотя бы таблицу умножения')
async def func_name_4(message: Message):
    Vtablizaumnoszheniya = FSInputFile('data/image/Vtablizaumnoszheniya.jpg')
    await message.answer_photo(Vtablizaumnoszheniya, caption='на, подавись, неуч')

@dp.message(F.text == 'Vну хотя бы таблицу менделеева')
async def func_name_4(message: Message):
    Vtablizamendeleeva = FSInputFile('data/image/Vtablizamendeleeva.jpg')
    await message.answer_photo(Vtablizamendeleeva, caption='на, подавись, неуч')

@dp.message(F.text == 'Vну хотя бы алфавит')
async def func_name_4(message: Message):
    Valfabet = FSInputFile('data/image/Valfabet.jpg')
    await message.answer_photo(Valfabet, caption='капец... алфавита не знаешь? бош')

@dp.message(F.text == 'Vспс ат душы в душу спс благодарен')
async def func_name_1(message: Message):
    await message.answer(text='не пиши мне больше')

@dp.message(Command('Vinfoall'))
async def func_name_4(message: Message):
    Vtablizaumnoszheniya = FSInputFile('data/image/Vtablizaumnoszheniya.jpg')
    Vtablizamendeleeva = FSInputFile('data/image/Vtablizamendeleeva.jpg')
    Valfabet = FSInputFile('data/image/Valfabet.jpg')
    await message.answer_photo(Valfabet, caption='на те алфавита')
    await message.answer_photo(Vtablizaumnoszheniya, caption='лови таблицу умножения')
    await message.answer_photo(Vtablizamendeleeva, caption='вот мб поможет тебе')

@dp.message(Command('Vanekdot1'))
async def func_name_4(message: Message):
    Vanekdot1 = FSInputFile('data/image/Vanekdot1.jpg')
    await message.answer_photo(Vanekdot1, caption='')

@dp.message(Command('Vanekdot2'))
async def func_name_4(message: Message):
    Vanekdot2 = FSInputFile('data/image/Vanekdot2.jpg')
    await message.answer_photo(Vanekdot2, caption='')

@dp.message(Command('Vanekdot3'))
async def func_name_4(message: Message):
    Vanekdot3 = FSInputFile('data/image/Vanekdot3.jpg')
    await message.answer_photo(Vanekdot3, caption='')

@dp.message(Command('Vanekdotall'))
async def func_name_4(message: Message):
    Vanekdot1 = FSInputFile('data/image/Vanekdot1.jpg')
    Vanekdot2 = FSInputFile('data/image/Vanekdot2.jpg')
    Vanekdot3 = FSInputFile('data/image/Vanekdot3.jpg')
    await message.answer_photo(Vanekdot1, caption='')
    await message.answer_photo(Vanekdot2, caption='')
    await message.answer_photo(Vanekdot3, caption='')