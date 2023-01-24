import telebot
from telebot import types

bot = telebot.TeleBot('5827315252:AAG3MaPfzVEPFkaawp7K53lF6xpNx0RCi70')

commands = {
    'Привет!':
        lambda msg: bot.send_message(msg.chat.id, 'Здарова'),
    'help':
        lambda msg: bot.send_message(msg.chat.id, 'Типа помощь'),
    'timothy':
        lambda msg: bot.send_animation(msg.chat.id, 'https://thumbs.gfycat.com/UnrulyThriftyHedgehog-size_restricted.gif'),
    'Пришли картинку':
        lambda msg: bot.send_photo(msg.chat.id, 'https://cdnn21.img.ria.ru/images/07e5/06/18/1738448523_0:89:864:575_1920x0_80_0_0_7541a4a6d36edb667d2de032b8aefc66.jpg'),
    'Пришли видео':
        lambda msg: bot.send_video(msg.chat.id, open('Кот - космонавт.mp4', 'rb')),
    'Пришли файл':
        lambda msg: bot.send_document(msg.chat.id, open('secret.txt', 'rb')),
    'Пришли стикер':
        lambda msg: bot.send_sticker(msg.chat.id, 'CAACAgIAAxkBAAEHTe5jxoeGyDoZG1NNs_pxgYj1xxxDBwACzxIAArMK0Uv0uoqGrkIZMS0E'),
}


@bot.message_handler(commands=['start'])
def start(msg: types.Message):
    markup = types.ReplyKeyboardMarkup()
    for command in commands.keys():
        print(command)
        btn = types.KeyboardButton(text=command)
        markup.add(btn)
    bot.send_message(msg.chat.id, 'Привет!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(msg: types.Message):
    answer = commands.get(msg.text)
    if answer is None:
        bot.send_message(msg.chat.id, 'Не знаю такой команды')
        return
    answer(msg)


bot.polling()
