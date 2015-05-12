init python:
    def dailyRecount(chars):
        global lastWork
        
        if (ptime - last_eat)/24 > 1:
            temp = (ptime - last_eat)/2
            player.setHealth( -temp )
        
        lastWork = -30
        
        for x in chars:
            x.setCorr((getPar(teachers, 'corr') - x.stats.corr)/10)
            x.setRep((getPar(studs, 'rep') - x.stats.reputation)/100)