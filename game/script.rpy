init -3 python:
    development = 1
    i = 500
    curloc = 'loc_home'
    students = 50
    last_eat = 0
    stat_loy = 0
    stat_fun = 0
    stat_lust = 0
    stat_corr = 0
    stat_edu = 0
    stat_rep = 0
    stat_penergy = 0
    stat_plust = 0
    
    lastWork = -30
    lastWashed = 0
    is_moneta = 0
    inhibLow = 0
    inhibLowTime = 0
    is_beach_event = 0
    is_glory_found = 0
    mile_qwest_2_stage = 0
    is_beauty_visited = 0
    reputation_intro = []
    
    is_cosplayClub = 0
    is_cherleaderClub = 0
    is_pantiesClub = 0
    
    
    
    him_zavivka = 0
    depilation = 0
    skin_care = 0
    manicure = 0
    pedicure = 0
    show_peopleTextList = 0
    
    detentions = []
    scoldWho = []

init 10 python:
    teacher_son = dummy
    callup = dummy
    
init:
    image white = "#FFFFFF"
    
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
                renpy.say('CREATOR','WRONG LOCATION! ADD TO LOCATIONS LIST! LABEL = [x.id]')
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
    