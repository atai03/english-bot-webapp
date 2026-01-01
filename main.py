from decouple import config
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = telebot.TeleBot(config("BOT_TOKEN"))

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton(
            "Open 📘",
            web_app=WebAppInfo(
                url="https://atai03.github.io/english-bot-webapp/"
            )
        )
    )

    bot.send_message(
        message.chat.id,
        "Открой тренажёр английского 👇",
        reply_markup=keyboard
    )

bot.polling()
