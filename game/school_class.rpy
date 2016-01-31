init -20 python:
    stolenMoney = 0
    ###################################################################
    #Класс школы
    ###################################################################

    class School():
        def __init__(self, uniform = 'uniform', clubs = [], buildings = [], furniture = [], eduMats = 'poor', detention = 'education', baseIncome = 1000, daysWorked = 0):
            self.uniform = uniform
            self.unlockedUniforms = ['uniform','strict']
            self.clubs = clubs
            self.buildings = buildings
            self.furniture = furniture
            self.eduMats = eduMats
            self.unlockedEduMats = ['poor']
            self.detention = detention
            self.unlockedDetentions = ['education','cleaning']
            self.baseIncome = baseIncome
            self.caughtChance = 0
            self.daysWorked = daysWorked
            self.budget = 0
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
        
        def myIncome(self,char):
            if char == player:
                temp = self.baseIncome + self.daysWorked*char.getEdu()*20
            else:
                temp = 1000 + 5*char.getEdu()*20
            return temp
        
        def getIncome(self,char):
            char.money += self.myIncome(char)
        
        def getBudget(self):
            temp = 0
            temp += 500*getPar(studs,'edu')
            self.budget += temp
        
        def expectedBudget(self):
            temp = 0
            temp += 500*getPar(studs,'edu')
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
                
        def addEduMat(self,eduMat):
            if eduMat in ['standart','poor','good','eduSexy']:
                self.unlockedEduMats.append(eduMat)
                return True
            else:
                return False
                
        def addClub(self,club):
            if club in self.getAllClubs():
                self.clubs.append(club)
                return True
            else:
                return False
                
        def getAllClubs(self,*args):
            if len(args) > 0:
                tempArr = []
                for x in self.clubs:
                    tempArr.append(x)
                return tempArr
            else:
                return ['cherleader','cosplay','sport','paint','medic','pants']
                
        def removeClub(self,club):
            if club in self.clubs:
                self.clubs.remove(club)
                return True
            else:
                return False
                
        def getUniform(self):
            if self.uniform == 'usual':
                return 'Обычная одежда'
            elif self.uniform == 'strict':
                return 'Строгая форма'
            elif self.uniform == 'uniform':
                return 'Стандартная форма'
            elif self.uniform == 'sexy':
                return 'Сексуальная форма'
            elif self.uniform == 'skimpy':
                return 'Шлюховатая форма'
            elif self.uniform == 'naked':
                return 'Обнажённая форма'
            elif self.uniform == 'bdsm':
                return 'БДСМ форма'
                
    school = School()
    
    def votingFunc(type,amount, what):
        global mile_qwest_2_stage, mile_qwest_3_stage, mile_qwest_1_stage
        voteYes = voteNo = voteVeto = 0
        for teacher in teachers:
            if mile_qwest_2_stage in [10,11] and teacher == kupruvna:
                amount = -1
            if mile_qwest_3_stage == 50 and teacher == danokova:
                amount = -1
            if mile_qwest_1_stage == 2 and teacher == mustangovich:
                amount = -1
            
            if type == 'loy':
                if teacher.getLoy() >= amount:
                    voteYes += 1
                elif teacher.getLoy()*2 >= amount:
                    voteNo += 1
                else:
                    voteVeto += 1
                    
            if type == 'corr':
                if (teacher.getCorr() + teacher.getLoy()) >= amount*2:
                    voteYes += 1
                elif (teacher.getCorr() + teacher.getLoy()) >= amount:
                    voteNo += 1
                else:
                    voteVeto += 1
                    
        if voteYes > voteNo and voteVeto == 0:
            if what in ['usual','strict','uniform','sexy','skimpy','naked','bdsm']:
                school.unlockedUniforms.append(what)
                school.uniform = what
            if what in ['streetCleaning','upskirt','no','lock','tortue']:
                school.unlockedDetentions.append(what)
                school.detention = what
            if what in ['eduSexy']:
                school.budget -= 50000
                school.unlockedEduMats.append(what)
                school.eduMats = what
            if what in ['manec','video','bed','dildo','sportgirls','splitSystem']:
                if what == 'manec':
                    school.budget -= 20000
                if what == 'video':
                    school.budget -= 10000
                if what == 'dildo':
                    school.budget -= 15000
                if what == 'sportgirls':
                    school.budget -= 50000
                if what == 'splitSystem':
                    player.money -= 2000
                school.furniture.append(what)
                
            if what in ['wall','library','dungeon','chemlab','doctor']:
                if what == 'wall':
                    school.budget -= 100000
                if what == 'library':
                    # teachers.append(dante)
                    # allChars.append(dante)
                    school.budget -= 150000
                if what == 'dungeon':
                    school.budget -= 100000
                if what == 'chemlab':
                    school.budget -= 75000
                if what == 'doctor':
                    # teachers.append(gonoreevna)
                    # allChars.append(gonoreevna)
                    school.budget -= 25000
                school.buildings.append(what)
            return True
        else:
            return False
