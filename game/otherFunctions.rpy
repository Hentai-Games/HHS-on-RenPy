init -5 python:
    import random
    from random import choice
    import time
    from operator import attrgetter

    dublicationChar = []
    classrooms = []
    
    def rand(a, b):
        if b == 0:
            return b
        else :
            return random.randint(a,b)

    def randf(a, b):
        return random.uniform(a,b)


    def getPar(list, *args):
        temp = 0
        if args[0] == 'loy':
            for x in list:
                temp = temp + x.stats.loyalty
            return round(temp/len(list),2)

        if args[0] == 'fun':
            for x in list:
                temp = temp + x.stats.fun
            return round(temp/len(list),2)

        if args[0] == 'corr':
            for x in list:
                temp = temp + x.stats.corr
            return round(temp/len(list),2)

        if args[0] == 'lust':
            for x in list:
                temp = temp + x.stats.lust
            return round(temp/len(list),2)

        if args[0] == 'edu':
            for x in list:
                temp = temp + x.stats.education
            return round(temp/len(list),2)

        if args[0] == 'rep':
            for x in list:
                temp = temp + x.stats.reputation
            return round(temp/len(list),2)
        return 'error'

    def waiting(t):
        player.stats.energy -= randf(t/2,t)
        changetime(t)
        move(curloc)

#Динамическая картинка
    def dynImage(st,at):
        return dynpicto, None

#Работа с людьми
    def getChar(*args):
        global dublicationChar
        temp = []

        if len(args) == 0:
            return choice(allChars)

        if len(args) == 1:
            if len(getLoc(curloc).people) > 0:
                for char in getLoc(curloc).people:
                    if char.body.sex() == args[0] and teachers.count(char) == 0 and dublicationChar.count(char) == 0:
                        temp.append(char)
                if len(temp) > 0:
                    choosen = choice(temp)
                    dublicationChar.append(choosen)
                    if len(dublicationChar) > 10:
                        dublicationChar = []
                    return choosen

            for char in studs:
                if char.body.sex() == args[0] and dublicationChar.count(char) == 0:
                    temp.append(char)

            choosen = choice(temp)
            dublicationChar.append(choosen)
            if len(dublicationChar) > 10:
                dublicationChar = []
            return choosen

        if len(args) == 2:
            for x in studs:
                if x.body.sex() == args[0] or args[0] == '':
                    temp.append(x)
            tempChar = temp[0]
            if args[1] == 'beautymax':
                return max(temp, key = lambda x: x.stats.beauty)
            if args[1] == 'beautymin':
                return min(temp, key = lambda x: x.stats.beauty)
            if args[1] == 'edumax':
                return max(temp, key = lambda x: x.stats.education)
            if args[1] == 'edumin':
                return min(temp, key = lambda x: x.stats.education)
            if args[1] == 'corrmax':
                return max(temp, key = lambda x: x.stats.corr)
            if args[1] == 'corrmin':
                return min(temp, key = lambda x: x.stats.corr)
            if args[1] == 'lustmax':
                return max(temp, key = lambda x: x.stats.lust)
            if args[1] == 'lustmin':
                return min(temp, key = lambda x: x.stats.lust)

    def clrscr():
        renpy.scene(layer='screens')

    def skipEvent():
        tryEvent(curloc)

    def setRep(count,amount):
        for x in range(0, count):
            studs[rand(0,len(studs)-1)].setRep(amount)

    def setLoy(count,amount):
        for x in range(0, count):
            studs[rand(0,len(studs)-1)].setLoy(amount)
            
    def setCorr(count,amount):
        for x in range(0, count):
            studs[rand(0,len(studs)-1)].setCorr(amount) 
            
    def setLust(count,amount):
        for x in range(0, count):
            studs[rand(0,len(studs)-1)].setLust(amount)
            

    def hadSex(*args):
        for x in args:
            if x.body.sex() != 'male':
                x.body.parts['вагина'].size += randf(0.0,0.1)
            x.setCorr(randf(0.0,len(args)))
            x.setLust(randf(-50,50))
            
            
    def addDetention(*args):
        for char in args:
            if char in detentions == False:
                detentions.append(char)
            
    def getDays(number):
        if number == 0 or number >= 5:
            return str(number) + ' дней'
        elif number == 1:
            return str(number) + ' день'
        else:
            return str(number) + ' дня'

            
    def fillClasses():
        global classrooms
        classrooms = []
        classrooms.append(getLoc('loc_class1'))
        classrooms.append(getLoc('loc_class2'))
        classrooms.append(getLoc('loc_class3'))
        classrooms.append(getLoc('loc_class4'))
        classrooms.append(getLoc('loc_class5'))
        
        getLoc('loc_class1').people.append(kupruvna)
        getLoc('loc_class2').people.append(danokova)
        getLoc('loc_class3').people.append(frigidovna)
        getLoc('loc_class4').people.append(bissektrisovna)
        getLoc('loc_class5').people.append(dikovna)
        
        if weekday == 2 or weekday == 4:
            getLoc('loc_pool').people.append(mustangovich)
            classrooms.append(getLoc('loc_pool'))
        else:
            getLoc('loc_gym').people.append(mustangovich)
            classrooms.append(getLoc('loc_gym'))

        for x in studs:
            if x.inClass == 1: # первый класс
                tempIndex = lt() - 1 + 0
                if tempIndex > 5: tempIndex -= 6
                classrooms[tempIndex].people.append(x)
                
            elif x.inClass == 2: # Второй класс
                tempIndex = lt() - 1 + 1
                if tempIndex > 5: tempIndex -= 6
                classrooms[tempIndex].people.append(x)
                
            elif x.inClass == 3: # Третий класс
                tempIndex = lt() - 1 + 2
                if tempIndex > 5: tempIndex -= 6
                classrooms[tempIndex].people.append(x)
                
            elif x.inClass == 4: # Четвёртый класс
                tempIndex = lt() - 1 + 3
                if tempIndex > 5: tempIndex -= 6
                classrooms[tempIndex].people.append(x)
                
            else: # Пятый класс
                tempIndex = lt() - 1 + 4
                if tempIndex > 5: tempIndex -= 6
                classrooms[tempIndex].people.append(x)
                
    def clearLocations():
        for x in locations:
            x.people = []
            
    def checkJail():
        for x in studs:
            if x.getRep() < 5 and x.name in complains:
                move('jail')