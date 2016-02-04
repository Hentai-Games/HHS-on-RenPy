############################################################################################
# loc_lessonAssist
# - вызываются стандартные эвенты класса.
############################################################################################
############################################################################################
# loc_lessonEduFail
# - round(player.getIntel(),1)*2 < 60
############################################################################################
label event_loc_lessonEduFail_0_help1:
    show expression 'pic/events/lection_help/fail5.jpg' at top as tempPic
    'Не смотря на всё ваше самомнение, урок не задался. Может ученики попались тупые или материал неадекватный, но скорее вам помешала собственная подготовка.'
    'Кроме того вероятно о вашем уровне знаний могут пойти не лучшие слухи.'
    $ setRep(10,-1)
    $ move(curloc)

############################################################################################
# loc_lessonEduNo
# - round(player.getIntel(),1)*2 < 120
############################################################################################
label event_loc_lessonEduNo_0_help1:
    show expression 'pic/events/lection_help/no4.jpg' at top as tempPic
    'Ну, в принципе, урок удался. Вы конечно не блистали, но и не выставили себя в неуместном виде...'
    $ move(curloc)


############################################################################################
# loc_lessonEduOk
# - round(player.getIntel(),1)*2 > 120
############################################################################################
label event_loc_lessonEduOk_0_help1:   
    show expression 'pic/events/lection_help/ok5.jpg' at top as tempPic
    'Новые методики и отличный подбор материала позволили вам наглядно продемострировать, что вы вполне заслуженно занимаете место директора!'
    'Ученики также были впечатлены, а некоторые, вероятно, расскажут об этом и дома.'
    $ setRep(5,1)
    $ move(curloc)

############################################################################################
# loc_lessonFun
# player.say 'Надо повышать лояльность учеников, это увеличит привлекательность школы для инвесторов.'
# interactionObj.say 'И какие действия вы считаете необходимыми?'
# player.say 'Ну вы же видите что дети скучают, значит нам нужно их развлечь!'
############################################################################################
label event_loc_lessonFun_0_help1:
    show expression 'pic/events/lection_help/fun1/00.jpg' at top as tempPic
    'Что может быть веселее взаимного общения? Именно поэтому вы решаете устроить конкурс поцелуев, где девочки покажут свои умения, а жюри из мальчиков их оценит!'
    if 30 <= getPar(studs, 'corr'):
        python:
            st1 = getChar('female','lustmax')
            st2 = getChar('male')
        show expression 'pic/events/lection_help/fun1/01.jpg' at top as tempPic with dissolve
        'Правда вот [st1.name] явно увлекалсь, хотя [st2.fname] и не выглядит расстроенным этим фактом.'
        $ setCorr(10,0.5)
        $ setLust(10,5)
        menu:
            'Прервать их':
                'Такое поведение явно не пройдет незамеченным, поэтому вы заканчиваете развлечение, пока оно не зашло сильно далеко.'
                $ setRep(10,2)
                $ st1.incLoy(-2)
            'Наблюдать дальше' if 30 <= player.getCorr():
                show expression 'pic/events/lection_help/fun1/02.jpg' at top as tempPic with dissolve
                'Как вы и ожидали всё это не продлилось долго. Зато у вас наметился победитель конкурса.'
                $ setRep(10,-2)
                $ st1.incLoy(5)     
                $ setCorr(10,1)
                $ setLust(10,5)
                if 60 <= getPar(studs, 'corr'):
                    show expression 'pic/events/lection_help/fun1/03.jpg' at top as tempPic with dissolve
                    'Удивительно, но [st2.fname] не удовлетворился произошедшим и перешел к еще более активным действиям.'
                    menu:
                        'Уж такое явно неприемлемо':
                            'Вы прирываете это действие и наказываете его участников.'
                            $ addDetention(st1,st2)
                            $ setRep(10,3)
                            $ st1.incLoy(-5)
                            $ st2.incLoy(-5)
                        'Смотреть чем все закончится' if 50 <= player.getCorr():
                            show expression 'pic/events/lection_help/fun1/04.jpg' at top as tempPic with dissolve
                            '[st2.fname], не обращая внимание на присутствующих, продолжил свое дело пока не кончил. Причем не вынимая член из киски [st1.fname]'
                            $ setRep(10,-2)
                            $ st1.incLust(-100)  
                            $ st2.incLust(-100)  
                            $ setCorr(10,1)
                            $ setLust(10,15)
                            if rand(1, 3) == 1 :
                                show expression 'pic/events/lection_help/fun1/05.jpg' at top as tempPic with dissolve
                                'К вашему непомерному изумлению, [st2.name] и не собирался останавливаться, а только поменял позу.'
                                player.say 'Да сколько же он собирается продолжать?'
                                show expression 'pic/events/lection_help/fun1/06.jpg' at top as tempPic with dissolve
                                'Дождавшись пока [st2.fname] кончит в очередной раз, вы отправляете всех обратно на занятие.'
    $ move(curloc)

############################################################################################
# loc_lessonCorr
# player.say 'У нас ведь отличная школа, а ученики выглядят несколько зажато. Мы должны обеспечить их раскрепощение!'
# interactionObj.say 'Что-то мне кажется это уже слишком...'
# player.say 'Да оставьте! Мы, как педагоги, просто обязаны готовить их ко всем аспектам жизни!'
# interactionObj.say 'Хмм, тогда возможно и я посмотрю что вы придумали...'
############################################################################################
label event_loc_lessonCorr_0_help1:
    show expression 'pic/events/lection_help/less_ero_00.jpg' at top as tempPic
    'Вы устраиваете просветительскую лекцию о взаимоотношении полов.'
    show expression 'pic/events/lection_help/less_ero_01.jpg' at top as tempPic
    'А к некоторым ученикам даже применяете наглядную агитацию.'
    $ move(curloc)

############################################################################################
# loc_LessonSportGym
# 'Вы активно размялись и подняли физическую форму.'
############################################################################################
label event_loc_LessonSportGym_0_help1:
    show expression 'pic/events/lection_help/SportGym1/01.png' at top as tempPic
    'Также во время занятия вы не забыли похвастаться своей мокрой маечкой.'
    show expression 'pic/events/lection_help/SportGym1/02.png' at top as tempPic with dissolve
    'Хотя по вашему ощущению учебный процесс это несколько сбило.'
    $ setCorr(10,0.5)
    $ setRep(5,-0.5)
    $ player.incCorr(0.05)
    if player.getCorr() > 50:
        show expression 'pic/events/lection_help/SportGym1/03.jpg' at top as tempPic
        'Вы также весьма ярко представили, как на самом деле должен выглядеть урок в вашей школе.'
        $ player.incLust(5)
    $ move(curloc)

############################################################################################
# loc_LessonSportGym
# 'Вы неплохо поплавали на занятии и улучшили своё здоровье.'
############################################################################################
label event_loc_LessonSportSwim_0_help1:
    python:
        st1 = getChar('female')
    show expression 'pic/events/lection_help/SportSwim1/01.jpg' at top as tempPic
    'Кроме того вам удалось пообниматься со [st1.name]'
    if player.getCorr() > 30:
        show expression 'pic/events/lection_help/SportSwim1/02.jpg' at top as tempPic with dissolve
        'И не только пообниматься, но и ощупать её груди.'
        show expression 'pic/events/lection_help/SportSwim1/03.jpg' at top as tempPic with dissolve
        'Довольно, кстати, немаленькие как для школьницы.'
        $ st1.incCorr(0.5)
        $ st1.incLoy(-1)
        $ player.incCorr(0.05)
        $ player.incLust(2)
    $ move(curloc)