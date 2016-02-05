init 10 python:
    locations = []
    global loc_btn, loc_txt
    loc_btn = []
    loc_txt = []
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
            if lt() > 0 or lt() == -4: rez = -1 # Если ночь, то на улице никого нет

            elif 'school' in self.position and lt() == -1: rez = self.base_prob/4 # Если внеурочное время, то в школе шансов встретить меньше
            elif 'school' in self.position and lt() == 0: rez = self.base_prob*2 # Если перемена, то в школе шансов встретить гораздо больше
            elif 'other' in self.position and lt() == 0: rez = -1 # Во время перемен никого не будет в городе
            elif self.id in ['loc_street','loc_shopStreet'] and hour < 8: rez = self.base_prob*2 # Перед уроками на улице чаще
            elif self.id in ['loc_beach'] and hour < 8: rez = self.base_prob/2 # Перед уроками на пляже реже
            else :
                rez = self.base_prob # Иначе настоящая вероятность

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
            statuses - список статусов, если нужно задать вероятности, то
                       список tuple'ов (status, prob)
            """

            for x in statuses:
                try:
                    self.addStatus(x[0], x[1])
                except TypeError:
                    self.addStatus(x)

        def getStatuses(self):
            """Возвращает список статусов с учетом их вероятностей.
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

        def removeStatus(self, rStatus):
            """Удаляет статус из локации"""
            self.__statuses = [x for x in self.__statuses\
                               if x[0].name!=rStatus.name]

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
                            N (заиграться до 100 fun не получится).
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

# Функция добавления эвентов в локации
    def getEvents():
        for eventLabel in _locs: # перебираем все лейблы
            if eventLabel[:6] == 'event_': # находим тот, что с евентом
                for location in locations: # начинаем перебирать локации
                    if eventLabel.find(location.id) > 0: # Если имя локации содержится в имени эвента
                        index = eventLabel.rfind(location.id) # находим правый индекс имени локации
                        corr = eventLabel[index:] # режем по нему
                        temp = corr.split("_") # разбиваем строку по_
                        corr = int(temp[2]) # находим развратность
                        event = Event(id = eventLabel, corr = corr) # создаём эвент
                        location.events.append(event) # добавляем его в массив эвентов локации
        return 0

    def getQwests():
        for eventLabel in _locs: # перебираем все лейблы
            if eventLabel[:6] == 'qwest_': # находим тот, что с квестом
                for location in locations: # начинаем перебирать локации
                    if eventLabel.find(location.id) > 0: # Если имя локации содержится в имени эвента
                        qwest = Qwest(id = eventLabel) # создаём эвент
                        qwests = []
                        for q in location.qwests:
                            qwests.append(q.id)
                        if qwest.id not in qwests:
                            location.qwests.append(qwest) # добавляем его в массив эвентов локации
        return 0
    _locs = renpy.get_all_labels()
# Создание массива всех локаций
    def genLocs():

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

                elif x == 'loc_hall': loc = Location(id = x, name = 'холл', base_prob = 5, position = ['school'])
                elif x == 'loc_dungeon': loc = Location(id = x, name = 'подвал', base_prob = -1, position = ['school'])
                elif x == 'loc_entrance': loc = Location(id = x, name = 'вход', base_prob = 10, position = ['school'])
                elif x == 'loc_library': loc = Location(id = x, name = 'библиотека', base_prob = 10, position = ['school'])
                elif x == 'loc_changeRoom': loc = Location(id = x, name = 'школьная раздевалка', base_prob = 5, position = ['school','safe','change'])
                elif x == 'loc_gym': loc = Location(id = x, name = 'спортивный зал', base_prob = 20, position = ['school','classroom','sport'])
                elif x == 'loc_pool': loc = Location(id = x, name = 'бассейн', base_prob = 20, position = ['school','classroom','swim'])
                elif x == 'loc_firstFloor': loc = Location(id = x, name = 'первый этаж', base_prob = 20, position = ['school'])
                elif x == 'loc_secondFloor': loc = Location(id = x, name = 'второй этаж', base_prob = 20, position = ['school'])
                elif x == 'loc_class1': loc = Location(id = x, name = 'Класс 1', base_prob = 10, position = ['school','classroom'])
                elif x == 'loc_class2': loc = Location(id = x, name = 'Класс 2', base_prob = 10, position = ['school','classroom'])
                elif x == 'loc_class3': loc = Location(id = x, name = 'Класс 3', base_prob = 10, position = ['school','classroom'])
                elif x == 'loc_class4': loc = Location(id = x, name = 'Класс 4', base_prob = 10, position = ['school','classroom'])
                elif x == 'loc_class5': loc = Location(id = x, name = 'Класс 5', base_prob = 10, position = ['school','classroom'])
                elif x == 'loc_teacherRoom': loc = Location(id = x, name = 'учительская', base_prob = 0, position = ['school'])
                elif x == 'loc_wcm': loc = Location(id = x, name = 'Туалет для мальчиков', base_prob = 5, position = ['school'])
                elif x == 'loc_wcf': loc = Location(id = x, name = 'Туалет для девочек', base_prob = 5, position = ['school'])
                elif x == 'loc_storage': loc = Location(id = x, name = 'кладовка', base_prob = 5, position = ['school'])
                elif x == 'loc_chemlab': loc = Location(id = x, name = 'Лаборатория', base_prob = -1, position = ['school'])
                elif x == 'loc_doctor': loc = Location(id = x, name = 'Медицинский кабинет', base_prob = 2, position = ['school'])
                elif x == 'loc_office': loc = Location(id = x, name = 'офис', base_prob = -1, position = ['safe','school'])

                elif x == 'loc_dreams': loc = Location(id = x, name = 'Сны', base_prob = -1, position = ['self'])
                elif x == 'loc_swim': loc = Location(id = x, name = 'Плавание', base_prob = -1, position = ['self'])
                elif x == 'loc_run': loc = Location(id = x, name = 'Бег', base_prob = -1, position = ['self'])
                elif x == 'loc_taxi': loc = Location(id = x, name = 'Такси', base_prob = -1, position = ['self'])
                elif x == 'loc_gloryHole': loc = Location(id = x, name = 'Глорихол', base_prob = 0, position = ['self'])
                elif x == 'loc_beachWalk': loc = Location(id = x, name = 'Загар', base_prob = -1, position = ['self'])

                elif x == 'loc_lessonAssist': loc = Location(id = x, name = 'Ассистирование', base_prob = -1, position = ['self'])
                elif x == 'loc_lessonEduFail': loc = Location(id = x, name = 'Обучение', base_prob = -1, position = ['self'])
                elif x == 'loc_lessonEduNo': loc = Location(id = x, name = 'Обучение', base_prob = -1, position = ['self'])
                elif x == 'loc_lessonEduOk': loc = Location(id = x, name = 'Обучение', base_prob = -1, position = ['self'])
                elif x == 'loc_lessonFun': loc = Location(id = x, name = 'Развлечь студентов', base_prob = -1, position = ['self'])
                elif x == 'loc_lessonCorr': loc = Location(id = x, name = 'Эротическое просвещение', base_prob = -1, position = ['self'])
                elif x == 'loc_LessonSportSwim': loc = Location(id = x, name = 'Занятия в бассейне', base_prob = -1, position = ['self'])
                elif x == 'loc_LessonSportGym': loc = Location(id = x, name = 'Занятия в спортзале', base_prob = -1, position = ['self'])

                elif x == 'loc_class1Learn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
                elif x == 'loc_class2Learn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
                elif x == 'loc_class3Learn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
                elif x == 'loc_class4Learn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
                elif x == 'loc_class5Learn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
                elif x == 'loc_gymLearn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
                elif x == 'loc_poolLearn': loc = Location(id = x, name = 'Учёба', base_prob = -1, position = ['tech'])
                elif x == 'loc_cabbage': loc = Location(id = x, name = 'Капуста', base_prob = -1, position = ['tech'])
                elif x == 'loc_shower': loc = Location(id = x, name = 'Душ', base_prob = -1, position = ['tech'])
                elif x == 'loc_ahmedSex': loc = Location(id = x, name = 'Эвенты с физруком', base_prob = -1, position = ['tech'])
                elif x == 'loc_ahmedFootjob': loc = Location(id = x, name = 'Эвенты с физруком', base_prob = -1, position = ['tech'])
                elif x == 'loc_ahmedSuck': loc = Location(id = x, name = 'Эвенты с физруком', base_prob = -1, position = ['tech'])
                
                else: loc = Location(id = x, name = 'UNKNOWN', base_prob = -1, position = ['other'])
                locations.append(loc)

    genLocs() # генерирую локации
    getEvents() # добавляю всем эвенты
    getQwests() # добавляю квесты
    
######################################################
# Объявление всех картинок локаций
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

# Для теста
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
    # show expression 'pic/status/male_toy.jpg' at Move((0.0, 0.0), (0.0, -1.1), 10.0, repeat = True, bounce = True, xanchor="left", yanchor="top") as tempPic
    # ''
    # $move(curloc)
    $ changetime(60*24)
    $ move('loc_home')

##############################################################
# Home
##############################################################
label loc_home:
    if ptime == 0:
        $ ptime += 1
        $ move ('intro')
    show home
    python:
        loc_btn = [
            ('Кухня', Function(move, 'loc_kitchen'), True),
            ('Спальня', Function(move, 'loc_bedroom'), True),
            ('Ванная', Function(move, 'loc_bathroom'), True),
            ('Улица', Function(move, 'loc_street'), True)
            ]
        loc_txt = ['Гостиная в вашей квартире. Маленькая, зато аккуратная. На стеклянном столе лежит пачка салфеток для ежедневного ухода за кожей. ']
        loc_txt += ['Напротив диванчика стоит телевизор. Вы не помните, чтобы по нему хоть раз показывали что-то хорошее. Возможно потому, что потеряли пульт сразу после переезда.']
    screen home:
        fixed:
            if development == 1:
                textbutton 'Test':
                    xalign 0.0 yalign 0.2
                    action Function(move,'test')
    call screen home

label loc_bedroom:
    $ endurance = player.getCorr()+player.getFun()
    show bedroom at left
    python:
        loc_btn = [
            ('Гостиная', Function(move, 'loc_home'), True),
            ('{i}Переодеться{/i}', Show('wardrobe'), True),
            ('{i}Спать{/i}', Jump('sleep'), ((ptime - last_sleeped >= 4) or (player.stats.energy < player.stats.health/4))),
            ('{i}Мастурбировать{/i}', Jump('startMastur'), (player.getLust() > 0))
            ]
        loc_txt = ['Уютненькая маленькая спальня. Слева находится небольшой шкаф, в котором висит ваша повседневная одежда. Справа кровать, довольно удобная. Тут ещё есть телевизор, но он не работает, так что совсем не будет мешать Вам отходить ко сну.']
    screen bedroom:
        null
    call screen bedroom


label loc_kitchen:
    show kitchen at left
    python:
        loc_btn = [
            ('Гостиная', Function(move, 'loc_home'), True),
            ('{i}Поесть{/i}', [Function(player.eat, player.getItem('Сырая еда')),Function(move, curloc, 15)],(player.hasItem('Сырая еда') and (ptime - last_eat > 4))),
            ('{i}Сделать сэндвич{/i}', [Function(player.addItems, 'Сэндвич'), Function(player.apply, 'Сырая еда'), Function(move, curloc, 15)], (player.hasItem('Сэндвич') == False and player.hasItem('Сырая еда') == True))
            ]
        if player.hasItem('Сырая еда'):
            loc_txt = ['Микроволновка, плита, раковина, шкафчики. Кухня одним словом. \nОценив количество оставшейся еды, вы прикидываете, что её хватит ещё на '+str(player.getItem('Сырая еда').durability)+' раз.']
        else :
            loc_txt = ['Микроволновка, плита, раковина, шкафчики. Кухня, одним словом. \nОценив количество оставшейся еды, вы понимаете, что её не осталось СОВСЕМ. Надо срочно сгонять в магазин.']
    screen kitchen:
        null
    call screen kitchen


label loc_bathroom:
    show bathroom at left
    python:
        loc_btn = [
            ('Гостиная', Function(move, 'loc_home'), True),
            ('{i}Принять душ{/i}', Jump('shower'), True),
            ]
        loc_txt = ['Ванная комната. Совмещённая. В лучших традициях далёкой страны. Тут можно искупаться, чтобы смыть с себя грязь и прочие человеческие нечистоты. А можно просто постоять под душем и отдохнуть.']
    screen bathroom:
        null
    call screen bathroom



##############################################################
# SCHOOL
##############################################################
label loc_entrance:
    show entrance at left
    python:
        loc_btn = [
            ('Холл', [Function(move, 'loc_hall')], True),
            ('Первый этаж', [Function(move, 'loc_firstFloor')], True),
            ('Второй этаж', [Function(move, 'loc_secondFloor')], True),
            ('Ваш офис', [Function(move, 'loc_office')], True),
            ('Домой', [Function(move, 'loc_street', 30)], True),
            ('Библиотека', [Function(move, 'loc_library')], ('library' in school.buildings)),
            #(),
            ]
        loc_txt = ['Вход в вашу новую школу. Ворота, крыльцо - всё как у всех, ничего необычного. Разве что кусты не особо пострижены, и дети там периодически играют, ну да ладно.']
        if 'library' not in school.buildings:
            loc_txt += ['Слева от школы полно места. Вроде как там раньше стоял сарай, но он давным давно рухнул, и теперь земля пустует. Библиотеку что ли там построить? ']
        else:
            loc_txt += ['Слева от школы виден вход в школьную библиотеку. В самом деле, замечательное приобретение! ']
        if 'wall' not in school.buildings:
            loc_txt += ['Окидывая взглядом свои владения, вы видите прекрасный вид на окна школы. Выглядит, конечно, красиво, но как-то всё напоказ. ']
        else:
            loc_txt += ['Довольно высокая стена окружает школу. С улицы вообще непонятно, то ли это школа, то ли режимный объект. ']
        if is_cabbage == 1 and hour == 7 and weekday < 6:
            loc_txt += ['{color=#00ff00} Сегодня день уборки урожая! Автобус ожидает вас и ваших учеников.{/color}']
    screen entrance:
        fixed:
            if is_cabbage == 1 and hour == 7 and weekday < 6:
                imagebutton:
                    idle im.MatrixColor('pic/events/cabbage/bus.png', im.matrix.opacity(0.5))
                    hover im.MatrixColor('pic/events/cabbage/bus.png', im.matrix.opacity(1.0))
                    xalign 4.8 yalign 1.2
                    action [Jump('cabbageStart')]
    call screen entrance

label loc_library:
    show library at left
    python:
        loc_btn = [
            ('Выход', [Function(move, 'loc_entrance')], True),
            ]
        loc_txt = ['Недавно построенная школьная библиотека. Всё сделано на удивление быстро и качественно. Городская библиотека выделила много книг на её заполнение, которые всё равно готовились списать.']
        loc_txt += ['В любом случае тут - прекрасное место для самообразования и не только!']
    screen library:
        null
    call screen library


label loc_hall:
    show hall at left
    python:
        loc_btn = [
            ('Первый этаж', [Function(move, 'loc_firstFloor')], True),
            ('Бассейн', [Function(move, 'loc_pool')], True),
            ('Спортзал', [Function(move, 'loc_gym')], True),
            ('Выход', [Function(move, 'loc_entrance')], True),
            ('Подвал', [Function(move, 'loc_dungeon')], ('dungeon' in school.buildings or development == 1)),
            ]
        loc_txt = ['По всему холлу расставлены шкафчики для личных вещей. И еще лавочки, сидя на которых удобно переобуваться. В образующих шкафчиками коридорах легко потеряться с непривычки. По школе ходят ужасные истории, что из первого выпуска школы, ещё никто не вернулся домой. Так и бродят они до сих пор по коридорам и воруют у новых учеников обувь, чтобы починить свои стоптанные за года блужданий ботинки. Глупая история, считаете вы.']
    screen hall:
        fixed:
            if getPar(studs,'corr') >= 20 and lt() == 0 and hour < 9 and mile_quest_1 == 0 or development == 1:
                imagebutton:
                    idle im.MatrixColor('pic/events/mile_1/start.png', im.matrix.opacity(0.5))
                    hover im.MatrixColor('pic/events/mile_1/start.png', im.matrix.opacity(1.0))
                    action [Jump('mileQwest1')] xalign 1.0 yalign 0.8
    call screen hall

label loc_dungeon:
    show dungeon at top
    python:
        loc_btn = [
            ('Выход', [Function(move, 'loc_hall')], True),
            ]
        loc_txt = ['Тёмный, мрачный подвал больше напоминающий подземелье из какой-то игры про рабынь, чем обычное подвальное помещение средней школы.']
    screen dungeon:
        null
    call screen dungeon

label loc_pool:
    show pool at left
    python:
        loc_btn = [
            ('Раздевалка', [Function(move, 'loc_changeRoom')], True),
            ('Холл', [Function(move, 'loc_hall')], True),
            ('{i}В душ{/i}', Jump('shower'), True),
            ]
        loc_txt = ['Бассейн. Здесь проходят занятия по вторникам и четвергам. Также в перемены и после уроков ученики могут придти сюда, чтобы поплавать или просто постоять, глядя на воду. Вы также можете немного потренировать своё здоровье, попытавшись проплыть стометровку пару раз.']
        loc_txt += ['Неподалеку от бассейна находится душ, где вы в любой момент можете освежиться.']
    screen pool:
        null
    call screen pool


label loc_changeRoom:
    show changeRoom at left
    python:
        loc_btn = [
            ('Бассейн', [Function(move, 'loc_pool')], True),
            ('Спортзал', [Function(move, 'loc_gym')], True),
            ('{i}Переодеться{/i}', Show('wardrobe'), True),
            ]
        loc_txt = ['Раздевалка. Она разделена на 2 отделения: для мальчиков и для девочек. Как ни странно, вы тоже можете тут переодеваться.']
    screen changeRoom:
        null
    call screen changeRoom


label loc_gym:
    show gym at left
    python:
        loc_btn = [
            ('Кладовка', [Function(move, 'loc_storage')], True),
            ('Раздевалка', [Function(move, 'loc_changeRoom')], True),
            ('Холл', [Function(move, 'loc_hall')], True),
            ]
        loc_txt = ['Спортзал, здесь проходят занятия по понедельникам, средам и пятницам. Но ученики и просто приходят сюда в перемены, чтобы покидать мяч.']
    screen gym:
        null
    call screen gym

label loc_storage:
    show storage at left
    python:
        loc_btn = [
            ('Спортзал', Function(move, 'loc_gym'), True),
            ]
        loc_txt = ['Кладовка спортинвентаря. В ней находятся мячи, маты, козлы и прочий спортинвентарь. Многие ученики ходят сюда, чтобы немного отдохнуть и уединиться от всех.']
    screen storage:
        null
    call screen storage

label loc_firstFloor:
    show firstFloor at left
    python:
        loc_btn = [
            ('Ваш офис', [Function(move, 'loc_office')], True),
            ('Класс 1', [Function(move, 'loc_class1')], True),
            ('Класс 2', [Function(move, 'loc_class2')], True),
            ('Класс 3', [Function(move, 'loc_class3')], True),
            ('Второй этаж', [Function(move, 'loc_secondFloor')], True),
            ('Холл', [Function(move, 'loc_hall')], True),
            ]
        loc_txt = ['Коридор первого этажа. Тут находится ваш офис, а также первые три классных кабинета: кабинет химии, кабинет биологии и класс уроков секспросвета. Вы видите лестницу на второй этаж и в холл.']
    screen firstFloor:
        null
    call screen firstFloor

label loc_office:
    show office at left
    # Часть квеста даноковой
    if hour >= 15 and hour < 17 and (weekday == 2 or weekday == 4) and mile_qwest_3_stage == 50:
        'Дверь в кабинет закрыта и из-за неё слышны тихие стоны. Вы вздыхаете и уходите. В конце концов, вы добились чего хотели. Наверное.'
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

    python:
        loc_btn = [
            ('Первый этаж', [Function(move, 'loc_firstFloor')], True),
            ('Воспользоваться окном', [Function(move, 'loc_entrance')], True),
            ('{i}Переодеться{/i}', Show('wardrobe'), True),
            ('{i}Компьютер{/i}', [Show('compScreen')], True),
            ('{i}Спать{/i}', [Jump('sleep')], ('bed' in school.furniture and ((ptime - last_sleeped >= 4) or (player.stats.energy < player.stats.health/4)))),
            ('{i}Вызвать Валентину Купрувну{/i}', [Jump('kupruvnaGotIt3')], (mile_qwest_2_stage == 7 and (lt() in [-1,0]) and callup == dummy)),
            ('{i}Готовить учеников к олимпиаде{/i}', [Jump('olympiad_edu')], olympiad.confirm),
            ]
        loc_txt = ['Ваш офис. Большой дубовый стол, компьютер - сразу видно, что вы здесь уважаемы.']
        if lt() >= 0 and is_cabbage == 0 and mile_qwest_2_stage > 0:
            loc_txt += ['Вы видите молодого, хорошо одетого мужчину в вашем кабинете.']
        if mile_qwest_2_stage == 10 and hour == 7:
            loc_txt += ['Почти голая, не считая фартука, Валентина Купрувна что то протирает в углу вашего кабинета.']
    screen office:
        zorder -1
        fixed:
            if callup != dummy:
                imagebutton:
                    idle im.MatrixColor(getCharImage(callup), im.matrix.opacity(0.5))
                    hover im.MatrixColor(getCharImage(callup), im.matrix.opacity(1.0))
                    action [Function(clrscr), SetVariable('reaction', reactionGen(callup)), Show('show_stat'), Function(showChars)]
                    hovered SetVariable('interactionObj',callup) xalign 0.5 yoffset 400

            if lt() >= 0 and is_cabbage == 0 and mile_qwest_2_stage > 0 or development > 0:
                imagebutton:
                    idle im.MatrixColor('pic/events/cabbage/secretary.png', im.matrix.opacity(0.5))
                    hover im.MatrixColor('pic/events/cabbage/secretary.png', im.matrix.opacity(1.0))
                    xalign 0.1 yalign 1.0
                    action [Jump('cabbageInit')]

            if 'splitSystem' in school.furniture:
                use splitSystem
            
            if mile_qwest_2_stage == 10 and hour == 7:
                add 'pic/locations/school/office/maid.png' at left
    screen splitSystem:
        fixed:
            vbox xalign 0.85 yalign 0.07:
                text 'Выставить температуру ([temperature] C)' style style.description
                hbox:
                    textbutton '+5' action SetVariable('temperature', temperature + 5), Function(move, curloc)
                    textbutton '-5' action SetVariable('temperature', temperature - 5), Function(move, curloc)
    call screen office

label loc_class1:
    show class1 at left
    if mile_qwest_3_stage == 15:
        jump get_chloroform
        
    python:
        loc_btn = [
            ('Первый этаж', Function(move, 'loc_firstFloor'), True),
            ('Лаборатория', Function(move, 'loc_chemlab'), ('chemlab' in school.buildings or development == 1)),
            ]
        loc_txt = ['Кабинет химии. Тут обычно преподаёт Валентина Купрувна. Весь учительский стол завален всякими колбами и ретортами. В стороне даже приютилась пара баночек для анализов.']
        if 'chemlab' in school.buildings:
            loc_txt += ['Вы построили пристройку, и из этого кабинета теперь можно попасть в лабораторию.']
        if camera.name in getLoc(curloc).getItems():
            loc_txt += ['Камера установлена.']
    screen class1:
        null
    call screen class1

label loc_chemlab:
    show chemlab at left
    python:
        loc_btn = [
            ('Назад', Function(move, 'loc_class1'), True),
            ]
        loc_txt = ['Химическая лаборатория, купленная за весьма немалые деньги. Будем надеяться, что вы сможете осуществить химический прорыв с её помощью!']
        loc_txt += ['Ну или, по крайней мере не взорвать всё к чёртовой матери...']
    screen chemlab:
        null
    call screen chemlab

label loc_class2:
    show class2 at left
    python:
        loc_btn = [
            ('Первый этаж', Function(move, 'loc_firstFloor'), True),
            ]
        loc_txt = ['Кабинет биологии. Тут обычно преподаёт Полина Данокова.']
        if 'manec' in school.furniture:
            loc_txt += ['В углу стоят обнажённые человекоподобные манекены. Сходство с человеком настолько сильное, что это даже пугает.']
    screen class2:
        null
    call screen class2

label loc_class3:
    show class3 at left
    python:
        loc_btn = [
            ('Первый этаж', Function(move, 'loc_firstFloor'), True),
            ]
        loc_txt = ['Кабинет секспросвета. Тут обычно преподаёт Ангелина Фригидовна. Студентов заставляют заниматься в этом классе в случае провинности.']
        if 'dildo' in school.furniture:
            loc_txt += ['На столе у учительницы лежит подборка из всевозможных дилдо и искуственных вагин.']
    screen class3:
        null
    call screen class3

label loc_class4:
    show class4 at left
    python:
        loc_btn = [
            ('Второй этаж', Function(move, 'loc_secondFloor'), True),
            ]
        loc_txt = ['Кабинет математики. Тут обычно преподаёт Валентина Биссектрисовна. У доски стоит здоровенная учительская тумба, в которой хранятся разные мелки, тряпки и прочая дребедень. Прикинув, вы понимаете, что такая тумба вместит даже небольшого человека. Только зачем бы там кому-то прятаться?']
    screen class4:
        null
    call screen class4

label loc_class5:
    show class5 at left
    python:
        loc_btn = [
            ('Второй этаж', Function(move, 'loc_secondFloor'), True),
            ]
        loc_txt = ['Кабинет английского языка. Тут обычно преподаёт Анжела Диковна.']
        if 'video' in school.furniture:
            loc_txt += ['К потолку прикручен кинопроектор для показа материалов по применению английского языка. Хотя, если задуматься, в первую очередь это материалы по применению языка, и только во вторую по применению английского.']
    screen class5:
        null
    call screen class5

label loc_secondFloor:
    show secondFloor at left
    python:
        loc_btn = [
            ('Первый этаж', Function(move, 'loc_firstFloor'), True),
            ('Класс 4', Function(move, 'loc_class4'), True),
            ('Класс 5', Function(move, 'loc_class5'), True),
            ('Учительская', Function(move, 'loc_teacherRoom'), True),
            ('Дверь с М', Function(move, 'loc_wcm'), True),
            ('Дверь с Ж', Function(move, 'loc_wcf'), True),
            ('Мед Кабинет', Function(move, 'loc_doctor'), ('doctor' in school.buildings or development == 1)),
            ]
        loc_txt = ['Из этого коридора вы видите оставшиеся два класса: класс математики и класс английского языка. А также учительскую и лестницу на первый этаж.']
        loc_txt += ['В конце коридора расположены туалеты для мальчиков и девочек.']
    screen secondFloor:
        null
    call screen secondFloor

label loc_teacherRoom:
    show teacherRoom at left
    python:
        loc_btn = [
            ('Второй этаж', Function(move, 'loc_secondFloor'), True),
            ]
        loc_txt = ['Тут обычно проходят кофе-брейки учителей, а также различные совещания. А ещё, у вас тут частенько будут вымогать деньги на нужды школы.']
    screen teacherRoom:
        null
    call screen teacherRoom

label loc_doctor:
    show doctor at left
    python:
        loc_btn = [
            ('Второй этаж', Function(move, 'loc_secondFloor'), True),
            ]
        loc_txt = ['Медкабинет принадлежащий вашей школе. В случае приступа острой хитрости, ученики обращаются именно сюда, непосредственно к медсестре Гонореевне.']
    screen doctor:
        null
    call screen doctor

label loc_wcm:
    show wcm at left
    python:
        loc_btn = [
            ('Второй этаж', Function(move, 'loc_secondFloor'), True),
            ]
        loc_txt = ['Мужской туалет. Писсуары явно говорят об этом. Вам здесь нечего делать. Будет неприятно, если вас здесь застукают.']
    screen wcm:
        null
    call screen wcm

label loc_wcf:
    show wcf at left
    python:
        loc_btn = [
            ('Второй этаж', Function(move, 'loc_secondFloor'), True),
            ('{i}Умывальник{/i}', Jump('cleanWCF'), True)
            ]
        loc_txt = ['Женский туалет. Очень миленький. Слева есть умывальник с зеркалом.']
        if camera.name in getLoc(curloc).getItems():
            loc_txt += ['Камера установлена.']
        else:
            loc_txt += ['Хорошее место для того, чтобы установить скрытую камеру.']
    screen wcf:
        null
    call screen wcf

##############################################################
# OTHER
##############################################################
label loc_street:
    show street    
    python:
        loc_btn = [
            ('Домой', Function(move, 'loc_home'), (1==1)),
            ('На пляж', [Function(changetime, 30),Function(move, 'loc_beach')], (1==1)),
            ('На Торговую', [Function(changetime, 15),Function(move, 'loc_shopStreet')], (1==1)),
            ('К школе', [Function(changetime, 30),Function(move, 'loc_entrance')], (1==1)),
            ('В министерство', Jump('olympiad_bribe_start'), (olympiad.confirm == 1 and olympiad.cheat == 0 and olympiad.qwest == 0)),
            ('К министру', Jump('olympiad_home_sex'), (olympiad.qwest == 1 and hour in range(20,24) and olympiad.cheat == 0)),            
            ('{i}Пробежка{/i}', Function(move, 'loc_run'), (1==1)),
            ]
        loc_txt = ['Простая улица, на которой стоит ваш дом. Вдоль улицы стоят другие дома ваших соседей. Кто знает, может быть где-то по соседству живёт кто-то из вашей школы?".']
        loc_txt += ['Улица пересекает почти весь небольшой городок и в конце упирается в улицу "Торговая".']
        if hour >= 5 and hour <= 20:
            loc_txt += ['Посмотрев вдоль, вы видите пару бегущих людей. Действительно, улица чрезвычайно удобна для пробежек.']
        else:
            loc_txt += ['Посмотрев вдоль, вы больше не видите бегущих людей. Наверное, убежали. Или же просто ночь наступила?']
    screen street:
        null
    call screen street

label loc_beach:
    show beach at left
    python:
        loc_btn = [
            ('К дому', Function(move, 'loc_street', 30), True),
            ('В раздевалку', Function(move, 'loc_beachChange'), True),
            ('{i}Плавать{/i}', Function(move, 'loc_swim'), (hour >= 7 and hour <= 20)),
            ('{i}Загорать{/i}', [Function(clrscr), Jump('playerTan')], (hour >= 7 and hour <= 20)),
            ]
        loc_txt = ['Пляж, просто пляж. На нём можно неплохо загореть, если уделить этому недельку времени, или же просто искупаться.']
    screen beach:
        null
    call screen beach

label loc_beachChange:
    show beachChange at left
    python:
        loc_btn = [
            ('На пляж', Function(move, 'loc_beach'), True),
            ('{i}Переодеться{/i}', Show('wardrobe'), True),
            ('{i}Проверить дырочку{/i}', Function(tryEvent, 'loc_gloryHole'), (is_beach_event == 1 and rand(1,10) == 1 and lt() != -4)),
            ('{i}Засунуть пальцы{/i}', Jump('loc_gloryHole'), (is_glory_found == 1)),
            ]
        loc_txt = ['Специально обустроенные комнатки для переодеваний. Внутри небольшая полочка для вещей, умывальник и полотенце. Очень удобно, хотя и необычно.']
    screen beachChange:
        null

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
    python:
        loc_btn = [
            ('К дому', [Function(move, 'loc_street', 15)], True),
            ('Магазин', [Function(move, 'loc_shop')], True),
            ('Салон красоты', [Function(move, 'loc_shopBeauty')], (hour >=8 and hour <= 19)),
            ('Сексшоп', [Function(move, 'loc_sexShop')], (hour >=8 and hour <= 19)),
            ]
        loc_txt = ['Торговая улица! На ней много всяких маленьких магазинчиков, в которых закупается весь город. Говорят, что в некоторых странах есть ОГРОМНЫЕ магазины, в которых есть ВСЁ. Но это как-то бездушно. Зачем тебе это всё, когда души-то нет?']
        loc_txt += ['Минимаркет работает круглосуточно.']
        loc_txt += ['Салон красоты работает с 8 до 19 ежедневно.']
    screen shopStreet:
        null
    call screen shopStreet


label loc_shop:
    show shop at left
    python:
        loc_btn = [
            ('На улицу', [Function(move, 'loc_shopStreet')], True),
            ('{i}Закупиться{/i}', [Hide('stats_screen'),Show('shopping')], True),
            ]
        loc_txt = ['Круглосуточный магазин, единственный в вашем районе. После прогулки в нем вы сможете без промедления набрать еды на кухню, выбрать себе напитки и некоторые иные вещи.']
    screen shop:
        null
    call screen shop


label loc_shopBeauty:
    show shopBeauty at left
    python:
        loc_btn = [
            ('На улицу', [Function(move, 'loc_shopStreet')], True),
            ]
        loc_txt = ['Салон красоты приветствует вас чистым полом и яркой стойкой администратора. Наверняка тут предлагают великолепные по качеству услуги для улучшения внешности, если природа вас обделила. Хотя и прирождённым красавицам они безусловно помогут стать ещё красивее. Вот только цена, не отпугнёт ли она случайного клиента?']

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

    screen shopBeautyBtn:
        fixed:
            vbox:
                xalign 0.99
                textbutton _('Депиляция'):
                    xalign 0.99
                    action [
                    SelectedIf(depilation > 0),
                    SensitiveIf(player.money > 1000),
                    Jump('beauty_depilation')
                    ] hovered [
                    Show('beauty_description', None, 'depilation') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
                    text_style "navigation_button_text"
                textbutton _('Химическая завивка'):
                    xalign 0.99
                    action [
                    SelectedIf(him_zavivka > 0),
                    SensitiveIf(player.money > 500),
                    Jump('beauty_him_zavivka')
                    ] hovered [
                    Show('beauty_description', None, 'him_zavivka') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
                    text_style "navigation_button_text"
                textbutton _('Чистка кожи'):
                    xalign 0.99
                    action [
                    SelectedIf(skin_care > 0),
                    SensitiveIf(player.money > 5000),
                    Jump('beauty_skin_care')
                    ] hovered [
                    Show('beauty_description', None, 'skin_care') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
                    text_style "navigation_button_text"
                textbutton _('Маникюр'):
                    xalign 0.99
                    action [
                    SelectedIf(manicure > 0),
                    SensitiveIf(player.money > 100),
                    Jump('beauty_manicure')
                    ] hovered [
                    Show('beauty_description', None, 'manicure') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
                    text_style "navigation_button_text"
                textbutton _('Педикюр'):
                    xalign 0.99
                    action [
                    SelectedIf(pedicure > 0),
                    SensitiveIf(player.money > 200),
                    Jump('beauty_pedicure')
                    ] hovered [
                    Show('beauty_description', None, 'pedicure') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
                    text_style "navigation_button_text"
                textbutton _('Пластическая операция'):
                    xalign 0.99
                    action [
                    SensitiveIf(player.stats.beauty < 100 and player.money > 50000),
                    Jump('beauty_operation')
                    ] hovered [
                    Show('beauty_description', None, 'beauty_operation') # При наведении показывается описание
                    ] unhovered [
                    Hide('beauty_description') # При потере фокуса - скрывается
                    ]
                    text_style "navigation_button_text"

    screen shopBeauty:
        null
    if is_beauty_visited == 0:
        $clrscr()
        $ is_beauty_visited = 1
        jump beauty_intro
    call screen shopBeauty

label loc_sexShop:
    show sexShop at left
    if ptime > 168 and lt() in [-1,-3] and rand(1,3) == 1:
        jump danokova_start
    python:
        loc_btn = [
            ('На улицу', [Function(move, 'loc_shopStreet')], True),
            ('{i}Закупиться{/i}', [Function(clrscr), Show('sexShopping')], True),
            ]
        loc_txt = ['Вы видите перед собой магазин для взрослых. Полки уставлены различными секс-игрушками. Дилдо, вибраторы, резиновые дырки для мальчиков, пони с уникальным седлом для девочек. Отдельная полка для афродизиаков и прочей медицины. Глаза прямо разбегаются от обилия выбора!']
    screen sexShop:
        null
    call screen sexShop
