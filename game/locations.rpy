init 10 python:
    locations = []
    class Location:
        def __init__(self, id, name, base_prob, position):
            self.id = id
            self.name = name
            self.base_prob = base_prob
            self.events = []
            self.qwests = []
            self.position = position
            self.items = []
            self.__statuses = []

        def getprob(self):
            global hour
            if lt() > 0 or lt() == -4: rez = -1 #Если ночь, то на улице никого нет
            
            elif 'school' in self.position and lt() == -1: rez = self.base_prob/4 #Если внеурочное время, то в школе шансов встретить меньше
            elif 'school' in self.position and lt() == 0: rez = self.base_prob*2 #Если перемена, то в школе шансов встретить гораздо больше
            elif 'other' in self.position and lt() == 0: rez = -1 # во время перемен никого не будет в городе
            elif self.id in ['loc_street','loc_shopStreet'] and hour < 8: rez = self.base_prob*2 # перед уроками на улице чаще
            elif self.id in ['loc_beach'] and hour < 8: rez = self.base_prob/2 # перед уроками на пляже реже
            else : 
                rez = self.base_prob #Иначе настоящая вероятность.
                
            return rez

        def __repr__(self):
            return '<{} name: "{}">'.format(self.__class__.__name__,
                                            self.name.encode('utf-8'))

        def getPeople(self):
            rez = []
            for x in allChars:
                try:
                    if x.getLocation().id==self.id:
                        rez.append(x)
                except AttributeError:
                    pass
            return rez
            
        def getItems(self):
            rez = []
            for x in self.items:
                rez.append(x)
            return rez

        def addStatus(self, status, prob=None):
            """Добавляет статус к локации
            
            status - LocationStatus объект
            prob - вероятность выбора статуса (от 0 до 100).
                   Можно оставить None - тогда вероятность будет вычислена 
                   автоматически, справедливо по отношению к остальным. Общая
                   сумма вероятностей для статусов не должна быть больше 100!
            """
            if not isinstance(status, LocationStatus):
                raise Exception('Status should be LocationStatus object')

            if prob is not None:
                int(prob)
                if not 0 < prob < 100:
                    raise Exception('Probability should be between 0 and 100: {}'
                                    .format(prob))

            # Statuses with automatic probabilities will have special flag
            if status not in self.__statuses:
                self.__statuses.append((status, prob, prob is None))
                self.__recalc_statuses_prob()

        def __recalc_statuses_prob(self):
            """Пересчитывает вероятности статусов"""

            auto_prob_statuses = [x for x in self.__statuses if x[2]]
            given_prob = sum([x[1] for x in self.__statuses if not x[2]])

            # Avoid division by zero and ensure that prob>=1
            auto_prob = max(abs(100-given_prob)/max(1, len(auto_prob_statuses)),
                            1)

            for idx, (status, prob, auto_f) in enumerate(self.__statuses):
                if not auto_f:
                    continue

                self.__statuses[idx] = (status, auto_prob, auto_f)
                
            # Make sure that whe have no >100 prob
            if sum([x[1] for x in self.__statuses]) > 100:
                raise Exception('Sum of LocationStatus probabilities should '
                                'be less than 100: {}'.format(self.__statuses))

        def addStatuses(self, statuses):
            """Добавляет список статусов к локации
            statuses - список статусов, если нужно задать вероятности - то
                       список tuple'ов (status, prob)
            """

            for x in statuses:
                try:
                    self.addStatus(x[0], x[1])

                except TypeError:
                    self.addStatus(x)

        def getStatuses(self):
            """Возвращает список статусов, с учетом их вероятностей.
            Т.е. более вероятные статусы в этом списке будут дублироваться"""

            if not self.__statuses:
                return []

            min_prob = float(min([x[1] for x in self.__statuses]))
            rez = []
            for status, prob, _ in self.__statuses:
                for _ in xrange(int(round(prob/min_prob))):
                    rez.append(status)

            return rez
            
        def eraseStatuses(self):
            # сносит все статусы с локации
            self.__statuses[:] = []
        
        def removeStatus(self, status):
            for x in self.__statuses:
                if x == status:
                    self.__statuses.remove(x)
            
    class Event:
        def __init__(self,id,corr):
            self.id = id
            self.corr = corr
            
    class Qwest:
        def __init__(self,id):
            self.id = id
            self.done = False

    # Location statuses
    class LocationStatus(object):
        def __init__(self, name, pic, sex='any', char_type='any', events=None,
                     requirements=None, stats_actions=None):
            """Создает новый статус для локации.

            name - имя для статуса
            pic - изображение для отображения статуса
            sex - пол для статуса, либо строка: male, female, futa, any,
                  либо список с комбинацией этих значений
            char_type - тип персонажа: any, student, teacher
            events - список меток ивентов, либо None - если статус не
                     порождает ивентов
            requirements - dict необходимых параметров
                           (key - corr, fun, ...;
                            value - минимально-необходимое значение параметра),
                           либо None если статус не имеет никаких требований
            stats_actions - как статус повлияет на взявшего его персонажа.
                            Задается как dict, где key - corr, fun, ...;
                            value - задает на сколько изменится параметр,
                            но финально параметр не вырастит больше
                            N(заиграться до 100 fun не получится).
                            Пример: stats_actions={'fun': (1, 20)} - fun
                            увеличится на 1, но в итоге будет не больше 20
            """
            self.name = name
            self.pic = pic

            # Sex
            if isinstance(sex, basestring):
                self.sex = [sex]
            elif hasattr(sex, '__iter__'):
                self.sex = sex
            else:
                raise Exception('Sex should be submitted as string ot list of strings')
            for s in self.sex:
                if s not in ['male', 'female', 'futa', 'any']:
                    raise Exception('Unknown sex submitted: {}'.format(s))

            # char_type
            if char_type.lower() not in frozenset(['any', 'teacher',
                                                   'student']):
                raise Exception('char_type shoulb be any, teacher or student: {}'
                                 .format(char_type))
            self.char_type = char_type

            # Events
            if events is None:
                events = []

            # Check that something iterable was submitted, but not string.
            # We need something like list
            if not hasattr(events, '__iter__') or isinstance(events, basestring):
                raise Exception('events arguments shoud be submitted as list')
            self.events = events

            # Requirements
            self.requirements = {key: (val if val is not None else 0)\
                                 for key, val in self.__check_stats(requirements)
                                                     .items()}

            # Stats actions
            self.stats_actions = {key: (val if val is not None else (0, 100))\
                                  for key, val in self.__check_stats(stats_actions)
                                                      .items()}

            # Check for tuples
            for a in self.stats_actions.values():
                if not hasattr(a, '__len__') or len(a) != 2:
                    raise Exception('Stats actions should be tuples length 2')

        def __check_stats(self, in_stats):
            if in_stats and (not hasattr(in_stats, 'items')\
                             or not hasattr(in_stats, 'keys')):
                    raise Exception('requirements should be submitted as dict')

            if in_stats is None:
                in_stats = {}

            rez = {}
            stats = ['loyalty', 'fun', 'corr', 'lust', 'will',
                     'education', 'health', 'intelligence', 'beauty',
                     'reputation', 'energy', 'dirty']
            for stat, val in in_stats.items():
                rez[stat] = val

            # Check that there is no typo stats
            if set(in_stats.keys()) - set(stats):
                raise Exception('Extra stats was submitted in requirements: {}'
                                .format(', '.join(set(in_stats.keys())
                                                  -set(stats))))

            return rez

        def checkApplicable(self, char):
            """Проверяет, что статус применим к данному персонажу"""

            if not isinstance(char, Char):
                raise Exception('Submitted char should be Char object')

            if 'any' not in self.sex and char.getSex() not in self.sex:
                return False

            if self.char_type != 'any':
                if self.char_type == 'teacher' and char not in teachers:
                    return False

                elif self.char_type == 'student' and char not in studs:
                    return False

            for key, val in self.requirements.items():
                if getattr(char.stats, key) < val:
                    return False

            return True

        def __repr__(self):
            return '<{} name: "{}">'.format(self.__class__.__name__,
                                            self.name.encode('utf-8'))


    def getLoc(id):
        for x in locations:
            if x.id == id:
                return x
        return False
        
    def getQwest(id):
        for loc in locations:
            for qwest in loc.qwests:
                if qwest.id == id:
                    return qwest
        return False

#Функция добавления эвентов в локации
    def getEvents():
        for eventLabel in _locs: # перебираем все лейблы
            if eventLabel[:6] == 'event_': #находим тот, что с евентом
                for location in locations: #начинаем перебирать локации
                    if eventLabel.find(location.id) > 0: #Если имя локации содержится в имени эвента
                        index = eventLabel.rfind(location.id) #находим правый индекс имени локации
                        corr = eventLabel[index:] #режем по нему
                        temp = corr.split("_") #разбиваем строку по_
                        corr = int(temp[2]) #находим развратность
                        event = Event(id = eventLabel, corr = corr) # создаём эвент
                        location.events.append(event) #добавляем его в массив эвентов локации
        return 0
        
    def getQwests():
        for eventLabel in _locs: # перебираем все лейблы
            if eventLabel[:6] == 'qwest_': #находим тот, что с квестом
                for location in locations: #начинаем перебирать локации
                    if eventLabel.find(location.id) > 0: #Если имя локации содержится в имени эвента
                        qwest = Qwest(id = eventLabel) # создаём эвент
                        qwests = []
                        for q in location.qwests:
                            qwests.append(q.id)
                        if qwest.id not in qwests:
                            location.qwests.append(qwest) #добавляем его в массив эвентов локации
        return 0

#Создание массива всех локаций
    _locs = renpy.get_all_labels()
    for x in _locs:
        if x[:4] == 'loc_':
            if x == 'loc_home': loc = Location(id = x, name = 'дом', base_prob = -1, position = ['home','safe'])
            elif x == 'loc_bedroom': loc = Location(id = x, name = 'спальня', base_prob = -1, position = ['home','safe'])
            elif x == 'loc_bathroom': loc = Location(id = x, name = 'ванная', base_prob = -1, position = ['home','safe'])
            elif x == 'loc_kitchen': loc = Location(id = x, name = 'кухня', base_prob = -1, position = ['home','safe'])

            elif x == 'loc_street': loc = Location(id = x, name = 'улица', base_prob = 20, position = ['other'])
            elif x == 'loc_beach': loc = Location(id = x, name = 'пляж', base_prob = 30, position = ['other','swim'])
            elif x == 'loc_beachChange': loc = Location(id = x, name = 'раздевалка', base_prob = -1, position = ['safe','other','change'])
            elif x == 'loc_shopStreet': loc = Location(id = x, name = 'торговая улица', base_prob = 20, position = ['other'])
            elif x == 'loc_shop': loc = Location(id = x, name = 'магазин', base_prob = 10, position = ['other'])
            elif x == 'loc_shopBeauty': loc = Location(id = x, name = 'салон красоты', base_prob = 10, position = ['other'])
            elif x == 'loc_sexShop': loc = Location(id = x, name = 'сексшоп', base_prob = 5, position = ['other'])

            elif x == 'loc_hall': loc = Location(id = x, name = 'холл', base_prob = 15, position = ['school'])
            elif x == 'loc_dungeon': loc = Location(id = x, name = 'подвал', base_prob = -1, position = ['school'])
            elif x == 'loc_entrance': loc = Location(id = x, name = 'вход', base_prob = 20, position = ['school'])
            elif x == 'loc_library': loc = Location(id = x, name = 'библиотека', base_prob = 10, position = ['school'])
            elif x == 'loc_changeRoom': loc = Location(id = x, name = 'школьная раздевалка', base_prob = 5, position = ['school','safe','change'])
            elif x == 'loc_gym': loc = Location(id = x, name = 'спортивный зал', base_prob = 20, position = ['school','classroom','sport'])
            elif x == 'loc_pool': loc = Location(id = x, name = 'бассейн', base_prob = 20, position = ['school','classroom','swim'])
            elif x == 'loc_firstFloor': loc = Location(id = x, name = 'первый этаж', base_prob = 20, position = ['school'])
            elif x == 'loc_secondFloor': loc = Location(id = x, name = 'второй этаж', base_prob = 20, position = ['school'])
            elif x == 'loc_class1': loc = Location(id = x, name = 'Класс 1', base_prob = 5, position = ['school','classroom'])
            elif x == 'loc_class2': loc = Location(id = x, name = 'Класс 2', base_prob = 5, position = ['school','classroom'])
            elif x == 'loc_class3': loc = Location(id = x, name = 'Класс 3', base_prob = 5, position = ['school','classroom'])
            elif x == 'loc_class4': loc = Location(id = x, name = 'Класс 4', base_prob = 5, position = ['school','classroom'])
            elif x == 'loc_class5': loc = Location(id = x, name = 'Класс 5', base_prob = 5, position = ['school','classroom'])
            elif x == 'loc_teacherRoom': loc = Location(id = x, name = 'учительская', base_prob = 0, position = ['school'])
            elif x == 'loc_wcm': loc = Location(id = x, name = 'Туалет для мальчиков', base_prob = 5, position = ['school'])
            elif x == 'loc_wcf': loc = Location(id = x, name = 'Туалет для девочек', base_prob = 5, position = ['school'])
            elif x == 'loc_storage': loc = Location(id = x, name = 'кладовка', base_prob = 5, position = ['school'])
            elif x == 'loc_chemlab': loc = Location(id = x, name = 'Лаборатория', base_prob = -1, position = ['school'])
            elif x == 'loc_doctor': loc = Location(id = x, name = 'Медицинский кабинет', base_prob = 2, position = ['school'])
            elif x == 'loc_office': loc = Location(id = x, name = 'офис', base_prob = 0, position = ['safe','school'])

            elif x == 'loc_dreams': loc = Location(id = x, name = 'Сны', base_prob = -1, position = ['self'])
            elif x == 'loc_swim': loc = Location(id = x, name = 'Плавание', base_prob = -1, position = ['self'])
            elif x == 'loc_run': loc = Location(id = x, name = 'Бег', base_prob = -1, position = ['self'])
            elif x == 'loc_taxi': loc = Location(id = x, name = 'Такси', base_prob = -1, position = ['self'])
            elif x == 'loc_gloryHole': loc = Location(id = x, name = 'Глорихол', base_prob = 0, position = ['self'])

            elif x == 'loc_class1Learn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
            elif x == 'loc_class2Learn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
            elif x == 'loc_class3Learn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
            elif x == 'loc_class4Learn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
            elif x == 'loc_class5Learn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
            elif x == 'loc_gymLearn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
            elif x == 'loc_poolLearn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
            elif x == 'loc_cabbage': loc = Location(id = x, name = 'Капуста', base_prob = -1, position = ['tech'])
            else: loc = Location(id = x, name = 'UNKNOWN', base_prob = -1, position = ['other'])
            locations.append(loc)

            # For tests
            #test_loc_status = LocationStatus('TEST', None, 'any', events=['cleanAss'])
            #loc.addStatus(test_loc_status, 50)

    getEvents() #добавляю всем эвенты
    getQwests() #добавляю квесты
######################################################
#Объявление всех картинок
init:
    image home = ConditionSwitch(
        "hour >= 5 and hour <= 20", 'pic/locations/home/2.png',
        "hour > 20 or hour < 5", 'pic/locations/home/1.png',
        )
    image bedroom = ConditionSwitch(
        "hour >= 5 and hour <= 20", 'pic/locations/home/3.png',
        "hour > 20 or hour < 5", 'pic/locations/home/4.png',
        )
    image bathroom = im.Scale('pic/locations/home/3.jpg', config.screen_width, config.screen_height)
    image kitchen = im.Scale('pic/locations/home/4.jpg', config.screen_width, config.screen_height)
    image street = ConditionSwitch(
        "hour >= 5 and hour < 9", im.Scale("pic/locations/street/bg19.png",config.screen_width, config.screen_height),
        "hour >= 9 and hour < 17", im.Scale("pic/locations/street/bg18.png",config.screen_width, config.screen_height),
        "hour >= 17 and hour < 22", im.Scale("pic/locations/street/bg19.png",config.screen_width, config.screen_height),
        "hour >= 22 or hour < 5", im.Scale("pic/locations/street/bg20.png",config.screen_width, config.screen_height),
        )
    image beach = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/beach/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/beach/2.jpg",config.screen_width, config.screen_height),
        )
    image beachChange = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/beach/changeRoom/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/beach/changeRoom/2.jpg",config.screen_width, config.screen_height),
        )
    image shopStreet = ConditionSwitch(
        "hour >= 5 and hour < 9", im.Scale("pic/locations/shopStreet/bg22.png",config.screen_width, config.screen_height),
        "hour >= 9 and hour < 17", im.Scale("pic/locations/shopStreet/bg40.png",config.screen_width, config.screen_height),
        "hour >= 17 and hour < 22", im.Scale("pic/locations/shopStreet/bg22.png",config.screen_width, config.screen_height),
        "hour >= 22 or hour < 5", im.Scale("pic/locations/shopStreet/bg23.png",config.screen_width, config.screen_height),
        )
    image shop = im.Scale('pic/locations/shop/1.jpg', config.screen_width, config.screen_height)
    image shopBeauty = im.Scale('pic/locations/shopBeauty/1.jpg', config.screen_width, config.screen_height)
    image sexShop = im.Scale('pic/locations/sexShop/1.jpg', config.screen_width, config.screen_height)
    image hall = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/school/hall/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/hall/2.jpg",config.screen_width, config.screen_height),
        )
    image entrance = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/school/entrance/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/entrance/2.jpg",config.screen_width, config.screen_height),
        )
    image library = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/school/library/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/library/2.jpg",config.screen_width, config.screen_height),
        )
    image pool = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/school/pool/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/pool/2.jpg",config.screen_width, config.screen_height),
        )
    image gym = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/school/gym/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/gym/2.jpg",config.screen_width, config.screen_height),
        )
    image changeRoom = im.Scale('pic/locations/school/changeRoom/1.png', config.screen_width, config.screen_height)
    image storage = im.Scale('pic/locations/school/storage/1.jpg', config.screen_width, config.screen_height)
    image firstFloor = ConditionSwitch(
        "hour >= 5 and hour < 9", im.Scale("pic/locations/school/firstFloor/1.jpg",config.screen_width, config.screen_height),
        "hour >= 9 and hour <= 20", im.Scale("pic/locations/school/firstFloor/2.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/firstFloor/3.jpg",config.screen_width, config.screen_height),
        )
    image office = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/school/office/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/office/2.jpg",config.screen_width, config.screen_height),
        )
    image class1 = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/school/class1/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/class1/2.jpg",config.screen_width, config.screen_height),
        )
    image class2 = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/school/class2/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/class2/2.jpg",config.screen_width, config.screen_height),
        )
    image class3 = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/school/class3/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/class3/2.jpg",config.screen_width, config.screen_height),
        )
    image class4 = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/school/class4/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/class4/2.jpg",config.screen_width, config.screen_height),
        )
    image class5 = ConditionSwitch(
        "hour >= 5 and hour <= 20", im.Scale("pic/locations/school/class5/1.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/class5/2.jpg",config.screen_width, config.screen_height),
        )
    image secondFloor = ConditionSwitch(
        "hour >= 5 and hour < 9", im.Scale("pic/locations/school/secondFloor/1.jpg",config.screen_width, config.screen_height),
        "hour >= 9 and hour <= 20", im.Scale("pic/locations/school/secondFloor/2.jpg",config.screen_width, config.screen_height),
        "hour > 20 or hour < 5", im.Scale("pic/locations/school/secondFloor/3.jpg",config.screen_width, config.screen_height),
        )
    image teacherRoom = ConditionSwitch(
        "hour >= 5 and hour <= 20", "pic/locations/school/teacherRoom/bg51.png",
        "hour > 20 or hour < 5", "pic/locations/school/teacherRoom/bg52.png",
        )
    image wcm =  im.Scale('pic/locations/school/secondFloor/wcm.jpg', config.screen_width, config.screen_height)
    image wcf =  im.Scale('pic/locations/school/secondFloor/wcf.jpg', config.screen_width, config.screen_height)
    image chemlab = 'pic/locations/school/chemlab.png'
    image dungeon = 'pic/locations/school/dungeon.jpg'
    image doctor = ConditionSwitch(
        "hour >= 5 and hour <= 20", 'pic/locations/school/doctor/1.png',
        "hour > 20 or hour < 5", 'pic/locations/school/doctor/2.png',
        )
    image movie = Movie(size=(1200, 768), xpos=0.5, ypos=0, xanchor=0.5, yanchor=0)
    
    python:
        intro_img = ['pic/locations/school/secondFloor/1.jpg','pic/locations/school/secondFloor/2.jpg','pic/locations/school/secondFloor/3.jpg']
        counter = 0
        for x in intro_img:
            counter += 1
            x = renpy.image(str(counter), x)
        
#Для теста
label test:
    show daytime
    # show movie
    # play movie "pic/locations/school/class1/lo7.ogv" loop
    # 'тест'
    # stop movie
    # hide movie
    #jump myintro
    
    # $changetime(60*24)
    # $move('loc_home')
    
    # python:
        # callup = studs[0]
        # callup.incCorr(30)
        # player.incCorr(60)
    # jump reputation
    
    # $ mystring = reactionGen(studs[0])
    # player.say '[mystring]'
    # python:
        # player.coverSperm('лицо')
        # player.incDirty(5)
        # move('loc_home')
        # for x in studs:
            # if x.getSex() != 'male':
                # x.club = 'pants'
        # renpy.jump('getPanties')
    # $ t = mustangovich
    # show expression getCharImage(t,'dialog') as tempPic
        # myString = ''
        # tempList = [tempList for tempList in range(1,20)]
        # for x in tempList:
            # myString += str(x) + ', '
        # temp = getQwest('qwest_loc_shop_cameraQwest').done
    # '[temp]'
    # screen test_screen:
        # vbox:
            # textbutton 'Эвент 1':
                # action Jump('event_loc_class1_10_StartKupruvnaQuest')
            # textbutton 'Эвент 2':
                # action Jump('kupruvnaGotIt1')
            # textbutton 'Эвент 3':
                # action Jump('kupruvnaGotIt2')
            # textbutton 'Эвент 4':
                # action Jump('event_loc_cabbage_0_sexWithSon')
            # textbutton 'Эвент 5':
                # action Jump('kupruvnaGotIt3')
    # call screen test_screen
    # $changetime(60*24)
    # $player.setHealth(10000)
    # $player.setEnergy(10000)
    show expression 'pic/status/male_toy.jpg' at Move((0.0, 0.0), (0.0, -1.1), 10.0, repeat = True, bounce = True, xanchor="left", yanchor="top") as tempPic
    ''
    $move(curloc)

##############################################################
# Home
##############################################################
label loc_home:
    if ptime == 0:
        $ ptime += 1
        $ move ('intro')
    show home

    screen home:
        fixed:
            text 'Гостинная в вашей квартире. Маленькая, зато аккуратная. На стеклянном столе лежит пачка салфеток для ежедневного ухода за кожей. Напротив диванчика стоит телевизор. Вы не помните, чтобы по нему хоть раз показывали что-то хорошее. Возможно потому, что потеряли пульт сразу после переезда.' xalign 0.0 yalign 1.0 style style.description
            textbutton 'Кухня':
                xalign 0.05 yalign 0.8 
                action Function(move, 'loc_kitchen') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Спальня':
                xalign 0.5 yalign 0.8 
                action Function(move, 'loc_bedroom')  
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Ванная': 
                xalign 0.9 yalign 0.8 
                action Function(move, 'loc_bathroom') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Улица': 
                xalign 0.5 yalign 0.5 
                action Function(move, 'loc_street') 
                style "navigation_button" text_style "navigation_button_text"
            if development == 1:
                textbutton 'Test':
                    xalign 0.0 yalign 0.2 
                    action Function(move,'test')
    call screen home

label loc_bedroom:
    $ endurance = player.getCorr()+player.getFun()
    show bedroom at left
    screen bedroom:
        fixed:
            text 'Уютненькая маленькая спальня. Слева находится небольшой шкаф, в котором висит ваша повседневная одежда. Справа кровать, довольно удобная. Тут ещё есть телевизор, но он не работает, так что совсем не будет мешать Вам отходить ко сну.' xalign 0.0 yalign 1.0 style style.description
            textbutton 'Гостинная':
                xalign 0.5 yalign 0.8 
                action Function(move, 'loc_home') 
                style "navigation_button" text_style "navigation_button_text"
            if (ptime - last_sleeped >= 4) or (player.stats.energy < player.stats.health/4):
                textbutton 'Спать' xalign 0.2 yalign 0.76 action Jump('sleep')
            if player.getLust() > 0:
                textbutton 'Маструбировать' xalign 0.156 yalign 0.8 action Jump('startMastur')
            textbutton 'Шкафчик\nс вещами' xalign 0.9 yalign 0.8 action Show('wardrobe')
    call screen bedroom


label loc_kitchen:
    show kitchen at left
    screen kitchen:
        fixed:
            if player.hasItem('Сырая еда'):
                $ temp = player.getItem('Сырая еда').durability
                text 'Микроволновка, плита, раковина, шкафчики. Кухня одним словом. \nОценив количество оставшейся еды, вы прикидываете, что её хватит ещё на [temp] раз.' xalign 0.0 yalign 1.0 style style.description
                if ptime - last_eat > 4:
                    textbutton 'Поесть' xalign 0.4 yalign 0.6 action [
                    Function(player.eat, player.getItem('Сырая еда')),
                    Function(changetime, 15),
                    Function(move, curloc)] 
            else :
                text 'Микроволновка, плита, раковина, шкафчики. Кухня одним словом. \nОценив количество оставшейся еды, вы понимаете, что её не осталось СОВСЕМ. Надо срочно сгонять в магазин.' xalign 0.0 yalign 1.0 style style.description
            textbutton 'Гостинная':
                xalign 0.5 yalign 0.8 
                action Function(move, 'loc_home') 
                style "navigation_button" text_style "navigation_button_text"
            if player.hasItem('Сэндвич') == False and player.hasItem('Сырая еда') == True:
                textbutton 'Сделать\nсэндвич' xalign 0.8 yalign 0.65 action [
                Function(player.addItems, 'Сэндвич'),
                Function(player.apply, 'Сырая еда'),
                Function(changetime, 15),
                Jump(curloc)]
    call screen kitchen


label loc_bathroom:
    show bathroom at left
    screen bathroom:
        fixed:
            text 'Ванная комната. Совмещённая. В лучших традициях далёкой страны. Тут можно искупаться, чтобы смыть с себя грязь и прочие человеческие нечистоты. А можно просто постоять под душем и отдохнуть.' xalign 0.0 yalign 1.0 style style.description
            textbutton 'Гостинная':
                xalign 0.5 yalign 0.8 
                action Function(move, 'loc_home') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Душ' xalign 0.4 yalign 0.3 action Jump('shower') # style "navigation_button" text_style "navigation_button_text"

    call screen bathroom



##############################################################
# SCHOOL
##############################################################
label loc_entrance:
    show entrance at left
    screen entrance:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Вход в Вашу новую школу. Ворота, крыльцо, всё как у всех, ничего необычного. Разве что кусты не особо пострижены, и дети там периодически играют, ну да ладно.' style style.description
                if 'library' not in school.buildings:
                    text 'Слева от школы полно места. Вроде как там раньше стоял сарай, но он давным давно рухнул, и теперь земля пустует. Библиотеку чтоли там построить? ' style style.description
                else:
                    text 'Справа от школы виден вход в школьную библиотеку. В самом деле, замечательное приобретение! ' style style.description
                if 'wall' not in school.buildings:
                    text 'Окидывая взглядом свои владения, вы видите прекрасный вид на окна школы. Выглядит конечно красиво, но как то всё напоказ. ' style style.description
                else:
                    text 'Довольно высокая стена окружает школу. С улицы вообще непонятно, толи это школа, толи режимный объект. ' style style.description
                if is_cabbage == 1 and hour == 7 and weekday < 6:
                    text 'Сегодня день уборки урожая! Автобус ожидает вас и ваших учеников.' style style.description
            textbutton 'Холл':
                xalign 0.456 yalign 0.73 
                action [Function(move, 'loc_hall')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Первый этаж':
                xalign 0.456 yalign 0.6 
                action [Function(move, 'loc_firstFloor')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Второй этаж':
                xalign 0.456 yalign 0.44 
                action [Function(move, 'loc_secondFloor')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Ваш офис': 
                xalign 0.6 yalign 0.6 
                action [Function(move, 'loc_office')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Домой': 
                xalign 0.1 yalign 0.7 
                action [Function(changetime, 30),Function(move, 'loc_street')] 
                style "navigation_button" text_style "navigation_button_text"
            if 'library' in school.buildings:
                textbutton 'Библиотека':
                    xalign 0.8 yalign 0.7 
                    action [Function(move, 'loc_library')] 
                    style "navigation_button" text_style "navigation_button_text"
            if is_cabbage == 1 and hour == 7 and weekday < 6:
                imagebutton:
                    idle im.MatrixColor('pic/events/cabbage/bus.png', im.matrix.opacity(0.5)) 
                    hover im.MatrixColor('pic/events/cabbage/bus.png', im.matrix.opacity(1.0))
                    xalign 4.8 yalign 1.2
                    action [Jump('cabbageStart')]
    call screen entrance

label loc_library:
    show library at left
    screen library:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Недавно построенная школьная библиотека. Всё  сделано на удивление быстро и качественно. Городская библиотека выделила много книг на её заполнение, которые всё равно готовились списать.' style style.description
                text 'В любом случае тут - прекрасное место для самообразования и не только!' style style.description
            textbutton 'Выход':
                xalign 0.5 yalign 0.8
                action [Function(move, 'loc_entrance')] 
                style "navigation_button" text_style "navigation_button_text"
    call screen library


label loc_hall:
    show hall at left
    screen hall:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'По всему холлу расставлены шкафчики для личных вещей. И еще лавочки, сидя на которых удобно переобуваться. В образующих шкафчиками коридорах легко потеряться с непривычки. По школе ходят ужасные истории, что из первого выпуска школы, ещё никто не вернулся домой. Так и бродят они до сих пор по коридорам, и воруют у новых учеников обувь, чтобы починить свои стоптанные за года блужданий ботинки. Глупая история, считаете Вы.' style style.description
            textbutton 'Первый этаж':
                xalign 0.1 yalign 0.7 
                action [Function(move, 'loc_firstFloor')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Бассейн': 
                xalign 0.8 yalign 0.7 
                action [Function(move, 'loc_pool')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Спортзал': 
                xalign 0.8 yalign 0.6 
                action [Function(move, 'loc_gym')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Выход': 
                xalign 0.5 yalign 0.5 
                action [Function(move, 'loc_entrance')] 
                style "navigation_button" text_style "navigation_button_text"
            if getPar(studs,'corr') >= 20 and lt() == 0 and hour < 9 and mile_quest_1 == 0 or development == 1:
                imagebutton:
                    idle im.MatrixColor('pic/events/mile_1/start.png', im.matrix.opacity(0.5))
                    hover im.MatrixColor('pic/events/mile_1/start.png', im.matrix.opacity(1.0)) 
                    action [Jump('mileQwest1')] xalign 1.0 yalign 0.8
            if 'dungeon' in school.buildings or development == 1:
                textbutton 'Подвал':
                    xalign 0.5 yalign 0.8
                    action [Function(move, 'loc_dungeon')] 
                    style "navigation_button" text_style "navigation_button_text"
    call screen hall

label loc_dungeon:
    show dungeon at top
    screen dungeon:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Тёмный, мрачный подвал, больше напоминающий подземелье из какой то игры про рабынь, чем обычное подвальное помещение средней школы.' style style.description
            textbutton 'Выход':
                xalign 0.5 yalign 0.8
                action [Function(move, 'loc_hall')] 
                style "navigation_button" text_style "navigation_button_text"
    call screen dungeon
    
label loc_pool:
    show pool at left
    screen pool:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Бассейн. Здесь проходят занятия по вторникам и четвергам. Хотя так же в перемены, и после уроков ученики могут придти сюда, чтобы поплавать или просто постоять глядя на воду. Вы так же можете немного потренировать своё здоровье, попытавшись проплыть стометровку пару раз.' style style.description
                text 'Неподалеку от бассейна находится душ, где Вы в любой момент можете освежиться.' style style.description
            textbutton 'Раздевалка':
                xalign 0.2 yalign 0.2 
                action [Function(move, 'loc_changeRoom')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'В душ':
                xalign 0.05 yalign 0.7 
                action Jump('shower') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Холл': 
                xalign 0.5 yalign 0.8 
                action [Function(move, 'loc_hall')] 
                style "navigation_button" text_style "navigation_button_text"
    call screen pool


label loc_changeRoom:
    show changeRoom at left
    screen changeRoom:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Раздевалка. Она разделена на 2 отделения для мальчиков и девочек. Как ни странно, вы тоже можете тут переодеваться. В отделении для девочек разумеется. Хотя кто знает, что там в соседнем отделении? Вы точно не знаете.' style style.description
            textbutton 'Бассейн':
                xalign 0.2 yalign 0.8 
                action [Function(move, 'loc_pool')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Спортзал':
                xalign 0.8 yalign 0.8 
                action [Function(move, 'loc_gym')] 
                style "navigation_button" text_style "navigation_button_text"
    call screen changeRoom


label loc_gym:
    show gym at left
    screen gym:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Раздевалка. Она разделена на 2 отделения для мальчиков и девочек. Как ни странно, вы тоже можете тут переодеваться. В отделении для девочек разумеется. Хотя кто знает, что там в соседнем отделении? Вы точно не знаете.' style style.description
            textbutton 'Кладовка': 
                xalign 0.35 yalign 0.4 
                action [Function(move, 'loc_storage')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Раздевалка': 
                xalign 0.8 yalign 0.8 
                action [Function(move, 'loc_changeRoom')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Холл': 
                xalign 0.5 yalign 0.8 
                action [Function(move, 'loc_hall')] 
                style "navigation_button" text_style "navigation_button_text"
    call screen gym

label loc_storage:
    show storage at left
    screen storage:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Кладовка спорт инвентаря. В ней находятся мячи, маты, козлы и прочий спортинвентарь. Многие ученики  ходят сюда, чтобы немного отдохнуть и уединиться ото всех.' style style.description
            textbutton 'Спортзал':
                xalign 0.5 yalign 0.8 
                action Function(move, 'loc_gym') 
                style "navigation_button" text_style "navigation_button_text"
    call screen storage

label loc_firstFloor:
    show firstFloor at left
    screen firstFloor:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Коридор первого этажа. Тут находится Ваш офис, а так же первые три классных кабинета: Кабинет химии, кабинет биологии и класс уроков Секспросвета. Вы видите лестницу на второй этаж и в холл.' style style.description
            textbutton 'Ваш офис':
                xalign 0.2 yalign 0.8 
                action Function(move, 'loc_office') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Класс 1':
                xalign 0.25 yalign 0.7 
                action Function(move, 'loc_class1') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Класс 2':
                xalign 0.3 yalign 0.6 
                action Function(move, 'loc_class2') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Класс 3':
                xalign 0.35 yalign 0.5 
                action Function(move, 'loc_class3') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Второй\nэтаж':
                xalign 0.4 yalign 0.4 
                action Function(move, 'loc_secondFloor') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Холл':
                xalign 0.6 yalign 0.8 
                action Function(move, 'loc_hall') 
                style "navigation_button" text_style "navigation_button_text"
    call screen firstFloor

label loc_office:
    show office at left
    # Часть квеста даноковой
    if hour >= 15 and hour < 17 and (weekday == 2 or weekday == 4) and mile_qwest_3_stage == 50:
        'Дверь в кабинет закрыта и из за неё слышны тихие стоны. Вы вздыхаете и уходите. В конце концов вы добились чего хотели. Наверное.'
        $ move (prevloc)
    if ptime >= work51 and ptime < work51 + 2 and mile_qwest_3_stage > 0:
        if callup == dummy:
            if temperature > 30:
                jump danokova_hot
            else:
                $ mile_qwest_3_hot = 0
                jump danokova_working
        else:
            jump danokova_office_action
            
    screen office:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Ваш офис. Большой дубовый стол, компьютер, сразу видно что Вы здесь уважаемы.' style style.description
                if lt() >= 0 and is_cabbage == 0 and mile_qwest_2_stage > 0:
                    text 'Вы видите молодого, хорошо одетого мужчину в вашем кабинете.'
            textbutton 'Первый этаж' xalign 0.8 yalign 0.8 action Function(move, 'loc_firstFloor') style "navigation_button" text_style "navigation_button_text"
            textbutton 'Воспользоваться\nокном' xalign 0.2 yalign 0.3 action Function(move, 'loc_entrance') style "navigation_button" text_style "navigation_button_text"
            textbutton 'Компьютер' xalign 0.9 yalign 0.5 action Show('compScreen')
            if 'bed' in school.furniture and ((ptime - last_sleeped >= 4) or (player.stats.energy < player.stats.health/4)):
                 textbutton 'Спать':
                     xalign 0.2 yalign 0.76 
                     action Jump('sleep')
            if callup != dummy:
                imagebutton:
                    idle im.MatrixColor(getCharImage(callup), im.matrix.opacity(0.5)) 
                    hover im.MatrixColor(getCharImage(callup), im.matrix.opacity(1.0)) 
                    action [Function(clrscr), Show('show_stat'), Function(showChars)] 
                    hovered SetVariable('interactionObj',callup) xalign 0.5 yoffset 400
                    
            if lt() >= 0 and is_cabbage == 0 and mile_qwest_2_stage > 0 or development > 0:
                imagebutton:
                    idle im.MatrixColor('pic/events/cabbage/secretary.png', im.matrix.opacity(0.5)) 
                    hover im.MatrixColor('pic/events/cabbage/secretary.png', im.matrix.opacity(1.0))
                    xalign 0.1 yalign 1.0
                    action [Jump('cabbageInit')]
            if mile_qwest_2_stage == 7 and (lt() in [-1,0]) and callup == dummy:
                textbutton 'Вызвать Валентину Купрувну' xalign 0.5 yalign 0.5 action Jump('kupruvnaGotIt1')
            if olympiad.confirm == True:
                textbutton 'Подготавливать учеников\nк олимпиаде' xalign 0.5 yalign 0.5 action Jump('olympiad_edu')
            if 'splitSystem' in school.furniture:
                use splitSystem
    screen splitSystem:
        fixed:
            vbox xalign 0.9 yalign 0.1:
                text 'Выставить температуру ([temperature] C)' style style.description
                hbox:
                    textbutton '+5' action SetVariable('temperature', temperature + 5), Function(move, curloc)
                    textbutton '-5' action SetVariable('temperature', temperature - 5), Function(move, curloc)
    call screen office

label loc_class1:
    show class1 at left
    screen class1:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Кабинет Химии. Тут обычно преподаёт Валентина Купрувна. Весь учительский стол завален всякими колбами и ретортами. В стороне даже приютилась пара баночек для анализов.' style style.description
                if 'chemlab' in school.buildings:
                    text 'Вы построили пристройку, и из этого кабинета теперь можно попать в лабораторию.' style style.description
                if camera.name in getLoc(curloc).getItems():
                    text 'Камера установлена.' style style.description
            textbutton 'Первый этаж':
                xalign 0.8 yalign 0.8 
                action Function(move, 'loc_firstFloor') 
                style "navigation_button" text_style "navigation_button_text"
            if 'chemlab' in school.buildings or development == 1:
                textbutton 'Лаборатория':
                    xalign 0.2 yalign 0.8 
                    action Function(move, 'loc_chemlab') 
                    style "navigation_button" text_style "navigation_button_text"
    call screen class1

label loc_chemlab:
    show chemlab at left
    screen chemlab:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Химическая лаборатория купленная за весьма немалые деньги. Будем надеяться, что вы сможете осуществить химический прорыв с её помощью!' style style.description
                text 'Ну или по крайней мере не взорвать всё к чёртовой матери...' style style.description
            textbutton 'Назад':
                xalign 0.8 yalign 0.8 
                action Function(move, 'loc_class1') 
                style "navigation_button" text_style "navigation_button_text"
    call screen chemlab
            
label loc_class2:
    show class2 at left
    screen class2:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Кабинет Биологии. Тут обычно преподаёт Полина Данокова.' style style.description
                if 'manec' in school.furniture:
                    text 'В углу стоят обнажённые человекоподобные манекены. Пугающе похожие на человека.' style style.description
            textbutton 'Первый этаж':
                xalign 0.8 yalign 0.8 
                action Function(move, 'loc_firstFloor') 
                style "navigation_button" text_style "navigation_button_text"
    call screen class2

label loc_class3:
    show class3 at left
    screen class3:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Кабинет Секспросвета. Тут обычно преподаёт Ангелина Фригидовна. Студентов заставляют заниматься в этом классе в случае провинности.' style style.description
                if 'dildo' in school.furniture:
                    text 'На столе у учительницы лежит подборка из всевозможных дилдо и искуственных вагин.'
            textbutton 'Первый этаж':
                xalign 0.8 yalign 0.8 
                action Function(move, 'loc_firstFloor') 
                style "navigation_button" text_style "navigation_button_text"
    call screen class3

label loc_class4:
    show class4 at left
    screen class4:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Кабинет Математики. Тут обычно преподаёт Валентина Биссектрисовна. У доски стоит здоровенная учительская тумба, в которой хранятся разные мелки, тряпки и прочая дребедень. Прикинув, вы понимаете, что такая тумба вместит даже небольшого человека. Только зачем бы там кому то прятаться?' style style.description
            textbutton 'Второй этаж':
                xalign 0.2 yalign 0.8 
                action Function(move, 'loc_secondFloor') 
                style "navigation_button" text_style "navigation_button_text"
    call screen class4

label loc_class5:
    show class5 at left
    screen class5:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Кабинет Английского языка. Тут обычно преподаёт Анжела Диковна.' style style.description
                if 'video' in school.furniture:
                    text 'К потолку прикручен кинопроектор для показа материалов по применению английского языка. Хотя если задуматься, в певую очередь это материалы по применению языка, и только во вторую по применению английского.'
            textbutton 'Второй этаж':
                xalign 0.2 yalign 0.8 
                action Function(move, 'loc_secondFloor') 
                style "navigation_button" text_style "navigation_button_text"
    call screen class5

label loc_secondFloor:
    show secondFloor at left
    screen secondFloor:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Из этого коридора Вы видите оставшиеся два класса, класс математики и класс английского языка. А так же учительскую и лестницу на первый этаж.' style style.description
                text 'В конце коридора расположены туалеты для мальчиков и девочек.' style style.description
            textbutton 'Класс 4':
                xalign 0.7 yalign 0.6 
                action Function(move, 'loc_class4') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Класс 5':
                xalign 0.3 yalign 0.4 
                action Function(move, 'loc_class5') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Учительская':
                xalign 0.05 yalign 0.5 
                action Function(move, 'loc_teacherRoom') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Дверь с М':
                xalign 0.2 yalign 0.27 
                action Function(move, 'loc_wcm')
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Дверь с Ж':
                xalign 0.2 yalign 0.32 
                action Function(move, 'loc_wcf') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Первый этаж':
                xalign 0.6 yalign 0.8 
                action Function(move, 'loc_firstFloor') 
                style "navigation_button" text_style "navigation_button_text"
            if 'doctor' in school.buildings or development == 1:
                textbutton 'Мед\nКабинет':
                    xalign 0.1 yalign 0.27 
                    action Function(move, 'loc_doctor') 
                    style "navigation_button" text_style "navigation_button_text"
    call screen secondFloor

label loc_teacherRoom:
    show teacherRoom at left
    screen teacherRoom:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Тут обычно проходят кофе-брейки учителей, а так же различные совещания. А ещё, у Вас тут частенько будут вымогать деньги на нужды школы.' style style.description
            textbutton 'Второй этаж':
                xalign 0.8 yalign 0.8 
                action Function(move, 'loc_secondFloor') 
                style "navigation_button" text_style "navigation_button_text"
    call screen teacherRoom

label loc_doctor:
    show doctor at left
    screen doctor:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Медкабинет принадлежащий вашей школе. В случае приступа острой хитрости, ученики обращаются именно сюда, непосредственно к медсестре Гонореевне.' style style.description
            textbutton 'Второй этаж':
                xalign 0.8 yalign 0.8 
                action Function(move, 'loc_secondFloor') 
                style "navigation_button" text_style "navigation_button_text"
    call screen doctor
            
label loc_wcm:
    show wcm at left
    screen wcm:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Мужской туалет. Писсуары явно говорят об этом. Вам здесь нечего делать. Будет неприятно, если Вас здесь застукают.' style style.description
            textbutton 'Второй этаж':
                xalign 0.8 yalign 0.8 
                action Function(move, 'loc_secondFloor') 
                style "navigation_button" text_style "navigation_button_text"
    call screen wcm

label loc_wcf:
    show wcf at left
    screen wcf:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Женский туалет. Очень миленький. Слева есть умывальник. С зеркалом.' style style.description
                if camera.name in getLoc(curloc).getItems():
                    text 'Камера установлена.' style style.description
                else:
                    text 'Хорошее место для того, чтобы установить скрытую камеру.' style style.description
            textbutton 'Второй этаж':
                xalign 0.8 yalign 0.8 
                action Function(move, 'loc_secondFloor') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Умывальник':
                xalign 0.1 yalign 0.6
                action Jump('cleanWCF')
    call screen wcf

##############################################################
# OTHER
##############################################################
label loc_street:
    show street
    screen street:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Простая улица на которой стоит Ваш дом. Вдоль улицы стоят другие дома ваших соседей. Кто знает, может быть где то по соседству живёт кто то из вашей школы?".' style style.description
                text 'Улица пересекает почти весь небольшой городок, и в конце упирается в улицу "Торговая".' style style.description
                if hour >= 5 and hour <= 20:
                     text 'Посмотрев вдоль, вы видите пару бегущих людей. Действительно, улица чрезвычайно удобна для пробежек.' style style.description
                else:
                     text 'Посмотрев вдоль, вы больше не видите бегущих людей. Наверное убежали. Или же просто ночь наступила?' style style.description
            textbutton 'Домой':
                xalign 0.8 yalign 0.4 
                action Function(move, 'loc_home') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'На пляж':
                xalign 0.3 yalign 0.77 
                action [Function(changetime, 30),Function(move, 'loc_beach')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Торговая\nулица':
                xalign 0.6 yalign 0.5 
                action [Function(changetime, 15),Function(move, 'loc_shopStreet')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'К школе':
                xalign 0.7 yalign 0.8 
                action [Function(changetime, 30),Function(move, 'loc_entrance')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Пробежка':
                xalign 0.3 yalign 0.5 
                action Function(move, 'loc_run')
            if olympiad.confirm == 1 and olympiad.cheat != 0 and olympiad.qwest == 0:
                textbutton 'В министерство':
                    xalign 0.5 yalign 0.8 
                    action Jump('olympiad_bribe_start')
                    style "navigation_button" text_style "navigation_button_text"
            if olympiad.qwest == 1 and hour in range(20,24) and olympiad.cheat == 0:
                textbutton 'К министру':
                    xalign 0.5 yalign 0.8 
                    action Jump('olympiad_home_sex')
                    style "navigation_button" text_style "navigation_button_text"
    call screen street

label loc_beach:
    show beach at left
    screen beach:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Пляж, просто пляж. На нём можно неплохо загореть, если уделить этому недельку времени, или же просто искупаться.' style style.description
            textbutton 'К дому':
                xalign 0.5 yalign 0.8 
                action [Function(changetime, 30),Function(move, 'loc_street')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Раздевалка':
                xalign 0.8 yalign 0.55 
                action Function(move, 'loc_beachChange') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Плавать':
                xalign 0.2 yalign 0.5 
                action Function(move, 'loc_swim')
    call screen beach

label loc_beachChange:
    show beachChange at left
    screen beachChange:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Специально обустроенные комнатки для переодеваний. Внутри небольшая полочка для вещей, умывальник и полотенце. Очень удобно, хотя и необычно.' style style.description
            textbutton 'Пляж':
                xalign 0.5 yalign 0.8 
                action Function(move, 'loc_beach') 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Переодеться':
                xalign 0.15 yalign 0.3 
                action Show('wardrobe')
            if is_beach_event == 1 and rand(1,10) == 1:
                textbutton 'Проверить\nдырочку' :
                    xalign 0.795 yalign 0.55 
                    action Function(tryEvent, 'loc_gloryHole')
            if is_glory_found == 1:
                textbutton 'Засунуть\nпальцы':
                    xalign 0.795 yalign 0.65 
                    action Jump('loc_gloryHole')
                    
    if is_beach_event == 0 and rand(1,10) == 1:
        $clrscr()
        jump beach_qwest
    if player.getLust() > 90:
        player.say 'Я слишком возбуждена, чтобы терпеть, мне срочно необходимо сбросить напряжение!'
        $ endurance = player.getFun() + player.getCorr()
        jump startMastur
    call screen beachChange


label loc_shopStreet:
    show shopStreet at left
    screen shopStreet:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Торговая улица! На ней много всяких маленьких магазинчиков, в которых закупается весь город. Говорят, что в некоторых странах Есть ОГРОМНЫЕ магазины, в которых есть ВСЁ. Но это как то бездушно. Зачем тебе это всё, когда души то нет?' style style.description
                text 'Мини маркет работает круглосуточно.' style style.description
                text 'Салон красоты работает с 8 до 19 ежедневно.' style style.description
            textbutton 'К дому':
                xalign 0.5 yalign 0.8 
                action [Function(changetime, 15),Function(move, 'loc_street')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Магазин':
                xalign 0.7 yalign 0.5 
                action [Function(move, 'loc_shop')] 
                style "navigation_button" text_style "navigation_button_text"
            if hour >=8 and hour <= 19:
                textbutton 'Салон\nКрасоты':
                    xalign 0.01 yalign 0.55 
                    action [Function(move, 'loc_shopBeauty')] 
                    style "navigation_button" text_style "navigation_button_text"
                textbutton 'Сексшоп':
                    xalign 0.85 yalign 0.5 
                    action [Function(move, 'loc_sexShop')] 
                    style "navigation_button" text_style "navigation_button_text"
    call screen shopStreet


label loc_shop:
    show shop at left
    screen shop:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Круглосуточный магазин, единственный в Вашем районе. После прогулки в нем Вы сможете без промедления набрать еды на кухню, выбрать себе напитки и некоторые иные вещи.' style style.description
            textbutton 'Назад':
                xalign 0.5 yalign 0.8 
                action [Function(move, 'loc_shopStreet')] 
                style "navigation_button" text_style "navigation_button_text"
            textbutton 'Закупиться':
                xalign 0.3 yalign 0.5 
                action [Hide('stats_screen'),Show('shopping')]
    call screen shop


label loc_shopBeauty:
    show shopBeauty at left
    screen beauty_description(what):
        fixed xpos 0.01 ypos 0.6 xmaximum 800:
            hbox:
                add im.FactorScale('pic/locations/shopBeauty/2.png',0.8)
                frame:
                    if what == 'him_zavivka':
                        vbox:
                            text _('Химическая завивка. Стоимость - 500. Длительность - 7 дней.')
                            if him_zavivka > 0:
                                text _('Дней до разрушения причёски: '+str(him_zavivka))
                    elif what == 'depilation':
                        vbox:
                            text _('Депиляция тела. Стоимость - 1000. Длительность - 14 дней.')
                            if depilation > 0:
                                text _('Дней до того, как станут заметны отросшие волоски: '+str(depilation))
                    elif what == 'skin_care':
                        vbox:
                            text _('Уход за кожей. Стоимость - 5000. Длительность - 30 дней.')
                            if skin_care > 0:
                                text _('Дней до того, как кожа придёт в прежнее состояние: '+str(skin_care))
                    elif what == 'manicure':
                        vbox:
                            text _('Маникюр. Стоимость - 100. Длительность - 3 дня.')
                            if manicure > 0:
                                text _('Дней до того, как отрастут ногти и маникюр испортится: '+str(manicure))
                    elif what == 'pedicure':
                        vbox:
                            text _('Педикюр. Стоимость - 200. Длительность - 6 дней.')
                            if pedicure > 0:
                                text _('Дней до того, как педикюр испортится: '+str(pedicure))
                    elif what == 'beauty_operation':
                        text _('Пластическая операция. Навсегда улучшает естественную красоту, вплоть до максимума. Стоимость - 50000.')
                    else:
                        text _('Нет описания для [what]')
    screen shopBeauty:
        fixed:
            vbox xalign 0.9 yalign 0.3 xminimum 200:
                textbutton _('Депиляция') action [
                    SelectedIf(depilation > 0),
                    SensitiveIf(player.money > 1000),
                    Jump('beauty_depilation')
                    ] hovered [
                    Show('beauty_description', None, 'depilation') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
                textbutton _('Химическая завивка') action [
                    SelectedIf(him_zavivka > 0),
                    SensitiveIf(player.money > 500),
                    Jump('beauty_him_zavivka')
                    ] hovered [
                    Show('beauty_description', None, 'him_zavivka') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
                textbutton _('Чистка кожи') action [
                    SelectedIf(skin_care > 0),
                    SensitiveIf(player.money > 5000),
                    Jump('beauty_skin_care')
                    ] hovered [
                    Show('beauty_description', None, 'skin_care') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
                textbutton _('Маникюр') action [
                    SelectedIf(manicure > 0),
                    SensitiveIf(player.money > 100),
                    Jump('beauty_manicure')
                    ] hovered [
                    Show('beauty_description', None, 'manicure') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
                textbutton _('Педикюр') action [
                    SelectedIf(pedicure > 0),
                    SensitiveIf(player.money > 200),
                    Jump('beauty_pedicure')
                    ] hovered [
                    Show('beauty_description', None, 'pedicure') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
                textbutton _('Пластическая операция') action [
                    SensitiveIf(player.stats.beauty < 100 and player.money > 50000),
                    Jump('beauty_operation')
                    ] hovered [
                    Show('beauty_description', None, 'beauty_operation') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
            vbox xalign 0.0 yalign 1.0:
                text 'Салон красоты приветствует Вас чистым полом и ярким рецепшеном. Наверняка тут предлагают великолепные по качеству услуги для улучшения внешности, если природа Вас обделила. Хотя и прирождённым красавицам они безусловно тоже помогут стать ещё красивее. Вот только цена, не отпугнёт ли она случайного клиента?' style style.description
            textbutton 'Назад' xalign 0.5 yalign 0.8 action [Function(move, 'loc_shopStreet')] style "navigation_button" text_style "navigation_button_text"
    if is_beauty_visited == 0:
        $clrscr()
        $ is_beauty_visited = 1
        jump beauty_intro
    call screen shopBeauty

label loc_sexShop:
        show sexShop at left
        if ptime > 366 and lt() == -1 and rand(1,3) = 1:
            jump danokova_start
        screen sexShop:
            fixed:
                vbox xalign 0.0 yalign 1.0:
                    text 'Вы видите перед собой магазин для взрослых. Полки уставлены различными игрушками для взрослых. Дилдо, вибраторы, резиновые дырки для мальчиков, пони с уникальным седлом для девочек. Отдельная полка для афродизиаков и прочей медицины. Глаза прямо разбегаются от обилия выбора!' style style.description
                textbutton 'Закупиться':
                    xalign 0.3 yalign 0.5 
                    action [Function(clrscr), Show('sexShopping')]
                textbutton 'Назад':
                    xalign 0.5 yalign 0.8 
                    action [Function(move, 'loc_shopStreet')] 
                    style "navigation_button" text_style "navigation_button_text"
        call screen sexShop
