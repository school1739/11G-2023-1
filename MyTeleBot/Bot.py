import telebot
from telebot import types
import os

import google.cloud.dialogflow_v2 as dialogflow

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(row_width=2)
#     btn1 = types.KeyboardButton(text='На сайт')
#     btn_photo = types.KeyboardButton('Meme(photo)')
#     btn_anim = types.KeyboardButton('animation')
#     btn_sticker = types.KeyboardButton('sticker')
#     btn_video = types.KeyboardButton('video')
#     btn_gif = types.KeyboardButton('document')
#
#     markup.add(btn1, btn_photo, btn_anim, btn_sticker, btn_video, btn_gif)
#     bot.send_message(message.from_user.id, "Нажми на кнопку", reply_markup=markup)
#     # bot.send_message(message.chat.id, "Что в коробке?", reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == 'Что в коробке?':
#         bot.send_message(message.from_user.id, 'Ничего')
#     elif message.text == 'На сайт':
#         bot.send_message(message.from_user.id, 'https://pedobraz.ru/')
#     elif message.text == 'Meme':
#         bot.send_photo(message.from_user.id,
#                        'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwelovedoodles.com%2Fwp-content%2Fuploads%2F2022%2F02%2Fwalter-dog-meme-original-790x1024.jpeg&imgrefurl=https%3A%2F%2Fwelovedoodles.com%2Fwalter-the-dog-memes%2F&tbnid=rXaK-iss7b_gHM&vet=12ahUKEwiL4vqDus78AhXK6CoKHZjzCvgQMygCegUIARC6AQ..i&docid=SEMVU32CaVBIwM&w=790&h=1024&q=mem%20dogs&ved=2ahUKEwiL4vqDus78AhXK6CoKHZjzCvgQMygCegUIARC6AQ')
#         bot.send_photo(message.from_user.id,
#                        'https://www.google.com/imgres?imgurl=https%3A%2F%2Fassets.puzzlefactory.pl%2Fpuzzle%2F348%2F045%2Foriginal.jpg&imgrefurl=https%3A%2F%2Fpuzzlefactory.pl%2Fen%2Fpuzzle%2Fplay%2Fanimals%2F348045-dog-meme&tbnid=o4vT6PDYQirDkM&vet=12ahUKEwiBvseGus78AhVMEXcKHWyTAroQxiAoB3oECAAQGw..i&docid=09kUjg51TZSFtM&w=720&h=737&itg=1&q=mem%20dogs&ved=2ahUKEwiBvseGus78AhVMEXcKHWyTAroQxiAoB3oECAAQGw')
#     elif message.text == "animation":
#         bot.send_animation(message.from_user.id, "https://media.tenor.com/dp_hQBGT0rIAAAPo/think-smart.mp4")
#     elif message.text == "sticker":
#         bot.send_sticker(message.from_user.id,
#                          "https://i.etsystatic.com/20023820/r/il/e12dd6/2885404230/il_1080xN.2885404230_tb41.jpg")
#     elif message.text == "video":
#         bot.send_video(message.from_user.id, video='MyTeleBot/videoplayback.mp4')
# elif message.text =="document":
#     bot.send_document(message.from_user.id, )
# bot.polling()

bot = telebot.TeleBot('5968657096:AAHy1LMUOs0RWu2ccUbT15BIPMe6luJ2IYM')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "alex-chat-bot-wquk-6fbcf577da95.json"
# GOOGLE_APPLICATIONS_CREDITIONALS = "alex-chat-bot-wquk-6fbcf577da95.json"
DIALOGFLOW_PROJECT_ID = "alex-chat-bot-wquk"
DIALOGFLOW_LANGUAGE_CODE = 'ru'
SESSION_ID = 'me'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Прив")


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    print('Session path: {}\n'.format(session))
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response


@bot.message_handler(func=lambda message: True)
def send_text(message):
    text_to_anal = message.text
    response = detect_intent_texts(DIALOGFLOW_PROJECT_ID, SESSION_ID, text_to_anal, DIALOGFLOW_LANGUAGE_CODE)
    bot.reply_to(message, response.query_result.fulfillment_text)


bot.polling()
