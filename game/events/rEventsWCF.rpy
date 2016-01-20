label event_loc_wcf_0_no1:
    show wcf
    python:
        st1 = getChar('female')
    'Зайдя в туалет, вы услышали тихий стон из кабинки.'
    menu:
        'Проверить':
            show expression ('pic/locations/school/wcf/no%d.jpg' %rand(1,5)) at top as tempPic
            'Вы приоткрыли дверь кабинки. Там сидит [st1.fname] в довольно интимной обстановке.'
            $ st1.setLoy(-5)
            menu:
                'Стоять и смотреть':
                    if st1.getCorr() > 40:
                        show expression 'pic/locations/school/wcf/no1_1.jpg' at top as tempPic
                        'Ученица невозмутимо заканчивает свои дела под вашим пристальным взором, потом, немного краснея, раздвигает свои ножки, представляя вашим глазам прекрасный вид на её бритую киску.'
                        st1.say 'Вам нравится? Или может быть вы ещё чтото хотели посмотреть?'
                        player.say 'Нет, всё в порядке! Я просто проверяла, всё ли хорошо!'
                    else:
                        'Видя, что вы не собираетесь уходить, ученица начинает кричать, и требовать уединения. Буквально чувствуя децибеллы, которых достигают её крики, вы поспешно ретируетесь, опасаясь за свои барабанные перепонки.'
                        $ st1.setLoy(-5)
                'Извиниться и уйти':
                    'Видя, что ничего страшного не происходит? Вы извиняетесь за причинённые неудобства, и уходите.'
                    player.say '"Да и что тут может произойти в самом деле?"'
        'Не проверять':
            player.say '"Мало ли что там... Не будем нарушать уединения."'
    $ move(curloc)
    
label event_loc_wcf_10_no10:
    show wcf
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/wcf/no10.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Зайдя в туалет, вы увидели, что [st1.fname] задрала юбочку и фотографирует свою попку на телефон.'
    player.say '"Очень интересно для кого?!"'
    if st1.getCorr() > 30:
        show expression 'pic/locations/school/wcf/no10.jpg' as tempPic:
            xalign 1.0 yalign 1.0
            ease  10.0 yalign 0.0
        'Заметив что она уже не одна, девушка вежливо здоровается, делает фотографию и поднимает на вас невинные глазки.'
    else:
        show expression 'pic/locations/school/wcf/no10.jpg' as tempPic:
            xalign 1.0 yalign 0.0
        'Заметив вас, она одергивает юбку, не успев сделать фото.'
    menu:
        'Наказать':
            $ scoldWho = [st1]
            jump scoldAll
        'Проигнорировать':
            'Вы делаете вид, как будто ничего не произошло, и вы ничего не заметили. [st1.fname] с благодарностью смотрит на вас.'
            $ st1.setLoy(10)
    $ move(curloc)
    
label event_loc_wcf_0_no2:
    show wcf
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/wcf/no2.png' at right as tempPic
    'Зайдя в туалет, Вы увидели, что [st1.fname] стоит, и курит сигарету.'
    if st1.getLoy() > 50:
        'Заметив вас, она вежливо здоровается и продолжает курить.'
    else:
        'Заметив вас, она пытается выкинуть сигарету.'
    menu:
        'Наказать':
            $ scoldWho = [st1]
            jump scoldAll
        'Проигнорировать':
            'Вы делаете вид, как будто ничего не произошло, и вы ничего не заметили. [st1.fname] с благодарностью смотрит на вас.'
            $ st1.setLoy(10)
    $ move(curloc)
    
label event_loc_wcf_15_low1:
    show wcf
    python:
        st1 = getChar('female')
        hadSex(st1)
    'Зайдя в туалет, вы услышали тихий стон из кабинки.'
    menu:
        'Проверить':
            'Решив проверить всё ли в порядке, вы открыли дверь.'
            show expression 'pic/locations/school/wcf/low1.jpg' at top as tempPic
            player.say '"Это... Интересно..."'
            '[st1.fname] стоит рачком, оперевшись на унитаз, и быстро водит пальчиками вдоль своего клитора. Смазка стекает из её киски, и по глазам видно, что девушка скоро кончит.'
            menu:
                'Наказать':
                    $ scoldWho = [st1]
                    jump scoldAll
                'Извиниться и уйти':
                    player.say 'Прости, что прервала, - скороговоркой выпаливаете вы, и быстро закрываете дверь, выходя из туалета.'
                'Стоять и смотреть':
                    if st1.getLoy() > 75 or st1.getCorr() > 50:
                        show expression 'pic/locations/school/wcf/low1a.jpg' at top as tempPic
                        'Несмотря на то, что вы смотрите на неё, [st1.fname] возбуждается всё сильнее, не переставая теребить свой бугорочек, и вот уже бодрая струйка и быстрые сокращения розовой киски возвещают о наступившем оргазме.'
                        'Ученица немного виновато улыбается, и просит вас уйти.'
                        player.say 'По моему уже поздновато, а? - улыбаетесь вы, но всё таки закрываете за собой дверь.'
                        $ st1.incCorr(5)
                    else:
                        show expression 'pic/locations/school/wcf/low1b.jpg' at top as tempPic
                        st1.say 'Вы не могли бы выйти, [player.name]??? - возмущённо спрашивает девушка.'
                        player.say 'Да - да, извини, - немного засмущались вы покинули туалет.'
        'Не проверять':
            player.say '"Мало ли что там... Не будем нарушать уединения."'
    $ move(curloc)

label event_loc_wcf_25_low2:
    show wcf
    python:
        st1 = getChar('female')
        hadSex(st1)
    'Зайдя в туалет, вы услышали тихий стон из кабинки.'
    menu:
        'Проверить':
            show expression 'pic/locations/school/wcf/low2.jpg' at top as tempPic
            'Как ответсвенный директор, вы решили лично убедиться, что всё в порядке. Уже открывая дверь, стало понятно, что это было не лучшее решение, ситуация довольно неловкая. Вы неуверены, чем занимается [st1.fname], но при вашем появлении, её пальчик быстро выскользнул из попки.'
            st1.say '[player.name]? Что вы тут делаете?'
            menu:
                'Наказать':
                    $ scoldWho = [st1]
                    jump scoldAll
                'Извиниться и уйти':
                    player.say 'Прости, что прервала, - скороговоркой выпаливаете вы, и быстро закрываете дверь, выходя из туалета.'
        'Не проверять':
            player.say '"Мало ли что там... Не будем нарушать уединения."'
    $ move(curloc)
    
label event_loc_wcf_10_low3:
    show wcf
    python:
        st1 = getChar('female')
        hadSex(st1)
    'Зайдя в туалет, вы услышали тихий стон из кабинки.'
    menu:
        'Проверить':
            show expression 'pic/locations/school/wcf/low3.jpg' at top as tempPic
            'Вы незаметно заглянули в неё через щёлку. [st1.fname] писала стоя, зажав галстучек в зубах. Вроде бы ничего особо странного, но постоянно прерывающаяся струя, тихие постанывания, и характерные влажные подтёки на влагалище намекали Вам на то, что девушка буквально на ваших глазах кончила.'
            'Дождавшись, пока вздрагивающая девушка приведёт в себя в порядок, вы вышли из соседней кабинки.'
        'Не проверять':
            player.say '"Мало ли что там... Не будем нарушать уединения."'
    $ move(curloc)
    
label event_loc_wcf_40_mid1:
    show wcf
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        hadSex(st1,st2)
    'Зайдя в туалет, вы услышали тихий стон из кабинки.'
    menu:
        'Проверить':
            show expression 'pic/locations/school/wcf/mid1.jpg' at top as tempPic
            st2.say '[st1.fname], ну что ты делаешь, [st1.fname], хи-хи-хи.'
            'Вы наблюдаете через щёлку двери, как [st2.fname] отдаётся парню прямо в кабинке женского туалета. Внезапно парень закончил свои прелюдии, и вошёл в девушку сзади.'
            st2.say '[st1.fname], аааах, какой у тебя большой! Скорее! Наполни мою киску своей спермой!'
            'Через секунду они уже активно двигались, распространяя по туалету запах секса.'
            menu:
                'Наказать':
                    $ scoldWho = [st1,st2]
                    jump scoldAll
                'Уйти':
                    $ st1.incLoy(5)
                    $ st2.incLoy(5)
                    pass
        'Не проверять':
            player.say '"Мало ли что там... Не будем нарушать уединения."'
    $ move(curloc)
            
label event_loc_wcf_0_mid2:
    show wcf
    python:
        if mile_qwest_2_stage != 12:
            skipEvent()
        st1 = bioBoy
        st2 = kupruvna
        hadSex(st1,st2)
    'Зайдя в туалет, вы услышали тихий стон из кабинки.'
    menu:
        'Проверить':
            show expression 'pic/locations/school/wcf/mid2.jpg' as tempPic:
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            'Не в силах справится со своим любопытсвом, вы заглянули в кабинку и увидели, что там [st2.name] занимается со своим сыном делами отнюдь не туалетными.'
            st2.say 'Вот так вот, мальчик, спускай в мамочку, да, - гладила [st2.fname] парня по голове.'
            'Похоже вы пришли как раз к финалу, потому что [st1.fname] без лишних слов дёрнулся, застонал и из набухшего бутона учительницы потекли вязкие капли семени.'
            player.say '"Хорошо всё таки, что я не сломала её!"'
        'Не проверять':
            player.say '"Мало ли что там... Не будем нарушать уединения."'
    $ move(curloc)