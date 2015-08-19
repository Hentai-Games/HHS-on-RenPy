init python:
    def dailyRecount(chars):
    
        global him_zavivka, depilation, skin_care, manicure, pedicure, ptime, last_eat
        
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
        
        
        for char in chars:
            char.setCorr((getPar(teachers, 'corr') - char.stats.corr)/10)
            char.setRep((getPar(studs, 'rep') - char.stats.reputation)/100)
            