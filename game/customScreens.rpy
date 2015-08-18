##############################################################################
# кастомные скрины
##############################################################################
init python:
    myItem = 0
    mySet = []
    voteDecision = False
##############################################################################
# Основной скрин статистики
##############################################################################
screen stats_screen:
 #   tag interface
    fixed xpos 0.01 ypos 0.01:
        vbox xmaximum config.screen_width/2:
            $ currtime = gettime()
            text '[currtime]' style style.my_text
            if lt() > 0:
                text _('Сейчас идёт '+ str(lt()) +' урок') style style.my_text
            if lt() == 0:
                text _('Сейчас перемена') style style.my_text
            if lt() < 0:
                text _('Сейчас нет уроков') style style.my_text
            if development > 0:    
                textbutton ('Список эвентов') action Show('pomogator') style "small_button" text_style "small_button_text"
            
            #Warnings
            if ptime - last_eat > 24:
                text _('Вы голодаете') style style.warning
            elif ptime - last_eat > 15:
                text _('Вы голодны') style style.my_text

            if player.isSperm() > 0:
                $ temp = player.printSperm()
                text _('В сперме [temp]') style style.warning

            if player.stats.dirty == 1:
                text _('Вы слегка вспотели') style style.my_text
            if player.stats.dirty == 2:
                text _('Вы вспотели') style style.my_text
            if player.stats.dirty == 3:
                text _('От Вас воняет') style style.my_text
            if player.stats.dirty >= 4:
                text _('От вас воняет, как от последнего бомжа') style style.warning

            #Buttons
            hbox style style.myBox:
                if player.getSperm('лицо') == True:
                    imagebutton auto 'pic/actions/face_%s.png' action Jump('cleanFace')
                if player.getSperm('рот') == True:
                    imagebutton auto 'pic/actions/mouth_%s.png' action Jump('cleanMouth')
                if player.getSperm('грудь') == True:
                    imagebutton auto 'pic/actions/body_%s.png' action Jump('cleanBody')
                if player.getSperm('руки') == True:
                    imagebutton auto 'pic/actions/hands_%s.png' action Jump('cleanHands')
                if player.getSperm('ноги') == True:
                    imagebutton auto 'pic/actions/feet_%s.png' action Jump('cleanFeet')
                if player.getSperm('вагина') == True:
                    imagebutton auto 'pic/actions/pussy_%s.png' action Jump('cleanPussy')
                if player.getSperm('анус') == True:
                    imagebutton auto 'pic/actions/ass_%s.png' action Jump('cleanAss')


    fixed xpos 0.3 ypos 0.01:
        hbox:
            grid 2 2:
                text _('Лояльность') style style.my_text
                $ temp = getPar(studs, 'loy')
                if temp > stat_loy:
                    text ' [temp]' style style.green
                elif temp < stat_loy:
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_loy
                    stat_loy = temp

                $ temp = getPar(studs, 'fun')
                text _('Счастье') style style.my_text
                if temp > stat_fun:
                    text ' [temp]' style style.green
                elif temp < stat_fun:
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_fun
                    stat_fun = temp

            grid 2 2:
                $temp = getPar(studs, 'lust')
                text _('Желание') style style.my_text
                if temp > stat_lust:
                    text ' [temp]' style style.green
                elif temp < stat_lust:
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_lust
                    stat_lust = temp

                $ temp = getPar(studs, 'corr')
                text _('Разврат') style style.my_text
                if temp > stat_corr:
                    text ' [temp]' style style.green
                elif temp < stat_corr:
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_corr
                    stat_corr = temp


            grid 2 2:
                $temp = getPar(studs, 'edu')
                text _('Учёба') style style.my_text
                if temp > stat_edu:
                    text ' [temp]' style style.green
                elif temp < stat_edu:
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_edu
                    stat_edu = temp

                $temp = getPar(studs, 'rep')
                text _('Репутация ') style style.my_text
                if temp > stat_rep:
                    text ' [temp]' style style.green
                elif temp < stat_rep:
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_rep
                    stat_rep = temp

            grid 2 3:
                $ temp = round(player.stats.energy, 0)
                if temp > player.stats.health/10:
                    text _('Ваша энергия ') style style.my_text
                    text ' [temp]' style style.my_text
                else:
                    text _('Ваша энергия ') style style.warning
                    text ' [temp]' style style.warning

                $ temp = round(player.stats.lust,0)
                text _('Ваше желание ') style style.my_text
                if temp > stat_plust:
                    text ' [temp]' style style.green
                elif temp < stat_plust:
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_plust
                    stat_plust = temp
                
                $ temp = player.money
                text _('Денег') style style.my_text
                text ' [temp]' style style.my_text

    vbox xalign 0.99 yalign 0.01:
        imagebutton auto 'pic/actions/wait15_%s.png' action [Function(waiting,15)]
        imagebutton auto 'pic/actions/wait60_%s.png' action [Function(waiting,60)]
        imagebutton idle im.FactorScale('pic/actions/smartphone_idle.png', 0.5) hover im.FactorScale('pic/actions/smartphone.png', 0.5) action [Hide('stats_screen'), Jump('notebook')]
        imagebutton auto 'pic/actions/inventory_%s.png' action [Function(clrscr), Show('inventory')]
        if curloc == 'loc_beach' or curloc == 'loc_street' or curloc == 'loc_shopStreet' or curloc == 'loc_entrance':
            imagebutton auto 'pic/actions/taxi_%s.png' action [Function(move, 'loc_taxi')]
        if getLoc(curloc) != False:
            if len(getLoc(curloc).people) > 0:
                imagebutton auto 'pic/actions/eye_%s.png' action [Function(clrscr),Jump('locationPeople')]

##############################################################################
# Стартовый скрин выбора персонажа
##############################################################################
screen char_select:
    fixed:
        text 'Выберите персонаж' xalign 0.5 yalign 0.1 style style.description
        imagebutton idle 'pic/Hero/1.png' hover im.FactorScale('pic/Hero/1.png',1.1) xalign 0.2 yalign 0.5 action [SetVariable('_picture','pic/Hero/1.png'), Jump('gendir')]
        imagebutton idle 'pic/Hero/2.png' hover im.FactorScale('pic/Hero/2.png',1.1) xalign 0.4 yalign 0.5 action [SetVariable('_picture','pic/Hero/2.png'), Jump('gendir')]
        imagebutton idle 'pic/Hero/3.png' hover im.FactorScale('pic/Hero/3.png',1.1) xalign 0.6 yalign 0.5 action [SetVariable('_picture','pic/Hero/3.png'), Jump('gendir')]
        imagebutton idle 'pic/Hero/4.png' hover im.FactorScale('pic/Hero/4.png',1.1) xalign 0.8 yalign 0.5 action [SetVariable('_picture','pic/Hero/4.png'), Jump('gendir')]
        
##############################################################################
# Инвентарь
##############################################################################
screen inventory:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            textbutton _('Назад') action Function(move, curloc)
            textbutton _('Одежда') action [Hide('inventory'),Hide('showItem'),Show('inventory_clothing')]

        $ xalig = 0.2
        $ yalig = 0.05
        for x in player.inventory:
            if x.type == 'food':
                imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action [Function(player.eat, x), Function(move,curloc)] hovered [SetVariable('myItem', x), Show('showItem')]
            elif x.type == 'tool':
                imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action NullAction() hovered [SetVariable('myItem', x), Show('showItem')]
            else:
                $ xalig -= 0.09
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2

# показ шмоток
screen inventory_clothing:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            textbutton _('Назад') action Function(move, curloc)
            textbutton _('Разное') action [Function(clrscr),Show('inventory')]

        $ xalig = 0.2
        $ yalig = 0.05
        for x in player.inventory:
            if x.type == 'clothing':
                imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action NullAction() hovered [SetVariable('myItem', x), Show('showItem')]
            else :
                $ xalig -= 0.09
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2
# менюшка с описанием предмета слева
screen showItem:
    zorder 1
    vbox xpos 0.01 ypos 0.1:
        if myItem != 0:
            add myItem.picto
            null height 10
            text '[myItem.name]' style style.my_text
            text _('Использований [myItem.durability]') style style.my_text
            if myItem.type == 'food':
                text _('Насыщение [myItem.energy]') style style.my_text
            if myItem.type == 'clothing':
                if myItem.corr > player.stats.corr:
                    text _('Требует развратности [myItem.corr]') style style.warning
                else :
                    text _('Требует развратности [myItem.corr]') style style.my_text
                text _('Сексуальность [myItem.lust]') style style.my_text
                text _('Репутация [myItem.reputation]') style style.my_text
                if development > 0:
                    text _('Чей [myItem.sex]') style style.my_text
                    text _('Назначение [myItem.purpose]') style style.my_text
            if player.hasItem(myItem.name):
                textbutton _('Выбросить') action [Function(player.removeItem, myItem), Hide ('showItem')]


##############################################################################
# Магазин
##############################################################################
screen shopping:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    frame :
        xalign 1.0
        text _('Денег - [player.money]')
    fixed xpos 0.01 ypos 0.01:
        textbutton _('Назад') action Function(move, curloc)
        hbox xpos 0.2 ypos 0.1:
            frame :
                vbox :
                    text _('Разное')
                    textbutton napkin.name action [Function(player.buy, napkin), Show('showSellItem')] hovered [SetVariable('myItem', napkin), Show('showSellItem')]
                    textbutton eDrink.name action [Function(player.buy, eDrink), Show('showSellItem')] hovered [SetVariable('myItem', eDrink), Show('showSellItem')]
                    textbutton rawFood.name action [Function(player.buy, rawFood), Show('showSellItem')] hovered [SetVariable('myItem', rawFood), Show('showSellItem')]
            frame :
                vbox :
                    #Список предметов на продажу
                    text _('Одежда')
                    textbutton jaket.name action [Function(player.buy, jaket, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', jaket), Show('showSellItem')]
                    textbutton longSkirt.name action [Function(player.buy, longSkirt, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', longSkirt), Show('showSellItem')]
                    textbutton browntights.name action [Function(player.buy, browntights, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', browntights), Show('showSellItem')]
                    textbutton swimsuit.name action [Function(player.buy, swimsuit, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', swimsuit), Show('showSellItem')]
                    textbutton bikini_top.name action [Function(player.buy, bikini_top, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', bikini_top), Show('showSellItem')]
                    textbutton bikini_bottom.name action [Function(player.buy, bikini_bottom, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', bikini_bottom), Show('showSellItem')]
                    textbutton minibikini.name action [Function(player.buy, minibikini, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', minibikini), Show('showSellItem')]
                    textbutton freejaket.name action [Function(player.buy, freejaket, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', freejaket), Show('showSellItem')]
                    textbutton skimpyjacket.name action [Function(player.buy, skimpyjacket, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', skimpyjacket), Show('showSellItem')]
                    textbutton shortSkirt.name action [Function(player.buy, shortSkirt, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', shortSkirt), Show('showSellItem')]
                    textbutton skimpySkirt.name action [Function(player.buy, skimpySkirt, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', skimpySkirt), Show('showSellItem')]
                    textbutton blacktights.name action [Function(player.buy, blacktights, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', blacktights), Show('showSellItem')]
                    textbutton nettights.name action [Function(player.buy, nettights, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', nettights), Show('showSellItem')]
                    textbutton simpleUnderwear.name action [Function(player.buy, simpleUnderwear, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', simpleUnderwear), Show('showSellItem')]
                    textbutton sexyUnderwear.name action [Function(player.buy, sexyUnderwear, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', sexyUnderwear), Show('showSellItem')]
                    textbutton skimpyUnderwear.name action [Function(player.buy, skimpyUnderwear, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', skimpyUnderwear), Show('showSellItem')]
                    textbutton sportUniform.name action [Function(player.buy, sportUniform, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', sportUniform), Show('showSellItem')]


screen showSellItem:
    zorder 1
    vbox xpos 0.01 ypos 0.1:
        if myItem != 0:
            add myItem.picto
            null height 10
            text _('[myItem.name]') style style.my_text
            text _('Использований [myItem.durability]') style style.my_text
            if myItem.type == 'food':
                text _('Насыщение [myItem.energy]') style style.my_text

            if myItem.type == 'clothing':
                if myItem.corr > player.stats.corr:
                    text _('Требует развратности [myItem.corr]') style style.warning
                else :
                    text _('Требует развратности [myItem.corr]') style style.my_text
                text _('Сексуальность [myItem.lust]') style style.my_text
                text _('Репутация [myItem.reputation]') style style.my_text

            if myItem.cost > player.money:
                 text _('Цена - [myItem.cost]') style style.warning
            else :
                text _('Цена - [myItem.cost]') style style.my_text

            if player.hasItem(myItem.name) > 0:
                $ temp_d = player.getItem(myItem.name).durability
                $ temp_c = player.countItem(myItem.name)
                text _('В наличии [temp_c] шт.') style style.my_text
                text _('Использований - [temp_d]') style style.my_text

##############################################################################
# Гардероб
##############################################################################
screen wardrobe:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
        # add 'pic/events/various/undress.png' at Move((0.8, 2.0), (0.8, 0.8), 0.5, xanchor='center', yanchor='center')

    fixed xpos 0.01 ypos 0.01:
        textbutton _('Назад') action Function(move, curloc)
        $ xalig = 0.2
        $ yalig = 0.05
        for x in player.inventory:
            if x.type == 'clothing':
                imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action [Function(player.wearing,x),Show('wardrobe')] hovered [SetVariable('myItem', x), Show('showItem')] unhovered Hide ('showItem')
            else :
                $ xalig -= 0.09
            $ xalig += 0.09
            if xalig >= 0.7 :
                $ yalig += 0.15
                $ xalig = 0.2

    fixed xpos 0.7 ypos 0.01 :
        frame :
            vbox :
                text _('На вас надето:')
                if len(player.wear) == 0:
                    text _('Ничего')
                else :
                    for x in player.wear:
                        textbutton x.name action [Function( player.dewearing, x ), Show ('wardrobe')] hovered [SetVariable('myItem', x), Show('showItem')] unhovered Hide ('showItem')
                    textbutton _('Раздеться') action [Function( player.undress ), Show ('wardrobe')]
                    
    fixed xpos 0.01 ypos 0.7:
        frame :
            vbox :
                text 'Сеты'
                $ counter = 0
                for x in player.sets:
                    hbox :
                        textbutton _('Сет [counter]') action [Function(player.createSet, counter), Show('wardrobe')]
                        if len(player.sets[counter]) > 0:
                            textbutton _('Надеть') action [Function(player.applySet, counter), Show('wardrobe')] hovered [SetVariable('mySet', x), Show ('showSet')] unhovered Hide('showSet')
                        $ counter += 1
                        
screen showSet:
    zorder 1
    fixed xpos 0.2 ypos 0.7:
        frame:
            vbox:
                for x in mySet:
                    text x

##############################################################################
# Помогатор для теста
############################################################################## 
screen pomogator:
    fixed xpos 0.01 ypos 0.1:
        $ x = getLoc(curloc)
        $ xalig = 0.01
        $ yalig = 0.1
        $ counter = 0
        for event in x.events:
            $ counter += 1
            textbutton _(str(counter)+ '. ' +event.id) xalign xalig yalign yalig action Function(move, event.id) style "small_button" text_style "small_button_text"
            $ xalig += 0.3
            if xalig >= 0.99:
                $ yalig += 0.02
                $ xalig = 0.01
                
                
    fixed xpos 0.01 ypos 0.3:
        vbox:
            $ x = getLoc(curloc+'Learn')
            $ counter = 0
            if x != False:
                for event in x.events:
                    $ counter += 1
                    textbutton _(str(counter)+ '. ' +event.id) action Function(move, event.id) style "small_button" text_style "small_button_text"
                    
    fixed xpos 0.01 ypos 0.5:
        vbox:
            $ x = getLoc(curloc+'Night')
            $ counter = 0
            if x != False:
                for event in x.events:
                    $ counter += 1
                    textbutton _(str(counter)+ '. ' +event.id) action Function(move, event.id) style "small_button" text_style "small_button_text"