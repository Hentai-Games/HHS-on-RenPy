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
                textbutton ('Список эвентов') action Show('pomogator') style "small_button" text_style "small_button_text" xalign 0.0
            
            #Warnings
            if ptime - last_eat > 24:
                text _('Вы голодаете') style style.warning
            elif ptime - last_eat > 15:
                text _('Вы голодны') style style.my_text

            if player.isSperm() > 0:
                $ temp = player.printSperm()
                text _('В сперме [temp]') style style.warning

            if player.getDirty() == 1:
                text _('Вы слегка вспотели') style style.my_text
            if player.getDirty() == 2:
                text _('Вы вспотели') style style.my_text
            if player.getDirty() == 3:
                text _('От Вас воняет') style style.my_text
            if player.getDirty() >= 4:
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
                    
            if show_peopleTextList == 0:
                textbutton ('Показать людей') action SetVariable('show_peopleTextList',1) style "small_button" text_style "small_button_text" xalign 0.0
            else:
                textbutton ('Скрыть людей') action SetVariable('show_peopleTextList',0) style "small_button" text_style "small_button_text" xalign 0.0
                
            if show_peopleTextList == 1:
                use peopleTextList
            # if development > 0:
                # use showStatuses
                # use showStatusEvents

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
                $ temp = int(player.stats.energy)
                if temp > player.stats.health/10:
                    text _('Ваша энергия ') style style.my_text
                    text ' [temp]' style style.my_text
                else:
                    text _('Ваша энергия ') style style.warning
                    text ' [temp]' style style.warning

                $ temp = round(player.getLust(),1)
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
                
                $ temp = int(player.money)
                text _('Денег') style style.my_text
                text ' [temp]' style style.my_text

    vbox xalign 0.99 yalign 0.01:
        imagebutton auto 'pic/actions/wait15_%s.png' action [Function(waiting,15)]
        imagebutton auto 'pic/actions/wait60_%s.png' action [Function(waiting,60)]
        imagebutton idle im.FactorScale('pic/actions/smartphone_idle.png', 0.5) hover im.FactorScale('pic/actions/smartphone.png', 0.5) action [Hide('stats_screen'), Jump('notebook')]
        imagebutton auto 'pic/actions/inventory_%s.png' action [Function(clrscr), Show(last_inventory)]
        if curloc == 'loc_beach' or curloc == 'loc_street' or curloc == 'loc_shopStreet' or curloc == 'loc_entrance':
            imagebutton auto 'pic/actions/taxi_%s.png' action [Function(move, 'loc_taxi')]
        if getLoc(curloc) != False:
            if len(getLoc(curloc).getPeople()) > 0:
                imagebutton auto 'pic/actions/eye_%s.png' action [Function(clrscr),Jump('locationPeople')]
                
              
screen showStatuses:
    fixed:
        vbox:
            $ showed[:] = []
            for x in getLoc(curloc).getStatuses():
                if x.name not in showed:
                    text x.name style style.my_text
                $ showed.append(x.name)
            
              
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
# Инвентарь весь
##############################################################################
screen inventory_all:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        $ showed[:] = []
        hbox :
            textbutton _('Назад') action Function(move, curloc)
            textbutton _('Всё') action [SetVariable('last_inventory','inventory_all'), Function(clrscr),Show('inventory_all')]
            textbutton _('Одежда') action [SetVariable('last_inventory','inventory_clothing'), Function(clrscr),Show('inventory_clothing')]
            textbutton _('Подарки') action [SetVariable('last_inventory','inventory_presents'), Function(clrscr), Show('inventory_presents')]
            textbutton _('Спец вещи') action [SetVariable('last_inventory','inventory_sexShop'), Function(clrscr),Show('inventory_sexShop')]
            textbutton _('Разное') action [SetVariable('last_inventory','inventory'), Function(clrscr),Show('inventory')]
        $ xalig = 0.2
        $ yalig = 0.05
        for x in player.inventory:
            if x.name not in showed:
                if x.type == 'sexShop':
                    imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action NullAction() hovered [SetVariable('myItem', x), Show('showItem')]
                elif x.type == 'present':
                    imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action NullAction() hovered [SetVariable('myItem', x), Show('showItem')]
                elif x.type == 'clothing':
                    imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action NullAction() hovered [SetVariable('myItem', x), Show('showItem')]
                elif x.type == 'food':
                    imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action [Function(player.eat, x), Function(move,curloc)] hovered [SetVariable('myItem', x), Show('showItem')]
                elif x.type == 'tool':
                    if x.purpose == 'camera':
                        imagebutton:
                            idle im.FactorScale(x.picto,0.4) 
                            hover im.FactorScale(x.picto,0.45) 
                            xalign xalig yalign yalig  
                            action Jump('installCam')
                            hovered [SetVariable('myItem', x), Show('showItem')]
                    else:
                        imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action NullAction() hovered [SetVariable('myItem', x), Show('showItem')]
                else:
                    imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action NullAction() hovered [SetVariable('myItem', x), Show('showItem')]
                python:
                    showed.append(x.name)
            else:
                $ xalig -= 0.09
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2
                
screen inventory:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        $ showed[:] = []
        hbox :
            textbutton _('Назад') action Function(move, curloc)
            textbutton _('Всё') action [SetVariable('last_inventory','inventory_all'), Function(clrscr),Show('inventory_all')]
            textbutton _('Одежда') action [SetVariable('last_inventory','inventory_clothing'), Function(clrscr),Show('inventory_clothing')]
            textbutton _('Подарки') action [SetVariable('last_inventory','inventory_presents'), Function(clrscr), Show('inventory_presents')]
            textbutton _('Спец вещи') action [SetVariable('last_inventory','inventory_sexShop'), Function(clrscr),Show('inventory_sexShop')]
            textbutton _('Разное') action [SetVariable('last_inventory','inventory'), Function(clrscr),Show('inventory')]
        $ xalig = 0.2
        $ yalig = 0.05
        for x in player.inventory:
            if x.type == 'food':
                imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action [Function(player.eat, x), Function(move,curloc)] hovered [SetVariable('myItem', x), Show('showItem')]
            elif x.type == 'tool' and x.name not in showed:
                if x.purpose == 'camera':
                    imagebutton:
                        idle im.FactorScale(x.picto,0.4) 
                        hover im.FactorScale(x.picto,0.45) 
                        xalign xalig yalign yalig  
                        action Jump('installCam')
                        hovered [SetVariable('myItem', x), Show('showItem')]
                else:
                    imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action NullAction() hovered [SetVariable('myItem', x), Show('showItem')]
                python:
                    showed.append(x.name)
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
            textbutton _('Всё') action [SetVariable('last_inventory','inventory_all'), Function(clrscr),Show('inventory_all')]
            textbutton _('Одежда') action [SetVariable('last_inventory','inventory_clothing'), Function(clrscr),Show('inventory_clothing')]
            textbutton _('Подарки') action [SetVariable('last_inventory','inventory_presents'), Function(clrscr), Show('inventory_presents')]
            textbutton _('Спец вещи') action [SetVariable('last_inventory','inventory_sexShop'), Function(clrscr),Show('inventory_sexShop')]
            textbutton _('Разное') action [SetVariable('last_inventory','inventory'), Function(clrscr),Show('inventory')]
            
        $ xalig = 0.2 # Starting x position
        $ yalig = 0.05 # Starting y position
        for x in player.inventory: # for all items in player inventory
            if x.type == 'clothing': 
                imagebutton: # imagebutton with item
                    idle im.FactorScale(x.picto,0.4) 
                    hover im.FactorScale(x.picto,0.45) 
                    xalign xalig yalign yalig  
                    action NullAction() 
                    hovered [SetVariable('myItem', x), Show('showItem')]
            else :
                $ xalig -= 0.09
            $ xalig += 0.09 # Every item xpos is a bit righter
            if xalig >= 0.99: # if end of screen, "new line" of items
                $ yalig += 0.15
                $ xalig = 0.2
                
# Показ подарков
screen inventory_presents:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            textbutton _('Назад') action Function(move, curloc)
            textbutton _('Всё') action [SetVariable('last_inventory','inventory_all'), Function(clrscr),Show('inventory_all')]
            textbutton _('Одежда') action [SetVariable('last_inventory','inventory_clothing'), Function(clrscr),Show('inventory_clothing')]
            textbutton _('Подарки') action [SetVariable('last_inventory','inventory_presents'), Function(clrscr), Show('inventory_presents')]
            textbutton _('Спец вещи') action [SetVariable('last_inventory','inventory_sexShop'), Function(clrscr),Show('inventory_sexShop')]
            textbutton _('Разное') action [SetVariable('last_inventory','inventory'), Function(clrscr),Show('inventory')]

        $ xalig = 0.2
        $ yalig = 0.05
        for x in player.inventory:
            if x.type == 'present':
                imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action NullAction() hovered [SetVariable('myItem', x), Show('showItem')]
            else :
                $ xalig -= 0.09
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2
                
# Показ афродизиаков, дилдаков и прочее
screen inventory_sexShop:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            textbutton _('Назад') action Function(move, curloc)
            textbutton _('Всё') action [SetVariable('last_inventory','inventory_all'), Function(clrscr),Show('inventory_all')]
            textbutton _('Одежда') action [SetVariable('last_inventory','inventory_clothing'), Function(clrscr),Show('inventory_clothing')]
            textbutton _('Подарки') action [SetVariable('last_inventory','inventory_presents'), Function(clrscr), Show('inventory_presents')]
            textbutton _('Спец вещи') action [SetVariable('last_inventory','inventory_sexShop'), Function(clrscr),Show('inventory_sexShop')]
            textbutton _('Разное') action [SetVariable('last_inventory','inventory'), Function(clrscr),Show('inventory')]

        $ xalig = 0.2
        $ yalig = 0.05
        for x in player.inventory:
            if x.type == 'sexShop':
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
            $ temp = player.countItems(myItem.name)
            text _('Количество [temp]') style style.my_text
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
# Гардероб
##############################################################################
screen wardrobe:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
        if development == 0:
            add 'pic/events/various/undress.png' at Move((0.8, 2.0), (0.8, 0.8), 0.5, xanchor='center', yanchor='center')

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
    
    frame ypos 0.01 xalign 1.0:
        text 'Текущая сексуальность: ' + str(player.getOutfitLust())
    
    fixed xpos 0.7 ypos 0.1 :
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
            textbutton _(str(counter)+ '. ' +event.id) xpos xalig ypos yalig action Function(move, event.id) style "small_button" text_style "small_button_text" xalign 0.0
            $ xalig += 0.25
            if xalig >= 0.8:
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
    fixed xpos 0.01 ypos 0.3:
        $ xalig = 0.01
        $ yalig = 0.1
        $ counter = 0
        for status in _locs: # перебираем все лейблы
            if status[:7] == 'status_': #находим тот, что со статусом
                $ counter += 1
                textbutton _(str(counter)+ '. ' +status) xpos xalig ypos yalig action [SetVariable('interactionObj', getChar()), Jump(status)] style "small_button" text_style "small_button_text" xalign 0.0
                $ xalig += 0.25
                if xalig >= 0.8:
                    $ yalig += 0.02
                    $ xalig = 0.01
        
            
