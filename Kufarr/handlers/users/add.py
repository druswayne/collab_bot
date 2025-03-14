from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start, kb_started
from loader import router, cursor, con, scheduler, bot
from aiogram import F
from script.parser import parser_update, parse_website
import json

class FormUrl(StatesGroup):
    url = State()

@router.message(F.text == 'Добавить ссылку')
async def fun_start(message: Message, state:FSMContext):
    id_user = message.chat.id
    cursor.execute('SELECT id FROM users where id=(?)', [id_user])
    data1 = cursor.fetchall()
    cursor.execute('SELECT url FROM users where id=(?)', [id_user])
    data2 = cursor.fetchall()
    if data2:
        builder = ReplyKeyboardBuilder()
        for button in kb_started:
            builder.add(button)
        builder.adjust(1)
        await message.answer(text='Вы уже добавили свою ссылку', reply_markup=builder.as_markup(resize_keyboard=True))
    else:
        await state.set_state(FormUrl.url)
        await message.answer('Отправьте ссылку на категории, за которыми хотите следить',
                             reply_markup=types.ReplyKeyboardRemove())

@router.message(FormUrl.url)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(url=message.text)
    data = await state.get_data()
    url = data['url']
    id_user = message.chat.id
    con.commit()
    await state.clear()
    task = scheduler.add_job(parser_update,
                              trigger='interval',
                              seconds=10,
                              kwargs={'user_id': id_user, 'bot': bot})
    cursor.execute('INSERT INTO users (id, url, id_task) VALUES (?,?, ?)', [id_user, url, task.id])
    con.commit()

    class_names = "styles_wrapper__5FoK7"
    inner_class_name = "styles_secondary__MzdEb"
    result = parse_website(data['url'], class_names, inner_class_name)[:5]
    with open(f'data/{id_user}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(result))

    builder = ReplyKeyboardBuilder()
    for button in kb_started:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text="Парсер запущен!", reply_markup=builder.as_markup(resize_keyboard=True))

