import datetime
from ConnectSheet import ConnectSheet

ch = ConnectSheet()
week = datetime.date.today().isocalendar()[1]

class Backend:

    def __init__(self):
        self.text = 'h'


    def scraper(self):
        pass

    def AllForToday(self):
        weekday = datetime.datetime.today().weekday()
        week = datetime.date.today().isocalendar()[1]

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

            if weekday < 3:
                try:
                    for subject in range(firstclass + 2, lastclass, 2):
                        text += ch.readCol()['values'][19][subject]
                        text += '\n\n'
                except:
                    pass

            elif weekday == 3:
                try:
                    for subject in range(firstclass + 2, lastclass, 2):
                        text += ch.readCol()['values'][19][subject]
                        text += '\n\n'
                except:
                    pass

                text += '[НЕ ТОЧНО!!] Пара матана\n\n'
                text += '[НЕ ТОЧНО!!] Пара матана\n\n'
                text += '[НЕ ТОЧНО!!] Пара матана\n\n'

            elif weekday == 4:
                try:
                    for subject in range(firstclass + 2, lastclass, 2):
                        text += ch.readCol()['values'][19][subject]
                        text += '\n\n'
                except:
                    pass

                text += '[НЕ ТОЧНО!!] 10:40 - 12:10 Пара Программирования\n\n'
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

            if weekday < 3:
                try:
                    for subject in range(firstclass+2, lastclass, 2):
                        text += ch.readCol()['values'][19][subject]
                        text += '\n\n'
                except:
                    pass

            elif weekday == 3:
                try:
                    for subject in range(firstclass+2, lastclass, 2):
                        text += ch.readCol()['values'][19][subject]
                        text += '\n\n'
                except:
                    pass

                text += '[НЕ ТОЧНО!!] Пара матана\n\n'
                text += '[НЕ ТОЧНО!!] Пара матана\n\n'
                text += '[НЕ ТОЧНО!!] Пара матана\n\n'

            elif weekday == 4:
                try:
                    for subject in range(firstclass+2, lastclass, 2):
                        text += ch.readCol()['values'][19][subject]
                        text += '\n\n'
                except:
                    pass

                text += '[НЕ ТОЧНО!!] 10:40 - 12:10 Пара Программирования\n\n'
            return text + '.'


    def tomorrowClasses(self):
        weekday = datetime.datetime.today().weekday()
        week = datetime.date.today().isocalendar()[1]
        if weekday == 4 or weekday == 5:
            return "Завтра адыхаем"
        else:
            weekday += 1

        if weekday > 4:
            weekday = 0
            week += 1

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
            return text + '.'

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

            if day < 3:
                try:
                    for subject in range(firstclass + 2, lastclass, 2):
                        text += ch.readCol()['values'][19][subject]
                        text += '\n\n'
                except:
                    pass

            if day == 3:
                try:
                    for subject in range(firstclass + 2, lastclass, 2):
                        text += ch.readCol()['values'][19][subject]
                        text += '\n\n'
                except:
                    pass

                text += '[НЕ ТОЧНО!!] Пара матана\n\n'
                text += '[НЕ ТОЧНО!!] Пара матана\n\n'
                text += '[НЕ ТОЧНО!!] Пара матана\n\n'

            if day == 4:
                try:
                    for subject in range(firstclass + 2, lastclass, 2):
                        text += ch.readCol()['values'][19][subject]
                        text += '\n\n'
                except:
                    pass

                text += '[НЕ ТОЧНО!!] 10:40 - 12:10 Пара Программирования\n\n'

            return text + '.'