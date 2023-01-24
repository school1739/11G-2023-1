import os
import google.cloud.dialogflow_v2 as dialogflow
import telebot


bot = telebot.TeleBot('5658399786:AAHo9KLbR1ubY6fk4d2dWDhjDbugBFsSvzM')
import google.cloud.dialogflow_v2 as dialogflow

'''@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Привет!')
    itembtn2 = types.KeyboardButton('На сайт')
    itembtn3 = types.KeyboardButton('Help')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "///", reply_markup=markup)

@bot.message_handler(content_types=['text'])

def get_text_message(message):
    if message.text == 'Привет!':
        bot.send_message(message.from_user.id, 'Привет, человек!')
    if message.text == 'Пришли картинку':
        bot.send_photo(message.from_user.id, 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fir.ozone.ru%2Fs3%2Fmultimedia-r%2Fc1000%2F6018790083.jpg&imgrefurl=https%3A%2F%2Fwww.ozon.ru%2Fproduct%2Fmartin-romas-mr-441-bk-gitara-akusticheskaya-tsvet-chernyy-181600535%2F&tbnid=V16zSA6RtHhf_M&vet=12ahUKEwi32vTYvc78AhWHxIsKHeO-CtAQMygDegUIARDkAQ..i&docid=0LfuW0-hYcgRhM&w=800&h=1000&q=%D0%B3%D0%B8%D1%82%D0%B0%D1%80%D0%B0&ved=2ahUKEwi32vTYvc78AhWHxIsKHeO-CtAQMygDegUIARDkAQ')
    if message.text == 'Пришли видео':
        bot.send_video(message.from_user.id, open('document_5348408192571287180.mp4', 'rb'))
    if message.text == 'Пришли файл':
        bot.send_document(message.from_user.id, open('Trudny_put_nekromanta.docx', 'rb'))
    if message.text == 'Пришли стикер':
        bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEHTaVjxoUkzL1VVznBo7IRq1JmJ1ZLSQACWxMAArshMEkz55bxMvha1C0E')
    if message.text == 'Пришли анимацию':
        bot.send_animation(message.from_user.id, 'https://gifgive.com/wp-content/uploads/2021/04/gorenie-ognya.gif')
    if message.text == 'Help':
        bot.send_message(message.from_user.id, 'Нажми на /start, там в будущем, возможно, будет меню с инструкцией')

bot.polling()'''

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'guitar-bot-lgyr-3828c91bd9b6.json'
DIALOGFLOW_PROJECT_ID = 'guitar-bot-lgyr'
DIALOGFLOW_LANGUAGE_CODE = 'ru'
SESSION_ID = 'me'


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, человек!')


@bot.message_handler(func=lambda message: True)
def send_text(message):
    text_to_be_analyzed = message.text
    response = detect_intent_texts(DIALOGFLOW_PROJECT_ID, SESSION_ID, text_to_be_analyzed, DIALOGFLOW_LANGUAGE_CODE)
    bot.reply_to(message, response.query_result.fulfillment_text)


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response


bot.polling()