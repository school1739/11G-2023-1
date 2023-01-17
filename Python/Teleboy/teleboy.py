import telebot
from telebot import types

bot = telebot.TeleBot(token="5739937091:AAFAjXwur5cuSIzliK8X55tt3FUmtxWsM-0")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton("Привет!")
    itembtn2 = types.KeyboardButton("На сайт педобраз.рф")
    itembtn3 = types.KeyboardButton("Timothy!")
    itembtn4 = types.KeyboardButton("Видео")
    itembtn5 = types.KeyboardButton("Документ")
    itembtn6 = types.KeyboardButton("Стикер")
    itembtn7 = types.KeyboardButton("Фото")
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Кнопки просто отправляют текст в чат",
                     reply_markup=markup)

@bot.message_handler(content_types=["text"])
def get_text_messanger(message):
    if message.text == "Привет!":
        bot.send_message(message.from_user.id, "Привет, человек!")
    elif message.text == "На сайт педобраз.рф":
        bot.send_message(message.from_user.id, "https://педобраз.рф")
    elif message.text == "Timothy!":
        bot.send_animation(message.from_user.id, "https://media.tenor.com/MGDjTI6j6toAAAAM/substitute-teacher-key-and-peele.gif")
    elif message.text == "Видео":
        bot.send_video(message.from_user.id, "https://педобраз.рф")
    elif message.text == "Документ":
        bot.send_document(message.from_user.id, "https://педобраз.рф")
    elif message.text == "Стикер":
        bot.send_sticker(message.from_user.id, "https://педобраз.рф")
    elif message.text == "Фото":
        bot.send_photo(message.from_user.id, "https://педобраз.рф")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /start")

bot.polling()