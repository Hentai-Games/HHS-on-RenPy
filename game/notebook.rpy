init python:
    lastNotebookScreen = 'studList'
label notebook:
    show expression "pic/bg.png"
    show screen notebook
    call screen personalInfo

screen notebook:
    fixed xpos 0.01 ypos 0.01:
        hbox :
            textbutton _('Назад') action [Show('stats_screen'), Hide('studList'), Hide('teacherList'), Hide('personalInfo'), Hide('charInfoLeft'), Function(move, curloc)]
            textbutton _('Вы') action [Hide ('charInfoLeft'), Show('personalInfo')]
            textbutton _('Список учеников') action Show('studList')
            textbutton _('Список учителей') action Show('teacherList')
            textbutton _('Статистика школы') action Show('schoolStats')


screen studList:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        $ xalig = 0.17
        $ yalig = 0.01
        for x in studs:
            imagebutton idle im.FactorScale(x.picto,0.5) hover im.FactorScale(x.picto,0.6) xalign xalig yalign yalig action NullAction() hovered [SetVariable('showHover',x),Show('charInfoLeft')] unhovered Hide('charInfoLeft')
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
            imagebutton idle im.FactorScale(x.picto,0.5) hover im.FactorScale(x.picto,0.6) xalign xalig yalign yalig action NullAction() hovered [SetVariable('showHover',x),Show('charInfoLeft')] unhovered Hide('charInfoLeft')
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
                $ playerName = player.fullName()
                text _('[showHover.name]') style style.my_text
                $ temp = showHover.age
                text _('Возраст [temp]') style style.my_text
                $ bsize = showHover.body.parts['грудь'].size
                if bsize > 0:
                    $ temp = round(bsize, 1)
                    text _('Размер груди [temp]') style style.my_text
                else:
                    text '' style style.my_text
                $ temp = round(showHover.body.height,1)
                text _('Рост [temp]') style style.my_text
                $ temp = round(showHover.stats.education,1)
                text _('Образование [temp]') style style.my_text
                $ temp = round(showHover.stats.fun,1)
                text _('Счастье [temp]') style style.my_text
                $ temp = round(showHover.stats.loyalty,1)
                text _('Лояльность [temp]') style style.my_text
                $ temp = round(showHover.stats.corr,1)
                text _('Развратность [temp]') style style.my_text
                $ temp = round(showHover.stats.beauty,1)
                text _('Красота [temp]') style style.my_text

screen personalInfo:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        vbox:
            python:
                name = player.fullName()
                age = str(player.age)
                sex = player.body.sex()
                beauty = player.getBeauty()
                loyalty = player.getLoy()
                edu = player.getEdu()
                lust = player.getLust()
                corr = player.getCorr()
                fun = player.getFun()
                health = player.getHealth()
                height = round(showHover.body.height,1)
                money = player.money
                
                bsize = round(player.body.parts['грудь'].size, 1)
                vsize = round(player.body.parts['вагина'].size)
                asize = round(player.body.parts['анус'].size)
                
            add im.FactorScale(player.picto,.5)
            null height 10
            text _('[name]') style style.my_text
            text _('Размер груди [bsize]') style style.my_text
            text _('Рост [height]') style style.my_text
            text _('Образование [edu]') style style.my_text
            text _('Счастье [fun]') style style.my_text
            text _('Развратность [corr]') style style.my_text
            text _('Красота [beauty]') style style.my_text
            text ''
            text _('Размер вагины [vsize]') style style.my_text
            text _('Размер ануса [asize]') style style.my_text
            text ''
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
            