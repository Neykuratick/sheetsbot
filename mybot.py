import telebot
from winreg import *
import subprocess
import os
from SheetHandler import SheetHandler
from ConnectSheet import ConnectSheet
from backend import Backend
import datetime
from flask import Flask, request

print("Successfully")
sh = SheetHandler()
TOKEN = '1279723497:AAEW_-tXerF6e3DRt1MsAt5fxX-d24synGk'
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

# bot.remove_webhook()
# secret = 'egege3423'
# bot.set_webhook(url='Neykuratick.pythonanywhere.com' + secret)
#
# app = Flask(__name__)
# @app.route('/'+secret, methods=['POST'])
# def webhook():
#     update = telebot.types.Update.de_json((request.stream.read().decode('utc-8')))
#     bot.process_new_updates([update])
#     return 'ok', 200

@bot.message_handler(commands=['site'])
def site(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, )
    linkBtn = telebot.types.KeyboardButton('Ссылка')
    todayBtn = telebot.types.KeyboardButton('Пары сёдня')
    todayBtn = telebot.types.KeyboardButton('Пары завтра')
    todayBtn = telebot.types.KeyboardButton('Расписание на эту неделю')
    todayBtn = telebot.types.KeyboardButton('Расписание на следующую неделю')

    markup.add(linkBtn, todayBtn)
    bot.send_message(message.chat.id, 'Buttons', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    message.text = message.text.lower()
    sh = SheetHandler()
    ch = ConnectSheet()

    fooStr = """
1. maintain
2. 1
3. test
4. del - deletes 2 worksheet in Botsheet
4.1 copy - copies worksheet from Spreadsheet to Botsheet
5. reset - deletes 2 worksheet in Botsheet and creates new instead
6. week - today's week
"""
    helpStr = """
Он не показывает 4 пары по нечётным неделям: три матана в четверг и одно программирование в пятницу

За всё вините апи гугла!1

0. хелп/help - помощь

1. ссылку - ссылка на расписание

2. пара - текущая пара [не работает]

3. след пара - следующая пара [не работает]

4. пары - все пары на сегодня

5. пары завтра - все пары на завтра

6. пн/вт/ср/чт/пт - какие пары на этой неделе

7. пн2/вт2/ср2/чт2/пт2 - какие пары будут на следующей неделе

8. черта

9. foo - для разрабов
"""
    maintainStr = """
да, я сноб. Знаю

1. Follow the link https://docs.google.com/spreadsheets/d/1sN4war5N8FGEkomKv0Vo-lwLmREsEmXt/edit#gid=112716612
2. Copy the worksheet over to "Spreadsheet"
3. Head over to https://docs.google.com/spreadsheets/d/1bM8GZfbp3UnvdOAIDhHzAOBK6-HTBIeVMueyy5ZrnxE/edit#gid=541466792
4. Delete the first worksheet so there's only one of them

"""

    if message.text == 'foo':
        bot.send_message(message.chat.id, 'https://cdn.fishki.net/upload/post/2018/02/18/2515915/8-1.jpg')

    if message.text in ['help', 'хелп', 'помоги', '/help']:
        bot.send_message(message.chat.id, helpStr)

    if message.text == 'maintain':
        bot.send_message(message.chat.id, maintainStr)

    if message.text in ['ссылку', 'ссылка', 'ссыль', 'сс']:
        bot.send_message(message.chat.id,
                         "https://docs.google.com/spreadsheets/d/1sN4war5N8FGEkomKv0Vo-lwLmREsEmXt/edit#gid=112716612")

    if message.text == '1':
        bot.send_message(message.chat.id, "2")

    if message.text == 'week':
        bot.send_message(message.chat.id, str(datetime.date.today().isocalendar()[1]))

    if message.text == 'test':
        text = ch.readCol()['values']
        bot.send_message(message.chat.id, text[0][1])
        bot.send_message(message.chat.id, text[1][1])
        bot.send_message(message.chat.id, text[19][1])

    if message.text == 'del':
        call = sh.deleteWorksheet()
        if call == True:
            bot.send_message(message.chat.id, "deleted")
        else:
            bot.send_message(message.chat.id, "no del")

    if message.text == 'copy':
        sh.copySheet()
        bot.send_message(message.chat.id, "copied")

    if message.text == 'reset':
        sh.deleteWorksheet()
        sh.copySheet()
        bot.send_message(message.chat.id, "reset")

    if message.text in ['пары', 'пары сёдня']:
        bc = Backend()
        bot.send_message(message.chat.id, bc.AllForToday())

    if message.text == 'пары завтра':
        bc = Backend()
        bot.send_message(message.chat.id, bc.tomorrowClasses())

    if message.text == 'черта':
        week = datetime.date.today().isocalendar()[1]
        if week % 2 == 0:
            bot.send_message(message.chat.id, "сёдня смотрим над чертой")
        if week % 2 == 1:
            bot.send_message(message.chat.id, "сёдня смотрим под чертой")

    # дни недели
    if message.text == 'пн':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDay(0) + '.')

    if message.text == 'вт':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDay(1) + '.')

    if message.text == 'ср':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDay(2) + '.')

    if message.text == 'чт':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDay(3) + '.')

    if message.text == 'пт':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDay(4) + '.')

    # дни следующей недели
    if message.text == 'пн2':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDayNext(0) + '.')

    if message.text == 'вт2':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDayNext(1) + '.')

    if message.text == 'ср2':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDayNext(2) + '.')

    if message.text == 'чт2':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDayNext(3) + '.')

    if message.text == 'пт2':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDayNext(4) + '.')

# @server.route('/' + TOKEN, methods=['POST'])
# def getMessage():
#     bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     return '!', 200
#
# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url='' + TOKEN)
#     return '!', 200

bot.polling()


# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))