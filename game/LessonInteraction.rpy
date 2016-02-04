init python:
    less_actions = 0

# screen less_act:
    # fixed:
        # vbox:
            # xalign 0.99
            # null height 10
            # text '{u}Учебный процесс:{/u}' style style.param xalign 0.99
            # textbutton 'Ассистировать преподавателю':
                # xalign 0.99
                # action Jump('loc_lessonAssist')
                # style "navigation_button" text_style "action_button_text"
            # textbutton 'Провести учебное соревнование':
                # xalign 0.99
                # action Jump('less_edu')
                # style "navigation_button" text_style "action_button_text"
            # textbutton 'Провести развлекательное представление':
                # xalign 0.99
                # action Jump('less_fun')
                # style "navigation_button" text_style "action_button_text"
            # textbutton 'Организовать эротический конкурс':
                # xalign 0.99
                # action Jump('less_ero')
                # style "navigation_button" text_style "action_button_text"
    
label loc_lessonAssist:
    player.say 'Давайте я просто помогу вам.'
    interactionObj.say 'Хорошо, с такими учениками лишняя помощь не помешает.'
    hide temp1
    hide temp2
    show expression 'pic/events/lection_help/less_asist_00.jpg' as tempPic
    'Вы решаете поучаствовать в учебном процессе вашей школы.\nНо в данный момент предпочитаете поработать на репутацию.'
    'Поэтому не выдумывая ничего оригинального просто присоединяетесь к уроку в качестве ассистента.'
    python:
        for x in getLoc(curloc).getPeople():
            x.incRep(1)
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent(curloc)
    $ move(curloc)

label loc_lessonEduFail:
    player.say 'Я думаю знаю как нужно их учить.'
    interactionObj.say 'Ну что же. Давайте посмотрим на это.'
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
    player.say 'Обучение детей довольно сложный процесс, я думаю, что смогу помочь вам в этом.'
    interactionObj.say 'Не откажусь от вашей помощи.'
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
    interactionObj.say 'Х-м-м. Неужели там действительно нечто стоящее?'
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
        player.say '"Нда, такую "лояльность" явно нужно исправлять."'
        $ move(curloc)
    player.say 'Надо повышать лояльность учеников, это увеличит привлекательность школы для инвесторов.'
    interactionObj.say 'И какие действия вы считаете необходимыми?'
    player.say 'Ну вы же видите что дети скучают, значит нам нужно их развлечь!'
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
    if interactionObj.getCorr() < float(40):
        interactionObj.say 'Хотя нет!'
        player.say 'Но?'
        interactionObj.say 'Нет! Я по вашему лицу вижу что бы вы там себе не надумали это неприемлемо!'
        player.say '"Нда, да ей бы и самой "просвещение" не помешает. Ну или хотя бы немного раскрепостить."'
        $ move(curloc)
    player.say 'У нас ведь отличная школа, а ученики выглядят несколько зажато. Мы должны обеспечить их раскрепощение!'
    interactionObj.say 'Что-то мне кажется это уже слишком...'
    player.say 'Да оставьте! Мы, как педагоги, просто обязаны готовить их ко всем аспектам жизни!'
    interactionObj.say 'Хмм, тогда возможно и я посмотрю что вы придумали...'
    hide temp1
    hide temp2
    python:
        for x in getLoc(curloc).getPeople():
            x.incLust(20)
            x.incCorr(1)
    $ player.incLust(15)
    $ player.incCorr(0.5)
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent('loc_lessonCorr')
    $ move(curloc)

label loc_LessonSportGym:
    show expression 'pic/events/lection_help/SportGym_00.jpg' as tempPic at top
    'Вы активно размялись и подняли физическую форму.'
    $ player.incDirty(1)
    $ player.stats.energy -= rand(100,200)
    $ player.stats.health += rand (10,20)
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent('loc_LessonSportGym')
    $ move(curloc)

label loc_LessonSportSwim:
    show expression 'pic/events/lection_help/SportSwim_00.jpg' as tempPic at top
    'Вы неплохо поплавали на занятии и улучшили своё здоровье.'
    $ player.stats.energy -= rand(100,200)
    $ player.stats.health += rand (10,20)
    $ player.cleanAll()
    $ less_actions = lt()
    $ changetime(15)
    $ interactionObj = ''
    $ tryEvent('loc_LessonSportSwim')
    $ move(curloc)
