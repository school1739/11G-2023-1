import telebot
from telebot import types

bot = telebot.TeleBot(token="5739937091:AAFAjXwur5cuSIzliK8X55tt3FUmtxWsM-0")


@bot.message_handler(commands=["start"])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="На сайт", url="https://педобраз.рф")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Нажми на кнопку, попадёшь на сайт!",
                     reply_markup=markup)