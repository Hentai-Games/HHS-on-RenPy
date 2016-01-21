init python:
    class Dialogue():
        def __init__(self, id, corr, type):
            self.id = id
            self.corr = corr
            self.type = type

    class Flirt():
        def __init__(self, id, corr, sex):
            self.id = id
            self.corr = corr
            self.sex = sex

    def dialogueParser():
        _locs = renpy.get_all_labels()
        textList = []
        for textLable in _locs: # перебираем все лейблы
            if textLable[:7] == 'dialog_': # находим тот, что с текстом
                corr = textLable.split("_")
                type = corr[1]
                corr = corr[2]
                tempText = Dialogue(id = textLable, corr = int(corr), type = type)
                textList.append(tempText)
        return textList

    dialogueList = dialogueParser()

    def dialogueSelector(speaker):
        tempList = []
        for x in dialogueList:
            if speaker.stats.corr >= x.corr and ((speaker in studs and x.type == 'stud') or (speaker in teachers and x.type == 'teacher')):
                tempList.append(x)
        return tempList[rand(0,len(tempList) - 1)].id

    def flirtParser():
        _locs = renpy.get_all_labels()
        textList = []
        for textLable in _locs: # перебираем все лейблы
            if textLable[:6] == 'flirt_': # находим тот, что с флиртом
                corr = textLable.split("_")
                sex = corr[1]
                corr = corr[2]
                tempText = Flirt(id = textLable, corr = int(corr), sex = sex)
                textList.append(tempText)
        return textList

    flirtList = flirtParser()

    def flirtSelector(speaker):
        tempList = []
        for x in flirtList:
            if speaker.body.sex() == 'futa' and x.sex == 'female':
                x.sex = 'futa'
            if speaker.body.sex() == x.sex and speaker.getCorr() >= x.corr and player.getCorr() >= x.corr:
                tempList.append(x)
        return tempList[rand(0,len(tempList) - 1)].id



    def showChars():
        changetime(1)
        renpy.show('temp0', what = Image('pic/bg.png'), zorder = 0)
        renpy.show('temp1', what = Image(getCharImage(player), xalign=0.2, yalign= 1.0, yanchor = 'center'), zorder = 1)
        renpy.show('temp2', what = Image(getCharImage(interactionObj), xalign=0.8, yalign= 1.0, yanchor = 'center'), zorder = 1)

    def getCharImage(char,*args):
        if char == player:
            anotherImage = player.picto

        elif char.getSex() == 'male':
            anotherImage = 'pic/showStud/m_1.png'
        else:
            anotherImage = 'pic/showStud/f_1.png'

        if char.lname == 'Данокова':
            anotherImage = 'pic/teachers/danokova_1.png'
        elif char.lname == 'Фригидовна':
            anotherImage = 'pic/teachers/frigidovna_1.png'
        elif char.lname == 'Биссектрисовна':
            anotherImage = 'pic/teachers/bissektrisovna_1.png'
        elif char.lname == 'Диковна':
            anotherImage = 'pic/teachers/dikovna_1.png'
        elif char.lname == 'Купрувна':
            anotherImage = 'pic/teachers/kupruvna_1.png'
        elif char.lname == 'Мустангович':
            anotherImage = 'pic/teachers/mustangovich_1.png'
        elif char.lname == 'Данте':
            anotherImage = 'pic/teachers/dante_1.png'
        elif char.lname == 'Гонореевна':
            anotherImage = 'pic/teachers/gonoreevna_1.png'
        if len(args) == 0:
            return anotherImage

        elif args[0] == 'dialog':
            if char.name == player.name:
                return Image(anotherImage, xalign=0.2, yalign= 1.0, yanchor = 'center')
            else:
                return Image(anotherImage, xalign=0.8, yalign= 1.0, yanchor = 'center')

    dummy = ''
    interactionObj = dummy
    lastView = 'locationPeoplePicto'
    showHover = dummy
    gift = ''


label locationPeople:
    $ renpy.call_screen(lastView)

screen peopleTextList:
    vbox:
        for x in getLoc(curloc).getPeople():
            python:
                mystyle = 'small_button_text'
                if x in teachers: mystyle = 'bluesmall_button'
                if x in highlightP: mystyle = 'warning'
                actions_list = [Function(clrscr),
                                SetVariable('interactionObj', x),
                                SetVariable('reaction', reactionGen(x))]
                if x.getLocationStatus() and x.getLocationStatus().events:
                    actions_list.append(Jump(choice(x.getLocationStatus()
                                                     .events)))

                else:
                    if x in teachers and x not in teacher_intro:
                        if x == kupruvna:
                            actions_list += [Jump('intro_kupruvna')]
                        elif x == danokova:
                            actions_list += [Jump('intro_danokova')]
                        elif x == frigidovna:
                            actions_list += [Jump('intro_frigidovna')]
                        elif x == bissektrisovna:
                            actions_list += [Jump('intro_bissektrisovna')]
                        elif x == dikovna:
                            actions_list += [Jump('intro_dikovna')]
                        else:
                            actions_list += [Show('show_stat'), Function(showChars)]    #, Function(changetime, 1)]
                    else:
                        actions_list += [Show('show_stat'), Function(showChars)]    #, Function(changetime, 1)]
            textbutton x.name +  ' ' + x.locationStatus.name.lower():
                action actions_list
                hovered [SetVariable('showHover',x),Show('showCharStatusText')]
                unhovered [Hide('showCharStatusText')]
                style "bluesmall_button" text_style mystyle xalign 0.0

screen locationPeoplePicto:
    tag interface
    fixed xpos 0.01 ypos 0.01:
        key "game_menu" action Function(move, curloc)
        textbutton 'Назад' action Function(move, curloc)
        $ xalig = 0.2
        $ yalig = 0.05
        for x in getLoc(curloc).getPeople():
            $ pictoSize = 0.5
            if x in highlightP:
                $ pictoSize += 0.1
            python:
                actions_list = [Function(clrscr),
                                SetVariable('interactionObj', x),
                                SetVariable('reaction', reactionGen(x))]
                if x.getLocationStatus() and x.getLocationStatus().events:
                    actions_list.append(Jump(choice(x.getLocationStatus()
                                                     .events)))

                else:
                    if x in teachers and x not in teacher_intro:
                        if x == kupruvna:
                            actions_list += [Jump('intro_kupruvna')]
                        elif x == danokova:
                            actions_list += [Jump('intro_danokova')]
                        elif x == frigidovna:
                            actions_list += [Jump('intro_frigidovna')]
                        elif x == bissektrisovna:
                            actions_list += [Jump('intro_bissektrisovna')]
                        elif x == dikovna:
                            actions_list += [Jump('intro_dikovna')]
                        else:
                            actions_list += [Show('show_stat'), Function(showChars)]    #, Function(changetime, 1)]
                    else:
                        actions_list += [Show('show_stat'), Function(showChars)]    #, Function(changetime, 1)]

            imagebutton:
                idle im.FactorScale(x.picto, pictoSize)
                hover im.FactorScale(x.picto, pictoSize + 0.1)
                xalign xalig yalign yalig
                action actions_list
                hovered [SetVariable('showHover', x), Show('charInfoLeft'),Show('showCharStatusText')]
                unhovered [Hide('showCharStatusText')]
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2

screen showCharStatusText:
    frame:
        xalign 0.01
        yalign 1.0
        text _('[showHover.locationStatus.name]')



screen show_stat:
    tag interface
    fixed xpos 0.01 ypos 0.01:
        vbox:
            add interactionObj.picto
            null height 10
            $ name = interactionObj.fullName()
            text '[name]' style style.my_text
            $ temp = round(interactionObj.getBeauty(), 1)
            text 'Красота [temp]' style style.my_text
            if interactionObj.body.parts['грудь'].size > 0:
                $ temp = round(interactionObj.body.parts['грудь'].size, 1)
                text 'Размер груди [temp]' style style.my_text
            $ temp = round(interactionObj.body.height, 1)
            text 'Рост [temp]' style style.my_text
            $ temp = round(interactionObj.getEdu(), 1)
            text 'Образование [temp]' style style.my_text
            $ temp = round(interactionObj.getFun(), 1)
            text 'Счастье [temp]' style style.my_text
            $ temp = round(interactionObj.getLoy(), 1)
            text 'Лояльность [temp]' style style.my_text
            $ temp = round(interactionObj.getCorr(), 1)
            text 'Развратность [temp]' style style.my_text
            $ temp = round(interactionObj.getLust(), 1)
            text 'Желание [temp]' style style.my_text
            if interactionObj not in teachers:
                $ temp = round(interactionObj.getRep(), 1)
                text 'Репутация [temp]' style style.my_text
            null height 10

    fixed xpos 0.18 ypos 0.01 :
        # add 'pic/bg2.png'
        vbox xmaximum 750:
            text textgen(interactionObj) style style.my_text
            for x in reaction:
                text x style style.my_text

    fixed xpos 0.8 ypos 0.1:
        vbox:
            if interactionObj in studs:
                if interactionObj not in highlightP:
                    textbutton 'Замечать' xminimum 200 action [Function(addHighlight,interactionObj), Show('show_stat')]
                else:
                    textbutton 'Не замечать' xminimum 200 action [Function(addHighlight,interactionObj), Show('show_stat')]
            if interactionObj.locationStatus not in [learnSelector(), teach_status]: # Если собеседник не занят
                if interactionObj.sayCount > 0:
                    textbutton 'Поговорить' xminimum 200 action Jump('speak')
                if interactionObj.sayCount >= 3:
                    textbutton 'Флирт' xminimum 200 action Jump('flirt')
                if interactionObj == mustangovich and mustangovich.getLust() > 70 and curloc == 'teacherRoom' and mile_quest_1 >= 1 and interactionObj.sayCount >= 5:
                    textbutton 'Заняться сексом' xminimum 200 action Jump('ahmed_sex_selector')
            if player.hasItem(aphrodisiac.name) and interactionObj not in aphroUsedArr:
                textbutton 'Использовать\nафродизиак' xminimum 200 action Show('use_aphrodisiac')
            if 'school' in getLoc(curloc).position and curloc != 'loc_office' and interactionObj in studs:
                textbutton 'Вызвать к себе' xminimum 200 action Jump('callup')

            if curloc == 'loc_office':
                if interactionObj.getRep() < 10:
                    textbutton 'О родителях' xminimum 200 action Jump('reputation')
                textbutton 'Выгнать' xminimum 200 action Jump('callout')

            textbutton 'Подарить' xminimum 200 action Show('make_gift_char')
            textbutton 'Попрощаться' xminimum 200 action Function(move,curloc)
            key "game_menu" action Function(move,curloc)
            if development == 1:
                textbutton 'Карманы' xminimum 200 action Show('inventory_clothing_char')

    frame ypos 0.01 xalign 1.0:
        text 'Очков общения: ' + str(interactionObj.sayCount)

###########################################################################################################################
screen make_gift_char:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            key "game_menu" action [Function(clrscr),Show('show_stat')]
            textbutton _('Назад') action [Function(clrscr),Show('show_stat')]

            $ xalig = 0.2

        $ yalig = 0.05
        for x in player.inventory:
            if x.type == 'present' and (x.sex=='any' or x.sex==interactionObj.getSex('mf')):
                imagebutton:
                    idle im.FactorScale(x.picto,0.4)
                    hover im.FactorScale(x.picto,0.45)
                    xalign xalig yalign yalig
                    # action [Function(interactionObj.takeGift, x), Function(player.removeItem, x), Function(move, curloc)]
                    action [SetVariable('gift',x),Jump('takeGift')]
                    hovered [SetVariable('myItem', x), Show('showItem')]
                    unhovered Hide('showItem')
            else :
                $ xalig -= 0.09
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2
###########################################################################################################################
screen use_aphrodisiac:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            key "game_menu" action [Function(clrscr),Show('show_stat')]
            textbutton _('Назад') action [Function(clrscr),Show('show_stat')]

            $ xalig = 0.2

        $ yalig = 0.05
        for x in player.inventory:
            if x.type == 'sexShop':
                if x.purpose == 'aphrodisiac':
                    imagebutton:
                        idle im.FactorScale(x.picto,0.4)
                        hover im.FactorScale(x.picto,0.45)
                        xalign xalig yalign yalig
                        action [Jump('use_aphrodisiac')]
                        hovered [SetVariable('myItem', x), Show('showItem')]
                        unhovered Hide('showItem')
            else :
                $ xalig -= 0.09
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2
###########################################################################################################################
screen inventory_clothing_char:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            key "game_menu" action Function(move, curloc)
            textbutton _('Назад') action Function(move, curloc)
            $ xalig = 0.2
        $ yalig = 0.05
        for x in interactionObj.inventory:
            imagebutton:
                idle im.FactorScale(x.picto,0.4)
                hover im.FactorScale(x.picto,0.45)
                xalign xalig yalign yalig
                action NullAction()
                hovered [SetVariable('myItem', x), Show('showItem')]
                unhovered Hide('showItem')
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2

 ###########################################################################################################################
label speak:
    python:
        clrscr()
        user = interactionObj
        user.sayCount -= 1
        changetime(5)
        player.stats.energy -= rand(5,10)
        user.incLoy(1)

        if user == danokova and 'school' in getLoc(curloc).position:
            if mile_qwest_3_stage == 1 and ptime - mile_qwest_3_time > 12 and hour > 14:
                renpy.jump('danokova_work')
            elif mile_qwest_3_stage == 13:
                renpy.jump('danokova_bdsm_offer')
            elif mile_qwest_3_stage > 1 and hour > 14 and ptime - work51 > 10 and mile_qwest_3_stage not in [13]:
                renpy.jump('danokova_continue')

        renpy.jump(dialogueSelector(user))
    call screen show_stat
###########################################################################################################################
label flirt:
    python:
        clrscr()
        user = interactionObj
        user.sayCount -= 3
        changetime(5)
        player.stats.energy -= rand(5,10)
        renpy.jump(flirtSelector(user))
    call screen show_stat
###########################################################################################################################
label takeGift:
    $ clrscr()
    $ giftName = gift.name.lower()
    if interactionObj.getItem(gift.name) == False:
        $ interactionObj.takeGift(gift)
        $ player.removeItem(gift)
        interactionObj.say 'Спасибо за [giftName]!'
    else:
        'Э-э-э, спасибо, конечно, но у меня уже есть [giftName] от вас.'
    call screen show_stat
###########################################################################################################################
label callup:
    $ clrscr()
    python:
        interactionObj.moveToLocation('loc_office')
        callup = interactionObj
    player.say 'Нам необходимо поговорить наедине.'
    callup.say 'Хорошо, я сейчас же отправлюсь к вам в кабинет.'
    $ move(curloc)
###########################################################################################################################
label callout:
    $ clrscr()
    player.say 'Я думаю, мы закончили, [callup.fname].'
    callup.say 'Хорошо, до свидания, [player.name].'
    python:
        callup.moveToLocation('loc_firstFloor') # Выгоняем в коридор
        callup = dummy
        move(curloc)
###########################################################################################################################
label use_aphrodisiac:
    $ clrscr()
    player.say 'Смотри, [interactionObj.fname], что это там?'
    'Пока [interactionObj.name] отворачивается, чтобы поглазеть на воображаемый объект за спиной, вы распыляете немного афродизиака.'
    interactionObj.say 'Что там? - по покрасневшим щекам, видно что препарат подействовал.'
    player.say 'Да ничего, показалось наверное! - отмахиваетесь вы рукой.'
    'Второй раз за день на это не купятся.'
    python:
        if myItem.name == aphrodisiac.name: interactionObj.incLust(25)
        player.apply(myItem.name)
        aphroUsedArr.append(interactionObj)
    call screen show_stat
###########################################################################################################################
label reputation:
    show office
    python:
        clrscr()
        renpy.show('temp1', what = Image(getCharImage(player), xalign=0.2, yalign= 1.0, yanchor = 'center'), zorder = 1)
        renpy.show('temp2', what = Image(getCharImage(callup), xalign=0.8, yalign= 1.0, yanchor = 'center'), zorder = 1)
    if callup.name not in reputation_intro:
        $ reputation_intro.append(callup.name)
        player.say 'Понимаешь, [callup.fname], мы живём не в то время и учимся не в том месте.'
        player.say 'В нашем мире могут не все и не так, а как надо нам не все могут и не всегда.'
        player.say 'Когда как у всех, мы не можем так поступать, потому что мы не все, не такие, но тоже имеем право!'
        player.say 'Не порок то, что все так считают, не всегда прав тот, кто считает иначе.'
        player.say 'И сегодня в завтрашний день не все могут смотреть... Вернее смотреть могут не только лишь все, мало кто может это делать.'
        callup.say '??? - немое удивление застыло в глазах ученика. Уж слишком пространно вы выражаетесь в этом щекотливом вопросе.'
        player.say 'Короче держи язык за зубами, когда рассказываешь о том, что видишь в школе, понятно?'
    else:
        player.say 'Твои родители опять плохо обо мне говорят. Они так часто плохо обо мне говорят, что, наверное, и думают нехорошо!'
    if callup.getCorr() < 10 or callup.getLoy() > 80:
        callup.say 'Хорошо, [player.name], я постараюсь утрясти этот вопрос с родителями. Мне можно идти?'
        player.say 'Конечно, [callup.fname], иди.'
        python:
            callup.incRep(15)
            callup = dummy
            move(curloc)
    callup.say 'А, вы об этом! Нет проблем, что я получу взамен?'
    menu:
        player.say 'Что предпримем?'
        'Предложить оральный секс' if player.getCorr() > 30:
            player.say 'У меня есть то, что тебе понравится! - говорите вы облизывая губы.'
            if player.getBeauty() > 50:
                hide temp1
                hide temp2
                if callup.getSex() == 'male':
                    show expression 'pic/events/office/1.jpg' at top as tempPic
                    'Вы опустились на колени перед учеником и, предварительно проведя языком вдоль его ствола, взяли бордовую головку в рот. Ритмично посасывая её, вы постепенно ускоряли темп. Иногда вы вытаскивали член изо рта и страстно облизывали его.'
                    'Не выдержав умелых ласк, [callup.name] задрожал всем телом и со стоном выплеснул своё семя, заполнив ваш рот терпкой горечью. Уходя, он пообещал, что мнение его родителей о вас изменится в лучшую сторону.'
                if callup.getSex() == 'futa':
                    show expression 'pic/events/office/2.jpg' at top as tempPic
                    'Видя согласие на вашем лице, [callup.name] вставила свой член вам в рот без всяких прелюдий. Лишив своего директора какой либо возможности возразить, ученица оттрахала вас в глотку и, кончив, пообещала рассказать родителям что-нибудь хорошее о школе и методах образования.'
                if callup.getSex() == 'female':
                    show expression 'pic/events/office/3.jpg' at top as tempPic
                    'С готовностью опустившись на колени, вы задрали юбку ученицы, попутно удивившись отсутствию трусиков, и принялись вылизывать её киску, помогая себе пальчиками. Вскоре ваш рот оросился её пахучими соками, и довольная ученица пообещала замолвить о вас словечко перед родителями.'
                python:
                    callup.incRep(15)
                    callup = dummy
                    player.incIntel(-0.5)
                    move(curloc)
            else:
                callup.say 'Не-не-не-не! К такому меня жизнь ещё не готовила! - подняв перед собой руки, отступает назад ученик.'
                'Уткнувшись задницей в заветный выход, [callup.fname] быстро скрывается за дверью. Вы в зеркало когда последний раз смотрелись?'
        'Предложить деньги':
            player.say 'Хорошо, [callup.name], сколько же ты хочешь? - спросили вы доставая бумажник.'
            $ bribe = int(1000 - callup.getLoy()*5 + callup.getCorr()*5)
            callup.say '[bribe] монет.'
            if is_moneta == 0:
                $ is_moneta = 1
                callup.say 'Кстати, почему монет, ведь мы все бумажками расплачиваемся?'
                player.say 'Потому что 200 лет назад тут был пиратский остров. Очень неприятное место. И к заезжим путешественникам часто обращались фразой: "Гони money, ты!". Что, спустя поколения, выродилось до moneyты или монеты, монета. Какого чёрта я должна тебе объяснять? Чем занимается учитель истории?'
                callup.say 'Кто?'
                player.say 'Ах да, у нас нет истории...'
            if bribe > player.money:
                player.say 'Прости, но у меня нет таких денег.'
                callup.say 'А у меня что-то пропало желание общаться с вами дальше. Всё равно вас скоро уволят!'
                '[callup.fname] разворачивается и уходит.'
                $ callup = dummy
                $ move(curloc)
            else:
                player.say 'Вот, держи. Надеюсь, эта сумма исправит ситуацию?'
                callup.say 'А как же! - довольно восклицает ученик, пересчитывая банкноты.'
                $ player.money -= bribe
                $ callup.incRep(15)
                $ move(curloc)
        'Попробовать надавить':
            $ callup.incLoy(-10)
            $ callup.incFun(-20)
            if player.getIntel() > callup.getWill():
                if callup.getSex() == 'male':
                    player.say 'Ты пойдёшь к родителям и скажешь, что в восторге от нового директора, иначе ты у меня оставшиеся до последнего звонка годы будешь сортиры после уроков драить, усёк?'
                else:
                    player.say 'Ты пойдёшь к родителям и скажешь, что в восторге от нового директора, иначе ты у меня оставшиеся до последнего звонка годы будешь мужские сортиры после уроков драить, усекла?'
                callup.say 'К-к-к-конечно, - заикаясь отвечает [callup.fname] и убегает из вашего кабинета.'
                'Чтож, по крайней мере, ситуация с репутацией немного исправилась!'
                python:
                    callup.incRep(10)
                    callup = dummy
                    move(curloc)
            else:
                player.say 'Так, либо ты идёшь к родителям и говоришь им, что у нас прекрасная школа, либо я...'
                callup.say 'Либо вы что, [player.name]? - прерывает вас [callup.fname].'
                callup.say 'Вы ничего не можете сделать со своим учеником. Если только попробуете, вас не просто уволят с волчьим билетом, так ещё и на кичу посадят, там таких под шконкой весьма любят. Или вы уже в курсе?'
                player.say '???????'
                '[callup.fname], скорчив презрительную гримасу, удаляется из кабинета, не спрашивая вашего разрешения.'
                'Похоже, что-то пошло не так.'
                python:
                    callup = dummy
                    move(curloc)
        'Выгнать':
            player.say '[callup.name]! Немедленно покинь мой кабинет!'
            callup.say 'Да как хотите. - [callup.fname] закатывает глаза и уходит.'
            python:
                callup = dummy
                move(curloc)
