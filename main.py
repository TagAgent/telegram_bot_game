import random
import telebot
from local_settings import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я Карлсон. 
Я скрываю много секретов, ответы на них тебе никогда не узнать. 
Хахаххахахахаххахахахахахахаххахахахахахахахаха!
Я предлагаю тебе сыграть в "камень ножницы бумагу".
Меня никто не смог победить, .....
С первого раза точно никто не побеждал.
Ну чтоб сыграем?
Введите камень (к), ножницы (н), бумагу (б): \
""")
@bot.message_handler(func=lambda message: True)
def play_game(message):
    user_move = message.text
    user_move = user_move.lower()
    if user_move not in ("к", "н", "б"):
        bot.reply_to(message, "Такого варианта нету!!!!!!!!!!!! Пожалуйста играй по правилам")
    else:
        computer_move = random.choice(["к", "н", "б"])
        bot.reply_to(message, "Ход игрока " + user_move + ", ход компьютера " + computer_move)
        if ((user_move == "к" and computer_move == "н")
                or (user_move == "н" and computer_move == "б")
                or (user_move == "б" and computer_move == "к")):
            random_answer = random.choice(["Как это так я ошибься. В следущии я выберу камень.",
                                           "Как ты посмел выиграть!!!! Я за тобой приду ночью когда ты спишь и думаешь что я не приду",
                                           "Ты выиграл, наэтот раз. Но в следущии раз я огогогооо."])
            bot.reply_to(message, random_answer)
        elif user_move == computer_move:
            bot.reply_to(message, "Ничья")
        else:
            random_answer = random.choice(["Я выиграл!!!!!",
                                           "Есть я выиграл. Я же говорил что меня невозможно победить",
                                           "Хахахахахах, теубу никогда меня не победить в честной игре"])
            bot.reply_to(message, random_answer)

@bot.message_handler(commands=['end'])
def threat_message(message):
    bot.reply_to(message, "Я за тобой приду ночью когда ты спишь и думаешь что я не приду")


bot.infinity_polling()
