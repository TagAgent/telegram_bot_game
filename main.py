
import telebot
from local_settings import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я Карлсон. 
Я скрываю много секретов, ответы на них тебе никогда не узнать. 
Хахаххахахахаххахахахахахахаххахахахахахахахаха!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Я за тобой приду ночью когда ты спишь и думаешь что я не приду")


bot.infinity_polling()
