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
        
    frame ypos 0.01 xalign 1.0 style style.myFrame:
        vbox:
            text _('Текущий бюджет: ' + str(int(school.budget)))
            text _('Ваш счёт: ' + str(int(player.money)))
        
    fixed xpos 0.01 ypos 0.1:
        vbox:
            
            if ptime - lastWork > 24:
                textbutton _('Работать') action Show('working') xminimum 300
            textbutton _('Клубы') action Show('clubs') xminimum 300
            textbutton _('Школьная форма') action Show('schoolUniform') xminimum 300
            textbutton _('Система наказаний') action Show ('detentions') xminimum 300
            textbutton _('Учебники') action Show ('eduMats') xminimum 300
            textbutton _('Мебель и Строения') action Show ('furniture') xminimum 300
            textbutton _('Ночные действия') action [SensitiveIf(lt() <= -3 and ptime - inhibLowTime > 8), Show ('studCorruption')] xminimum 300
            if hasLocationsItem(camera.name):
                textbutton _('Проверка камер') action [SensitiveIf(ptime - camSold > 24 and weekday not in [1,7]), Function(clrscr),Jump('checkCam')] xminimum 300
                
screen description(what):
    zorder 1
    fixed xpos 0.01 ypos 0.5:
        vbox:
            if what == 'usual':
                text _('Ученикам будет разрешено приходить в школу в обычной одежде, что позволит им быть более раскрепощёнными, а так же увеличит радость пребывания в "строгих" стенах вашего заведения. Требует пройти проверку на лояльность вам учителей.')
            elif what == 'strict':
                text _('Ученики будут приходить в школу в сторогой форме. Это дисциплинирует их, что приводит к улучшенным показателям в учёбе.')
            elif what == 'uniform':
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
                text _('Ученицы в наказание будут вынуждены после уроков показывать своё нижнее бельё перед классом. Это сподвигнет их стать более скромными и трудолюбивыми. Или наоборот. Кстати, ваша репутация может пострадать от этого наказания.')
            elif what == 'eduPoor':
                text _('Б/у материалы - это старые учебники, книги купленные у старьёвщиков и на распродаже, самый низкокачественный и плохой продукт, который можно найти.')
            elif what == 'eduStandart':
                text _('Обычные учебники - всё как у всех. Есть несколько хороших учебников, они хранятся в школе, и передаются из класса в класс. В основном материалы немного устаревшие, но Вы и не ставите перед собой задачу вырастить академиков.')
            elif what == 'eduGood':
                text _('Высококлассная литература - это качественная, написанная по последнему слову педагогики, литература рассчитанная на все виды образовательной деятельности. Это прекрасные учебники, по которым приятно, и полезно учиться.')
            elif what == 'eduSexy':
                text _('Лучшие сочинения непризнанного педагога Луки Мудищева, окажутся на школьных партах ваших подопечных. Не то, чтобы это было особо дорого, просто как посмотрят на вас родители, если их дети начнут цитировать отрывки из бессмертных произведений автора?')
            elif what == 'inhib1':
                text _('Данное действие повысит желание учеников на следующий день.')
            elif what == 'inhib2':
                text _('Данное действие повысит желание учеников на следующий день ещё сильнее.')
            elif what == 'inhib3':
                text _('Данное действие слегка повысит развратность учеников на следующий день.')
            elif what == 'inhib4':
                text _('Данное действие сильно повысит желание учеников мужского пола на следующий день.')
            elif what == 'manec':
                text _('Анатомически корректные манекены будут установлены в класс биологии.')
            elif what == 'video':
                text _('Видео с интересным контентом будет закуплено для уроков английского языка.')
            elif what == 'bed':
                text _('При покупке вы сможете спать прямо в офисе. Смотрите не сгорите на работе!')
            elif what == 'wall':
                text _('Постройка стены скроет школу от лишних глаз.')
            elif what == 'library':
                text _('Библиотека. Что тут ещё можно сказать? Вы войдёте в историю школу этой постройкой!')
            elif what == 'dildo':
                text _('Наглядные пособия будут закуплены для занятий cексуального просвящения. Очень наглядные. И практичные.')
            elif what == 'cherleader':
                vbox:
                    text _('Клуб черлидеров.')
                    text _('Команда поддержки вашего спортивного клуба. Девушки, короткие юбчонки, помпоны. Что может быть прекрасней и веселей? Разве что девушки без юбчонок...')
                    text _('Стоимость клуба - 200 монет в день')
                    text _('Занятия клуба проводятся в спортзале в понедельник, среду и пятницу с 15 до 18.')
            elif what == 'cosplay':
                vbox:
                    text _('Клуб косплейщиков.')
                    text _('Косплеят всё, от поней до служанок. Всегда можной зайти и посмотреть, чего же там накосплеили сегодня.')
                    text _('Стоимость клуба - 500 монет в день')
                    text _('Занятия проводятся в первом классе, с 15 до 18.')
            elif what == 'sport':
                vbox:
                    text _('Спортивный клуб.')
                    text _('"В хоккей играют настоящие мужчины!". На самом деле не только в хоккей и не только мужчины, но чтобы создать успешную команду, школе придётся раскошеливаться на дополнительный спорт инвентарь.')
                    text _('Стоимость клуба - 100 монет в день')
                    text _('Занятия клуба проводятся в спортзале, с 15 до 18 каждый вторник и четверг.')
            elif what == 'paint':
                vbox:
                    text _('Кружок рисования.')
                    text _('Мольберт, кисть и обнажённая натура. Кто знает, может быть на этом кружке родится новый Пикассо?')
                    text _('Стоимость клуба - 300 монет в день')
                    text _('Занятия клуба проводятся во втором классе, с 15 до 18 ежедневно.')
            elif what == 'pants':
                vbox:
                    text _('Клуб грязных трусиков.')
                    text _('Секретный клуб, участники которого используют вас в качестве посредника для перепродажи свих грязных трусиков всяким извращенцам. Приносит одно нижнее бельё в день за каждого участника. Пострайтесь быть в школе на переменах, вас найдут.')
            elif what == 'medic':
                vbox:
                    text _('Медицинский клуб.')
                    text _('Ученики в этом клубе учатся основам врачебного искусства.')
                    text _('Стоимость клуба - 250 монет в день')
                    text _('Занятия клуба проводятся в медицинском кабинете, с 15 до 18 ежедневно.')
            else:
                text _('Описания пока нет для [what]. Напишите на форум, если видите это, я постраюсь добавить описание.')

screen clubs:
    zorder 1
    tag compScreens
    fixed xpos 0.3 ypos 0.1:
        vbox:
            if is_cherleaderClub == 1:
                textbutton _('Клуб черлидеров') action [
                    If('cherleader' in school.clubs, false=[Function(school.addClub,'cherleader'),Show('clubs')],true = [Function(school.removeClub,'cherleader'),Show('clubs')]),
                    SelectedIf('cherleader' in school.clubs),
                    SensitiveIf('sport' in school.clubs)
                    ] hovered [
                    Show('description', None, 'cherleader') # При наведении показывается описание
                    ] unhovered [
                    Hide('description') # При потере фокуса - скрывается
                    ]
                    
            if is_cosplayClub == 1:
                textbutton _('Косплей клуб') action [
                    If('cosplay' in school.clubs, false=[Function(school.addClub,'cosplay'),Show('clubs')],true = [Function(school.removeClub,'cosplay'),Show('clubs')]),
                    SelectedIf('cosplay' in school.clubs)
                    ] hovered [
                    Show('description', None, 'cosplay') # При наведении показывается описание
                    ] unhovered [
                    Hide('description') # При потере фокуса - скрывается
                    ]
                    
            textbutton _('Спортивный клуб') action [
                If('sport' in school.clubs, false=[Function(school.addClub,'sport'),Show('clubs')],true = [Function(school.removeClub,'sport'),Function(school.removeClub,'cherleader'),Show('clubs')]),
                SelectedIf('sport' in school.clubs)
                ] hovered [
                Show('description', None, 'sport') # При наведении показывается описание
                ] unhovered [
                Hide('description') # При потере фокуса - скрывается
                ]
                
            textbutton _('Кружок рисования') action [
                If('paint' in school.clubs, false=[Function(school.addClub,'paint'),Show('clubs')],true = [Function(school.removeClub,'paint'),Show('clubs')]),
                SelectedIf('paint' in school.clubs)
                ] hovered [
                Show('description', None, 'paint') # При наведении показывается описание
                ] unhovered [
                Hide('description') # При потере фокуса - скрывается
                ]
            
            if 'doctor' in school.buildings:
                textbutton _('Медицинский клуб') action [
                    If('medic' in school.clubs, false=[Function(school.addClub,'medic'),Show('clubs')],true = [Function(school.removeClub,'medic'),Show('clubs')]),
                    SelectedIf('medic' in school.clubs)
                    ] hovered [
                    Show('description', None, 'medic') # При наведении показывается описание
                    ] unhovered [
                    Hide('description') # При потере фокуса - скрывается
                    ]
                
            if is_pantiesClub == 1:
                textbutton _('Клуб грязных трусиков') action [
                    If('pants' in school.clubs, false=[Function(school.addClub,'pants'),Show('clubs')],true = [Function(school.removeClub,'pants'),Show('clubs')]),
                    SelectedIf('pants' in school.clubs)
                    ] hovered [
                    Show('description', None, 'pants') # При наведении показывается описание
                    ] unhovered [
                    Hide('description') # При потере фокуса - скрывается
                    ]
                
screen furniture:
    zorder 1
    tag compScreens
    fixed xpos 0.3 ypos 0.1:
        vbox:
            text _('Дополнительные предметы в классах')
            textbutton _('Анатомические манекены (Бюджет - 20000)') action [
                If('manec' in school.furniture, false=Show('preVoting', None, 'corr', 20, 'manec')),
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
                
            textbutton _('Наглядные пособия (Бюджет - 15000)') action [
                If('dildo' in school.furniture, false=Show('preVoting', None, 'corr', 25, 'dildo')),
                SelectedIf('dildo' in school.furniture),
                SensitiveIf(school.budget > 15000 or 'dildo' in school.furniture)
                ] hovered [
                Show('description', None, 'dildo') # При наведении показывается описание
                ] unhovered [
                Hide('description') # При потере фокуса - скрывается
                ]
                
                
            text _('\nСтроения и мебель')
            textbutton _('Кровать в офис (Стоимость - 2000)') action [
                If('bed' in school.furniture, false=Show('preVoting', None, 'loy', 15, 'bed')),
                SelectedIf('bed' in school.furniture),
                SensitiveIf(player.money > 2000 or 'bed' in school.furniture)
                ] hovered [
                Show('description', None, 'bed') # При наведении показывается описание
                ] unhovered [
                Hide('description') # При потере фокуса - скрывается
                ]
                
            textbutton _('Хим лаборатория (Бюджет - 75000)') action [
                If('chemlab' in school.buildings, false=Show('preVoting', None, 'loy', 50, 'chemlab')),
                SelectedIf('chemlab' in school.furniture),
                SensitiveIf(school.budget > 75000 or 'chemlab' in school.furniture)
                ] hovered [
                Show('description', None, 'chemlab') # При наведении показывается описание
                ] unhovered [
                Hide('description') # При потере фокуса - скрывается
                ]
                
            textbutton _('Медицинский кабинет (Бюджет - 25000)') action [
                If('doctor' in school.buildings, false=Show('preVoting', None, 'loy', 25, 'doctor')),
                SelectedIf('doctor' in school.furniture),
                SensitiveIf(school.budget > 25000 or 'doctor' in school.furniture)
                ] hovered [
                Show('description', None, 'doctor') # При наведении показывается описание
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
                
            textbutton _('Подвал (Бюджет - 100000)') action [
                If('dungeon' in school.buildings, false=Show('preVoting', None, 'corr', 50, 'dungeon')),
                SelectedIf('dungeon' in school.buildings),
                SensitiveIf(school.budget > 100000 or 'dungeon' in school.buildings)
                ] hovered [
                Show('description', None, 'dungeon') # При наведении показывается описание
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
            
            textbutton _('Стандартная форма') action [
                SetField(school,'uniform','uniform'),
                SelectedIf(school.uniform == 'uniform')
                ] hovered [
                Show('description', None, 'uniform')
                ] unhovered [
                Hide('description')
                ]
                
            textbutton _('Сексуальная форма') action [
                If('sexy' in school.unlockedUniforms, false=Show('preVoting', None, 'corr', 30, 'sexy'), true=SetField(school,'uniform','sexy')),
                SelectedIf(school.uniform == 'sexy')
                ] hovered [
                Show('description', None, 'sexy')
                ] unhovered [
                Hide('description')
                ]
                
            textbutton _('Шлюховатая форма') action [
                If('skimpy' in school.unlockedUniforms, false=Show('preVoting', None, 'corr', 60, 'skimpy'), true=SetField(school,'uniform','skimpy')),
                SelectedIf(school.uniform == 'skimpy'),
                SensitiveIf('sexy' in school.unlockedUniforms)
                ] hovered [
                Show('description', None, 'skimpy')
                ] unhovered [
                Hide('description')
                ]
                
            textbutton _('Голая форма') action [
                If('naked' in school.unlockedUniforms, false=Show('preVoting', None, 'corr', 75, 'naked'), true=SetField(school,'uniform','naked')),
                SelectedIf(school.uniform == 'naked'),
                SensitiveIf('skimpy' in school.unlockedUniforms)
                ] hovered [
                Show('description', None, 'naked')
                ] unhovered [
                Hide('description')
                ]
                
            textbutton _('БДСМ форма') action [
                If('bdsm' in school.unlockedUniforms, false=Show('preVoting', None, 'corr', 80, 'bdsm'), true=SetField(school,'uniform','bdsm')),
                SelectedIf(school.uniform == 'bdsm'),
                SensitiveIf('naked' in school.unlockedUniforms)
                ] hovered [
                Show('description', None, 'bdsm')
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
            textbutton _('Инвестировать в школу') action [Function(move,'invest')]
            if player.getItem(clubPanties.name) != False:
                textbutton _('Продать трусики в интернете') action [Function(player.sellItems,clubPanties.name),Show('compScreen')]
            
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
                
            if 'dungeon' in school.buildings:
                textbutton _('Заключение в подвале') action [
                    If('upskirt' in school.unlockedUniforms, false=Show('preVoting', None, 'corr', 50, 'lock'), true=SetField(school,'detention','lock')),
                    SelectedIf(school.detention == 'lock')
                    ] hovered [
                    Show('description', None, 'lock')
                    ] unhovered [
                    Hide('description')
                    ]
                    
                textbutton _('Пытки') action [
                    If('upskirt' in school.unlockedUniforms, false=Show('preVoting', None, 'corr', 80, 'torue'), true=SetField(school,'detention','torue')),
                    SelectedIf(school.detention == 'torue')
                    ] hovered [
                    Show('description', None, 'torue')
                    ] unhovered [
                    Hide('description')
                    ]
                
screen eduMats:
    zorder 1
    tag compScreens
    fixed xpos 0.3 ypos 0.1:
        vbox:
            textbutton _('Б/У материалы') action [
                SelectedIf(school.eduMats == 'poor'),
                SetField(school,'eduMats','poor')
                ] hovered [
                Show('description', None, 'eduPoor')
                ] unhovered [
                Hide('description')
                ]
            textbutton _('Стантартные (Бюджет - 5 000)') action [
                SelectedIf(school.eduMats == 'standart'),
                If('standart' in school.unlockedEduMats, false=[SetField(school,'budget',school.budget - 5000),Function(school.addEduMat,'standart')]),
                SetField(school,'eduMats','standart'),
                SensitiveIf('standart' in school.unlockedEduMats or school.budget >= 5000)
                ] hovered [
                Show('description', None, 'eduStandart')
                ] unhovered [
                Hide('description')
                ]
            textbutton _('Хорошие (Бюджет - 15 000)') action [
                SelectedIf(school.eduMats == 'good'),
                If('good' in school.unlockedEduMats, false=[SetField(school,'budget',school.budget - 15000),Function(school.addEduMat,'good')]),
                SetField(school,'eduMats','good'),
                SensitiveIf('good' in school.unlockedEduMats or school.budget >= 15000)
                ] hovered [
                Show('description', None, 'eduGood')
                ] unhovered [
                Hide('description')
                ]
            textbutton _('"Нестандартные" (Бюджет - 50 000)') action [
                If('eduSexy' in school.unlockedEduMats, false=Show('preVoting', None, 'corr', 25, 'eduSexy'), true=SetField(school,'eduMats','eduSexy')),
                SensitiveIf('eduSexy' in school.unlockedEduMats or school.budget >= 50000)
                ] hovered [
                Show('description', None, 'eduSexy')
                ] unhovered [
                Hide('description')
                ]

screen studCorruption:
    zorder 1
    tag compScreens
    fixed xpos 0.3 ypos 0.1:
        vbox:
            textbutton _('Разложить по классам эротические фотографии') action [
                Function(clrscr),
                Jump('inhib1'),
                SensitiveIf(player.getCorr() > 10)
                ] hovered [
                Show('description', None, 'inhib1')
                ] unhovered [
                Hide('description')
                ]
            textbutton _('Разложить по классам порнографические фотографии') action [
                Function(clrscr),
                Jump('inhib2'),
                SensitiveIf(player.getCorr() > 20)
                ] hovered [
                Show('description', None, 'inhib2')
                ] unhovered [
                Hide('description')
                ]
            textbutton _('Разложить по классам фотки со скрытой камеры') action [
                Function(clrscr),
                Jump('inhib3'),
                SensitiveIf(player.getCorr() > 50)
                ] hovered [
                Show('description', None, 'inhib3')
                ] unhovered [
                Hide('description')
                ]
            textbutton _('Распространить свой запах') action [
                Function(clrscr),
                Jump('inhib4'),
                SensitiveIf(player.getCorr() > 70)
                ] hovered [
                Show('description', None, 'inhib4')
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
            $ temp = 'лояльности и развратности'
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
                        if (teacher.getCorr() + teacher.getLoy()) >= amount*2:
                            text 'За'
                            $ voteYes += 1
                        elif (teacher.getCorr() + teacher.getLoy()) >= amount:
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