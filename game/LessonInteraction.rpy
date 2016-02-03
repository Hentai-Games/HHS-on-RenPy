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
    
label loc_lessonAssist:
    player.say 'Давайте я просто помогу вам.'
    interactionObj.say 'Хорошо, с такими учениками лишняя помощь пригодится.'
    hide temp1
    hide temp2
    show expression 'pic/events/lection_help/less_asist_00.jpg' as tempPic
    'Вы рашаете поучаствовать в учебном процессе вашей школы.\nНо в данный момент предпочитаете поработать на репутацию.'
    'Поэтому не выдумывая ничего оригинального просто присоединяетесь к уроку в качестве ассистента.'
    python:
        for x in getLoc(curloc).getPeople():
            x.incRep(5)
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent(curloc)
    $ move(curloc)

label loc_lessonEduFail:
    player.say 'Я думаю знаю как нужно их учить.'
    interactionObj.say 'Чтож давайте посмотрим.'
    hide temp1
    hide temp2
    python:
        for x in getLoc(curloc).getPeople():
            x.incEdu(1)
    $ player.incIntel(3)
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent('loc_lessonEduFail')
    $ move(curloc)

label loc_lessonEduNo:
    player.say 'Обучение детей довольно сложный процесс, но мы с вами ведь умеем справляться.'
    interactionObj.say 'Хорошо, тогда этим и займемся.'
    hide temp1
    hide temp2
    python:
        for x in getLoc(curloc).getPeople():
            x.incEdu(3)
    $ player.incIntel(2)
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent('loc_lessonEduNo')
    $ move(curloc)

label loc_lessonEduOk:
    player.say 'Я недавно изучила новые методики подачи материала, было бы неплохо их продемонстрировать.'
    interactionObj.say 'И неужели там действительно нечто стоящее?'
    hide temp1
    hide temp2
    python:
        for x in getLoc(curloc).getPeople():
            x.incEdu(5)
    $ player.incIntel(1)
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent('loc_lessonEduOk')
    $ move(curloc)

label loc_lessonFun:
    if interactionObj.getLoy() < float(25) :
        interactionObj.say 'Хотя нет!'
        player.say 'Но?'
        interactionObj.say 'Нет! Я по вашему лицу вижу что бы вы там себе не надумали это неприемлемо!'
        'Нда, такую "лояльность" явно нужно исправлять.'
        $ move(curloc)
    player.say 'Надо повышать лояльность учеников, это увеличит привлекательность школы для инвесторов.'
    interactionObj.say 'И какие дайствия вы считаете необходимыми?'
    player.say 'Ну вы же видите что дети скучают, значит нужно их развлечь.'
    hide temp1
    hide temp2
    python:
        for x in getLoc(curloc).getPeople():
            x.incLoy(5)
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent('loc_lessonFun')
    $ move(curloc)

label loc_lessonCorr:
    if interactionObj.getLoy() < float(50) :
        interactionObj.say 'Хотя нет!'
        player.say 'Но?'
        interactionObj.say 'Нет! Я по вашему лицу вижу что бы вы там себе не надумали это неприемлемо!'
        'Нда, такую "лояльность" явно нужно исправлять.'
        $ move(curloc)
    player.say 'У нас ведь отличная школа, а ученики выглядят несколько зажато. Мы должны обеспечить их раскрепощение!'
    interactionObj.say 'Что-то мне кажется это уже слишком...'
    player.say 'Да оставте, как педагоги мы обязаны готовить их ко всем аспектам жизни.'
    interactionObj.say 'Хмм, тогда возможно и я посмотрю что вы придумали'
    hide temp1
    hide temp2
    python:
        for x in getLoc(curloc).getPeople():
            x.incLust(10)
            x.incCorr(1)
    $ player.incLust(15)
    $ player.incCorr(0.5)
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent('loc_lessonCorr')
    $ move(curloc)

label loc_LessonSportGym:
    show expression 'pic/events/lection_help/sport_ok2.jpg' as tempPic # Заменить
    'Вы активно размялись и подняли физическую форму..'
    $ player.incDirty(1)
    $ player.stats.energy -= rand(100,200)
    $ player.stats.health += rand (10,20)
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent(curloc) # Заменить на специальные
    $ move(curloc)

label loc_LessonSportSwim:
    show expression 'pic/events/lection_help/pool_no2.jpg' as tempPic # Заменить
    'Вы неплохо поплавали на занятии и улучшили своё здоровье.'
    $ player.stats.energy -= rand(100,200)
    $ player.stats.health += rand (10,20)
    $ player.cleanAll()
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent(curloc) # Заменить на специальные
    $ move(curloc)
##############################################
# ToDo:
# Перенести эвенты в отдельный файл?
##############################################
label event_loc_lessonFun_0_help1:
    show expression 'pic/events/lection_help/less_fun_00.jpg' as tempPic
    'Что может быть веселее взаимного общения? Именно поэтому вы решаете устроить конкурс поцелуев, где девочки покажут свои умения, а жюри из мальчиков их оценит.'
    $ move(curloc)

label event_loc_lessonCorr_0_help1:
    show expression 'pic/events/lection_help/less_ero_00.jpg' as tempPic
    'Вы устраиваете просветительскую лекцию об взаимоотношениях полов.'
    show expression 'pic/events/lection_help/less_ero_01.jpg' as tempPic
    'А к некоторым ученикам даже применяете наглядную агитацию.'
    $ move(curloc)

label event_loc_lessonEduFail_0_help1:
    show expression 'pic/events/lection_help/fail5.jpg' as tempPic
    'Не смотря на всё ваше самомнение урок не задался. Может ученики попались тупые или материал неадекватный, но скорее вам не позволил выступить собственный интеллект.'
    'Кроме того вероятно о вашем уровне знаний могут пойти не лучшие слухи.'
    $ setRep(5,-1)
    $ move(curloc)

label event_loc_lessonEduNo_0_help1:
    show expression 'pic/events/lection_help/no4.jpg' as tempPic
    'Ну в принципе урок удался. Вы конечно не блистали, но и не выставили себя в неуместном виде..'
    $ move(curloc)

label event_loc_lessonEduOk_0_help1:   
    show expression 'pic/events/lection_help/ok5.jpg' as tempPic
    'Новые методики и отличный подбор материала позволили вам наглядно продемострировать, что место директора вы вполне заслужили.'
    'Ученики также быле впечатлены, а некоторые, вероятно, расскажут об этом и дома.'
    $ setRep(5,1)
    $ move(curloc)
    