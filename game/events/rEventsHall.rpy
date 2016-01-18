label event_loc_hall_0_no1:
    show hall
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/school/hall/no1.jpg' at top as tempPic
    '[st2.fname] и [st1.fname]. Очевидно, вы прервали важную беседу, и вам здесь не рады.'
    if getPar(studs, 'corr') > 40 or development == 1:
        menu:
            'Спрятаться в шкафчик':
                'Вы якобы покидаете парочку, но проворно прячетесь в шкафчик и наблюдаете оттуда.'
                st1.say 'Ушла что ли?'
                if rand(1,3) == 1:
                    st2.say 'Да если бы. Вот в шкафчик мой спряталась.'
                    player.say '"Чёрт!"'
                    'Вы краснеете от стыда и пулей вылетаете из шкафчика, покидая холл.'
                    $ st1.incLoy(-10)
                    $ st2.incLoy(-10)
                    $ setRep(2,-5)
                    $ move('loc_firstFloor')
                else:
                    st2.say 'Вроде да. Ну так что, давай при всех попробуем?'
                    st1.say 'И как ты себе это представляешь?'
                    st2.say 'Ну ты сядешь мне на коленки, а я буду тебе якобы с математикой помогать!'
                    st1.say 'Чёрт с тобой! Уболтал, чертяка языкастый!'
                    show expression 'pic/locations/school/hall/no1_1.jpg' at top as tempPic
                    'Вы сидите в шкафчике и смотрите, как [st1.fname] приподнимает юбку и, расстегнув ширинку своего дружка, с тихим всхлипом усаживается ему на коленки. [st2.fname] берёт в руку тетрадку и начинает что-то говорить на ушко.'
                    player.say '"Не думаю, что он всерьёз обсуждает проблемы теоремы Пифагора в евклидовом пространстве."'
                    'Ноги девушки начинают подрагивать, но она не встаёт с колен, а лишь немного ускоряет покачивания своей попы на члене парня. Вы видите, как на пол падают первые капли из её возбуждённой киски. [st2.fname] продолжает что-то нашёптывать ей и внезапно кусает за мочку.'
                    st1.say 'А-ах! - как-то слишком эротично для занятия по математике вскрикивает девушка.'
                    st1.say 'В смысле - ах, как интересно! М-м-м...'
                    'Движения парочки всё ускоряются, и уже со стороны должно быть отчётливо заметно, чем они занимаются, но всё таки никто не обращает внимания, словно ничего не происходит.'
                    st1.say '[st2.fname]! Я сейчас кончу! КОНЧУ! В смысле, кончу доказывать эту задачу! Кончи со мной! Давай придём к решению вместе!'
                    show expression 'pic/locations/school/hall/no1_2.jpg' at top as tempPic
                    'Парень вдруг затих на секунду, и крупные капли спермы из влагалища начали падать на пол. Наклонив голову, девушка закусила губу и постанывала.'
                    st1.say 'Всё, [st2.fname], я закончила...'
                    st2.say 'Отличное было решение!'
                    'Парочка собирается и уходит, позволяя вам выйти из шкафчика.'
                    player.say '"Чёрт! Как же всё затекло!"'
                    $ player.incEnergy(-50)
                    $ player.incLust(20)
            'Уйти':
                'Вы решаете не испытывать судьбу и покидаете парочку.'
    $ move(curloc)
    
label event_loc_hall_0_no2:
    show hall
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st1.incLust(20)
        st2.incCorr(5)
    show expression 'pic/locations/school/hall/no2.jpg' at top as tempPic
    player.say 'Ого! Тут похоже не обошлось без любовного послания! Давненько вы таких лиц не видели!'
    if st1.getCorr() > 50 or development == 1:
        $ hadSex(st1)
        player.say '[st1.fname], что-то случилось?'
        'Вы участливо интересуетесь у девушки. Ведь суициды в таком возрасте не так уж и редки, особенно на почве неразделённой любви.'
        show expression 'pic/locations/school/hall/no2_1.jpg' as tempPic:
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        st1.say 'Нет, [player.name], всё уже в порядке. Я просто внезапно кончила...'
        'Девушка демонстрирует вам небольшой вибратор, который продолжает тихо жужжать в её трусиках.'
        $ player.incLust(10)
        menu:
            'Наказать':
                $ scoldWho = [st1]
                jump scoldAll
            'А... Ну...':
                player.say 'А... Ну тогда всё в порядке... Я надеюсь...'
    $ move(curloc)
    
label event_loc_hall_0_no3:
    show hall
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st1.incLust(20)
        st2.incCorr(5)
    show expression 'pic/locations/school/hall/no3.jpg' at top as tempPic
    'Очередное любовное послание? Мило. Похоже шкафчики для обуви используют как угодно, но только не для обуви.'
    if player.getCorr() > 50 or development == 1:
        show expression 'pic/locations/school/hall/no3_1.jpg' at top as tempPic
        player.say '"Интересно, что они там пишут друг другу? Как он страстно желает снова засунуть свой член в её маленькую вагину?"'
        player.say '"Как ему нравятся чавкающие звуки вперемешку со стонами, которые издаёт [st1.fname] во время оргазма?"'
        player.say '"О том, что любит, когда его головку массируют влажные стенки её юного лона?"'
        player.say '"В общем, непонятно, чего там нужно такого написать, чтобы так покраснеть!"'
    $ move(curloc)
    
label event_loc_hall_0_no4:
    show hall
    python:
        st1 = getChar('female')
        st1.incLoy(10)
    show expression 'pic/locations/school/hall/no4.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    player.say '"Ну хоть кто-то использует шкафчики для обуви, а не для хранения писем поклонников! Какая же [st1.fname] молодец! И как мне нравятся её симпатичные ножки!"'
    if player.getCorr() > 50 or development == 1:
        show expression 'pic/locations/school/hall/no4_1.jpg' at top as tempPic
        player.say '"А ещё сильнее красивых ножек, мне нравятся эти ножки на толстенном члене! Как жаль, что я ни разу не видела, как [st1.fname] работает ножками! Должно быть, у неё много поклонников."'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_hall_0_no5:
    show hall
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st2.incLust(20)
        st1.incCorr(5)
    show expression 'pic/locations/school/hall/no5.jpg' at top as tempPic
    'Что-то новенькое. Раньше я встречала только парней, подкатывающих к девушкам. А вот [st1.fname], судя по всему, имеет своё мнение насчёт того, кто должен начать ухаживания.'
    if st1.getCorr() > 40 or development == 1:
        $ st1.incCorr(5)
        'Вы замечаете, что девушка вдруг начинает тяжело дышать.'
        player.say '"От волнения что ли?"'
        show expression 'pic/locations/school/hall/no5_1.jpg' as tempPic:
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        'Подойдя поближе, причина учащённого дыхания становится ясна.'
        player.say '[st1.fname], так ты кого любишь больше вибраторы или парня за стеной?'
        'Вы наклоняетесь к девушке поближе, шепча ей эти слова в ушко.'
        st1.say 'К-к-ончать!'
        'И на белых трусиках ученицы начинает расплываться пятно влаги, выброшенное текущей от оргазма киской.'
        player.say 'Понятно...'
        menu:
            'Наказать':
                $ scoldWho = [st1]
                jump scoldAll
            'Не трогать её':
                pass
    $ move(curloc)
    
label event_loc_hall_0_no6:
    show hall
    python:
        st1 = getChar('female')
        player.incLust(5)
        setFun(5,10)
    show expression 'pic/locations/school/hall/no6.jpg' at top as tempPic
    'Девушки переобуваются в школьную обувь. Вы не можете упустить момента и не полюбоваться на их ножки! Уж слишком игриво они двигают своими пальчиками в чулочках!'
    if player.getCorr() > 20 or development == 1:
        show expression 'pic/locations/school/hall/no6_1.jpg' at top as tempPic
        'Вам почему-то вдруг представилась [st1.name], которая, сидя в классе, показывает всем, что трусиков под колготками не носит.'
        $ player.incLust(10)
    $ move(curloc)
