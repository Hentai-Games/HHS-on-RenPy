init python:
    def dailyRecount(chars):
    
        global him_zavivka, depilation, skin_care, manicure, pedicure, ptime, last_eat
        
        if development == 0:
            # Голод
            if (ptime - last_eat)/24 > 1:
                temp = (ptime - last_eat)/2
                player.setHealth( -temp )
                
            # Вонь    
            if ptime - lastWashed > 48:
                player.setDirty(1)
            
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

            
        for char in chars:
            char.setCorr((getPar(teachers, 'corr') - char.getCorr())/10)
            char.setRep((getPar(studs, 'rep') - char.getRep())/100)
            if char in studs:
                # inhibLow
                if inhibLow == 1:
                    char.setLust(10)
                elif inhibLow == 2:
                    char.setLust(15)
                elif inhibLow == 3:
                    char.setCorr(0.5)
                elif inhibLow == 4 and char.getSex() == 'male':
                    char.setLust(30)
                    
                if school.uniform == 'strict': # Строгая школьная форма
                    char.setRep(1)
                    char.setFun(-5)
                    char.setEdu((getPar(teachers, 'edu') - char.getEdu())/10/eduMod)
                elif school.uniform == 'uniform': # Обычная школьная форма
                    if char.getFun() > 10: char.setFun(-2)
                    char.setEdu((getPar(teachers, 'edu') - char.getEdu())/20/eduMod)
                elif school.uniform == 'usual': # Обычная одежда
                    if char.getFun() < 20: char.setFun(1)
                    char.setEdu((getPar(teachers, 'edu') - char.getEdu())/30/eduMod)
                elif school.uniform == 'sexy': # Сексуальная форма
                    if char.getCorr() < 25: char.setCorr(0.5)
                    if char.getFun() < 40: char.setFun(1)
                    char.setEdu((getPar(teachers, 'edu') - char.getEdu())/50/eduMod)
                elif school.uniform == 'skimpy': # Шлюховатая форма
                    if char.getCorr() < 50: char.setCorr(0.8)
                    if char.getFun() < 60: char.setFun(1)
                    char.setEdu((getPar(teachers, 'edu') - char.getEdu())/100/eduMod)
                else: # Голая форма
                    char.setEdu((getPar(teachers, 'edu') - char.getEdu())/500/eduMod)
                    if char.getCorr() > 50:
                        if char.getCorr() < 80: char.setCorr(1)
                        if char.getFun() < 80: char.setFun(1)
                    else:
                        if char.getCorr() > 25: char.setCorr(-1)
                        char.setFun(-5)
                        
                if school.eduMats == 'good': # Хорошие образовательные материалы
                    if char.getFun() < 15: char.setFun(1)
                elif school.eduMats == 'eduSexy': # Лука Мудищев
                    if char.getFun() < 35: char.setFun(1)
                    
                if 'manec' in school.furniture: # Манекен
                    if char.getFun() < 25: char.setFun(1)
                    if char.getCorr() < 15: char.setCorr(0.5)
                    
                if 'video' in school.furniture: # Видео
                    if char.getFun() < 55: char.setFun(1)
                    if char.getCorr() < 25: char.setCorr(0.5)
                    
                if 'dildo' in school.furniture: # Дилды
                    if char.getFun() < 35: char.setFun(1)
                    if char.getCorr() < 30: char.setCorr(0.5)
                    
    def hourlyReset():
        global hour, weekday
        
        if hour % 4 == 0:
            for char in allChars:
                char.sayCount = int(1 + char.getLoy()/10 + (player.getBeauty()/20))
        
        if hour >= 17:
            detentions[:] = []
        
        if school.budget < 0: 
            school.removeClub('cherleader')
            school.removeClub('sport')
            school.removeClub('cosplay')
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
                

        