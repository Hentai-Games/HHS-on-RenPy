init:
    image computer = im.FactorScale('pic/events/office/computer/work1.jpg', 1.1)

##############################################################################
# Компьютер
##############################################################################

screen compScreen:
    zorder 1 
    modal True
    add 'computer' at top
    add 'pic/bg.png'
    
    fixed xpos 0.01 ypos 0.01:
        textbutton _('Назад') action Function(move, curloc)
    
    fixed xpos 0.01 ypos 0.1:
        vbox:
            
            if ptime - lastWork > 24:
                textbutton _('Работать') action Show('working')
            textbutton _('Почта') action NullAction()
            textbutton _('Клубы') action NullAction()
            textbutton _('Школьная форма') action Show('schoolUniform')
            textbutton _('Система наказаний') action Show ('detentions')
            textbutton _('Учебники') action Show ('eduMats')
            textbutton _('Мебель и Строения') action Show ('furniture')
            textbutton _('Работа с учениками') action NullAction()
            textbutton _('Проверка камер') action NullAction()
                
screen description(what):
    zorder 1
    fixed xpos 0.01 ypos 0.5:
        vbox:
            if what == 'usual':
                text _('Ученикам будет разрешено приходить в школу в обычной одежде, что позволит им быть более раскрепощёнными, а так же увеличит радость пребывания в "строгих" стенах вашего заведения. Требует пройти проверку на лояльность вам учителей.')
            elif what == 'strict':
                text _('Ученики будут приходить в школу в сторогой форме. Это дисциплинирует их, что приводит к улучшенным показателям в учёбе.')
            elif what == 'normal':
                text _('Обычная школьная форма. Не имеет ни положительных, ни отрицательных качеств.')
            elif what == 'sexy':
                text _('Сексуальная одежда требует пройти проверку на развратность у учителей. Она даст снижение скромности учителей и учеников ежедневно, вплоть до средних значений. Так же она будет повышать развратность учителей и учеников ежедневно. Ну и бонусное возбуждение прямо с утра.')
            elif what == 'skimpy':
                text _('Совершенно нетрадиционная форма. Юбки укорачиваются до состояния пояса, кружевные чулки и глубокие вырезы поощряются, нижнее бельё порицается. Необходима высокая развратность учителей, чтобы ввести эту форму.')
            elif what == 'naked':
                text _('Голая форма требует пройти проверку на развратность у учителей. Она даст сильное снижение скромности учителей и учеников ежедневно, вплоть до нуля. Так же она повысит развратность учителей и учеников ежедневно, вплоть до максимума.')
            elif what == 'education':
                text _('Студенты могут оставаться на дополнительные занятия в третьем классе, после конца уроков, что улучшит их образование и поведение.')
            elif what == 'cleaning':
                text _('Студенты могут убирать кабинеты после уроков, что уменьшит их счастье.')
            elif what == 'streetCleaning':
                text _('Студенты могут убирать улицы, что принесёт Вам небольшой ежедневный доход и уменьшит их счастье. Нужно одобрение педсовета.')
            elif what == 'no':
                text _('Студенты не будут никак наказываться, что уменьшит их послушность и увеличит счастье. Нужно одобрение педсовета.')
            elif what == 'upskirt':
                text _('Ученицы в наказание будут вынуждены после уроков показывать своё нижнее бельё перед классом. Это сподвигнет их стать более скромными и трудолюбивыми. Или наоборот. Кстати, Ваша репутация может пострадать от этого наказания.')
            elif what == 'eduPoor':
                text _('Б/у материалы - это старые учебники, книги купленные у старьёвщиков и на распродаже, самый низкокачественный и плохой продукт, который можно найти. Это сэкономит Вам 1000 монет в неделю.')
            elif what == 'eduStandart':
                text _('Обычные учебники - всё как у всех. Есть несколько хороших учебников, они хранятся в школе, и передаются из класса в класс. В основном материалы немного устаревшие, но Вы и не ставите перед собой задачу вырастить академиков. Этот выбор не принесёт ни убытков, ни бонусов.')
            elif what == 'eduGood':
                text _('Высококлассная литература - это качественная, написанная по последнему слову педагогики, литература рассчитанная на все виды образовательной деятельности. Это прекрасные учебники, по которым приятно, и полезно учиться. Лучший выбор педагога будет стоит Вам 1000 монет в неделю.')
            elif what == 'eduSexy':
                text _('Лучшие сочинения непризнанного педагога Луки Мудищева, окажуться на школьных партах ваших подопечных. Не то, чтобы это было особо дорого, просто как посмотрят на вас родители, если их дети начнут цитировать отрывки из бессмертных произведений автора?')
            else:
                text _('Описания пока нет для [what].')

screen furniture:
    zorder 1
    tag compScreens
    fixed xpos 0.3 ypos 0.1:
        vbox:
            textbutton _('Анатомические манекены (Бюджет - 20000)') action [
                If('manec' in school.furniture, false=Show('preVoting', None, 'corr', 0, 'manec')),
                SelectedIf('manec' in school.furniture),
                SensitiveIf(school.budget > 20000 or 'manec' in school.furniture)
                ] hovered [
                Show('description', None, 'manec') # При наведении показывается описание
                ] unhovered [
                Hide('description') # При потере фокуса - скрывается
                ]
                
            textbutton _('Обучающие видео (Бюджет - 10000)') action [
                If('video' in school.furniture, false=Show('preVoting', None, 'corr', 40, 'video')),
                SelectedIf('video' in school.furniture),
                SensitiveIf(school.budget > 10000 or 'video' in school.furniture)
                ] hovered [
                Show('description', None, 'video') # При наведении показывается описание
                ] unhovered [
                Hide('description') # При потере фокуса - скрывается
                ]
                
            textbutton _('Кровать в офис (Стоимость - 2000)') action [
                If('bed' in school.furniture, false=Show('preVoting', None, 'loy', 15, 'bed')),
                SelectedIf('bed' in school.furniture),
                SensitiveIf(player.money > 2000 or 'bed' in school.furniture)
                ] hovered [
                Show('description', None, 'bed') # При наведении показывается описание
                ] unhovered [
                Hide('description') # При потере фокуса - скрывается
                ]
                
            textbutton _('Стена вокруг школы (Бюджет - 100000)') action [
                If('wall' in school.buildings, false=Show('preVoting', None, 'corr', 20, 'wall')),
                SelectedIf('wall' in school.buildings),
                SensitiveIf(school.budget > 100000 or 'wall' in school.buildings)
                ] hovered [
                Show('description', None, 'wall') # При наведении показывается описание
                ] unhovered [
                Hide('description') # При потере фокуса - скрывается
                ]
                
            textbutton _('Библиотека (Бюджет - 150000)') action [
                If('library' in school.buildings, false=Show('preVoting', None, 'loy', 15, 'library')),
                SelectedIf('library' in school.buildings),
                SensitiveIf(school.budget > 150000 or 'library' in school.buildings)
                ] hovered [
                Show('description', None, 'library') # При наведении показывается описание
                ] unhovered [
                Hide('description') # При потере фокуса - скрывается
                ]
                
screen schoolUniform:
    zorder 1
    tag compScreens
    fixed xpos 0.3 ypos 0.1:
        vbox:
            textbutton _('Обычная одежда') action [
                If('usual' in school.unlockedUniforms, false=Show('preVoting', None, 'loy', 20, 'usual'), true=SetField(school,'uniform','usual')), # Если форма уже открыта, то выбираем её, иначе идём в preVoting
                SelectedIf(school.uniform == 'usual') # кнопка подсвечивается, если выбран этот пункт
                ] hovered [
                Show('description', None, 'usual') # При наведении показывается описание
                ] unhovered [
                Hide('description') # При потере фокуса - скрывается
                ]
                
            textbutton _('Строгая форма') action [
                SetField(school,'uniform','strict'),
                SelectedIf(school.uniform == 'strict')
                ] hovered [
                Show('description', None, 'strict')
                ] unhovered [
                Hide('description')
                ]
            
            textbutton _('Стандартная фома') action [
                SetField(school,'uniform','normal'),
                SelectedIf(school.uniform == 'normal')
                ] hovered [
                Show('description', None, 'normal')
                ] unhovered [
                Hide('description')
                ]
                
            textbutton _('Сексуальная форма') action [
                If('sexy' in school.unlockedUniforms, false=Show('preVoting', None, 'corr', 20, 'sexy'), true=SetField(school,'uniform','sexy')),
                SelectedIf(school.uniform == 'sexy')
                ] hovered [
                Show('description', None, 'sexy')
                ] unhovered [
                Hide('description')
                ]
                
            textbutton _('Шлюховатая форма') action [
                If('skimpy' in school.unlockedUniforms, false=Show('preVoting', None, 'corr', 50, 'skimpy'), true=SetField(school,'uniform','skimpy')),
                SelectedIf(school.uniform == 'skimpy'),
                SensitiveIf('sexy' in school.unlockedUniforms)
                ] hovered [
                Show('description', None, 'skimpy')
                ] unhovered [
                Hide('description')
                ]
                
            textbutton _('Голая форма') action [
                If('naked' in school.unlockedUniforms, false=Show('preVoting', None, 'corr', 80, 'naked'), true=SetField(school,'uniform','naked')),
                SelectedIf(school.uniform == 'naked'),
                SensitiveIf('skimpy' in school.unlockedUniforms)
                ] hovered [
                Show('description', None, 'naked')
                ] unhovered [
                Hide('description')
                ]
 
screen working:
    zorder 1
    tag compScreens
    fixed xpos 0.3 ypos 0.1:
        vbox:
            textbutton _('Заполнять ежедневные бумаги') action [SetVariable('lastWork',ptime), Function(school.working), Hide('working'), Show('compScreen')]
            textbutton _('Выбивать повышение') action [SetVariable('lastWork', ptime), Function(move,'increaseIncome')]
            textbutton _('Вывести часть бюджета') action [SetVariable('lastWork',ptime), Function(school.steal,player)]
            if school.caughtChance > 0:
                textbutton _('Замести следы выведения средств') action [SetVariable('lastWork',ptime), Function(move,'cover')]
            textbutton _('Инвестировать в школу') action [SetVariable('lastWork',ptime), Function(move,'invest')]
            
screen detentions:
    zorder 1
    tag compScreens
    fixed xpos 0.3 ypos 0.1:
        vbox:
            textbutton _('Обучение после уроков') action [
                SetField(school,'detention','education'),
                SelectedIf(school.detention == 'education')
                ] hovered [
                Show('description', None, 'education')
                ] unhovered [
                Hide('description')
                ]
                
            textbutton _('Уборка в школе') action [
                SetField(school,'detention','cleaning'),
                SelectedIf(school.detention == 'cleaning')
                ] hovered [
                Show('description', None, 'cleaning')
                ] unhovered [
                Hide('description')
                ]
                
            textbutton _('Нет наказания') action [
                If('no' in school.unlockedUniforms, false=Show('preVoting', None, 'loy', 20, 'no'), true=SetField(school,'detention','no')),
                SelectedIf(school.detention == 'no')
                ] hovered [
                Show('description', None, 'no')
                ] unhovered [
                Hide('description')
                ]
                
            textbutton _('Уборка улиц') action [
                If('streetCleaning' in school.unlockedUniforms, false=Show('preVoting', None, 'loy', 40, 'streetCleaning'), true=SetField(school,'detention','streetCleaning')),
                SelectedIf(school.detention == 'streetCleaning')
                ] hovered [
                Show('description', None, 'streetCleaning')
                ] unhovered [
                Hide('description')
                ]
        
            textbutton _('Наказание стыдом') action [
                If('upskirt' in school.unlockedUniforms, false=Show('preVoting', None, 'corr', 30, 'upskirt'), true=SetField(school,'detention','upskirt')),
                SelectedIf(school.detention == 'upskirt')
                ] hovered [
                Show('description', None, 'upskirt')
                ] unhovered [
                Hide('description')
                ]
                
screen eduMats:
    zorder 1
    tag compScreens
    fixed xpos 0.3 ypos 0.1:
        vbox:
            textbutton _('Б/У материалы') action [
                SetField(school,'eduMats','poor'),
                SelectedIf(school.eduMats == 'poor')
                ] hovered [
                Show('description', None, 'eduPoor')
                ] unhovered [
                Hide('description')
                ]
            textbutton _('Стантартные') action [
                SetField(school,'eduMats','standart'),
                SelectedIf(school.eduMats == 'standart')
                ] hovered [
                Show('description', None, 'eduStandart')
                ] unhovered [
                Hide('description')
                ]
            textbutton _('Хорошие') action [
                SetField(school,'eduMats','good'),
                SelectedIf(school.eduMats == 'good')
                ] hovered [
                Show('description', None, 'eduGood')
                ] unhovered [
                Hide('description')
                ]
            textbutton _('"Нестандартные"') action [
                If('eduSexy' in school.unlockedUniforms, false=Show('preVoting', None, 'corr', 50, 'eduSexy'), true=SetField(school,'detention','eduSexy')),
                SelectedIf(school.eduMats == 'eduSexy')
                ] hovered [
                Show('description', None, 'eduSexy')
                ] unhovered [
                Hide('description')
                ]
                
screen preVoting(type,amount,what):
    zorder 2
    modal True
    frame xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5:
        if type == 'loy':
            $ temp = 'лояльности'
        if type == 'corr':
            $ temp = 'развратности'
        vbox:
            text 'Будет проведено голосование по [temp]. Вы хотите продолжить?'
            hbox:
                textbutton 'Да' action [
                Function(votingFunc, type, amount, what),
                Hide('preVoting'),
                Show('voting', None, type, amount)]
                textbutton 'Нет' action Hide('preVoting')
                
screen voting(type,amount): # Просто скрин для наглядности. На самом деле всё обсчитывается в votingFunc
    zorder 2
    tag compScreens
    fixed xpos 0.3 ypos 0.1:
        python:
            voteYes = voteNo = voteVeto = 0
        hbox:
            spacing 20
            for teacher in teachers:
                vbox:
                    spacing 10
                    if type == 'loy':
                        imagebutton idle im.FactorScale(teacher.picto,0.5) hover im.FactorScale(teacher.picto,0.5) action NullAction() hovered [SetVariable('showHover',teacher), Show('charInfoLeft')] unhovered [Hide('charInfoLeft')]
                        if teacher.getLoy() >= amount:
                            text 'За'
                            $ voteYes += 1
                        elif teacher.getLoy()*2 >= amount:
                            text 'Против' 
                            $ voteNo += 1
                        else:
                            text 'Вето' 
                            $ voteVeto += 1
                            
                    if type == 'corr':
                        imagebutton idle im.FactorScale(teacher.picto,0.5) hover im.FactorScale(teacher.picto,0.5) action NullAction() hovered [SetVariable('showHover',teacher), Show('charInfoLeft')] unhovered [Hide('charInfoLeft')]
                        if teacher.getCorr() >= amount:
                            text 'За'
                            $ voteYes += 1
                        elif teacher.getCorr()*2 >= amount:
                            text 'Против' 
                            $ voteNo += 1
                        else:
                            text 'Вето' 
                            $ voteVeto += 1
                            
    fixed xpos 0.3 ypos 0.3:
        if voteYes > voteNo and voteVeto == 0:
            text 'Предложение поддержано' style style.description
        elif voteYes <= voteNo and voteVeto == 0:
            text 'Предложение отклонено' style style.description
        else: 
            text 'Один или несколько учителей наложили вето на ваше предложение.' style style.description