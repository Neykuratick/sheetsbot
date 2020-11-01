import datetime
from ConnectSheet import ConnectSheet

ch = ConnectSheet()
week = datetime.date.today().isocalendar()[1]

class Backend:

    def __init__(self):
        self.text = 'h'

    def AllForToday(self):
        weekday = datetime.datetime.today().weekday()
        firstclass = weekday * 10
        lastclass = firstclass + 10

        if week % 2 == 0:
            text = ''
            try:
                for subject in range(firstclass, lastclass):
                    if subject % 2 != 0:
                        text += ch.readCol()['values'][19][subject]
                        text += '\n\n'
            except:
                pass
            return text

        elif week % 2 != 0:
            text = ''
            try:
                for subject in range(firstclass, lastclass, 2):
                    text += ch.readCol()['values'][19][subject]
                    text += '\n\n'
            except:
                pass
            return text + '.'

    def byDay(self, day):
        weekday = day
        week = datetime.date.today().isocalendar()[1]

        firstclass = weekday * 10
        lastclass = firstclass + 10

        if week % 2 == 0:
            text = ''
            try:
                for subject in range(firstclass+1, lastclass, 2):
                    text += ch.readCol()['values'][19][subject]
                    text += '\n\n'
            except:
                pass
            return text

        elif week % 2 != 0:
            text = ''
            try:
                for subject in range(firstclass+2, lastclass, 2):
                    text += ch.readCol()['values'][19][subject]
                    text += '\n\n'
            except:
                pass
            return text + '.'


    def tomorrowClasses(self):
        weekday = datetime.datetime.today().weekday()
        week = datetime.date.today().isocalendar()[1]
        if weekday >= 4:
            return "Завтра адыхаем"
        else:
            weekday += 1

        firstclass = weekday * 10
        lastclass = firstclass + 10

        if week % 2 == 0:
            text = ''
            try:
                for subject in range(firstclass+1, lastclass, 2):
                    text += ch.readCol()['values'][19][subject]
                    text += '\n\n'
            except:
                pass
            return text

        elif week % 2 != 0:
            text = ''
            try:
                for subject in range(firstclass+2, lastclass, 2):
                    text += ch.readCol()['values'][19][subject]
                    text += '\n\n'
            except:
                pass
            return text + '.'

    def byDayNext(self, day): #nextweek
        weekday = day
        week = datetime.date.today().isocalendar()[1]
        week += 1

        firstclass = weekday * 10
        lastclass = firstclass + 10

        if week % 2 == 0:
            text = ''
            try:
                for subject in range(firstclass + 1, lastclass, 2):
                    text += ch.readCol()['values'][19][subject]
                    text += '\n\n'
            except:
                pass
            return text

        elif week % 2 != 0:
            text = ''
            try:
                for subject in range(firstclass + 2, lastclass, 2):
                    text += ch.readCol()['values'][19][subject]
                    text += '\n\n'
            except:
                pass
            return text + '.'




bc = Backend()
bc.AllForToday()
