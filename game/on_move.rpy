init:
    image daytime = ConditionSwitch(
        "hour < 5 or hour > 20", "#646464",
        "hour >=5  and hour <= 8", "#FFD6BD",
        "hour > 8  and hour <= 18", "#FFFFFF",
        "hour > 18  and hour <= 20", "#EB9191",
        )
    image black = '#000000'
    $ lastEventTime = 0

init python:
#базовая функция перемещения. Использовать всегда и всюду
    from random import shuffle
    def move(where,*args):
        global curloc, hour, prevloc, same_loc, defaultSymbol, school, noEventTime, development, interactionObj, mtime, lastEventTime  #объявление глобальных переменных
        if development == 1:    
            player.setEnergy(2000)
        interactionObj = ''
        if renpy.has_label(where) == True: #Проверка на то, что локация существует. Если нет, прыгаем домой.
            renpy.scene(layer='master') # Сброс картинок
            renpy.scene(layer='screens') # Сброс скринов
            renpy.show('daytime') # Базовый фон
            player.incEnergy(-randf(2,5)) #расход энергии
            resetStats(allChars) #Сброс статов
            player.checkDur() # Удаление использованных предметов

            # Переходы с технических локаций и на технические локации не занимают времени
            # if (curloc.startswith('loc_') and 'tech' not in getLoc(curloc).position)\
                # and (where.startswith('loc') and 'tech' not in getLoc(where).position)\
                # and curloc != where:
                
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
                tempLoc = getLoc(where)
                checkClothes(where) # проверка одетости
                checkUnconscious(tempLoc) # потеря сознания
                checkSperm(tempLoc) # снятие репутации за сперму.
                checkOrgasm(tempLoc) # проверка на перевозбуждение
                checkMisc() # Прочие мелкие проверки
                
            if rand(1,100) < 10 + noEventTime and len(getLoc(curloc).getPeople()) > 0 and lastEventTime + 15 < mtime: #and  same_loc == 0: # Если на локации кто то есть и локация поменялась, дёргаем эвент по рандому
                tryEvent(where) # попытка дёрнуть рандомный эвент с локации. Ожидание не даёт эвентов.
            renpy.retain_after_load() # чтобы сохранялся интерфейс, иначе ошибка
            
            if  where[:4] == 'loc_': trySpecialEvent(where) # спец эвент
            if len(args) > 0:
                changetime(args[0])
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
        global noEventTime, mtime, lastEventTime, same_loc
        if 'classroom' in getLoc(location).position and lt() > 0: 
            location += 'Learn' #Если сейчас уроки, то добавляем к поиску локаций Learn
        if lt() == -4: location += 'Night' # Если ночь, добавляем Night
        if location in ['loc_office'] and same_loc == 1:
            return False
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
            lastEventTime = mtime #запоминаем время
            noEventTime = 0 # Сбрасываем переменную "время без эвентов"
            renpy.jump(callEvent) #эвент
        return False

    def trySpecialEvent(location):
        if len(getLoc(location).qwests) > 0:
            qArr = []
            for q in getLoc(location).qwests:
                if q.done == False:
                    qArr.append(q)
            if len(qArr) > 0:
                renpy.jump(choice(qArr).id)
                
            
    #Добавление людей на локации
    def addPeopleLocations():
        global hour, weekday, callup, detentions, movedArray
        mystring = ''
        counter = 0
        statusDistribution() # распределяем статусы по локациям
        if lt() > 0: # заполняем классы, если уроки
            fillClasses()
        else:
            avaliableLocations = []
            for x in locations:
                if x.getprob() > 0:
                    avaliableLocations.append(x)
            for x in allChars:
                x.reaction = ''
                if x != callup and x not in movedArray and x != interactionObj:
                    if x.getLocationStatus() == stop_status:
                        x.moveToLocation(x.location)
                        continue
                        
                    x.moveToLocation(None) # Всех выкидываем с локаций
                    
                    if x in teachers and lt() == 0 and rand(1,3) == 1: # учителя будут тусоваться в учительской
                        x.moveToLocation('loc_teacherRoom')
                        continue
                        
                    if x == dante and lt() >= 0: # библиотекарша всегда в библиотеке
                            x.moveToLocation('loc_library')
                            continue
                        
                    if x == gonoreevna and lt() >= 0: # Доктор должен быть в мед кабинете
                            x.moveToLocation('loc_doctor')
                            continue
                        
                    if x in detentions and hour >= 15 and school.detention != 'no': # если наказан, то после уроков
                        if school.detention in ['education','upskirt']: # будет в 3-ем классе
                            x.moveToLocation('loc_class3','noStatus')
                            x.forceLocationStatus(learn_status)
                            
                        elif school.detention == 'cleaning': # если уборка в школе,то скорее всего будет где то в школе
                            for loc in locations:
                                if 'school' in loc.position and rand(1,5) == 1:
                                     x.moveToLocation(loc,'noStatus')
                                     x.forceLocationStatus(clean_status)
                                     
                        elif school.detention == 'streetCleaning': # Если уборка улиц, тогда на улицу
                            x.moveToLocation(choice(['loc_street','loc_entrance','loc_shopStreet']),'noStatus')
                            x.forceLocationStatus(clean_status)
                            
                        elif school.detention in ['lock','tortue']: # Если закрыть или пытки - в подвал.
                            x.moveToLocation('loc_dungeon','noStatus')
                            if school.detention == 'lock':
                                x.forceLocationStatus(lock_status)
                            else:
                                x.forceLocationStatus(torture_status)
                        continue
                    
                    if x.club != '' and hour >= 15 and hour < 18 and x in studs: # Распределение клубов
                        if x.club == 'cherleader' and weekday in [1,3,5]:
                            x.moveToLocation('loc_gym')
                            x.forceLocationStatus(cheerleader_status)
                            
                        elif x.club == 'cosplay' and lt() == -1:
                            x.moveToLocation('loc_class1')
                            x.forceLocationStatus(cosplay_status)
                            
                        elif x.club == 'sport' and weekday in [2,4]:
                            x.moveToLocation('loc_gym')
                            x.forceLocationStatus(sport_status)
                            
                        elif x.club == 'paint' and lt() == -1:
                            x.moveToLocation('loc_class2')
                            x.forceLocationStatus(paint_status)
                            
                        elif x.club == 'medic' and lt() == -1:
                            x.moveToLocation('loc_doctor')
                            if rand(1,3) == 1:
                                x.forceLocationStatus(medic_status1)
                            else:
                                x.forceLocationStatus(medic_status2)
                        continue

                    if len(avaliableLocations) > 0:
                        for counter in range(0,1000):
                            temp = choice(avaliableLocations)
                            if rand(0,99) < temp.getprob():
                                if temp.id in ['loc_wcf','loc_wcm'] and x.getCorr() < 20:
                                    if x.getSex() == 'male':
                                        temp = 'loc_wcm'
                                    else:
                                        temp = 'loc_wcf'
                                x.moveToLocation(temp)
                                break
        if lt() == -4:
            # Сейчас ночь, нужно убрать всех с локаций
            clearLocations()
            if callup != dummy : callup = dummy # Заодно убираем вызванного ученика

        for loc in locations:
            dressPeople(loc.id) # Одеваем людей на локациях
        
       
    def clearLocations():
        for x in allChars:
            x.moveToLocation(None)

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
            if player.isCover('верх','низ') == False and player.getCorr() < 80:
                renpy.scene(layer='screens')
                renpy.jump('naked')
            elif player.isCover('верх','низ') == False and player.getCorr() >= 80 and location.id != 'loc_beach' and location.id != 'loc_pool':
                renpy.scene(layer='screens')
                renpy.jump('naked')
            elif player.getClothPurpose('swim') and location.id != 'loc_beach' and location.id != 'loc_pool':
                renpy.scene(layer='screens')
                renpy.jump('naked')
            elif player.isCover('попа') == False and player.getCorr() < 40:
                renpy.scene(layer='screens')
                renpy.jump('noPanties')
                
            if 'school' not in location.position and 'beach' != location.id and useClothesReputation == 1: # Снимаем репутацию за одежду
                repChange = 0
                if len(player.getCover()) <= 1:
                    repChange = -5
                for x in player.wear:
                    repChange += x.reputation
                    
                peoples = location.getPeople()
                for char in peoples:
                    if rand(1,3) == 1:
                        char.incRep(repChange)
                        
            if 'попа' not in player.getCover():
                player.incLust(0.1)
                
                
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
                if x.getCorr() < 50 and x.getLoy() < 50:
                    x.incRep(-1)
                    x.incCorr(0.5)

    def checkDeath():
        if player.getHealth() < 200 and rand(1,20) == 1:
            move('death')
            
    def checkOrgasm(location):
        if player.getLust() >= 100:
            if player.getCorr() < 35 or 'other' in location.position:
                renpy.jump('madness_low')
            else:
                if 'home' in location.position:
                    renpy.jump('madness_home')
                if 'school' in location.position and 'safe' not in location.position:
                    renpy.jump('madness_school')
# Прочие прооверки             
    def checkMisc():
        global flagIncome, temperature, mile_qwest_1_stage, mile_qwest_2_stage,mile_qwest_3_stage
        
        if hour >= 8 and olympiad.confirm == False and olympiad.active == True:
            olympiad.confirm = True
            clrscr()
            renpy.jump('olympiad_start')
            
        if hour >= 8 and olympiad.active == True and olympiad.weekday == weekday:
            clrscr()
            renpy.jump('olympiad_go')
            
        if hour >= 8 and weekday == 1 and flagIncome == 1:
            flagIncome = 0
            clrscr()
            renpy.jump('income')
            
        temperature = min(max(temperature,15),40)
        if ptime - work51 > 2 and curloc == 'loc_office':
            if temperature < 20 and same_loc == 0:
                renpy.jump('splitSystem_cold')
            if temperature > 35 and same_loc == 0:
                renpy.jump('splitSystem_hot')
                
        # В школе на перемену, если есть кто то в клубе трусиков и он открыт, вам их отдадут
        if 'school' in getLoc(curloc).position and lt() == 0 and 'pants' in school.clubs and len(getClubChars('pants')) > 0 and ptime - timeGetPanties > 24 and rand(1,3) == 1:
            renpy.jump('getPanties')
        
        # ограничения квестовых учителей
        if mile_qwest_1_stage == 0: 
            mustangovich.setCorr(min(20, mustangovich.getCorr()))
            
        if mile_qwest_1_stage == 1: 
            mustangovich.setCorr(min(50, mustangovich.getCorr()))
            
        if mile_qwest_2_stage == 0: 
            kupruvna.setCorr(min(20, kupruvna.getCorr()))
            
        if mile_qwest_2_stage == 10: 
            kupruvna.setCorr(min(10, kupruvna.getCorr()))
            kupruvna.setLoy(0)
            
        if mile_qwest_2_stage == 11: 
            kupruvna.setCorr(min(60, kupruvna.getCorr()))
            kupruvna.setLoy(0)
            
        if mile_qwest_3_stage == 0:
            danokova.setCorr(min(20, danokova.getCorr()))
            
        if mile_qwest_3_stage == 50:
            danokova.setCorr(min(30, danokova.getCorr()))
            danokova.setLoy(min(20, danokova.getLoy()))
            
        if mile_qwest_3_stage < 10:
            danokova.setCorr(min(60, danokova.getCorr()))
