init -3 python:
    #Start time
    minute = 0
    check_minute = 0
    hour = 6
    ptime = 0
    mtime = 0
    timeMoved = 0
    ltMoved = 0
    weekday = 1
    month = 5
    number = 1
    year = 2010
    ptime = 0
    last_sleeped = 0
    
    def gettime(*args):
        #Дни недели
        if weekday == 1: _weekday = 'Понедельник'
        if weekday == 2: _weekday = 'Вторник'
        if weekday == 3: _weekday = 'Среда'
        if weekday == 4: _weekday = 'Четверг'
        if weekday == 5: _weekday = 'Пятница'
        if weekday == 6: _weekday = 'Суббота'
        if weekday == 7: _weekday = 'Воскресенье'

        #Месяца
        if month == 1: _month = 'Января'
        if month == 2: _month = 'Февраля'
        if month == 3: _month = 'Марта'
        if month == 4: _month = 'Апреля'
        if month == 5: _month = 'Мая'
        if month == 6: _month = 'Июня'
        if month == 7: _month = 'Июля'
        if month == 8: _month = 'Августа'
        if month == 9: _month = 'Сентября'
        if month == 10: _month = 'Октября'
        if month == 11: _month = 'Ноября'
        if month == 12: _month = 'Декабря'
        
        if minute < 10:
            output = '%d %s %d, %s. %s:0%s' % (number, _month, year, _weekday, hour, minute)
        else:
            output = '%d %s %d, %s. %s:%s' % (number, _month, year, _weekday, hour, minute)
            
        if 'day' in args:
            output = '%d %s %d, %s.' % (number, _month, year, _weekday)
            
        return output
        
    def changetime(change):
        global minute, check_minute, hour, ptime, weekday, number, year, month, mtime, ltMoved, timeMoved, flagIncome, noEventTime
        player.picto = sel_player_picto()
        while change != 0:
            tempChange = min(10,change)
            change -= min(10,change)
            minute += tempChange
            mtime += tempChange
            counter = 0
            if minute >= 60:
                hourlyReset()
                minute -= 60
                hour += 1
                noEventTime += 10
                if hour == 8 and weekday == 1:
                    flagIncome = 1
                ptime += 1
                if hour >= 24:
                    hour -= 24
                    weekday += 1
                    if weekday >=8: weekday -=7
                    dailyRecount(allChars)
                    number += 1
                    if number >= 31:
                        school.getBudget()
                        monthlyReset()
                        number -= 30
                        month += 1
                        if month == 13:
                            month -=12
                            year += 1
                            
            if timeMoved + 10 < mtime or ltMoved != lt():
                counter = max(1, int((mtime - timeMoved)/10))
                movedArray[:] = []
                for x in range(counter): # Если прошло больше 10 минут, двигаем несколько раз за всё прошедшее время.
                    addPeopleLocations() # двигаем людей
                timeMoved = mtime
                ltMoved = lt()
         
        return counter
    
    def getWeekday(day):
        if day == 1: return 'Понедельник'
        if day == 2: return 'Вторник'
        if day == 3: return 'Среду'
        if day == 4: return 'Четверг'
        if day == 5: return 'Пятницу'
        if day == 6: return 'Субботу'
        if day == 7: return 'Воскресенье'
    
    def lt():
        #время первого урока
        if hour == 8 and minute <=40: result = 1
        #перемена
        if hour == 8 and minute > 40: result = 0
        #второй урок
        if hour == 9 and minute <=40: result = 2
        if hour == 9 and minute > 40: result = 0
        #третий урок
        if hour == 10 and minute <=40: result = 3
        if hour == 10 and minute > 40: result = 0
        #четвёртый урок
        if hour == 11 and minute <=40: result = 4
        if hour == 11 and minute > 40: result = 0
        #большая перемена
        if hour == 12: result = 0
        #пятый урок
        if hour == 13 and minute <=40: result = 5
        if hour == 13 and minute > 40: result = 0
        #шестой урок
        if hour == 14 and minute <=40: result = 6
        if hour == 14 and minute > 40: result = 0
        #внеурочное время
        if hour <= 7 or hour >= 15: result = -1
        #Выходные
        if weekday == 6 or weekday == 7: result = -3
        #Ночь
        if hour > 20 or hour < 6: result = -4
        return result
