init python:
    def dailyRecount(chars):
    
        global him_zavivka, depilation, skin_care, manicure, pedicure, ptime, last_eat, timeGetPanties
        
        timeGetPanties = 0 # сброс времени выдачи трусов
        aphroUsedArr[:] = [] # сброс людей под афродизиаком
        
        if development == 0:
            # Голод
            if (ptime - last_eat)/24 > 1:
                temp = (ptime - last_eat)/2
                player.incHealth( -temp )
                
            # Вонь    
            if ptime - lastWashed > 48:
                player.incDirty(1)
            
        # Работа
        lastWork = -30
        
        # Салон красоты
        if him_zavivka > 0:
            him_zavivka -= 1
        if depilation > 0:
            depilation -= 1
        if skin_care > 0:
            skin_care -= 1
        if manicure > 0:
            manicure -= 1
        if pedicure > 0:
            pedicure -= 1

        # Модификатор образования
        if school.eduMats == 'standart':
            eduMod = 1
        elif school.eduMats == 'poor':
            eduMod = 0.5
        elif school.eduMats == 'good':
            eduMod = 2
        elif school.eduMats == 'eduSexy':
            eduMod = 0.1

        
        # Если есть клуб, забиваем в него как минимум 4 человек
        if 'cherleader' in school.clubs and len(getClubChars('cherleader')) < 4:
            while len(getClubChars('cherleader')) < 4:
                choice(getClubChars('','female')).club = 'cherleader'
                
        if 'cosplay' in school.clubs and len(getClubChars('cosplay')) < 4:
            while len(getClubChars('cosplay')) < 4:
                choice(getClubChars('')).club = 'cosplay'

        if 'sport' in school.clubs and len(getClubChars('sport')) < 4:
            while len(getClubChars('sport')) < 4:
                choice(getClubChars('')).club = 'sport'
                
        if 'medic' in school.clubs and len(getClubChars('medic')) < 4:
            while len(getClubChars('medic')) < 4:
                choice(getClubChars('')).club = 'medic'
                
        if 'pants' in school.clubs and len(getClubChars('pants')) < 4:
            while len(getClubChars('pants')) < 4:
                choice(getClubChars('','female')).club = 'pants'

                
        for char in chars:
            
            # Поломка подарков
            for item in char.inventory:
                if item.type == 'present':
                    item.durability -= rand(1,2)
                    if item.durability <= 0:
                        char.removeItem(item)
                        
            char.incCorr((getPar(teachers, 'corr') - char.getCorr())/10)
            char.incRep((getPar(studs, 'rep') - char.getRep())/100)
            if char in studs:
                # Добавление трусов, если их нет у чара.
                if char.getSex != 'male' and char.getItem(studpantiesF.name) == False:
                    char.addItem(studpantiesF)
                    
                # Убираем клуб, если его удалили или ученик не в том клубе
                if char.club not in school.clubs or (char.getSex() == 'male' and char.club in ['cherleader','pants']):
                    char.club = ''
                
                # Добавляем клуб (предварительная версия)
                if char.club == '' and rand(1,10) == 1 and len(school.getAllClubs('available')) > 0:
                    if char.getSex() != 'male':
                        char.club = choice(school.getAllClubs('available'))
                    else:
                        available = school.getAllClubs('available')
                        tempArr = []
                        for club in available:
                            if club not in ['pants','cherleader']:
                                tempArr.append(club)
                        if len(tempArr) > 0:
                            char.club = choice(tempArr)
                    
                
                # inhibLow
                if inhibLow == 1:
                    char.incLust(10)
                elif inhibLow == 2:
                    char.incLust(15)
                elif inhibLow == 3:
                    char.incCorr(0.5)
                elif inhibLow == 4 and char.getSex() == 'male':
                    char.incLust(30)
                    
                if school.uniform == 'strict': # Строгая школьная форма
                    char.incRep(1)
                    char.incFun(-5)
                    char.incEdu((getPar(teachers, 'edu') - char.getEdu())/10/eduMod)
                    
                elif school.uniform == 'uniform': # Обычная школьная форма
                    if char.getFun() > 10: char.incFun(-2)
                    char.incEdu((getPar(teachers, 'edu') - char.getEdu())/20/eduMod)
                    
                elif school.uniform == 'usual': # Обычная одежда
                    if char.getFun() < 20: char.incFun(1)
                    char.incEdu((getPar(teachers, 'edu') - char.getEdu())/30/eduMod)
                    
                elif school.uniform == 'sexy': # Сексуальная форма
                    if char.getCorr() < 25: char.incCorr(0.5)
                    if char.getFun() < 40: char.incFun(1)
                    char.incEdu((getPar(teachers, 'edu') - char.getEdu())/50/eduMod)
                    
                elif school.uniform == 'skimpy': # Шлюховатая форма
                    if char.getCorr() < 50: char.incCorr(0.8)
                    if char.getFun() < 60: char.incFun(1)
                    char.incEdu((getPar(teachers, 'edu') - char.getEdu())/100/eduMod)
                    
                else: # Голая форма
                    char.incEdu((getPar(teachers, 'edu') - char.getEdu())/500/eduMod)
                    if char.getCorr() > 50:
                        if char.getCorr() < 80: char.incCorr(1)
                        if char.getFun() < 80: char.incFun(1)
                    else:
                        if char.getCorr() > 25: char.incCorr(-1)
                        char.incFun(-5)
                        
                if school.eduMats == 'good': # Хорошие образовательные материалы
                    if char.getFun() < 15: char.incFun(1)
                elif school.eduMats == 'eduSexy': # Лука Мудищев
                    if char.getFun() < 35: char.incFun(1)
                    
                if 'manec' in school.furniture: # Манекен
                    if char.getFun() < 25: char.incFun(1)
                    if char.getCorr() < 15: char.incCorr(0.5)
                    
                if 'video' in school.furniture: # Видео
                    if char.getFun() < 55: char.incFun(1)
                    if char.getCorr() < 25: char.incCorr(0.5)
                    
                if 'dildo' in school.furniture: # Дилды
                    if char.getFun() < 35: char.incFun(1)
                    if char.getCorr() < 30: char.incCorr(0.5)
                    
    def hourlyReset():
        global hour, weekday, inhibLow
        
        if hour == 18:
            inhibLow = 0
        
        if hour % 4 == 0:
            for char in allChars:
                char.sayCount = int(1 + char.getLoy()/10 + (player.getBeauty()/20))
        
        if hour >= 17:
            detentions[:] = []
        
        if school.budget < 0: 
            school.removeClub('cherleader')
            school.removeClub('sport')
            school.removeClub('cosplay')
            school.removeClub('medic')
            school.removeClub('paint')
            
        if hour == 15 and weekday < 6:
            if 'cherleader' in school.clubs and weekday in [1,3,5]:
                school.budget -= 200
            if 'sport' in school.clubs and weekday in [2,4]:
                school.budget -= 100
            if 'cosplay' in school.clubs:
                school.budget -= 500
            if 'paint' in school.clubs:
                school.budget -= 300
            if 'medic' in school.clubs:
                school.budget -= 250
                
        