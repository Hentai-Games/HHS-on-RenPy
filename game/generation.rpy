
init -10 python:
    config.use_cpickle = True
    dynpicto = ''

init -2 python:
    #############################################################
    #Создание студентов
    #############################################################
    #объявление массивов
    picto_m = []
    picto_f = []
    _studs = []

    #будущий массив студентов
    _allStuds = []
    _allChars = []
    _teachers = []

    # Загружаем все имеющиеся картинки
    import os
    for path in config.searchpath:
        # Ищем каталоги с картинками во всех возможных RenPy каталогах ресурсов
        try:
            for x in os.listdir(os.path.join(path, 'pic/events/students/picto/male/')):
                picto_m.append(os.path.join('pic/events/students/picto/male/', x))

            for x in os.listdir(os.path.join(path, 'pic/events/students/picto/female/')):
                picto_f.append(os.path.join('pic/events/students/picto/female/', x))

        except OSError:
            pass

    def generate_students_number(students_number, classes_number):
        """Генерирует количество мальчиков, девочек и фут"""
        futas = rand(classes_number, round(students_number*0.1)+3)
        girls = rand(round(students_number*0.45), round(students_number*0.55))
        boys = students_number-futas-girls

        return futas, boys, girls

    def print_students_statistics(futas, boys, girls):
        print 'Total:', futas + boys + girls
        print 'Futa:', futas
        print 'Boys:', boys
        print 'Girls:', girls

    def eat_picto(picto_list):
        """Выбирает случайную картинку из списка и удаляет ее"""
        picto = choice(picto_list)
        picto_list.remove(picto)

        return picto

    def generate_students(students_number, classes_number):
        """Генерирует объекты учеников согласно заданному количеству"""

        # Количество учеников
        futas, boys, girls = generate_students_number(students_number,
                                                      classes_number)
        print_students_statistics(futas, boys, girls)

        # Списки с учениками
        futas_l = [Char.random('futa', eat_picto(picto_f))\
                   for x in xrange(futas)]
        boys_l = [Char.random('male', eat_picto(picto_m))\
                  for x in xrange(boys)]
        girls_l = [Char.random('female', eat_picto(picto_f))\
                   for x in xrange(girls)]

        all_students = futas_l + boys_l + girls_l

        # Распределение по классам
        # Как минимум по одной футе в класс
        for i in xrange(classes_number):
            futas_l[i].inClass = i+1
        
        # Если фут больше пяти - в случайные классы
        for x in futas_l[classes_number:]:
            x.inClass = choice(range(1, classes_number+1))

        # Минимум по два мальчика и девочки в классе
        for i in xrange(1, classes_number+1):
            boys_l.pop(rand(0, len(boys_l)-1)).inClass = i
            boys_l.pop(rand(0, len(boys_l)-1)).inClass = i
            girls_l.pop(rand(0, len(boys_l)-1)).inClass = i
            girls_l.pop(rand(0, len(boys_l)-1)).inClass = i

        # Пул учеников
        students_pool = boys_l + girls_l

        # Количество учеников в классах должно быть одинаковым
        students_in_class = int(students_number / classes_number)
        for class_n in xrange(1, classes_number+1):
            in_class = len([x for x in all_students if x.inClass==class_n])
            for i in xrange(students_in_class - in_class):
                s = students_pool.pop(rand(0, len(students_pool)-1))
                s.inClass=class_n

        # На случай, если количество учеников не делится на количество
        # классов поровну
        for x in students_pool:
            x.inClass = rand(1, classes_number)

        # Debug информация
        # for i in xrange(1, classes_number+1):
            # s = [x for x in all_students if x.inClass==i]
            # print 'Class: {}, total: {}'.format(i, len(s))
            # for x in s:
                # print '\t{}'.format(x)

        return all_students

    def set_students_intelligence(students):
        """Выставляет интелект ученикам

        С вероятностью 10% он может быть меньше 20 или больше 80.
        Иначе от 30 до 70.
        """
        for x in students:
            r = rand(1, 10)
            if r == 1:
                x.stats.intelligence = randf(80, 100)

            elif r == 2:
                x.stats.intelligence = randf(1, 20)

            else:
                x.stats.intelligence = randf(30, 70)

    def set_students_will(students):
        """Выставляет волю ученикам

        С вероятностью 10% она может быть меньше 20 или больше 80.
        Иначе от 30 до 70.
        """
        for x in students:
            r = rand(1, 10)
            if r == 1:
                x.stats.will = randf(80, 100)

            elif r == 2:
                x.stats.will = randf(1, 20)

            else:
                x.stats.will = randf(30, 70)

    def print_debug_will_and_int(students):
        """debug информация о выставленных воле и интеллекте"""
        int_rez = {'<20': 0, '>80': 0, '30-70': 0}
        will_rez = {'<20': 0, '>80': 0, '30-70': 0}
        for s in students:
            intel = s.getIntel()
            if 30 <= intel <= 70:
                int_rez['30-70'] += 1
            elif intel <= 20:
                int_rez['<20'] += 1
            else:
                int_rez['>80'] += 1

            will = s.getWill()
            if 30 <= will <= 70:
                will_rez['30-70'] += 1
            elif will <= 20:
                will_rez['<20'] += 1
            else:
                will_rez['>80'] += 1
            
        total_s = float(len(students))
        print 'Intelligence:'
        print '\t<20: {} ({}%)'.format(int_rez['<20'], int_rez['<20']/total_s*100)
        print '\t>80: {} ({}%)'.format(int_rez['>80'], int_rez['>80']/total_s*100)
        print '\t30-70: {} ({}%)'.format(int_rez['30-70'], int_rez['30-70']/total_s*100)

        print 'Will:'
        print '\t<20: {} ({}%)'.format(will_rez['<20'], will_rez['<20']/total_s*100)
        print '\t>80: {} ({}%)'.format(will_rez['>80'], will_rez['>80']/total_s*100)
        print '\t30-70: {} ({}%)'.format(will_rez['30-70'], will_rez['30-70']/total_s*100)
#####################################################
# codeBlc Генерация директора 
#####################################################

init -1 python:
    _fname = 'Имя'
    _lname = 'Фамилия'
    _age = 25
    _beauty = 20
    _health = 700
    _anus = randf(0,5)
    _vagina = randf(0,10)
    _corr = 0
    _intel = 50
    _money = 5000
    _bsize = 2
    _picture = "pic/Hero/2.png"
    history = 0
    answer = [0,0,0,0,0]


label gendir:
    show white
    show expression 'pic/new.jpg' at Position(xpos = 0.6, xanchor=0.5, ypos=0.6, yanchor=0.5)
    menu:
        'Имя: [_fname]':
            $ _fname = renpy.input("Введите имя, и нажмите Enter для продолжения", default= _fname, exclude='{1234567890}')
            jump gendir
        'Отчество: [_lname]':
            $ _lname = renpy.input("Введите отчество, и нажмите Enter для продолжения", default= _lname, exclude='{1234567890}')
            jump gendir
        "Выбрать историю" if _fname != '' and _lname != '':
            jump history
        "Закончить" if answer == [1,1,1,1,1]:
            jump skipall

label history:
    menu:
        "Младенчество" if answer[0] == 0:
            $ answer[0] = 1
            menu:
                'Вы родились красивой девочкой\n+Красота -Интеллект':
                    $ _beauty += 20
                    $ _intel -= 5
                    jump history
                'Вы смогли вставать на ножки уже в 3-х месячном возрасте\n+Здоровье':
                    $ _health += 150
                    jump history
                'Вы обожали сосать сиську, даже когда не были голодны\n+Развратность +Грудь +Дырочки --Интеллект':
                    $ _corr += 15
                    $ _anus += 5
                    $ _vagina += 5
                    $ _intel -= 10
                    $ _bsize += 1
                    jump history
                'Вы смогли осмысленно говорить уже в пол года\n ++Интеллект':
                    $ _intel += 10
                    jump history
                'Вы обожали яркие и блестящие предметы.\n +Деньги':
                    $ _money += 5000
                    jump history
        "Детство" if answer[1] == 0:
            $ answer[1] = 1
            menu:
                'Вы любили смотреть, как красится ваша мама\n+Красота -Интеллект':
                    $ _beauty += 20
                    $ _intel -= 5
                    jump history
                'Вы были очень активным ребёнком\n+Здоровье':
                    $ _health += 150
                    jump history
                'Вы показывали свою письку мальчишкам в детском саду\n+Развратность +Дырочки --Интеллект':
                    $ _corr += 15
                    $ _anus += 5
                    $ _vagina += 5
                    $ _intel -= 10
                    jump history
                'Вы рано научились читать\n ++Интеллект':
                    $ _intel += 10
                    jump history
                'Вы откладывали деньги, которые Вам давали на сладости.\n +Деньги':
                    $ _money += 5000
                    jump history
        "Школа" if answer[2] == 0:
            $answer[2] = 1
            menu:
                'В школе Вы старались выглядеть лучше своих подруг\n+Красота -Интеллект':
                    $ _beauty += 20
                    $ _intel -= 5
                    jump history
                'Вашим любимым предметом была физкультура\n+Здоровье':
                    $ _health += 150
                    jump history
                'Вы любили мастурбировать на занятиях\n+Развратность +Дырочки --Интеллект':
                    $ _corr += 15
                    $ _anus += 5
                    $ _vagina += 5
                    $ _bsize += 1
                    $ _intel -= 10
                    jump history
                'Вы принимали участие в олимпиадах, и даже занимали там призовые места\n ++Интеллект':
                    $ _intel += 10
                    jump history
                'Вы экономили на обедах, чтобы купить себе что-нибудь дорогое\n +Деньги':
                    $ _money += 5000
                    jump history
        "Университет" if answer[3] == 0:
            $answer[3] = 1
            menu:
                ' Вы всегда старались быть накрашенной и ухоженной\n+Красота -Интеллект':
                    $ _beauty += 20
                    $ _intel -= 5
                    jump history
                'Вы участвовали во всех спартакиадах, и даже занимали там призовые места\n+Здоровье':
                    $ _health += 150
                    jump history
                'Вы с лёгкостью меняли сексуальных партнёров\n+Развратность +Дырочки --Интеллект':
                    $ _corr += 15
                    $ _anus += 5
                    $ _vagina += 5
                    $ _intel -= 10
                    jump history
                'Вы любили естественные науки, и всегда получали по ним хорошие оценки\n ++Интеллект':
                    $ _intel += 10
                    jump history
                'Вы давали деньги в рост одноклассникам. И Вам их даже возвращали с процентами\n +Деньги':
                    $ _money += 5000
                    jump history
        "Работа" if answer[4] == 0:
            $answer[4] = 1
            menu:
                'Вы тщательно следите за собой, и регулярно посещаете парикмахерские и салоны красоты\n+Красота -Интеллект':
                    $ _beauty += 20
                    $ _intel -= 5
                    jump history
                'Вы бегаете утром, и следите за своим здоровьем\n+Здоровье':
                    $ _health += 150
                    jump history
                'Вы использовали своё тело для продвижения по карьерной лестнице\n+Развратность +Дырочки +Грудь --Интеллект':
                    $ _corr += 15
                    $ _anus += 5
                    $ _vagina += 5
                    $ _bsize += 1
                    $ _intel -= 10
                    jump history
                'Вы регулярно повышаете свой уровень образования\n ++Интеллект':
                    $ _intel += 10
                    jump history
                'Вы любите деньги, а они любят вас\n +Деньги':
                    $ _money += 5000
                    jump history
        "Назад":
            jump gendir
        "Сбросить историю":
            $ answer = [0,0,0,0,0]
            jump history
# endBlc
label selchar:
    # show white
    # call screen char_select
    $ _picture = 'pic/Hero/2.png'
    jump gendir

label skipall:
    python:
#####################################################
#Создание директора
#####################################################
        playerBody = FemaleBody(175)
        playerBody.parts['грудь'].size = _bsize
        playerBody.parts['анус'].size = _anus
        playerBody.parts['вагина'].size = _vagina

        playerStats = Stats(
            corr = _corr,
            lust = _corr / 10,
            education  = _intel / 2,
            intelligence = _intel,
            health = _health,
            energy = _health,
            beauty = _beauty,
            fun = 50
        )

        player = Char(
            fname = _fname,
            lname = _lname,
            age = _age,
            body = playerBody,
            stats = playerStats,
            color = '#5A20F7',
            inventory = [],
            wear = [],
            club = '',
            picto = _picture,
            location = curloc,
            money = _money
        )
        player.addItems('Салфетка', 'Сырая еда', jaket.name, longSkirt.name, browntights.name, simpleUnderwear.name, pantalons.name, oldShirt.name)
        
        player.initSet(0,[jaket.name, longSkirt.name, browntights.name, simpleUnderwear.name])
        player.initSet(1,[pantalons.name, oldShirt.name])
        player.applySet(0)
        player.say = Character (player.fullName(), kind=adv, dynamic = False, color = player.color, show_side_image = Image(im.FactorScale(player.picto,.6, xalign=0.01, yalign= 2.0)), window_left_padding = 170)
        
#####################################################
#Генерация и создание студентов
#####################################################

        # Rules:
        # мальчиков должно быть 40%, фут - 10%, но минимум по 1 в каждый
        #     класс, девочек - 50%.
        # В каждом классе распределение мальчиков и девочек должно быть
        #     равномерно. Т.е. не должно быть только мальчиковых или только
        #     девочковых классов.
        # Интеллект - с вероятностью 10% он может быть меньше 20 или больше
        #     80. Иначе от 30 до 70.
        # То же самое с волей. волевых и безвольных - мало. Остальные 
        #     болтаются посередине.
        # Мальчиков не может быть больше 30, девочек - 40. Больше нету
        #     пиктограмм. Дублировать пиктограммы не надо.
        # Количество людей в классах должно быть одинаковым
        # Равномерного распределения не надо, но минимум по 2 человека 
        #     разного пола должны быть в одном классе.
        # Генерируем учеников, 50 человек, 5 классов
        
        _studs = generate_students(students, 5)
        set_students_intelligence(_studs)
        set_students_will(_studs)
        print_debug_will_and_int(_studs)

        for x in _studs:
            tempSex = x.getSex()
            if x.getSex() == 'futa':
                tempSex = 'female'
            for y in clothing:
                if y.sex == tempSex and y.char == 'stud':
                    x.addItem(y)


#######################################################
# codeBlc Создание учителей
#######################################################

        kupruvna = Char(
            fname = 'Валентина',
            lname = 'Купрувна',
            age = 37,
            body = FemaleBody(
                175,
                breastSize = 5,
                vaginaSize = 8
            ),
            stats = Stats(
                will = 25,
                education = 60,
                intelligence = 50,
                beauty = 40,
                health = 1000,
                energy = 1000,
                loyalty = randf(10, 20),
                fun = randf(0, 50)
            ),
            color = '#FF85F1',
            inventory = [],
            wear = [],
            club = 'химия',
            picto = 'pic/teachers/kupruvna_picto.png',
            location = curloc,
            money = 10000
        )
        _teachers.append(kupruvna)

        danokova = Char(
            fname = 'Полина',
            lname = 'Данокова',
            age = 25,
            body = FemaleBody(
                160,
                breastSize = 2,
                vaginaSize = 5
            ),
            stats = Stats(
                will = 45,
                education = 20,
                intelligence = 100,
                beauty = 60,
                health = 1000,
                energy = 1000,
                loyalty = randf(10, 20),
                fun = randf(0, 50)
            ),
            color = '#FF85F1',
            inventory = [],
            wear = [],
            club = 'биология',
            picto = 'pic/teachers/danokova_picto.png',
            location = curloc,
            money = 5000
        )
        _teachers.append(danokova)

        frigidovna = Char(
            fname = 'Ангелина',
            lname = 'Фригидовна',
            age = 32,
            body = FemaleBody(
                175,
                breastSize = 6
            ),
            stats = Stats(
                will = 30,
                education = 15,
                intelligence = 40,
                beauty = 40,
                health = 1000,
                energy = 1000,
                loyalty = randf(10, 20),
                fun = randf(0, 50)
            ),
            color = '#FF85F1',
            inventory = [],
            wear = [],
            club = 'сексуальное просвящение',
            picto = 'pic/teachers/frigidovna_picto.png',
            location = curloc,
            money = 5000
        )
        _teachers.append(frigidovna)

        bissektrisovna = Char(
            fname = 'Валентина',
            lname = 'Биссектрисовна',
            age = 35,
            body = FemaleBody(
                165,
                breastSize = 3,
                vaginaSize = 8
            ),
            stats = Stats(
                will = 60,
                education = 60,
                intelligence = 40,
                beauty = 85,
                health = 1000,
                energy = 1000,
                loyalty = randf(10, 20),
                fun = randf(0, 50)
            ),
            color = '#FF85F1',
            inventory = [],
            wear = [],
            club = 'математика',
            picto = 'pic/teachers/bissektrisovna_picto.png',
            location = curloc,
            money = 5000
        )
        _teachers.append(bissektrisovna)

        dikovna = Char(
            fname = 'Анжела',
            lname = 'Диковна',
            age = 23,
            body = FutaBody(
                180,
                breastSize = 5,
                vaginaSize = 8,
                anusSize = 4,
                penisSize = 20
            ),
            stats = Stats(
                corr = 20,
                will = 30,
                education = 50,
                intelligence = 50,
                beauty = 60,
                health = 1000,
                energy = 1000,
                loyalty = randf(10, 20),
                fun = randf(0, 50)
            ),
            color = '#FC3A3A',
            inventory = [],
            wear = [],
            club = 'английский язык',
            picto = 'pic/teachers/dikovna_picto.png',
            location = curloc,
            money = 5000
        )
        _teachers.append(dikovna)

        mustangovich = Char(
            fname = 'Ахмед',
            lname = 'Мустангович',
            age = 30,
            body = MaleBody(
                190,
                penisSize = 30
            ),
            stats = Stats(
                will = 15,
                education = 30,
                intelligence = 40,
                beauty = 40,
                health = 1500,
                energy = 1500,
                loyalty = randf(40, 60),
                fun = randf(0, 50)
            ),
            color = '#269AFF',
            inventory = [],
            wear = [],
            club = 'физкультура',
            picto = 'pic/teachers/mustangovich_picto.png',
            location = curloc,
            money = 200
        )
        _teachers.append(mustangovich)
        
        dante = Char(
            fname = 'Ева',
            lname = 'Данте',
            age = 35,
            body = FemaleBody(
                120,
                breastSize = 0.5,
                vaginaSize = 2
            ),
            stats = Stats(
                will = 80,
                education = 60,
                intelligence = 60,
                beauty = 85,
                health = 1000,
                energy = 1000,
                loyalty = randf(0, 10),
                fun = randf(0, 50)
            ),
            color = '#FF85F1',
            inventory = [],
            wear = [],
            club = 'литература',
            picto = 'pic/teachers/dante_picto.png',
            location = curloc,
            money = 5000
        )
                
        gonoreevna = Char(
            fname = 'Венера',
            lname = 'Гонореевна',
            age = 21,
            body = FemaleBody(
                180,
                breastSize = 4,
                vaginaSize = 16
            ),
            stats = Stats(
                will = 20,
                education = 30,
                intelligence = 20,
                beauty = 90,
                health = 1000,
                energy = 1000,
                loyalty = randf(20, 30),
                fun = randf(0, 50)
            ),
            color = '#FF85F1',
            inventory = [],
            wear = [],
            club = 'медицина',
            picto = 'pic/teachers/gonoreevna_picto.png',
            location = curloc,
            money = 5000
        )
        

        for char in _teachers:
            tempSex = char.getSex()
            if tempSex == 'futa':
                tempSex = 'female'
            for cloth in clothing:
                if cloth.sex == tempSex and cloth.char == 'teacher':
                    char.addItem(cloth)
                    
# endBlc
#######################################################
#Пересохранение этого добра для того, чтобы сохранялось.
#######################################################
    $ _allChars.extend(_studs)
    $ _allChars.extend(_teachers)
    $ school = School()
    $ allChars = _allChars
    $ studs = _studs
    $ teachers = _teachers
    $ school.getBudget()
    $ hourlyReset()
    $ move('myintro')
