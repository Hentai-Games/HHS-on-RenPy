##############################################################################
# кастомные скрины
##############################################################################
init python:
    import string
    myItem = 0
    mySet = []
    voteDecision = False
    last_inventory = 'all'
    def inv_show_list(type) :
        global myItem
        if not type in ['all','clothing','present','sexShop','dif']:
            type = 'all'
        list = []
        showed = []
        for x in player.inventory:
            if type == 'all' and not x.name in showed:
                list += [x]
                showed += [x.name]
            elif type == 'clothing' and x.type == type:
                list += [x]
            elif type == 'present' and x.type == type:
                list += [x]
            elif type == 'sexShop' and (x.type == type or x.type == 'lust'):
                list += [x]
            elif type == 'dif' and (x.type == 'food' or x.type == 'tool'):
                list += [x]
        if len(list) > 0 :
            if not myItem in list :
                myItem = list[0]
        else :
            myItem = 0        
        return list
    def inv_action (item):
        if item.type == 'food':
            return [Function(player.eat, item), Function(move,curloc)] 
        elif item.type == 'tool':
            if item.purpose == 'camera':
                return [Jump('installCam')]
        elif item.type == 'lust':
            return [Jump('use_tablet')]
        else :
            return [NullAction()]
        return [NullAction()]
##############################################################################
# Основной скрин статистики
##############################################################################
screen stats_screen:
    # tag interface
    # add 'pic/overlay.png'
    fixed xpos 0.01 ypos 0.01:
        vbox xmaximum config.screen_width/2:
            $ currtime = gettime('day')
            text '[currtime]' style style.param
            if lt() > 0 :
                text _('Сейчас идёт '+ str(lt()) +' урок') style style.paramwarning
            elif lt() == 0 :
                text _('Сейчас перемена') style style.paramgreen
            elif lt() == -1 :
                text _('Сейчас нет уроков') style style.param
            elif lt() == -3 :
                text _('Сегодня выходной') style style.paramgreen
            elif lt() == -4 :
                text _('Сейчас ночь') style style.paramwarning
            else :
                text _('{b}Сейчас БАГ{b}') style style.paramwarning    
            if development > 0:    
                textbutton ('Список эвентов') action Show('pomogator') style "small_button" text_style "small_button_text" xalign 0.0
            null height 10
            $ temp = int(player.stats.energy)
            if temp > player.stats.health/10:
                text _('Ваша энергия: [temp]') style style.param
            else:
                text _('Ваша энергия: [temp]') style style.paramwarning
            null height 10
            # Warnings
            if ptime - last_eat > 24:
                text _('Вы голодаете') style style.paramwarning
            elif ptime - last_eat > 15:
                text _('Вы голодны') style style.param

            if player.isSperm() > 0:
                $ temp = player.printSperm()
                text _('В сперме [temp]') style style.paramwarning

            if player.getDirty() == 1:
                text _('Вы слегка вспотели') style style.param
            if player.getDirty() == 2:
                text _('Вы вспотели') style style.param
            if player.getDirty() == 3:
                text _('От вас воняет') style style.param
            if player.getDirty() >= 4:
                text _('От вас воняет, как от последнего бомжа') style style.paramwarning

            # Buttons
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
            if len(getLoc(curloc).getPeople()) > 0:
                if show_peopleTextList == 0:
                    textbutton ('Показать людей') action SetVariable('show_peopleTextList',1) style "small_button" text_style "small_button_text" xalign 0.0
                else:
                    textbutton ('Скрыть людей') action SetVariable('show_peopleTextList',0) style "small_button" text_style "small_button_text" xalign 0.0
                    
                if show_peopleTextList == 1:
                    use peopleTextList
            # if development > 0:
                # use showStatuses
                # use showStatusEvents

    fixed xpos 0.25 ypos 0.01:
        grid 4 1:
            grid 2 1:
                $temp = getPar(studs, 'edu')
                text _('Учёба') style style.param
                if temp > stat_edu:
                    text ' [temp]' style style.paramgreen
                elif temp < stat_edu:
                    text ' [temp]' style style.paramwarning
                else :
                    text ' [temp]' style style.param
                python:
                    global stat_edu
                    stat_edu = temp            
            grid 2 1:
                text _('Лояльность') style style.param
                $ temp = getPar(studs, 'loy')
                if temp > stat_loy:
                    text ' [temp]' style style.paramgreen
                elif temp < stat_loy:
                    text ' [temp]' style style.paramwarning
                else :
                    text ' [temp]' style style.param
                python:
                    global stat_loy
                    stat_loy = temp
            grid 2 1:
                $temp = getPar(studs, 'rep')
                text _('Репутация ') style style.param
                if temp > stat_rep:
                    text ' [temp]' style style.paramgreen
                elif temp < stat_rep:
                    text ' [temp]' style style.paramwarning
                else :
                    text ' [temp]' style style.param
                python:
                    global stat_rep
                    stat_rep = temp
            grid 2 1:
                $ temp = getPar(studs, 'corr')
                text _('Разврат') style style.param
                if temp > stat_corr:
                    text ' [temp]' style style.paramgreen
                elif temp < stat_corr:
                    text ' [temp]' style style.paramwarning
                else :
                    text ' [temp]' style style.param
                python:
                    global stat_corr
                    stat_corr = temp            

    vbox xalign 0.99 yalign 0.0:
        if minute < 10:
            $ temtime = '%s:0%s' % (hour, minute)
        else:
            $ temtime = '%s:%s' % (hour, minute)
        text '[temtime]' style style.mytimer xalign 0.99
        null height 10
        text '{u}Промотать:{/u}' style style.param xalign 0.99
        grid 2 1:
            xalign 0.99
            imagebutton auto 'pic/actions/wait15_%s.png' action [Function(waiting,15)]
            imagebutton auto 'pic/actions/wait60_%s.png' action [Function(waiting,60)]
        text '{u}Посмотреть:{/u}' style style.param xalign 0.99
        grid 2 1:         
            xalign 0.99
            imagebutton :
                idle im.FactorScale('pic/actions/smartphone_idle.png', 0.5) 
                hover im.FactorScale('pic/actions/smartphone.png', 0.5) 
                action [Hide('stats_screen'), Hide('showStatistic'), Jump('notebook')]
                hovered [Show('showStatistic')] 
                unhovered [Hide('showStatistic')]
            imagebutton auto 'pic/actions/inventory_%s.png' action [Function(clrscr), Show('inventory_unit')]
        grid 2 1:  
            xalign 0.99
            null
            if getLoc(curloc) != False:
                if len(getLoc(curloc).getPeople()) > 0:
                    imagebutton auto 'pic/actions/eye_%s.png' action [Function(clrscr),Jump('locationPeople')]
                else:
                    null
        grid 2 1:  
            xalign 0.99
            null       
            if curloc == 'loc_beach' or curloc == 'loc_street' or curloc == 'loc_shopStreet' or curloc == 'loc_entrance':
                imagebutton auto 'pic/actions/taxi_%s.png' action [Function(move, 'loc_taxi')]
            else:
                null
        grid 2 1:  
            xalign 0.99
            null        
            if curloc == 'loc_teacherRoom':
                imagebutton:
                    idle im.MatrixColor('pic/actions/corrMeeting.png', im.matrix.opacity(0.5))
                    hover im.MatrixColor('pic/actions/corrMeeting.png', im.matrix.opacity(1.0))   
                    action [Function(clrscr), Jump('select_corrMeeting')]
            else:
                null

        text '{u}Действия:{/u}' style style.param xalign 0.99
        for lab, act, req in loc_btn :
            if req:
                if lab[:3] != '{i}':
                    textbutton lab:
                        xalign 0.99
                        action act
                        style "navigation_button" text_style "navigation_button_text"
                else:
                    textbutton lab:
                        xalign 0.99
                        action act
                        style "navigation_button" text_style "action_button_text"
                   
        if curloc == 'loc_shopBeauty' : 
            use shopBeautyBtn 
    
    fixed :
        vbox:
            yalign 0.99
            for tmp_text in loc_txt :
                text '[tmp_text]' :
                    style style.description 
    

screen showStatistic:
    zorder 1
    fixed xpos 0.72 ypos 0.1:
        grid 1 2 : 
            frame style style.peopleTextList:
                xalign 0.01
                vbox:
                    text '{u}Ваши параметры:{/u} ' style style.param
                    python:
                        name = player.fullName()
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
                
                    null height 10
                    text _('{u}[name]{/u}') style style.my_text
                    text _('Развратность: [corr]') style style.my_text
                    text _('Желание: [lust]') style style.my_text
                    text _('Здоровье: [health]') style style.my_text
                    text _('Размер груди: [bsize]') style style.my_text
                    text _('Рост: [height]') style style.my_text
                    text _('IQ: [intel]') style style.my_text
                    text _('Счастье: [fun]') style style.my_text
                    text _('Красота: [beauty]') style style.my_text
                    # text ''
                    text _('Денег: [money]') style style.my_text
            frame style style.peopleTextList:
                xalign 0.99
                vbox:
                    text ''
                    text '{u}Параметры школы:{/u} ' style style.param
                    python:   
                        St_l = getPar(studs, 'loy')
                        St_f = getPar(studs, 'fun')
                        St_lu = getPar(studs, 'lust')
                        St_c = getPar(studs, 'corr')
                        St_e = getPar(studs, 'edu')
                        St_r = getPar(studs, 'rep')

                    null height 10
                    text _('Лояльность: [St_l]') style style.my_text
                    text _('Счастье: [St_f]') style style.my_text
                    text _('Желание: [St_lu]') style style.my_text
                    text _('Разврат: [St_c]') style style.my_text
                    text _('Учёба: [St_e]') style style.my_text
                    text _('Репутация: [St_r]') style style.my_text
              
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
# Инвентарь v 2
##############################################################################
screen inventory_unit:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            key "game_menu" action Function(move, curloc)
            textbutton _('Назад') action Function(move, curloc)
            textbutton _('Всё') action [SetVariable('last_inventory','all'), Function(clrscr),Show('inventory_unit')]
            textbutton _('Одежда') action [SetVariable('last_inventory','clothing'), Function(clrscr),Show('inventory_unit')]
            textbutton _('Подарки') action [SetVariable('last_inventory','present'), Function(clrscr), Show('inventory_unit')]
            textbutton _('Спецвещи') action [SetVariable('last_inventory','sexShop'), Function(clrscr),Show('inventory_unit')]
            textbutton _('Разное') action [SetVariable('last_inventory','dif'), Function(clrscr),Show('inventory_unit')]
    $ adj = ui.adjustment()
    python:
        tab_i = inv_show_list(last_inventory)
        tab_cols = 10.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        area (250, 75, 925, 660)
        viewport:
            yadjustment adj
            mousewheel True
            grid tab_cols tab_rows:   
                xfill True
                spacing 10
                for x in tab_i:
                    imagebutton:
                        idle im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(0.7))
                        hover im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(1.0))
                        hovered [SetVariable('myItem', x)] 
                        action inv_action (x)
                for i in range(int(tab_n)):
                    vbox:
                        null
        bar adjustment adj style "vscrollbar"
    use showItem

# менюшка с описанием предмета слева
screen showItem:
    zorder 1

    vbox xpos 0.01 ypos 0.1:
        if myItem != 0:
            add myItem.picto
            null height 10
            text '[myItem.name]' style style.my_text
            if myItem.type == 'clothing':
                frame style style.peopleTextList xsize 200:
                    text _('[myItem.description]') style style.my_text
            $ temp = player.countItems(myItem.name)
            text _('Количество [temp]') style style.my_text
            if myItem.type != 'present': 
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
                textbutton _('Выбросить') action [Hide ('showItem'), Function(player.FremoveItem, myItem)]


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

        key "game_menu" action Function(move, curloc)
        textbutton _('Назад') action Function(move, curloc)
    $ adj = ui.adjustment()
    python:
        tab_i = [x for x in player.inventory if x.type == 'clothing']
        tab_cols = 6.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        area (250, 40, 580, 700)
        viewport:
            yadjustment adj
            mousewheel True
            grid tab_cols tab_rows:   
                xfill True
                spacing 10
                for x in tab_i:
                    imagebutton:
                        idle im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(0.7))
                        hover im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(1.0))  
                        action [Function(player.Fwearing,x),Show('wardrobe')] 
                        hovered [SetVariable('myItem', x), Show('showItem')] 
                        unhovered Hide ('showItem')
                for i in range(int(tab_n)):
                    vbox:
                        null
        bar adjustment adj style "vscrollbar"
    
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
                    
    fixed xpos 0.7 ypos 0.7:
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
    fixed xpos 0.7 ypos 0.68:
        frame yanchor 1.0:
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
                
                
    fixed xpos 0.01 ypos 0.5:
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
                    
    # fixed xpos 0.01 ypos 0.3:
        # $ xalig = 0.01
        # $ yalig = 0.1
        # $ counter = 0
        # for status in _locs: # перебираем все лейблы
            # if status[:7] == 'status_': #находим тот, что со статусом
                # $ counter += 1
                # textbutton _(str(counter)+ '. ' +status) xpos xalig ypos yalig action [SetVariable('interactionObj', getChar()), Jump(status)] style "small_button" text_style "small_button_text" xalign 0.0
                # $ xalig += 0.25
                # if xalig >= 0.8:
                    # $ yalig += 0.02
                    # $ xalig = 0.01
        
            
