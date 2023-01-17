import telebot
import types

bot = telebot.TeleBot('5850289269:AAEmzK1WG6gMxC9ME__LtfvoX3y130G6sRs')


@bot.message_handler(commands=['start'])
# def url(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text='На сайт', url='https://pedobraz.ru/')
#     markup.add(btn1)
#     bot.send_message(message.from_user.id, "Нажми на кнопку", reply_markup=markup)
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "перейти на сайт", reply_markup = markup)

@bot.message_handler(content_types = ["text"])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, человек")
    if message.text == "На сайт":
        bot.send_message(message.from_user.id, "https://педобраз.рф")
    if message.text == "help":
        bot.send_message(message.from_user.id, "Нажми на кнопку и получишь результат")
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Это кнопка хелпы")

