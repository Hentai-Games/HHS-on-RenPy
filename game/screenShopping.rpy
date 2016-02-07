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
        key "game_menu" action Function(move, curloc)
        hbox xpos 0.2 ypos 0.1:
            frame :
                vbox :
                    text _('Разное')
                    textbutton napkin.name action [Function(player.buy, napkin), Show('showSellItem')] hovered [SetVariable('myItem', napkin), Show('showSellItem')]
                    textbutton eDrink.name action [Function(player.buy, eDrink), Show('showSellItem')] hovered [SetVariable('myItem', eDrink), Show('showSellItem')]
                    textbutton rawFood.name action [Function(player.buy, rawFood), Show('showSellItem')] hovered [SetVariable('myItem', rawFood), Show('showSellItem')]
                    if is_camera == 3:
                        textbutton camera.name action [Function(player.buy, camera,'add'), Show('showSellItem')] hovered [SetVariable('myItem', camera), Show('showSellItem')]
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
            frame :
                vbox :
                    #Список подарков на продажу
                    text _('Подарки')
                    for x in allItems:
                        if x.type == 'present':
                            if x.corr == 0:
                                textbutton x.name action [Function(player.buy, x, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', x), Show('showSellItem')]


screen showSellItem:
    zorder 1
    vbox xpos 0.01 ypos 0.1:
        if myItem != 0:
            add myItem.picto
            null height 10
            text _('[myItem.name]') style style.my_text
            if myItem.type == 'clothing':
                frame style style.peopleTextList xsize 200:
                    text _('[myItem.description]') style style.my_text
            if myItem.type != 'present':
                text _('Использований [myItem.durability]') style style.my_text
            
            if myItem.type == 'food':
                text _('Насыщение [myItem.energy]') style style.my_text
            
            if myItem.type == 'present':
                if myItem.reputation > 0: 
                    text _('Репутация [myItem.reputation]') style style.my_text
                if myItem.loy > 0: 
                    text _('Лояльность [myItem.loy]') style style.my_text
                if myItem.corr > 0: 
                    text _('Развратность [myItem.corr]') style style.my_text
            
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
                if myItem.type != 'present':
                    text _('Использований - [temp_d]') style style.my_text

screen sexShopping:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    frame :
        xalign 1.0
        text _('Денег - [player.money]')
    fixed xpos 0.01 ypos 0.01:
        key "game_menu" action Function(move, curloc)
        textbutton _('Назад') action Function(move, curloc)
        hbox xpos 0.2 ypos 0.1:
            frame :
                vbox :
                    text _('Афродизиаки')
                    textbutton aphrodisiac.name action [Function(player.buy, aphrodisiac, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', aphrodisiac), Show('showSellItem')]
            frame :
                vbox :
                    #Список предметов на продажу
                    text _('Игрушки')
                    if player.hasItem(rope.name) == False:
                        textbutton rope.name action [Function(player.buy, rope, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', rope), Show('showSellItem')]
            frame :
                vbox :
                    #Список подарков на продажу
                    text _('Подарки')
            frame :
                vbox :
                    #Список одежды на продажу
                    text _('Одежда')
                    textbutton bdsmUniform.name action [Function(player.buy, bdsmUniform, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', bdsmUniform), Show('showSellItem')]
                    