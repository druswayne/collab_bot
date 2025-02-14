from aiogram.types import Message
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from loader import router, cursor, con
from aiogram import F

class Form_reg(StatesGroup):
    fio = State()
    numbers = State()
    email = State()
    age = State()

@router.message(F.text == "Регистрация")
async def start_reg_fun(message: Message, state:FSMContext):
    id_user = message.chat.id
    cursor.execute('SELECT id FROM users where id=(?)', [id_user])
    data = cursor.fetchall()
    if data:
        await message.answer(text="ты уже рег")
        return
    cursor.execute('SELECT status FROM start_reg')
    result = cursor.fetchall()[0][0]
    if result == 'False':
        await message.answer(text="Регистрация на розыгрыш завершена")
    else:
        await state.set_state(Form_reg.fio)
        await message.answer('Для начала введите ФИО полностью', reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_reg.fio)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await state.set_state(Form_reg.age)
    await message.answer("Введите свой возраст", reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_reg.age)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Form_reg.numbers)
    await message.answer("Введите номер телефона", reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_reg.numbers)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(numbers=message.text)
    await state.set_state(Form_reg.email)
    await message.answer("Введите свою почту", reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_reg.email)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    data = await state.get_data()
    fio = data['fio']
    age = data['age']
    numbers = data['numbers']
    email = data['email']
    user_id = message.chat.id
    cursor.execute("INSERT INTO users (FIO, numbers, email, age, id) VALUES (?, ?, ?, ?, ?)", (fio, numbers, email, age, user_id))
    con.commit()
    await state.clear()
