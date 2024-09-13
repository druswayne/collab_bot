import random
import bot
from loader import dp, Bot
from aiogram import F
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram.filters import Command


@dp.message(Command('game'))
def get_user_choice():
    user_choice = input("Выберите: камень, ножницы, бумага: ").lower()
    while user_choice not in ['камень', 'ножницы', 'бумага']:
        print("Неправильный выбор. Попробуйте снова.")
        user_choice = input("Выберите: камень, ножницы, бумага: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return "Вы выиграли!"
    else:
        return "Вы проиграли!"

def play_game():
    print("Давайте сыграем в 'Камень, ножницы, бумага'!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nВы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(f"\n{result}")

if __name__ == "__main__":
    play_game()