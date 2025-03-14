import requests
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bs4 import BeautifulSoup
from loader import cursor, Bot
import json
from aiogram import types

def parse_website(url, class_name, inner_class_name):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Ошибка запроса: {response.status_code}')
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    parser_data = []
    elements = soup.find_all(class_=class_name)
    for element in elements:
        text = element.get_text(strip=True)

        img_tag = element.find('img')
        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None

        inner_element = element.find(class_=inner_class_name)
        inner_text = inner_element.get_text(strip=True) if inner_element else None

        link_url = element.get('href') if element.has_attr('href') else None
        link_url = link_url.split('?')[0]

        parser_data.append([text, img_url, inner_text, link_url])
    return parser_data

async def parser_update(user_id, bot:Bot):
    cursor.execute('SELECT url FROM users where id=(?)', [user_id])
    url = cursor.fetchall()
    class_names = "styles_wrapper__5FoK7"
    inner_class_name = "styles_secondary__MzdEb"
    results = parse_website(url[0][0], class_names, inner_class_name)[:5]
    with open(f'data/{user_id}.json', 'r', encoding='utf-8') as file:
        old = json.loads(file.read())
    data_new = []
    for result in results:
        if result not in old:
            data_new.append(result)
    if len(data_new)>0:
        with open(f'data/{user_id}.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(data_new))
        for mess in data_new:
            builder = InlineKeyboardBuilder()
            builder.add(types.InlineKeyboardButton(text='открыть объявление',
                                                   web_app=WebAppInfo(url=mess[3])))
            await bot.send_photo(caption=f'{mess[0]}\n{mess[2]}',
                                 chat_id=user_id, photo=mess[1],
                                 reply_markup=builder.as_markup(resize_keyboard=True))