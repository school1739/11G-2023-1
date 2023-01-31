import os

import telebot
from google.cloud import dialogflow_v2
from telebot import types

bot = telebot.TeleBot('5827315252:AAG3MaPfzVEPFkaawp7K53lF6xpNx0RCi70')

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
    bot.send_message(msg.chat.id, 'Слава Арстоцке!')


@bot.message_handler(content_types=['text'])
def send_text(msg: types.Message):
    response = detect_intent_text(msg.text)
    bot.reply_to(msg, response.query_result.fulfillment_text)


bot.polling()
