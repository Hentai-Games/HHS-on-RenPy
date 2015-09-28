init -20 python:
    import copy
    from random import choice
    from operator import itemgetter, attrgetter, methodcaller

    ###################################################################
    #Класс частей тела
    ###################################################################

    class BodyPart():
        def __init__(self, name, visibility = False, sperm = False, size = 0, maxSize = 0, minSize = 0):
            self.name = name
            self.visibility = visibility
            self.sperm = sperm
            self.size = size
            self.minSize = minSize
            self.maxSize = maxSize

        def normalize(self):
            self.size = max(self.minSize, min(self.size, self.maxSize))

    # Общий класс тела с частями, общими для всех
    class Body(object):
        def __init__(self, height = 140, bodyparts = {}):
            self.parts = {}
            self.parts['ноги'] = BodyPart('ноги', True)
            self.parts['лицо'] = BodyPart('лицо', True)
            self.parts['грудь'] = BodyPart('грудь', True, minSize = 0, maxSize = 10)
            self.parts['анус'] = BodyPart('анус', minSize = 0, maxSize = 25)
            self.parts['рот'] = BodyPart('рот')
            self.parts['руки'] = BodyPart('руки', True)
            self.height = height

            # Копируем и перезаписываем части тела, если надо
            for k,v in bodyparts:
                self.parts[k] = v

        @classmethod
        def random(cls):
            body = cls(height = rand(140, 170))
            body.parts['анус'].size = randf(0, 1)
            return body

        def normalize(self):
            for _,v in self.parts.iteritems():
                v.normalize()

        def sex(self):
            return 'U wot m8'

        def partsWithSperm(self):
            return [v for k,v in self.parts.iteritems() if v.sperm]


    # Мужское тело
    class MaleBody(Body):
        def __init__(self, height, bodyparts = {}, anusSize = 0, penisSize = 0):
            super(MaleBody, self).__init__(height, bodyparts)
            self.parts['пенис'] = BodyPart('пенис', minSize = 0, maxSize = 30, size = penisSize) #
            self.parts['анус'].size = anusSize

        @classmethod
        def random(cls):
            body = super(MaleBody, cls).random()
            body.parts['пенис'].size = randf(10, 15)
            return body

        def sex(self):
            return 'male'

    # Женское тело
    class FemaleBody(Body):
        def __init__(self, height, bodyparts = {}, anusSize = 0, vaginaSize = 0, breastSize = 0):
            super(FemaleBody, self).__init__(height, bodyparts)
            self.parts['вагина'] = BodyPart('вагина', minSize = 0, maxSize = 40, size = vaginaSize)
            self.parts['анус'].size = anusSize
            self.parts['грудь'].size = breastSize

        @classmethod
        def random(cls):
            body = super(FemaleBody, cls).random()
            body.parts['вагина'].size = randf(0, 1)
            body.parts['грудь'].size = randf(0, 3)
            return body

        def sex(self):
            return 'female'

    # Фута
    class FutaBody(Body):
        def __init__(self, height, bodyparts = {}, anusSize = 0, vaginaSize = 0, penisSize = 0, breastSize = 0):
            super(FutaBody, self).__init__(height, bodyparts)
            self.parts['вагина'] = BodyPart('вагина', minSize = 0, maxSize = 40, size = vaginaSize)
            self.parts['пенис'] = BodyPart('пенис', minSize = 0, maxSize = 30, size = penisSize)
            self.parts['анус'].size = anusSize
            self.parts['грудь'].size = breastSize

        @classmethod
        def random(cls):
            body = super(FutaBody, cls).random()
            body.parts['пенис'].size = randf(10, 15)
            body.parts['вагина'].size = randf(0, 1)
            body.parts['грудь'].size = randf(0, 3)
            return body

        def sex(self):
            return 'futa'

    # Параметры персонажа
    class Stats:
        def __init__(self, **stats):
            self.loyalty = stats['loyalty'] if 'loyalty' in stats else 0
            self.fun = stats['fun'] if 'fun' in stats else 0
            self.corr = stats['corr'] if 'corr' in stats else 0
            self.lust = stats['lust'] if 'lust' in stats else 0
            self.will = stats['will'] if 'will' in stats else 0
            self.education = stats['education'] if 'education' in stats else 0
            self.health = stats['health'] if 'health' in stats else 0
            self.intelligence = stats['intelligence'] if 'intelligence' in stats else 0
            self.beauty = stats['beauty'] if 'beauty' in stats else 0
            self.reputation = stats['reputation'] if 'reputation' in stats else 0
            self.energy = stats['energy'] if 'energy' in stats else 0
            self.dirty = stats['dirty'] if 'dirty' in stats else 0

        def normalize(self):
            self.loyalty = min(max(self.loyalty,0),100)
            self.fun = min(max(self.fun,0),100)
            self.corr = min(max(self.corr,0),100)
            self.lust = min(max(self.lust,0),100)
            self.will = min(max(self.will,0),100)
            self.education = min(max(self.education,0),150)
            self.health = min(max(self.health,0),2000)
            self.energy = min(max(self.energy,0),self.health)
            self.intelligence = min(max(self.intelligence,0),100)
            self.beauty = min(max(self.beauty,0),200)
            self.dirty = min(max(self.dirty,0),30)
            self.reputation = min(max(self.reputation,0),100)

        @classmethod
        def random(cls):
            stats = cls()
            stats.loyalty = randf(0, 10)
            stats.fun = randf(10, 20)
            stats.corr = randf(0, 5)
            stats.lust = randf(0, 5)
            stats.will = randf(0, 100)
            stats.intelligence = randf(0, 100)
            stats.education = stats.intelligence / 4
            stats.health = randf(800, 1200)
            stats.energy = stats.health
            stats.beauty = randf(20, 90)
            stats.reputation = 50
            return stats

    class Char(object):

        # Мужские имена
        maleNames = ['Саша', 'Андрей', 'Влад', 'Саня', 'Дима', 'Коля', 'Женя', 'Ваня', 'Миша', 'Егор', 'Тимур', 'Руслан', 'Макс', 'Даня', 'Кирилл', 'Никита', 'Денис', 'Илюша', 'Тёма', 'Артур', 'Рома', 'Богдан', 'Глеб', 'Захар', 'Владик', 'Ян', 'Паша', 'Юра', 'Антон', 'Игорь', 'Степан', 'Вадим', 'Сеня', 'Лёва', 'Федя', 'Филя', 'Виктор', 'Витя', 'Олег']

        # Женские имена
        femaleNames = ['Софья', 'Маша', 'Настя', 'Даша', 'Анна', 'Лиза', 'Полина', 'Вика', 'Катя', 'Варвара', 'Ксеня', 'Саша', 'Алиса', 'Вероника', 'Арина', 'Валерия', 'Маргарита', 'Василиса', 'Ульяна', 'Алина', 'Милана', 'Ева', 'Алёна', 'Юля', 'Диана', 'Кристина', 'Оля', 'Вера', 'Таня', 'Ирина', 'Яна', 'Лена', 'Женя', 'Ангелина', 'Марина', 'Света', 'Надя', 'Олеся', 'Наташа', 'Ника']

        # Фамилии
        lastNames = ['Смирнов', 'Иванов', 'Кузнецов', 'Попов', 'Соколов', 'Козлов', 'Новиков', 'Морозов', 'Петров', 'Волков', 'Соловьев', 'Васильев', 'Зайцев', 'Павлов', 'Семенов', 'Голубев', 'Виноградов', 'Богданов', 'Воробьев', 'Федоров', 'Михайлов', 'Беляев', 'Тарасов', 'Белов', 'Комаров', 'Орлов', 'Киселев', 'Макаров', 'Андреев', 'Ковалев', 'Ильин', 'Гусев', 'Титов', 'Кузьмин', 'Кудрявцев', 'Баранов', 'Куликов', 'Алексеев', 'Степанов', 'Яковлев']

        def __init__(self, fname = '', lname = '', color = '#FFFFFF', age = 0, body = Body(), stats = Stats(), inventory = 0, sets = 5, wear = [], club = '', picto = '', location = '', sayCount = 0, money = 0):
            self.fname = fname
            self.lname = lname
            self.name = fname + ' ' + lname
            self.sex = body.sex()
            self.age = age
            self.body = body
            self.stats = stats
            self.color = color
            self.inventory = inventory
            self.sets = []
            for x in range(0,sets):
                self.sets.append([])
            self.wear = wear
            self.inClass = 0
            self.club = club
            self.picto = picto
            self.location = location
            self.money = money
            self.sayCount = sayCount
            self.say = Character (self.fullName(), kind=adv, dynamic = False, color = self.color, show_side_image = Image(self.picto, xalign=0.0, yalign=1.0), window_left_padding = 170)
            config.side_image_tag = self.picto
            self.locationStatus = None
            self.partner = None
        
        # Создание случайного персонажа с полом sex ('male', 'female' или 'futa') и картинкой picto
        @classmethod
        def random(cls, sex, picto):
            #выбор пола
            body = Body()
            if sex == 'female':
                body = FemaleBody.random()
            elif sex == 'futa':
                body = FutaBody.random()
            elif sex == 'male':
                body = MaleBody.random()

            stats = Stats.random()
            firstName = choice(cls.maleNames) if body.sex() == 'male' else choice(cls.femaleNames)
            lastName = choice(cls.lastNames)
            if body.sex() != 'male':
                lastName += 'а'

            color = '#FFFFFF'
            if body.sex() == 'female':
                color = '#FF85F1'
            elif body.sex() == 'male':
                color = '#269AFF'
            elif body.sex() == 'futa':
                color = '#FC3A3A'
            
            character = cls(firstName, lastName, color = color, age = rand(12, 16), body = body, stats = stats, picto = picto, inventory = [], wear = [])
            return character

        def normalize(self):
            self.body.normalize()
            self.stats.normalize()

        def fullName(self):
            return self.fname + ' ' + self.lname
            
###################################################################
#Incrementers
###################################################################

# Измнение loyalty
        def incLoy(self,amount):
            self.stats.loyalty += amount*max(0.1, (100 - self.getWill())/100)
# Измнение fun
        def incFun(self,amount):
            self.stats.fun += amount
# Измнение развратности
        def incCorr(self,amount):
            if self != player:
                self.stats.corr += amount*max(0.1, (100 - self.getWill())/100)
            else:
                self.stats.corr += amount
                
# Измнение lust
        def incLust(self,amount):
            self.stats.lust += amount
# Измнение will
        def incWill(self,amount):
            self.stats.will += amount
# Измнение education
        def incEdu(self,amount):
            if self.getFun() < 25:
                funMod = 4
            elif self.getFun() < 50:
                funMod = 3
            elif self.getFun() < 75:
                funMod = 2
            else:
                funMod = 1
            self.stats.education += (amount*(self.getIntel()/100))/funMod
# Измнение health
        def incHealth(self,amount):
            self.stats.health += amount
# Измнение intelligence
        def incIntel(self,amount):
            self.stats.intelligence += amount
# Измнение beauty
        def incBeauty(self,amount):
            self.stats.beauty += amount
# Измнение reputation
        def incRep(self,amount):
            self.stats.reputation += amount
# Измнение energy
        def incEnergy(self,amount):
            self.stats.energy += amount
# Измнение dirty
        def incDirty(self,amount):
            self.stats.dirty += amount
            
###################################################################
#Setters
###################################################################

# Измнение loyalty
        def setLoy(self,amount):
            self.stats.loyalty = amount
# Измнение fun
        def setFun(self,amount):
            self.stats.fun = amount
# Измнение развратности
        def setCorr(self,amount):
            self.stats.corr = amount
                
# Измнение lust
        def setLust(self,amount):
            self.stats.lust = amount
# Измнение will
        def setWill(self,amount):
            self.stats.will = amount
# Измнение education
        def setEdu(self,amount):
            self.stats.education = amount
# Измнение health
        def setHealth(self,amount):
            self.stats.health = amount
# Измнение intelligence
        def setIntel(self,amount):
            self.stats.intelligence = amount
# Измнение beauty
        def setBeauty(self,amount):
            self.stats.beauty = amount
# Измнение reputation
        def setRep(self,amount):
            self.stats.reputation = amount
# Измнение energy
        def setEnergy(self,amount):
            self.stats.energy = amount
# Измнение dirty
        def setDirty(self,amount):
            self.stats.dirty = amount
            
###################################################################
# Getters
###################################################################

# Получение loyalty
        def getLoy(self):
            return self.stats.loyalty
# Получение fun
        def getFun(self):
            return self.stats.fun
# Получение развратности
        def getCorr(self):
            return self.stats.corr
# Получение lust
        def getLust(self):
            return self.stats.lust
# Получение will
        def getWill(self):
            return self.stats.will
# Получение education
        def getEdu(self):
            return self.stats.education
# Получение health
        def getHealth(self):
            return self.stats.health
# Получение intelligence
        def getIntel(self):
            return self.stats.intelligence
# Получение beauty
        def getBeauty(self):
            beauty = self.stats.beauty - self.getDirty()*5
            if him_zavivka > 0:
                beauty += 10
            if depilation > 0:
                beauty += 20
            if skin_care > 0:
                beauty += 40
            if manicure > 0:
                beauty += 5
            if pedicure > 0:
                beauty += 5
            return beauty
# Получение reputation
        def getRep(self):
            return self.stats.reputation
# Получение energy
        def getEnergy(self):
            return self.stats.energy
# Получение dirty
        def getDirty(self):
            return self.stats.dirty
            
        def getSex(self,*args):
            if len(args) == 0:
                return self.body.sex()
            else:
                if args[0] == 'mf':
                    if self.body.sex() == 'male':
                        return self.body.sex()
                    else:
                        return 'female'
            
###################################################################
#инвентарь
###################################################################
        #Добавление нескольких предметов в инвентарь
        def addItems(self,*args):
            flag = 0
            for x in args:
                for y in allItems:
                    if x == y.name:
                        temp = copy.copy(y)
                        self.inventory.append(temp)
                        flag += 1
            if flag == len(args):
                return True
            else:
                renpy.say('','ITEMS ARE NOT ADDED!')
                return False

        #Добавлние одного предмета (можно использовать и addItems) просто на всякий пожарный.
        def addItem(self,item):
            temp = copy.copy(item)
            self.inventory.append(temp)

        # Удаление айтема
        def removeItem(self,item):
            if self.inventory.count(item) > 0:
                self.inventory.remove(item)
                return True
            if self.wear.count(item) > 0:
                self.wear.remove(item)
                return True
            return False

        def initSet(self,number,list):
            self.sets[number] = []
            for x in list:
                self.sets[number].append(x)
                
        # Создание сета:
        def createSet(self, number):
            self.sets[number] = []
            for x in self.wear:
                self.sets[number].append(x.name)
                
        # Применение сета
        def applySet(self,number):
            self.undress()
            for x in self.sets[number]:
                if self.getItem(x) != False :
                    player.wearing(self.getItem(x))
                
                
        # Удаление айтемов !!! Сносит ВСЕ с данным названием!!!
        def removeItems(self,*args):
            flag = 0
            for x in args:
                for y in self.inventory:
                    if x == y.name:
                        self.inventory.remove(y)
                        flag += 1
            for x in args:
                for y in self.wear:
                    if x == y.name:
                        self.wear.remove(y)
                        flag += 1
            if flag == len(args):
                return True
            else:
                return False

        # Проверка на наличие айтема
        def hasItem(self, name):
            for x in self.inventory:
                if name == x.name:
                    return True
            for x in self.wear:
                if name == x.name:
                    return True
            return False

        # Подсчёт айтемов
        def countItem(self, name):
            counter = 0
            for x in self.inventory:
                if name == x.name:
                    counter += 1
            return counter

        # Применение айтема
        def apply(self, name):
            for x in self.inventory:
                if x.name == name:
                    x.durability -= 1
                    self.checkDur()
                    return
                    
            for x in self.wear:
                if x.name == name:
                    x.durability -= 1
                    self.checkDur()
                    return
                    
        # Удаление всех использованных айтемов
        def checkDur(self):
            for x in self.inventory:
                if x.durability <= 0:
                    self.inventory.remove(x)
            for x in self.wear:
                if x.durability <= 0:
                    self.wear.remove(x)

        # Функция еды
        def eat(self, food):
            global last_eat
            if food.name == 'Энергетик':
                last_eat -= 2
            else:
                last_eat = ptime
            self.stats.energy += food.energy
            food.durability -= 1
            self.checkDur()

        #Есть ли сперма вообще
        def isSperm(self):
            parts = self.body.partsWithSperm()
            for i in parts:
                if i.visibility:
                    return 2
            return 1 if len(parts) > 0 else 0

        #Если ли сперма на чём то из
        def getSperm(self,*args):
            partNames = [x.name for x in self.body.partsWithSperm()]
            for x in args:
                if x in partNames:
                    return True
            return False

        #Возвратить стрингу с перечислением заляпанных частей тела
        def printSperm(self):
            partNames = [x.name for x in self.body.partsWithSperm()]
            return ", ".join(partNames)

        #Заляпать спермой части тела
        def coverSperm(self, *args):
            for x in args:
                if x in self.body.parts:
                    self.body.parts[x].sperm = True

        #Помыться
        def cleanAll(self):
            self.dirty = 0
            for _,x in self.body.parts.iteritems():
                x.sperm = False

        #Очистить часть тела
        def clean(self, *args):
            for x in args:
                if x in self.body.parts:
                    self.body.parts[x].sperm = False

        def buy(self, item, *args):
            if len(args) == 0:
                if self.money >= item.cost:
                    self.money -= item.cost
                    if self.hasItem(item.name) == True:
                        self.getItem(item.name).durability += item.durability
                    else :
                        temp = copy.copy(item)
                        self.inventory.append(temp)
            else :
                 if self.money >= item.cost:
                    self.money -= item.cost
                    temp = copy.copy(item)
                    self.inventory.append(temp)

        # Функция получения предмета по имени
        def getItem(self,name):
            for x in self.inventory:
                if x.name == name:
                    return x
            for x in self.wear:
                if x.name == name:
                    return x
            return False
            
        def sellItem(self,name):
            for x in self.inventory:
                if x.name == name:
                    self.money += x.cost
                    self.inventory.remove(x)
                    return True
            return False
            
        def sellItems(self,name):
            counter = 0
            while self.sellItem(name):
                counter += 1
            return counter

        def countItems(self,name):
            counter = 0
            for x in self.inventory:
                if x.name == myItem.name:
                    counter += 1
            return counter
            
        #Сброс переменных
        def reset(self):
            self.normalize()

        # Функция одевания
        def wearing(self, cloth):
            if cloth.type == 'clothing':
                tempSex = self.getSex()
                if tempSex == 'futa':
                    tempSex = 'female'
                if cloth.corr > self.getCorr() or cloth.sex != tempSex:
                    return False
                for x in cloth.cover:
                    for y in self.wear:
                        for z in y.cover:
                            if x == z:
                                self.wear.remove(y)
                                self.inventory.append(y)
                                break
                if rand(1,100) > 90:
                    cloth.durability -= 1
                self.inventory.remove(cloth)
                self.wear.append(cloth)
                self.checkDur()
            else:
                return False
        
        # Функция одевания по назначению. НЕ ДЛЯ ИГРОКА!
        def wearingByPurpose(self, purpose):
            nameInventory = []
            if purpose == 'naked':
                self.undress()
                return True
            for x in self.inventory:
                nameInventory.append(x.name)
            for name in nameInventory:
                currItem = self.getItem(name)
                if currItem.type == 'clothing':
                    if currItem.purpose == purpose:
                        self.wearing(currItem)
                        if 'попа' in currItem.cover and self.getCorr() > 50 and rand(1,3) == 1:
                            self.dewearing(currItem)
            
            
        # Функция частичного раздевания
        def dewearing(self,cloth):
            if self.wear.count(cloth) > 0:
                self.wear.remove(cloth)
                self.inventory.append(cloth)
            else:
                return False

        # Функция полного раздевания
        def undress(self):
            self.inventory.extend(self.wear)
            self.wear = []

        # Возвращение всех прикрытых частей
        def getCover(self):
            temp = []
            for x in self.wear:
                temp.extend(x.cover)
            return temp
            
        def getOutfitLust(self):
            if len(self.wear) == 0:
                return self.getBeauty()
            else:
                temp = 0
                for cloth in self.wear:
                    temp += cloth.lust
                return temp

                
                
        # Проверка на прикрытость
        def isCover(self, *args):
            temp = self.getCover()
            counter = 0
            for iscovered in args:
                for covered in temp:
                    if covered == iscovered:
                        counter += 1
                        break
            if counter == len(args):
                return True
            else :
                return False

        # Проверка на определённый тип одежды. Провреяется только верхняя одежда! Купальники тоже верхняя одежда!
        def getClothPurpose(self, purpose):
            covered = 0
            for x in self.wear:
                if x.purpose == purpose and ('верх' in x.cover or 'низ' in x.cover):
                    if 'верх' in x.cover and 'низ' in x.cover:
                        covered += 2
                    else:
                        covered += 1
            if covered == 2:
                return True
            else:
                return False

        def moveToLocation(self, loc, *args):
            """Перемещает персонажа в заданную локацию

            loc - объект класса Location, имя локации или None.
                  Если задан None - персонаж убирается с локации (на ночь)
            """

            if loc is None:
                self.location = None
                return
                
            if isinstance(loc, basestring):
                loc = getLoc(loc)

            else:
                if not isinstance(loc, Location):
                    raise Exception('Argument for the moveToLocation method '
                                    'should be location name or location object')

            self.location = loc

            # Filter statuses that fit to our stats
            if len(args) == 0:
                statuses = [x for x in loc.getStatuses() if x.checkApplicable(self)]
                if statuses:
                    applyStatus = choice(statuses)
                    
                    if applyStatus.name in ['Целуется']: # В случае поцелуев спавним партнёров вместе и заставляем целоваться.
                        if self.partner == None:
                            self.partner = getPartner(self)
                        
                        if self.partner == None:  # Если партнёров больше нет, тогда всё.
                            self.moveToLocation(loc,'noStatus')
                        self.applyLocationStatus(applyStatus)
                        self.partner.location = self.location
                        self.partner.forceLocationStatus(applyStatus)
                    else:
                        self.applyLocationStatus(applyStatus)
                else:
                    self.applyLocationStatus(None)

        def applyLocationStatus(self, status, force=False):
            """Применяет LocationStatus на персонажа"""
            if status is None:
                self.locationStatus = None

            else:
                self.locationStatus = status
                if not force:
                    if not status.checkApplicable(self):
                        raise Exception('Status {} could not be applied to character {}'
                                        .format(status, self))

                for stat, (mod, max_val) in status.stats_actions.items():
                    char_stat = getattr(self.stats, stat)
                    
                    # Stat will be limited by max_val, if modificator is #
                    # negative - status will not go lower than max_val
                    if mod > 0:
                        char_stat = min(max_val, char_stat+mod)

                    else:
                        char_stat = max(max_val, char_stat+mod)

                    setattr(self.stats, stat, char_stat)
        
        def forceLocationStatus(self, status):
            """Форсирует LocationStatus на персонажа"""
            self.applyLocationStatus(status, force=True)

        def getLocationStatus(self):
            return self.locationStatus

        def getLocation(self):
            return self.location

        def takeGift(self, gift):
            if gift.sex != 'any' and self.getSex('mf') != gift.sex:
                raise Exception('Wrong sex of the {} gift was present to {}'
                                .format(gift, self))
                                
            self.inventory.append(gift)
            self.incCorr(gift.corr)
            self.incLoy(gift.loy)
            self.incRep(gift.reputation)

        def __repr__(self):
            return ('<{} name: "{}", sex: "{}">'
                    .format(self.__class__.__name__,
                            self.name.encode('utf-8'),
                            self.sex))

# End class Char definition
    def getCharByName(name):
        global allChars
        for x in allChars:
            if x.fullName() == name:
                return x
        return False
        
    def getPartner(char):
        for x in studs: # Сначала пробуем гетеросексуальные отношения
            if x.partner == None and x.getSex() != char.getSex():
                x.partner = char
                return x
        for x in studs: # Потом гомосексуальные
            if x.partner == None and x != char:
                x.partner = char
                return x
        return None
