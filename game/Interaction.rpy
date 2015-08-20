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
                textbutton 'Поговорить' xminimum 200 action Jump('speak')
                textbutton 'Флирт' xminimum 200 action Jump('flirt')
            if 'school' in getLoc(curloc).position and curloc != 'loc_office':
                textbutton 'Вызвать к себе' xminimum 200 action Jump('callup')
            if curloc == 'loc_office':
                textbutton 'Выгнать' xminimum 200 action Jump('callout')
            textbutton 'Карманы' xminimum 200 action Show('inventory_clothing_char')
            textbutton 'Назад' xminimum 200 action Function(move,curloc)
            
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
                
label speak:
    $ clrscr()
    $ user = showHover
    $ changetime(10)
    $ player.stats.energy -= rand(5,10)
    $ user.setLoy(0.5)
    $ renpy.jump(dialogueSelector(user))

    call screen show_stat

label flirt:
    $ clrscr()
    $ user = showHover
    $ changetime(10)
    $ player.stats.energy -= rand(5,10)
    $ renpy.jump(flirtSelector(user))

    call screen show_stat

label callup:
    $ clrscr()
    python:
        getLoc(curloc).people.remove(showHover)
        callup = showHover
    player.say 'Нам необходимо поговорить наедине.'
    callup.say 'Хорошо, я сейчас же отправлюсь к вам в кабинет.'
    $ move(curloc)
    
label callout:
    $ clrscr()
    player.say 'Я думаю, мы закончили, [callup.fname].'
    callup.say 'Хорошо, до свидания, [player.name].'
    $ callup = dummy
    $ move(curloc)