init -3 python:
    development = 1 #Режим разработчика
    
    i = 500
    curloc = 'loc_home' # Инициализация curloc
    students = 50 # количество студентов
    last_eat = 0 # Инициализация времени с последнего обеда
    stat_loy = 0 # Инициализация переменных интерфейса
    stat_fun = 0
    stat_lust = 0
    stat_corr = 0
    stat_edu = 0
    stat_rep = 0
    stat_penergy = 0
    stat_plust = 0
    
    lastWork = -30 # Инициализация времени последней работы
    lastWashed = 0 # Инициализация душа
    lastMastur = 0 # Инициализация мастурбации
    is_moneta = 0 # Инициализация объяснения валюты
    inhibLow = 0 # Инициализация послешкольных эвентов увеличения разврата
    inhibLowTime = 0 # Время с последнего разврата
    is_beach_event = 0 # Инициализация триггера эвента дырки в душе
    is_glory_found = 0 # Инициализация триггера глорихола
    mile_quest_1 = 0 # Статус квеста физрука
    mile_qwest_2_stage = 0 # Статус квеста купрувны
    is_beauty_visited = 0 # Триггер первого посещения салона красоты
    timeGetPanties = 0 # Время последнего получения трусов
    
    is_cosplayClub = 0 # триггер эвента косплей клуба
    is_cherleaderClub = 0 # Триггер эвента клуба чирлидеров
    is_pantiesClub = 0 # Триггер эвента секретного клуба
    
    
    him_zavivka = 0 # инициализация переменных салона красоты
    depilation = 0
    skin_care = 0
    manicure = 0
    pedicure = 0
    show_peopleTextList = 0
    
    defaultSymbol = 'O' # херня для перехода по локациям дома.
    temp1 = defaultSymbol
    temp2 = defaultSymbol
    temp3 = defaultSymbol
    temp4 = defaultSymbol
    temp5 = defaultSymbol
    temp6 = defaultSymbol
    
    reputation_intro = [] # Интро эвента для поднятия репутации
    showed = [] # Стак предметов в отображении
    detentions = [] # Лист провинившихся
    scoldWho = [] # Лист тех, кого будем наказывать в эвенте
    highlightP = [] # лист подсвечивающихся на локации

init 10 python:
    teacher_son = dummy
    callup = dummy
    
init:
    image white = "#FFFFFF"
    
    # Прочие персонажи
    
    define med = Character("Медсестра", who_color="#c8ffc8", show_side_image = Image(im.FactorScale('pic/locations/shopBeauty/2.png',0.6, xalign=0.01, yalign= 1.2)), window_left_padding = 170)
    
    define me = Character("Разработчик", who_color="#0553FA", show_side_image = im.Scale("pic/Hero/me/me_norm.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    define meSad = Character("Разработчик", who_color="#0553FA", show_side_image = im.Scale("pic/Hero/me/me_sad.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    define meSceptic = Character("Разработчик", who_color="#0553FA", show_side_image = im.Scale("pic/Hero/me/me_sceptic.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    define meAngry = Character("Разработчик", who_color="#0553FA", show_side_image = im.Scale("pic/Hero/me/me_angry.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    
label start:
    show white
    python:
        for x in locations:
            if x.name == 'UNKNOWN':
                renpy.say('CREATOR','WRONG LOCATION! ADD TO LOCATIONS LIST! LABEL = [x.id]. LOOK IN locations.rpy AT TOP!')
    menu:
        'selchar':
            jump selchar
        'skipall':
            jump skipall
    return


label after_load:
    $ _allChars = allChars
    $ _studs = studs
    $ studs = []
    $ allChars = []
    $ allChars = _allChars
    $ studs = _studs
    return
    
#Useful arts:
#yamada_(gotyui)
#motoi_hiroumi
#speh
#tama (monster1553)
#mishima_toshihiro
#happoubi_jin