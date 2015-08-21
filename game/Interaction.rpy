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
            if textLable[:7] == 'dialog_': #находим тот, что с текстом
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
            if textLable[:6] == 'flirt_': #находим тот, что с флиртом
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
        renpy.show('temp0', what = Image('pic/bg.png'), zorder = 0)
        renpy.show('temp1', what = Image(getCharImage(player), xalign=0.2, yalign= 1.0, yanchor = 'center'), zorder = 1)
        renpy.show('temp2', what = Image(getCharImage(showHover), xalign=0.8, yalign= 1.0, yanchor = 'center'), zorder = 1)
        
    def getCharImage(char):
        if char == player:
            anotherImage = player.picto
            return anotherImage
            
        if char.getSex() == 'male':
            anotherImage = 'pic/showStud/m_1.png'
        else:
            anotherImage = 'pic/showStud/f_1.png'
            
        if showHover.lname == 'Данокова':
            anotherImage = 'pic/teachers/danokova_1.png'
        if showHover.lname == 'Фригидовна':
            anotherImage = 'pic/teachers/frigidovna_1.png'
        if showHover.lname == 'Биссектрисовна':
            anotherImage = 'pic/teachers/bissektrisovna_1.png'
        if showHover.lname == 'Диковна':
            anotherImage = 'pic/teachers/dikovna_1.png'
        if showHover.lname == 'Купрувна':
            anotherImage = 'pic/teachers/kupruvna_1.png'
        if showHover.lname == 'Мустангович':
            anotherImage = 'pic/teachers/mustangovich_1.png'
            
        return anotherImage
        
    dummy = Char()
    interactionObj = ''
    lastView = 'locationPeoplePicto'
    showHover = dummy


label locationPeople:
    $ renpy.call_screen(lastView)


screen locationPeoplePicto:
    tag interface
    fixed xpos 0.01 ypos 0.01:
        textbutton 'Назад' action Function(move, curloc)

        $ xalig = 0.2
        $ yalig = 0.05
        for x in getLoc(curloc).people:
            imagebutton idle im.FactorScale(x.picto,0.5) hover im.FactorScale(x.picto,0.6) xalign xalig yalign yalig action [Hide('charInfoLeft'), SetVariable('interactionObj',x), Show('show_stat'), Function(showChars)] hovered [SetVariable('showHover',x),Show('charInfoLeft')]
            # add im.FactorScale(x.picto,0.6) xalign xalig yalign yalig
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2

screen show_stat:
    tag interface
    fixed xpos 0.1 ypos 0.1:
        vbox:
            add showHover.picto

            $ x = interactionObj
            null height 10
            $ name = showHover.fullName()
            text '[name]' style style.my_text
            if showHover.body.parts['грудь'].size > 0:
                $ temp = round(showHover.body.parts['грудь'].size, 1)
                text 'Размер груди [temp]' style style.my_text
            $ temp = round(showHover.body.height, 1)
            text 'Рост [temp]' style style.my_text
            $ temp = round(showHover.stats.education, 1)
            text 'Образование [temp]' style style.my_text
            $ temp = round(showHover.stats.fun, 1)
            text 'Счастье [temp]' style style.my_text
            $ temp = round(showHover.stats.loyalty, 1)
            text 'Лояльность [temp]' style style.my_text
            $ temp = round(showHover.stats.corr, 1)
            text 'Развратность [temp]' style style.my_text
            $ temp = round(showHover.getBeauty(), 1)
            text 'Красота [temp]' style style.my_text
            null height 10

    fixed xpos 0.3 ypos 0.1 :
        # add 'pic/bg2.png'
        vbox xmaximum config.screen_width/2:
            text textgen(showHover) style style.my_text
        
    fixed xpos 0.8 ypos 0.1:
        vbox:
            if lt() <= 0 or 'safe' in getLoc(curloc).position:
                if showHover.sayCount > 0: 
                    textbutton 'Поговорить' xminimum 200 action Jump('speak')
                if showHover.sayCount >= 3: 
                    textbutton 'Флирт' xminimum 200 action Jump('flirt')
            if 'school' in getLoc(curloc).position and curloc != 'loc_office' and showHover in studs:
                textbutton 'Вызвать к себе' xminimum 200 action Jump('callup')
                
            if curloc == 'loc_office':
                if showHover.getRep() < 10:
                    textbutton 'О родителях' xminimum 200 action Jump('reputation')
                textbutton 'Выгнать' xminimum 200 action Jump('callout')
                
            textbutton 'Назад' xminimum 200 action Function(move,curloc)
            if development == 1:
                textbutton 'Карманы' xminimum 200 action Show('inventory_clothing_char')
            
    frame ypos 0.01 xalign 1.0:
        text 'Очков общения: ' + str(showHover.sayCount)
        
###########################################################################################################################            
screen inventory_clothing_char:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            textbutton _('Назад') action Function(move, curloc)

            $ xalig = 0.2
        $ yalig = 0.05
        for x in showHover.inventory:
            if x.type == 'clothing':
                imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action NullAction() hovered [SetVariable('myItem', x), Show('showItem')]
            else :
                $ xalig -= 0.09
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2
                
 ###########################################################################################################################               
label speak:
    python:
        clrscr()
        user = showHover
        user.sayCount -= 1
        changetime(5)
        player.stats.energy -= rand(5,10)
        user.setLoy(1)
        renpy.jump(dialogueSelector(user))

    call screen show_stat
###########################################################################################################################
label flirt:
    python:
        clrscr()
        user = showHover
        user.sayCount -= 3
        changetime(5)
        player.stats.energy -= rand(5,10)
        renpy.jump(flirtSelector(user))

    call screen show_stat
###########################################################################################################################
label callup:
    $ clrscr()
    python:
        getLoc(curloc).people.remove(showHover)
        callup = showHover
    player.say 'Нам необходимо поговорить наедине.'
    callup.say 'Хорошо, я сейчас же отправлюсь к вам в кабинет.'
    $ move(curloc)
###########################################################################################################################    
label callout:
    $ clrscr()
    player.say 'Я думаю, мы закончили, [callup.fname].'
    callup.say 'Хорошо, до свидания, [player.name].'
    python:
        callup = dummy
        move(curloc)
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
            callup.setRep(15)
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
                    'Не выдержав умелых ласк, [callup.name] задрожал всем телом, и со стоном выплеснул своё семя, заполнив ваш рот терпкой горечью. Уходя, он пообещал, что мнение его родителей о вас изменится в лучшую сторону.'
                if callup.getSex() == 'futa':
                    show expression 'pic/events/office/2.jpg' at top as tempPic
                    'Видя согласие на вашем лице, [callup.name] вставила свой член вам в рот без всяких прелюдий. Лишив своего директора какой либо возожности возразить, ученица оттрахала вас в глотку, и кончив, пообещала рассказать родителям что нибудь хорошее о школе и методах образования.'
                if callup.getSex() == 'female':
                    show expression 'pic/events/office/3.jpg' at top as tempPic
                    'С готовностью опустившись на колени, вы задрали юбку ученицы, попутно удивившись отсутствию трусиков, и принялись вылизывать её киску помогая себе пальчиками. Вскоре ваш рот оросился её пахучими соками и довольная ученица пообещала замолвить о вас словечко перед родителями.'
                python:
                    callup.setRep(15)
                    callup = dummy
                    player.setIntel(-0.5)
                    move(curloc)
            else:
                callup.say 'Не не не не! К такому меня жизнь ещё не готовила! - подняв перед собой руки, отступает назад ученик.'
                'Уткнувшись задницей в заветный выход, [callup.fname] быстро скрывается за дверью. Вы в зеркало когда последний раз смотрелись?'
        'Предложить деньги':
            player.say 'Хорошо, [callup.name], сколько же ты хочешь? - спросили вы доставая бумажник.'
            $ bribe = int(1000 - callup.getLoy()*5 + callup.getCorr()*5)
            callup.say '[bribe] монет.'
            if is_moneta == 0:
                $ is_moneta = 1
                callup.say 'Кстати почему монет, ведь мы все бумажками расплачиваемся?'
                player.say 'Потому что 200 лет назад, тут был пиратский остров. Очень неприятное место, и к заезжим путешественникам часто обращались фразой: "Гони money, ты!". Что спустя поколения выродилось до moneyты или монеты, монета. Какого чёрта я должна тебе объяснять? Чем занимается учитель истории?'
                callup.say 'Кто?'
                player.say 'Ах да, у нас нет истории...'
            if bribe > player.money:
                player.say 'Прости, но у меня нет таких денег.'
                callup.say 'А у меня что то пропало желание общаться с вами дальше. Всё равно вас скоро уволят!'
                '[callup.fname] разворачивается и уходит.'
                $ callup = dummy
                $ move(curloc)
            else:
                player.say 'Вот, держи. Надеюсь эта сумма исправит ситуацию?'
                callup.say 'А как же! - довольно восклицает ученик пересчитывая банкноты.'
                $ player.money -= bribe
                $ callup.setRep(15)
                $ move(curloc)
        'Попробовать надавить':
            $ callup.setLoy(-10)
            $ callup.setFun(-20)
            if player.getIntel() > callup.getWill():
                if callup.getSex() == 'male':
                    player.say 'Ты пойдёшь к родителям и скажешь, что в восторге от нового директора, иначе ты у меня оставшиеся до последнего звонка годы будешь сортиры после уроков драить, усёк?'
                else:
                    player.say 'Ты пойдёшь к родителям и скажешь, что в восторге от нового директора, иначе ты у меня оставшиеся до последнего звонка годы будешь мужские сортиры после уроков драить, усекла?'
                callup.say 'К-к-к-конечно, - заикаясь отвечает [callup.fname] и убегает из вашего кабинета.'
                'Чтож, по крайней мере ситуация с репутацией немного исправилась!'
                python:
                    callup.setRep(10)
                    callup = dummy
                    move(curloc)
            else:
                player.say 'Так, либо ты идёшь к родителям и говоришь им, что у нас прекрасная школа, либо я'
                callup.say 'Либо вы что, [player.name]? - прерывает вас [callup.fname].'
                callup.say 'Вы ничего не можете сделать со своим учеником. Если только попробуете, вас не просто уволят с волчьим билетом, так ещё и на кичу посадят, там таких под шконкой весьма любят. Или вы уже в курсе?'
                player.say '???????'
                '[callup.name], скорчив презрительную гримасу удаляется из кабинета, не спрашивая вашего разрешения.'
                'Похоже что то пошло не так.'
                python:
                    callup = dummy
                    move(curloc)
        'Выгнать':
            player.say '[callup.name]! Немедленно покинь мой кабинет!'
            callup.say 'Да как хотите. - [callup.fname] закатывает глаза и уходит.'
            python:
                callup = dummy
                move(curloc)