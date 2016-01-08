init -3 python: 
    development = 1 #Режим разработчика
    
    i = 500
    curloc = 'loc_home' # Инициализация curloc
    students = 50 # количество студентов
    last_eat = 0 # Инициализация времени с последнего обеда
    last_inventory = 'inventory_all'
    noEventTime = 0 # Время без эвентов
    
    stat_loy = 0 # Инициализация переменных интерфейса
    stat_fun = 0
    stat_lust = 0
    stat_corr = 0
    stat_edu = 0
    stat_rep = 0
    stat_penergy = 0
    stat_plust = 0
    
    temperature = 25 # Температура в офисе
    flagIncome = 0 # флаг получки
    lastWork = -30 # Инициализация времени последней работы
    lastWashed = 0 # Инициализация душа
    lastMastur = 0 # Инициализация мастурбации
    is_moneta = 0 # Инициализация объяснения валюты
    camSold = -30 # Инициализация камеры в туалете
    inhibLow = 0 # Инициализация послешкольных эвентов увеличения разврата
    inhibLowTime = 0 # Время с последнего разврата
    is_beach_event = 0 # Инициализация триггера эвента дырки в душе
    is_glory_found = 0 # Инициализация триггера глорихола
    mile_quest_1 = 0 # Статус квеста физрука
    is_beauty_visited = 0 # Триггер первого посещения салона красоты
    timeGetPanties = 0 # Время последнего получения трусов
    
    mile_qwest_2_stage = 0 # Статус квеста Купрувны    
    is_cabbage = 0 # Триггер квеста капусты
    mile_qwest_2_Ahmed = 0 # триггер нахождения беседки
    mile_qwest_3_stage = 0 # Статус квеста Даноковой
    work51 = 0 # Последний рабочий час Даноковой
    
    is_cosplayClub = 0 # триггер эвента косплей клуба
    is_cherleaderClub = 0 # Триггер эвента клуба чирлидеров
    is_pantiesClub = 0 # Триггер эвента секретного клуба
    
    
    him_zavivka = 0 # инициализация переменных салона красоты
    depilation = 0
    skin_care = 0
    manicure = 0
    pedicure = 0
    show_peopleTextList = 0
    
    reputation_intro = [] # Интро эвента для поднятия репутации
    showed = [] # Стак предметов в отображении инвентаря
    detentions = [] # Лист провинившихся
    scoldWho = [] # Лист тех, кого будем наказывать в эвенте
    highlightP = [] # лист подсвечивающихся на локации
    aphroUsedArr = [] #лист тех, на ком юзался афродизиак
    teacher_intro = [] #лист просмотренных интро

init 10 python:
    teacher_son = dummy
    callup = dummy
    
init:
    image white = "#FFFFFF"
    
    # Прочие персонажи
    
    define med = Character("Медсестра", who_color="#c8ffc8", show_side_image = Image(im.FactorScale('pic/locations/shopBeauty/2.png',0.6, xalign=0.01, yalign= 1.2)), window_left_padding = 170)
    
    define seller = Character("Продавец", who_color="#0553FA", show_side_image = im.Scale("pic/otherChars/seller_picto.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    
    define secretary = Character("Александр", who_color="#0553FA", show_side_image = im.Scale("pic/otherChars/secretary_picto.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    
    define farmer = Character("Сидор Тяпкович", who_color="#0553FA", show_side_image = im.Scale("pic/otherChars/farmer_picto.jpg",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    
    define female = Character("Женщина", who_color="#c8ffc8")
    
    define minister = Character("Григорий Совдепович", who_color="#0553FA", show_side_image = im.Scale("pic/otherChars/minister_picto.jpg",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    
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
    jump warning
    return


label after_load:
    $ _allChars = allChars
    $ _studs = studs
    $ studs = []
    $ allChars = []
    $ allChars = _allChars
    $ studs = _studs
    $ temp_furniture = school.furniture
    $ school.furniture = []
    $ school.furniture = temp_furniture
    return
    
#Useful arts:
#yamada_(gotyui)
#motoi_hiroumi
#speh
#tama (monster1553)
#mishima_toshihiro
#happoubi_jin
