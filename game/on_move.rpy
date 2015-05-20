init:
    image daytime = ConditionSwitch(
        "hour < 5 or hour > 20", "#646464",
        "hour >=5  and hour <= 8", "#FFD6BD",
        "hour > 8  and hour <= 18", "#FFFFFF",
        "hour > 18  and hour <= 20", "#EB9191",
        )
    $ lastEventTime = 0

init python:
#базовая функция перемещения. Использовать всегда и всюду
    def move(where):
        global curloc, hour, prevloc, same_loc #объявление глобальных переменных
        if renpy.has_label(where) == True: #Проверка на то, что локация существует. Если нет, прыгаем домой.
            renpy.scene(layer='master') # Сброс картинок
            renpy.scene(layer='screens') # Сброс скринов
            renpy.show('daytime')
            if getLoc(curloc) != False: getLoc(curloc).people = [] #Сброс людей с предыдущей локации

            player.stats.energy -= randf(2,5) #расход энергии
            resetStats(allChars) #Сброс статов
            player.checkDur() # Удаление использованных предметов
            changetime(rand(1, 3)) #изменение времени

            if where[:4] == 'loc_' and getLoc(where).position != 'tech': #Если локация - локация и если она не техническая
                checkDeath() # проверка на смерть
                clearLocations() # Очищаем все локации
                addPeopleLocation(where) #Добавление людей на локацию
                if where != curloc and getLoc(where).position != 'self':
                    prevloc = curloc
                    curloc = where
                    same_loc = 0
                else:
                    same_loc = 1
                if getLoc(where).position != 'self':
                    renpy.show_screen('stats_screen') #При перемещении всегда появляется интерфейс
                checkClothes(where) # проверка одетости
                checkUnconscious(getLoc(where)) # потеря сознания
                checkSperm(getLoc(where)) # снятие репутации за сперму.
                
                
            if rand(1,100) < 10 and where[:4] == 'loc_' and same_loc == 0: tryEvent(where) # попытка дёрнуть рандомный эвент с локации. Ожидание не даёт эвентов.

            renpy.retain_after_load() # чтобы сохранялся интерфейс, иначе ошибка
            renpy.jump(where) #Переход на локу
        else:
            renpy.jump('loc_home')

#Просто дёргает всех людей и сбрасывает выделющиеся статы
    def resetStats(input):
        for x in input:
            x.normalize()
        player.normalize()


#Вызов эвента
    def tryEvent(location):
        if getLoc(location).position == 'classroom' and lt() > 0: location += 'Learn' #Если сейчас уроки, то добавляем к поиску локаций Learn
        if lt() == -4: location += 'Night'
        tempEv = []
        for x in locations: #перебираем локи и ищем подходящие эвенты
            if x.id == location:
                for event in x.events:
                    if x.position == 'self':
                        if event.corr <= player.stats.corr:
                            tempEv.append(event)
                    else :
                        if event.corr <= getPar(studs, 'corr'):
                            tempEv.append(event)

        if len(tempEv) > 0:
            renpy.hide_screen('stats_screen')
            rands = rand(0,len(tempEv)-1)
            callEvent = tempEv[rands].id
            lastEventTime = ptime #запоминаем время
            renpy.jump(callEvent) #эвент

#Добавление людей на локации
    def addPeopleLocation(location):
        location = getLoc(location) #Получение объекта локации
        if lt() > 0: # заполняем классы, если уроки
            fillClasses()
            return
        for x in allChars:
            if rand(0,99) < location.getprob(): #В зависимости от вероятности (меняется от времени)
                temp = getChar()
                if location.people.count(temp) == 0:
                    location.people.append(temp)
                

# Проверка одежды
    def checkClothes(location):
        location = getLoc(location)
        if location.position != 'safe' and location.position != 'self' and location.position != 'tech':
            if player.isCover('верх','низ') == False and player.stats.corr < 80:
                renpy.scene(layer='screens')
                renpy.jump('naked')
            elif player.isCover('верх','низ') == False and player.stats.corr >= 80 and location.id != 'loc_beach' and location.id != 'loc_pool':
                renpy.scene(layer='screens')
                renpy.jump('naked')
            elif player.getClothPurpose('swim') and location.id != 'loc_beach' and location.id != 'loc_pool':
                renpy.scene(layer='screens')
                renpy.jump('naked')
                
# бессознательное состояние
    def checkUnconscious(location):
        if player.stats.energy < 100 and rand(1,3) == 1:
            if location.position == 'safe':
                renpy.jump('sleep')
            if location.position == 'school' or location.position == 'classrom':
                renpy.jump('unconsciousSchool')
            else :
                renpy.jump('unconsciousOther')
                
# снятие репутации за сперму    
    def checkSperm(location):
        if player.isSperm() == 2 and rand(1,3) == 1:
            for x in location.people:
                x.setRep(-2)
                x.setCorr(.5)

    def checkDeath():
        if player.getHealth() < 200 and rand(1,50) == 1:
            move('death')