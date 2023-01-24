import telebot
from telebot import types

bot = telebot.TeleBot("5485807889:AAEbo4kBHUCwdXextgde5ZQhKS18D6ZE6qE")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types. ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types. KeyboardButton("Привет!")
    itembtn2 = types.KeyboardButton("Hа сайт")
    itembtn3 = types. KeyboardButton("ASMR")
    itembtn4 = types.KeyboardButton('Help')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Есичо, кнопки тупо отправляют текст в чат!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет!":
        bot.send_message(message.from_user.id, "Привет, человек!")
    elif message.text == "На сайт":
        bot.send_message(message.from_user.id, "https://cheburek.by")
    elif message.text == "ASMR":
        bot. send_animation(message.from_user.id,
                                    "https://media.tenor.com/NVZhbilEfhEAAAAd/asmr.gif")
    elif message.text == "Help":
        bot.send_dice(message.from_user.id)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Нажми на кнопкy, получишь результат!")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")
"""T0D0:
коммит: всё что выше
2 коммит: всё что ниже:
"Пришли картинку"- send_photo
"Пришли внимацию" - send_animation
"Пришли видео" - send_video
"Привли файл" - send_document
"Пришли стикер" - send_sticker"""

bot.polling()