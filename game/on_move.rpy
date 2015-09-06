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
    from random import shuffle
    def move(where):
        global curloc, hour, prevloc, same_loc #объявление глобальных переменных

        if renpy.has_label(where) == True: #Проверка на то, что локация существует. Если нет, прыгаем домой.
            renpy.scene(layer='master') # Сброс картинок
            renpy.scene(layer='screens') # Сброс скринов
            renpy.show('daytime') # Базовый фон
            player.stats.energy -= randf(2,5) #расход энергии
            resetStats(allChars) #Сброс статов
            player.checkDur() # Удаление использованных предметов

            # Переходы с технических локаций и на технические локации не занимают времени
            if (curloc.startswith('loc_') and 'tech' not in getLoc(curloc).position)\
                    and (where.startswith('loc') and 'tech' not in getLoc(where).position)\
                    and curloc != where:

                changetime(rand(1, 3)) #изменение времени

            if where[:4] == 'loc_' and 'tech' not in getLoc(where).position: #Если локация - локация и если она не техническая
                checkDeath() # проверка на смерть
                if where != curloc and 'self' not in getLoc(where).position:
                    prevloc = curloc
                    curloc = where
                    same_loc = 0
                else:
                    same_loc = 1
                if 'self' not in getLoc(where).position:
                    renpy.show_screen('stats_screen') #При перемещении всегда появляется интерфейс
                    # if show_peopleTextList == 1: renpy.show_screen('peopleTextList')
                checkClothes(where) # проверка одетости
                checkUnconscious(getLoc(where)) # потеря сознания
                checkSperm(getLoc(where)) # снятие репутации за сперму.
                checkOrgasm(getLoc(where)) # проверка на перевозбуждение
                
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
        if 'classroom' in getLoc(location).position and lt() > 0: location += 'Learn' #Если сейчас уроки, то добавляем к поиску локаций Learn
        if lt() == -4: location += 'Night'
        tempEv = []
        for x in locations: #перебираем локи и ищем подходящие эвенты
            if x.id == location:
                for event in x.events:
                    if 'self' in x.position:
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
    def addPeopleLocations():
        if lt() > 0: # заполняем классы, если уроки
            fillClasses()

        else:
            for x in allChars:
                if x != callup:
                    for location in locations:
                        if rand(0,99) < location.getprob(): #В зависимости от вероятности (меняется от времени)
                            temp = getChar()
                            if temp.getLocation() != location:
                                temp.moveToLocation(location)
                                break

        for loc in locations:
            dressPeople(loc.id) # Одеваем людей на локации

# Функция одевания людей
    def dressPeople(location):
        location = getLoc(location)
        for char in location.getPeople():
            if len(char.wear) == 0 or (char.getClothPurpose('swim') == True and 'swim' not in location.position):
                char.wearingByPurpose('usual')
                if rand(1,4) == 1 and char in studs:
                    char.wearingByPurpose(school.uniform)
            if 'school' in location.position and char in studs:
                char.wearingByPurpose(school.uniform)
            if char in teachers:
                if char.getCorr() < 10:
                    char.wearingByPurpose('strict')
                elif char.getCorr() < 50:
                    char.wearingByPurpose('usual')
                elif char.getCorr() < 75:
                    char.wearingByPurpose('sexy')
                else:
                    char.wearingByPurpose('skimpy')
            if 'swim' in location.position:
                char.wearingByPurpose('swim')
                if 'school' in location.position and school.uniform == 'naked':
                    char.undress()
                        
# Проверка одежды
    def checkClothes(location):
        location = getLoc(location)
        if 'safe' not in location.position and 'self' not in location.position and 'tech' not in location.position:
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
            if 'safe' in location.position:
                renpy.jump('sleep')
            if 'school' in location.position:
                renpy.jump('unconsciousSchool')
            else :
                renpy.jump('unconsciousOther')
                
# снятие репутации за сперму    
    def checkSperm(location):
        if player.isSperm() == 2 and rand(1,3) == 1:
            for x in location.getPeople():
                x.setRep(-2)
                x.setCorr(.5)

    def checkDeath():
        if player.getHealth() < 200 and rand(1,50) == 1:
            move('death')
            
    def checkOrgasm(location):
        if player.getLust() >= 100:
            if player.getCorr() < 50:
                renpy.jump('madness_low')
            else:
                if 'home' in location.position:
                    renpy.jump('madness_home')
                if 'school' in location.position and 'safe' not in location.position:
                    renpy.jump('madness_school')
