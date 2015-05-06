init python:
    def dailyRecount(chars):
        if (ptime - last_eat)/24 > 1:
            temp = (ptime - last_eat)/2
            player.setHealth( -temp )
            
        for x in chars:
            x.setCorr((getPar(teachers, 'corr') - x.stats.corr)/10)
            x.setRep((getPar(studs, 'rep') - x.stats.reputation)/100)