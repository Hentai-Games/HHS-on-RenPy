init -20 python:

    ###################################################################
    #Класс школы
    ###################################################################

    class School():
        def __init__(self, uniform = 'usual', clubs = [], buldings = [], furniture = [], eduMats = 'normal', detention = 'education', baseIncome = 1000, daysWorked = 0):
            self.uniform = uniform
            self.clubs = clubs
            self.buldings = buldings
            self.furniture = furniture
            self.eduMats = eduMats
            self.detention = detention
            self.baseIncome = baseIncome
            self.caughtChance = 0
            self.daysWorked = daysWorked
            self.income = 0
            
        def working(self):
            self.daysWorked += 1
            move('working')
            
        def steal(self,who):
            self.caughtChance += 1
            if self.caughtChance*10 - who.getEdu() > rand(0,99):
                move('catched')
            else:
                move('stolen')
        
        def myIncome(self):
            return max(self.baseIncome, self.daysWorked*self.baseIncome)