import telebot
from telebot import types
import json
import requests
import random
import time

bot = telebot.TeleBot("TOKEN")
print(bot.get_me())


@bot.message_handler(commands=["start", "info"])
def command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    box_1sec = types.KeyboardButton("1secmail")
    markup.add(box_1sec)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def onesec(message):
    if message.text == "1secmail":
        for _ in range(5):
            sec = ""
        for _ in range(5):
            sec += random.choice("qwertyuiopasdfghjklzxcvbnm")
        bot.send_message(message.chat.id, sec + "@yoggm.com")
        r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={sec}&domain=yoggm.com").text
        for _ in range(10):
            if r == '[]':
                time.sleep(5)
                r = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={sec}&domain=yoggm.com").text
            else: break
        try:
            json_data = json.loads(r)
            re = requests.get(
                f"https://www.1secmail.com/api/v1/?action=readMessage&login={sec}&domain=yoggm.com&id={json_data[0]['id']}"
            ).text
            print(
                f"Тема:{json_data[0]['subject']}\nОт:{json_data[0]['from']}\nID : {json_data[0]['id']}\nСообщение : {json.loads(re)['textBody']}"
            )
            bot.send_message(
                message.chat.id,
                f"Заголовок : {json_data[0]['subject']}\nОт : {json_data[0]['from']}\nID : {json_data[0]['id']}\nСообщение : {json.loads(re)['textBody']}",
            )
        except Exception:
            bot.send_message(message.chat.id, 'Время действия почты истёк!')

bot.polling(none_stop=True)
