init -20 python:
    stolenMoney = 0
    ###################################################################
    #Класс школы
    ###################################################################

    class School():
        def __init__(self, uniform = 'normal', clubs = [], buildings = [], furniture = [], eduMats = 'standart', detention = 'education', baseIncome = 1000, daysWorked = 0):
            self.uniform = uniform
            self.unlockedUniforms = ['normal','strict']
            self.clubs = clubs
            self.buildings = buildings
            self.furniture = furniture
            self.eduMats = eduMats
            self.unlockedEduMats = ['standart','poor','good']
            self.detention = detention
            self.unlockedDetentions = ['education','cleaning']
            self.baseIncome = baseIncome
            self.caughtChance = 0
            self.daysWorked = daysWorked
            self.budget = 25000
            self.income = 0
            
        def working(self):
            self.daysWorked += 1
            move('working')
            
        def steal(self,who):
            global stolenMoney
            self.caughtChance += 1
            stolenMoney = min(self.budget, who.getEdu()*rand(50,100))
            if self.caughtChance*10 - who.getEdu() > rand(0,99):
                move('catched')
            else:
                move('stolen')
        
        def myIncome(self):
            temp = max(self.baseIncome, self.daysWorked*self.baseIncome)
            return temp
            
        def getEduMats(self):
            if self.eduMats == 'standart':
                return 'Стандартные'
            elif self.eduMats == 'poor':
                return 'Дешёвые'
            elif self.eduMats == 'good':
                return 'Хорошие'
            elif self.eduMats == 'eduSexy':
                return '"Нестандартные"'
            else:
                return 'WTF???'
                
        def getUniform(self):
            if self.uniform == 'usual':
                return 'Обычная одежда'
            elif self.uniform == 'scrict':
                return 'Строгая форма'
            elif self.uniform == 'normal':
                return 'Стандартная форма'
            elif self.uniform == 'sexy':
                return 'Сексуальная форма'
            elif self.uniform == 'skimpy':
                return 'Шлюховатая форма'
            else:
                return 'Обнажённая форма'
                
    def votingFunc(type,amount, what):
        voteYes = voteNo = voteVeto = 0
        for teacher in teachers:
            if type == 'loy':
                if teacher.getLoy() >= amount:
                    voteYes += 1
                elif teacher.getLoy()*2 >= amount:
                    voteNo += 1
                else:
                    voteVeto += 1
                    
            if type == 'corr':
                if teacher.getCorr() >= amount:
                    voteYes += 1
                elif teacher.getCorr()*2 >= amount:
                    voteNo += 1
                else:
                    voteVeto += 1
                    
        if voteYes > voteNo and voteVeto == 0:
            if what in ['usual','scrict','normal','sexy','skimpy','naked']:
                school.unlockedUniforms.append(what)
                school.uniform = what
            if what in ['streetCleaning','upskirt','no']:
                school.unlockedDetentions.append(what)
                school.detention = what
            if what in ['eduSexy']:
                school.unlockedEduMats.append(what)
                school.eduMats = what
            if what in ['manec','video','bed']:
                if what == 'manec':
                    school.budget -= 20000
                if what == 'video':
                    school.budget -= 10000
                school.furniture.append(what)
            if what in ['wall','library']:
                if what == 'wall':
                    school.budget -= 100000
                if what == 'library':
                    school.budget -= 150000
                school.furniture.append(what)
            return True
        else:
            return False