init python:
    lastNotebookScreen = 'studList'
label notebook:
    show expression "pic/bg.png"
    show screen notebook
    call screen personalInfo

screen notebook:
    fixed xpos 0.01 ypos 0.01:
        hbox :
            key "game_menu" action [Show('stats_screen'), Hide('studList'), Hide('teacherList'), Hide('personalInfo'), Hide('charInfoLeft'), Function(move, curloc)]
            textbutton _('Назад') action [Show('stats_screen'), Hide('studList'), Hide('teacherList'), Hide('personalInfo'), Hide('charInfoLeft'), Function(move, curloc)]
            textbutton _('Вы') action [Hide ('charInfoLeft'), Show('personalInfo')]
            textbutton _('Список учеников') action Show('studList')
            textbutton _('Список учителей') action Show('teacherList')
            textbutton _('Статистика школы') action Show('schoolStats')
            textbutton _('Журнал') action Show('journal')
            if development > 0:
                textbutton _('Список по партнёрам') action Show('partnerList')

screen partnerList:
    tag notebookList
    fixed xpos 0.20 ypos 0.1:
        vbox:
            $ showed[:] = []
            for x in studs:
                if x.partner != None and x not in showed:
                    $ sex1 = x.getSex()
                    $ sex2 = x.partner.getSex()
                    textbutton '[x.name] [sex1] === [x.partner.name] [sex2]' action NullAction() hovered [SetVariable('showHover',x),Show('charInfoLeft')] text_style "small_button_text"
                    $ showed.append(x)
                    $ showed.append(x.partner)
                
screen studList:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        $ xalig = 0.17
        $ yalig = 0.01
        for x in studs:
            $ pictoSize = 0.5
            if x in highlightP:
                $ pictoSize += 0.1
            if 'school' in getLoc(curloc).position and lt() >= -1:
                imagebutton:
                    idle im.FactorScale(x.picto,pictoSize) 
                    hover im.FactorScale(x.picto,pictoSize + 0.1) 
                    xalign xalig yalign yalig 
                    action [Jump('inviteToOffice')]
                    hovered [SetVariable('showHover',x),Show('charInfoLeft')] 
                    unhovered Hide('charInfoLeft')
            else:
                imagebutton:
                    idle im.FactorScale(x.picto,pictoSize) 
                    hover im.FactorScale(x.picto,pictoSize + 0.1) 
                    xalign xalig yalign yalig 
                    action [Function(addHighlight,x), Show('charInfoLeft')] 
                    hovered [SetVariable('showHover',x),Show('charInfoLeft')] 
                    unhovered Hide('charInfoLeft')
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.17

screen teacherList:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        $ xalig = 0.17
        $ yalig = 0.01
        for x in teachers:
            imagebutton:
                idle im.FactorScale(x.picto,0.5) 
                hover im.FactorScale(x.picto,0.6) 
                xalign xalig yalign yalig action NullAction() 
                hovered [SetVariable('showHover',x),Show('charInfoLeft')] 
                unhovered Hide('charInfoLeft')
            $ xalig += 0.15
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.17

screen charInfoLeft:
    zorder 1
    frame xpos 0.01 ypos 0.1:
        vbox:
            if showHover.age > 0:
                add showHover.picto
                null height 10
                
                text _('[showHover.name]') style style.my_text
                
                if development > 0:
                    if showHover.partner != None:
                        text _('Партнёр [showHover.partner.name]') style style.my_text
                    else:
                        text _('Одиночка') style style.my_text
                    
                $ temp = showHover.age
                if temp < 20:
                    text _('Возраст Nнадцать') style style.my_text
                else:
                    text _('Возраст [temp] лет') style style.my_text
                
                $ temp = round(showHover.stats.beauty,1)
                text _('Красота [temp]') style style.my_text
                
                $ bsize = showHover.body.parts['грудь'].size
                if bsize > 0:
                    $ temp = round(bsize, 1)
                    text _('Размер груди [temp]') style style.my_text
                else:
                    text '' style style.my_text
                    
                $ temp = round(showHover.body.height,1)
                text _('Рост [temp]') style style.my_text
                
                $ temp = round(showHover.getEdu(),1)
                text _('Образование [temp]') style style.my_text
                
                $ temp = round(showHover.getFun(),1)
                text _('Счастье [temp]') style style.my_text
                
                $ temp = round(showHover.getLoy(),1)
                text _('Лояльность [temp]') style style.my_text
                
                $ temp = round(showHover.getCorr(),1)
                text _('Развратность [temp]') style style.my_text
                
                if showHover not in teachers:
                    $ temp = round(showHover.getRep(),1)
                    text _('Репутация [temp]') style style.my_text

                if showHover in highlightP:
                    text _('Подсвечивается') style style.green
                else:
                    text _('Не подсвечивается') style style.warning

screen personalInfo:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        vbox:
            python:
                name = player.fullName()
                age = str(player.age)
                sex = player.body.sex()
                beauty = round(player.getBeauty(),1)
                loyalty = round(player.getLoy(),1)
                intel = round(player.getIntel(),1)*2
                lust = round(player.getLust(),1)
                corr = round(player.getCorr(),1)
                fun = round(player.getFun(),1)
                health = round(player.getHealth(),1)
                height = round(player.body.height,1)
                money = round(player.money,1)
                
                bsize = round(player.body.parts['грудь'].size, 1)
                vsize = round(player.body.parts['вагина'].size,1)
                asize = round(player.body.parts['анус'].size,1)
                
            add im.FactorScale(player.picto,.5)
            null height 10
            text _('[name]') style style.my_text
            text _('Размер груди [bsize]') style style.my_text
            text _('Рост [height]') style style.my_text
            text _('IQ [intel]') style style.my_text
            text _('Счастье [fun]') style style.my_text
            text _('Развратность [corr]') style style.my_text
            text _('Красота [beauty]') style style.my_text
            text ''
            # text _('Диаметр вагины [vsize]см') style style.my_text
            # text _('Диаметр ануса [asize]см') style style.my_text
            # text ''
            text _('Денег [money]') style style.my_text
            
    fixed xpos 0.2 ypos 0.1 :
        vbox xmaximum 800:
            text textgen(player) style style.my_text

screen schoolStats:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        vbox:
            hbox:
                text _('Текущие фонды школы:') style style.description
                text '[school.budget]' style style.description
            hbox:
                text _('Ежемесячный предполагаемый доход:') style style.description
                text str(school.expectedBudget()) style style.description
            hbox:
                text _('Образовательные материалы:') style style.description
                text school.getEduMats() style style.description
                    
            hbox:
                text _('Школьная форма:') style style.description
                text school.getUniform() style style.description
                
            hbox:
                text _('Строения:') style style.description
                if len(school.buildings) == 0:
                    text _('Нет') style style.description
                else:
                    for x in school.buildings:
                        text '[x] ' style style.description
            hbox:
                text _('Прочее:') style style.description
                if len(school.furniture) == 0:
                    text _('Нет') style style.description
                else:
                    for x in school.furniture:
                        text '[x] ' style style.description
                        
screen journal:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        vbox:
            if is_camera > 0:
                text _('Достать скрытую камеру:') style style.description
                if is_camera == 1:
                    text _('Надо сходить в магазин и обратиться к продавцу.')
                if is_camera == 2:
                    text _('Не думаю, что есть какая то другая возможность достать эту штучку. Надо снова пообщаться с продавцом.')
                if is_camera == 3:
                     text _('Теперь я могу покупать камеры в магазине!')
            if is_camera == 0 and is_camera_init > 0:
                text _('Проверить 4 класс:') style style.description
                text _('Надо проверить, что за странные слухи о четвёртом классе и мыши под учительской тумбой.')
            text _('')
            
            if mile_qwest_2_stage_init == 1 or development == 1 or mile_qwest_2_stage > 0:
                text _('[kupruvna.name]:') style style.description
                if mile_qwest_2_stage == 0:
                    text _('Мне необходимо подловить её в перемену или после уроков в первом классе.')
                elif mile_qwest_2_stage == 1 and camera.name not in getLoc('loc_class1').getItems():
                    text _('Необходимо установить камеру в её классе')
                elif mile_qwest_2_stage == 1 and camera.name in getLoc('loc_class1').getItems():
                    text _('Я должна регулярно проверять камеру, установленную в её классе через свой компьютер.')
                elif mile_qwest_2_stage == 3:
                    text _('Нужно продолжать наблюдать за ней через камеру.')
                    if mile_qwest_2_caught == 1:
                        text _('[kupruvna.name] обиделась на меня за то, что я показала ей снимки.')
                elif mile_qwest_2_stage == 5 and is_cabbage == 0:
                    text _('Нужно подождать.')
                elif mile_qwest_2_stage == 5 and is_cabbage > 0:
                    if mile_qwest_2_stage_init >= 2:
                        text _('Надо как то подтолкнуть её на согласие... Возможно что-то из секс-шопа мне поможет?')
                    else:
                        text _('Нужно почаще прогуливаться во время уборки капусты. Возможно я что то замечу?')
                elif mile_qwest_2_stage == 5 and mile_qwest_2_Ahmed == 1:
                    text _('Интересный сарайчик я нашла неподалёку. Довольно укромное место.')
                elif mile_qwest_2_stage == 5 and mile_qwest_2_stage_init == 3:
                    text _('Мне необходимо достать камеру в следующий раз.')
                elif mile_qwest_2_stage == 7:
                    text _('Надо вызвать её к себе в кабинет для последнего разговора.')
                elif mile_qwest_2_stage == 10:
                    text _('[kupruvna.name] всегда будет поддерживать меня на голосовании. К сожалению я так и не узнала, что сподвигло её заниматься сексом с учеником. Да и отношения уже не исправить.')
                elif mile_qwest_2_stage == 11:
                    text _('[kupruvna.name] всегда будет поддерживать меня на голосовании. К сожалению, после вашего напора, её отношения с сыном закончились. Зато она стало абсолютно безвольной! (Что пока абсолютно бесполезно)')
                elif mile_qwest_2_stage == 12:
                    text _('[kupruvna.name] стала гораздо развратней, чем была и больше не будет скрывать свои отношения с сыном. ')
                else:
                    text _('Что то пошло не так с журналом. Заскриншотьте это сообщение и напишите на форуме или в мой блог:\n mile_qwest_2_stage = [mile_qwest_2_stage], mile_qwest_2_stage_init = [mile_qwest_2_stage_init], mile_qwest_2_caught = [mile_qwest_2_caught], mile_qwest_2_Ahmed = [mile_qwest_2_Ahmed]')
            text _('')
            
            if mile_qwest_3_stage_init > 0 or mile_qwest_3_stage > 0:
                text _('[danokova.name]:') style style.description
                if mile_qwest_3_stage >= 1:
                    text _('Похоже, что [bioBoy.name] "втёрся" в её доверие.')
                if mile_qwest_3_stage == 0:
                    text _('Надо как нибудь заглянуть в секс-шоп после уроков')
                if mile_qwest_3_stage == 1 and ptime - mile_qwest_3_time > 12:
                    text _('Надо поговорить с ней сегодня после уроков.')
                if mile_qwest_3_stage == 1 and ptime - mile_qwest_3_time <= 12:
                    text _('Надо поговорить с ней завтра.')
                if mile_qwest_3_stage == 2:
                    text _('Когда она в моём кабинете, надо попробовать поиграть с температурой, а потом пригласить её любимчика.')
                if mile_qwest_3_stage == 3:
                    text _('Надо снова поговорить с ней после уроков.')
                if mile_qwest_3_stage == 4:
                    text _('Похоже, что настало время сделать в кабинете пожарче, и пригласить всем известную личность.')
                if mile_qwest_3_stage == 5:
                    text _('[danokova.fname] очевидно втянулась в процесс. Интересно, что она приготовит ему на следующий раз? И да, мне больше не кажется, что подерживать высокую температуру в кабинете - хорошая идея.')
                if mile_qwest_3_stage == 6:
                    text _('[danokova.fname] очевидно втянулась в процесс написания своей статьи. Я думаю, что больше не стоит мешать ей высокой температурой. Достаточно продолжать подкидывать этого "необычного" ученика.')
                if mile_qwest_3_stage == 10:
                    text _('Боюсь, что эта ветка пока не дописана. Напиши в консоли mile_qwest_3_stage = 6, чтобы попасть в соседнюю ветку.')
                if mile_qwest_3_stage == 11:
                    text _('В новый день с новыми идеями! Хотя нет, зачем что то менять, когда можно просто продолжать в том же духе?')
                if mile_qwest_3_stage == 13:
                    text _('По моему у меня есть всё, что мне нужно, для того, чтобы склонить учительницу на свою сторону. Надо поговорить с ней после уроков.')
                if mile_qwest_3_stage == 15:
                    text _('Как жестоко я ошибалась, думая, что у меня есть всё... Ну что же, если честно я не против сыграть по её правилам, и посмотреть, что из этого выйдет. Для этого мне нужно:')
                    text _('1. Верёвка')
                    text _('2. БДСМ костюм')
                    text _('3. Хлороформ.')
                    text _('С последним будет посложнее. Даже если я найду что то похожее, хватит ли у меня знаний, чтобы проверить, что это имнно он? Я не хочу просто так отравлять ученика...')
                if mile_qwest_3_stage == 17:
                    text _('Я достала хлороформ!')
                    if player.hasItem(rope.name):
                        text _('И верёвку!')
                    if player.hasItem(bdsmUniform.name):
                        text _('И костюм!')
                    text _('К сожалению это бесполезно, так как продолжения квеста пока нет.')
                    
            if mile_qwest_1_stage_init > 0 or mile_qwest_1_stage > 0:
                if mile_qwest_1_stage == 0:
                    text _('Странные события:') style style.description
                else:
                    text _('[mustangovich.name]:') style style.description
                if mile_qwest_1_stage_init > 0 and mile_qwest_1_stage == 0:
                    text _('Говорят, что на первой перемене в холле происходят странные события с девочками.')
                if mile_qwest_1_stage == 1:
                    text _('Ну [mustangovich.lname]! Ну сукин сын! Хотя было неплохо... Надо закрепить успех. Например в учительской. Да и возбудить его перед этим, чтобы не увильнул. Ну и, разумеется, надо показать, кто тут главный!')
                if mile_qwest_1_stage == 2:
                    text _('Я так полагаю, что я закончила с этим мужчиной. Хотя в учительской он весьма и весьма неплохо себя показал... Да, можно и повторить на досуге!')
                    