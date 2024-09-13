import bot
import random



@bot.message_handler(commands=['game'])
def game(message):
    markup = '{"keyboard":[["Камень","Ножницы","Бумага"]],"one_time_keyboard":true}'
    bot.send_message(message.chat.id, 'Выберите: Камень, Ножницы или Бумага', reply_markup=markup)
    bot.register_next_step_handler(message, play_game)

def play_game(message):
    player_choice = message.text.lower()
    choices = ['камень', 'ножницы', 'бумага']
    if player_choice not in choices:
        bot.send_message(message.chat.id, 'Неверный выбор. Пожалуйста, выберите Камень, Ножницы или Бумага.')
        bot.register_next_step_handler(message, play_game)
        return
    bot_choice = random.choice(choices)
    result = determine_winner(player_choice, bot_choice)
    bot.send_message(message.chat.id, f'Вы выбрали {player_choice.capitalize()}, бот выбрал {bot_choice.capitalize()}. {result}')
    ask_play_again(message)

def determine_winner(player, bot):
    if player == bot:
        return 'Это ничья! Введите /start для перехода в меню.'
    elif (player == 'камень' and bot == 'ножницы') or \
         (player == 'ножницы' and bot == 'бумага') or \
         (player == 'бумага' and bot == 'камень'):
        return 'Вы победили! Введите /start для перехода в меню.'
    else:
        return 'Бот победил! Введите /start для перехода в меню.'

def ask_play_again(message):
    markup = '{"keyboard":[["Да","Нет"]],"one_time_keyboard":true}'
    bot.send_message(message.chat.id, 'Хотите еще раз?', reply_markup=markup)
    bot.register_next_step_handler(message, play_again)

def play_again(message):
    if message.text.lower() == 'да':
        game(message)
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Возвращайтесь в главное меню, введя /start.')
    else:
        bot.send_message(message.chat.id, 'Выберите "Да" или "Нет".')
        bot.register_next_step_handler(message, play_again)



bot.polling(none_stop=True)