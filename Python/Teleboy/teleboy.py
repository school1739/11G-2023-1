import os

import telebot
from google.cloud import dialogflow_v2
from telebot import types


bot = telebot.TeleBot(token="5739937091:AAFAjXwur5cuSIzliK8X55tt3FUmtxWsM-0")


"""@bot.message_handler(commands=["start"])
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
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /start")"""

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'papupipapopubot-mfps-bb320d66ef80.json'

DIALOGFLOW_PROJECT_ID = 'papupipapopubot-mfps'
DIALOGFLOW_LANGUAGE_CODE = 'ru'
SESSION_ID = 'me'

session_client = dialogflow_v2.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)


def detect_intent_text(text):
    text_input = dialogflow_v2.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow_v2.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response


@bot.message_handler(commands=['start'])
def start_message(msg: types.Message):
    bot.send_message(msg.chat.id, 'Слава Славе!')


@bot.message_handler(content_types=['text'])
def send_text(msg: types.Message):
    response = detect_intent_text(msg.text)
    bot.reply_to(msg, response.query_result.fulfillment_text)


bot.polling()