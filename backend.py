import datetime
from ConnectSheet import ConnectSheet

ch = ConnectSheet()
week = datetime.date.today().isocalendar()[1]

class Backend:

    def __init__(self):
        self.text = 'h'


    def scraper(self, weekday, week):
        text = ''

        firstclass = weekday * 10
        lastclass = firstclass + 10

        if week % 2 == 0:
            firstclass_const = 1
            range_const = 2
        else:
            firstclass_const = 2
            range_const = 2

        if weekday < 3 or week % 2 == 0:
            try:
                for subject in range(firstclass + firstclass_const, lastclass, range_const):
                    text += ch.readCol()['values'][19][subject]
                    text += '\n\n'
            except:
                pass

        elif weekday == 3 and week % 2 != 0:
            try:
                for subject in range(firstclass + firstclass_const, lastclass, range_const):
                    text += ch.readCol()['values'][19][subject]
                    text += '\n\n'
            except:
                pass

            text += '[НЕ ТОЧНО!!] Пара матана\n\n'
            text += '[НЕ ТОЧНО!!] Пара матана\n\n'
            text += '[НЕ ТОЧНО!!] Пара матана\n\n'

        elif weekday == 4 and week % 2 != 0:
            try:
                for subject in range(firstclass + firstclass_const, lastclass, range_const):
                    text += ch.readCol()['values'][19][subject]
                    text += '\n\n'
            except:
                pass

            text += '[НЕ ТОЧНО!!] 10:40 - 12:10 Пара Программирования\n\n'

        return text

    def AllForToday(self):
        weekday = datetime.datetime.today().weekday()
        week = datetime.date.today().isocalendar()[1]

        return self.scraper(weekday, week)

    def byDay(self, day):
        weekday = day
        week = datetime.date.today().isocalendar()[1]

        return self.scraper(weekday, week)


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

        return self.scraper(weekday, week)

    def byDayNext(self, day): #nextweek
        weekday = day
        week = datetime.date.today().isocalendar()[1]
        week += 1

        return self.scraper(weekday, week)