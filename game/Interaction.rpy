init python:

    class Dialogue():
        def __init__(self, id, corr, type):
            self.id = id
            self.corr = corr
            self.type = type

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
            if speaker.stats.corruption >= x.corr and ((speaker in studs and x.type == 'stud') or (speaker in teachers and x.type == 'teacher')):
                tempList.append(x)
        return tempList[rand(0,len(tempList) - 1)].id
        
    def showChars():
        myImage = player.picto
        if showHover.sex == 'male':
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
            
        renpy.show('temp1', what = Image(myImage, xalign=0.2, yalign= 1.0, yanchor = 'center'), zorder = 1)
        renpy.show('temp2', what = Image(anotherImage, xalign=0.8, yalign= 1.0, yanchor = 'center'), zorder = 1)
        
    dummy = Char()
    interactionObj = ''
    lastView = 'locationPeoplePicto'
    showHover = dummy


label locationPeople:
    show expression "pic/bg.png"
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
            $ temp = round(showHover.stats.corruption, 1)
            text 'Развратность [temp]' style style.my_text
            $ temp = round(showHover.stats.beauty, 1)
            text 'Красота [temp]' style style.my_text
            null height 10

    fixed xpos 0.3 ypos 0.1 :
        vbox xmaximum config.screen_width/2:
            text textgen(showHover) style style.my_text
        
    fixed xpos 0.8 ypos 0.1:
        vbox:
            textbutton 'Поговорить' xminimum 200 action Jump('speak')
            textbutton 'Флирт' xminimum 200 action Jump('flirt')
            textbutton 'Назад' xminimum 200 action Function(move,curloc)

label speak:
    if lt() > 0 or lt() == -2:
        $ renpy.jump('exitInteraction')
    $ user = showHover
    $ changetime(10)
    $ player.stats.energy -= rand(5,10)
    $ user.stats.loyalty += 0.5
    $ renpy.jump(dialogueSelector(user))

    call screen show_stat

label flirt:
    if lt() > 0 or lt() == -2:
        $ renpy.jump('exitInteraction')

    $ user = showHover

    player.say 'Ого какие сиськи!'
    user.say 'Ага!'

    call screen show_stat

label exitInteraction:
    showHover.say 'Простите, мне пора на урок!'
    $ move(curloc)