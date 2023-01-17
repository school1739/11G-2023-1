import telebot
from telebot import types

bot = telebot.TeleBot(token="5739937091:AAFAjXwur5cuSIzliK8X55tt3FUmtxWsM-0")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton("Привет!")
    itembtn2 = types.KeyboardButton("На сайт")
    itembtn3 = types.KeyboardButton("Соме шит")
    itembtn4 = types.KeyboardButton("Самшит2")
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Кнопки просто отправляют текст в чат",
                     reply_markup=markup)

@bot.message_handler(content_types=["text"])
def get_text_messanger(message):
    if message.text == "Привет!":
        bot.send_message(message.from_user.id, "Привет, человек!")
    elif message.text == "На сайт":
        bot.send_message(message.from_user.id, "https://педобраз.рф")
    elif message.text == "Timothy!":
        bot.send_animation(message.from_user.id, "https://media.tenor.com/MGDjTI6j6toAAAAM/substitute-teacher-key-and-peele.gif")
    elif message.text == "Help":
        bot.send_message(message.from_user.id, "Ты уже нажал на кныпку")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Нажми на кнопку, получишь результат!")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /start")

bot.polling()