init python:
    less_actions = 0

screen less_act:
    fixed:
        vbox:
            xalign 0.99
            null height 10
            text '{u}Учебный процесс:{/u}' style style.param xalign 0.99
            textbutton 'Ассистировать преподавателю':
                xalign 0.99
                action Jump('less_asist')
                style "navigation_button" text_style "action_button_text"
            textbutton 'Провести учебное соревнование':
                xalign 0.99
                action Jump('less_edu')
                style "navigation_button" text_style "action_button_text"
            textbutton 'Провести развлекательное представление':
                xalign 0.99
                action Jump('less_fun')
                style "navigation_button" text_style "action_button_text"
            textbutton 'Организовать эротический конкурс':
                xalign 0.99
                action Jump('less_ero')
                style "navigation_button" text_style "action_button_text"
    
label less_asist:
    $ clrscr()
    if less_actions == lt():
        player.say 'я уже достаточно поработала на текущем уроке.'
        $ move(curloc)
    $ t = []
    $ t = [e for e in getLoc(curloc).getPeople() if e.getLocationStatus().name == 'Преподаёт']
    if len(t) == 0 :
        player.say 'Что-то тут никго нет.\nВидимо они ушли в другой класс.'
        $ move(curloc)
    show expression 'pic/events/lection_help/less_asist_00.jpg' as tempPic
    'Вы рашаете поучаствовать в учебном процессе вашей школы.\nНо в данный момент предпочитаете поработать на репутацию.'
    'Поэтому не выдумывая ничего оригинального просто присоединяетесь к уроку в качестве ассистента.'
    python:
        for x in getLoc(curloc).getPeople():
            x.incRep(5)
    $ less_actions = lt()
    $ changetime(15)
    $ move(curloc)

label less_edu:
    $ clrscr()
    if less_actions == lt():
        player.say 'я уже достаточно поработала на текущем уроке.'
        $ move(curloc)
    $ t = []
    $ t = [e for e in getLoc(curloc).getPeople() if e.getLocationStatus().name == 'Преподаёт']
    if len(t) == 0 :
        player.say 'Что-то тут никго нет.\nВидимо они ушли в другой класс.'
        $ move(curloc)
    show expression 'pic/events/lection_help/less_edu_00.jpg' as tempPic
    'Учёба тут поставленна явно на уровне. А вот на каком именно уровне всё поставленно и насколько его можно поднять вы и решили выяснить.'
    python:
        for x in getLoc(curloc).getPeople():
            x.incEdu(2)
    $ less_actions = lt()
    $ changetime(15)
    $ move(curloc)

label less_fun:
    $ clrscr()
    if less_actions == lt():
        player.say 'я уже достаточно поработала на текущем уроке.'
        $ move(curloc)
    $ t = []
    $ t = [e for e in getLoc(curloc).getPeople() if e.getLocationStatus().name == 'Преподаёт']
    if len(t) == 0 :
        player.say 'Что-то тут никго нет.\nВидимо они ушли в другой класс.'
        $ move(curloc)
    if t[0].getLoy() < float(25) :
        show expression getCharImage(t[0],'dialog') as char1
        t[0].say 'Нет!'
        show expression getCharImage(player,'dialog') as char2
        player.say 'Но?'
        t[0].say 'Нет! Что бы вы там себе не надумали!'
        player.say 'Нда, такую "лояльность" явно нужно исправлять.'
        $ move(curloc)
    show expression 'pic/events/lection_help/less_fun_00.jpg' as tempPic
    'Ученики явно скучают, а в вашей школе это не годится ни в коем виде. Именно по этой причине вы решаете устроить на уроке вместо скучного занятия более веселое представление.'
    python:
        for x in getLoc(curloc).getPeople():
            x.incLoy(5)
    $ less_actions = lt()
    $ changetime(15)      
    $ move(curloc)

label less_ero:
    $ clrscr()
    if less_actions == lt():
        player.say 'я уже достаточно поработала на текущем уроке.'
        $ move(curloc)
    $ t = []
    $ t = [e for e in getLoc(curloc).getPeople() if e.getLocationStatus().name == 'Преподаёт']
    if len(t) == 0 :
        player.say 'Что-то тут никго нет.\nВидимо они ушли в другой класс.'
        $ move(curloc)
    if t[0].getLoy() < float(50) :
        show expression getCharImage(t[0],'dialog') as char1
        t[0].say 'Нет!'
        show expression getCharImage(player,'dialog') as char2
        player.say 'Но?'
        t[0].say 'Нет! Что бы вы там себе не надумали!'
        player.say 'Нда, такую "лояльность" явно нужно исправлять.'
        $ move(curloc)
    show expression 'pic/events/lection_help/less_ero_00.jpg' as tempPic
    'В данный раз вы предпочли устроить в классе эротический конкурс.'
    show expression 'pic/events/lection_help/less_ero_01.jpg' as tempPic
    'И даже предоставили некоторый приз победителю.'
    python:
        for x in getLoc(curloc).getPeople():
            x.incLust(10)
            x.incCorr(1)
    $ player.incLust(15)
    $ player.incCorr(0.5)
    $ less_actions = lt()
    $ changetime(15)
    $ move(curloc)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    