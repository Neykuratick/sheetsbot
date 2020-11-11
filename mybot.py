import telebot
from SheetHandler import SheetHandler
from ConnectSheet import ConnectSheet
from backend import Backend
import datetime
from flask import Flask, request

"""
https://teletype.in/@cozy_codespace/Hk70-Ntl4 - heroku deploy
switch to release token!!
git add .
git commit -m "commit"
git push origin master
git push heroku master
heroku ps:scale worker=1
"""

print("Successfully")
sh = SheetHandler()

# TOKEN = '1364748694:AAE__vAI4IZJAFOvw5DUp29vyNaO6t3kZkg'  # test
TOKEN = '1279723497:AAEW_-tXerF6e3DRt1MsAt5fxX-d24synGk'  # release
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Пибет", reply_markup=keyboardMain())


@bot.message_handler(content_types=['text'])
def handle_text(message):
    message.text = message.text.lower()

    # creating google sheets session
    sh = SheetHandler()
    ch = ConnectSheet()

    # writing to log
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    chat_id = str(message.chat.id)
    if chat_id == '388953283':
        chat_id = 'me'
    with open('log.txt', 'a') as log:
        log.write('Used. Time: ' + now + '. By: ' + chat_id + '\n')

    fooStr = """
1. maintain
2. 1
3. test
4. del - deletes 2 worksheet in Botsheet
4.1 copy - copies worksheet from Spreadsheet to Botsheet
5. reset - deletes 2 worksheet in Botsheet and creates new instead
6. week - today's week
7. heroku - heroku link
8. clear log
9. print log
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

foohelp
"""
    maintainStr = """
1. Follow the link https://docs.google.com/spreadsheets/d/1sN4war5N8FGEkomKv0Vo-lwLmREsEmXt/edit#gid=112716612
2. Copy the "1 курс" worksheet over to "Botsheet"
"""
    if message.text == 'heroku':
        bot.send_message(message.chat.id, 'https://dashboard.heroku.com/apps/guarded-retreat-31483/logs')

    if message.text == 'clear log':
        with open('log.txt', 'w') as log:
            log.write('')
        bot.send_message(message.chat.id, 'log cleared')

    if message.text == 'print log':
        with open('log.txt', 'r') as log:
            text = log.read()

        try:
            bot.send_message(message.chat.id, text)
        except:
            bot.send_message(message.chat.id, 'message might be too long\nconsider cleaning logs')

    if message.text == 'foohelp':
        bot.send_message(message.chat.id, fooStr)

    if message.text == 'foo':
        bot.send_message(message.chat.id, 'https://cdn.fishki.net/upload/post/2018/02/18/2515915/8-1.jpg')

    if message.text in ['help', 'хелп', 'помоги', '/help']:
        bot.send_message(message.chat.id, helpStr, reply_markup=keyboardMain())

    if message.text == 'maintain':
        bot.send_message(message.chat.id, maintainStr)

    if message.text in ['ссылку', 'ссылка', 'ссыль', 'сс']:
        bot.send_message(
            message.chat.id,
            "https://docs.google.com/spreadsheets/d/1sN4war5N8FGEkomKv0Vo-lwLmREsEmXt/edit#gid=112716612",
            reply_markup=keyboardMain())

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

    # week days
    if message.text == 'пн':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDay(0))

    if message.text == 'вт':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDay(1))

    if message.text == 'ср':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDay(2))

    if message.text == 'чт':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDay(3))

    if message.text == 'пт':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDay(4))

    # next week
    if message.text == 'пн2':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDayNext(0))

    if message.text == 'вт2':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDayNext(1))

    if message.text == 'ср2':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDayNext(2))

    if message.text == 'чт2':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDayNext(3))

    if message.text == 'пт2':
        bc = Backend()
        bot.send_message(message.chat.id, bc.byDayNext(4))

    if message.text == "расписание-на-эту-неделю":
        bot.send_message(message.chat.id, 'Выбери день', reply_markup=keyboardThisWeek())

    if message.text == "расписание-на-следующую-неделю":
        bot.send_message(message.chat.id, 'Выбери день', reply_markup=keyboardNextWeek())

    if message.text == "назад":
        bot.send_message(message.chat.id, 'Ок', reply_markup=keyboardMain())


def keyboardMain():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    linkBtn = telebot.types.KeyboardButton('Ссылка')
    todayBtn = telebot.types.KeyboardButton('Пары сёдня')
    todayBtn1 = telebot.types.KeyboardButton('Пары завтра')
    whatWeek = telebot.types.KeyboardButton('Черта')
    todayBtn2 = telebot.types.KeyboardButton("расписание-на-эту-неделю")
    todayBtn3 = telebot.types.KeyboardButton('расписание-на-следующую-неделю')

    markup.add(linkBtn, todayBtn, todayBtn1, whatWeek, todayBtn2, todayBtn3)
    return markup


def keyboardThisWeek():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, )
    mon = telebot.types.KeyboardButton('пн')
    tue = telebot.types.KeyboardButton('вт')
    wed = telebot.types.KeyboardButton('ср')
    thr = telebot.types.KeyboardButton('чт')
    fri = telebot.types.KeyboardButton('пт')
    back = telebot.types.KeyboardButton('назад')

    markup.add(mon, tue, wed, thr, fri, back)
    return markup


def keyboardNextWeek():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, )
    mon = telebot.types.KeyboardButton('пн2')
    tue = telebot.types.KeyboardButton('вт2')
    wed = telebot.types.KeyboardButton('ср2')
    thr = telebot.types.KeyboardButton('чт2')
    fri = telebot.types.KeyboardButton('пт2')
    back = telebot.types.KeyboardButton('назад')

    markup.add(mon, tue, wed, thr, fri, back)
    return markup


while True:
    try:
        bot.polling()
    except:
        pass
