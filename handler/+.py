from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command, Text
flag_num_1 = False
flag_num_2 = False
a = 0
b = 0

@dp.message(F.text == '+')
async def sum_func1(message: Message):
    await message.answer(text='Введи первое число #')



@dp.message(Text(startswith='#'))
async def func_sum_1(message: Message):
    global flag_num_1,a,b,c, flag_num_2
    if flag_num_1 == False and flag_num_2 == False:
        a = int(message.text[1:])
        print(a)
        flag_num_1 = True
        await message.answer(text='Введи второе число #')
    elif flag_num_2 == False and flag_num_1 == True:
        b = int(message.text[1:])
        print(b)
        flag_num_2 = True
        c = a+b
        flag_num_2 = False
        flag_num_1 = False
        a=0
        b=0
        c=0
        await message.answer(text=f'Твой результат:{c}')








