label event_loc_class4_0_no1:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('female')
        st5 = getChar('futa')
        setFun(10,10)
    show expression 'pic/locations/school/class4/no1.jpg' at top as tempPic
    'Школьная рок группа репетирует песню "Это математично" из своего нового альбома "Время приключений". Казалось бы причём тут собака? Вы не стали мешать репетиции, и ушли.'
    $ move(curloc)
    
label event_loc_class4_0_no10:
    show class4
    python:
        st1 = bissektrisovna
        st2 = getChar('female')
        st3 = getChar('male')
        st4 = getChar('male')
        setFun(5,10)
    show expression 'pic/locations/school/class4/no10.jpg' at top as tempPic
    'Похоже [st3.fname] всё таки смог доказать теорему Пифагора. Правда [st1.name] немного шокирована формулировкой "Пифагоровы трусы".'
    $ move(curloc)
    
label event_loc_class4_0_no2:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('male','lustmax')
        st4 = getChar('male','corrmax')
    show expression 'pic/locations/school/class4/no2.jpg' at top as tempPic
    'Похоже назревает конфликт. [st1.fname] поставила ноги на стол однокласснице, и снисходительно смотрит на неё сидя на соседней парте. Если так пойдёт дальше, [st2.fname] тоже в долгу не останется.'
    menu:
        'Наказать их':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Разнять их':
            'Вы отчитали обеих учениц, за недостойное поведение, и пригрозили сообщить обо всём их родителям.'
            $ st1.incLoy(10)
            $ st2.incLoy(10)
        'Не обращать внимания':
            $ st1.incLoy(10)
            $ st2.incLoy(-10)
    $ move(curloc)
    
    
label event_loc_class4_0_no3:
    show class4
    python:
        st1 = getChar('female')
        st1.incFun(10)
    show expression 'pic/locations/school/class4/no3.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.name] проветривает ножки на перемене. Вы и сами не понимаете, почему обратили на это внимание.'
    if player.getCorr() > 40:
        show expression 'pic/locations/school/class4/no3a.jpg' at top as tempPic
        player.say '"Наверное потому, что эта ножка гораздо лучше смотрелась бы на члене одноклассника..."'
        $ player.incLust(5)
    $ move(curloc)
 
label event_loc_class4_0_no5:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('male')
        setFun(4,15)
    show expression 'pic/locations/school/class4/no5.jpg' at top as tempPic
    '[st1.fname], [st2.fname], [st3.fname] и [st4.fname] решили устроить соревнование по новой игре для дандендо - "Шмота 2". Ну чтож, время не учебное, пусть отдыхают.'
    if st4.getCorr() > 40:
        show expression 'pic/locations/school/class4/no5a.png' at top as tempPic
        'Вы отвлеклись на свои дела на несколько минут, но когда обернулись, обнаружили, что [st4.fname] уболтал одноклассницу на лёгкий интим.'
        'Как ни странно, соревнований по игре это не прекратило, хотя победитель определённо наметился.'
        menu:
            'Наказать их':
                $ scoldWho = [st1,st4]
                jump scoldAll
            'Не обращать внимания':
                $ hadSex(st1,st4)
                $ setLust(4,20)
                $ st1.incLoy(10)
                $ st4.incLoy(10)
    $ move(curloc)

label event_loc_class4_0_no6:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/school/class4/no6.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] решили обсудить достижения Перельмана в математике.'
    if player.getIntel() > 50:
        'Вы довольно обоснованно вспомнили про доказательство гипотезы Пуанкаре, а так же про дальнейший отказ от "Премии тысячелетия".'
        'Ученики обязательно расскажут родителям, какой у них эрегированный директор.'
        $ setRep(2,10)
    else:
        'Откровенно говоря, слово "соснула" довольно чётко описывает вашу дальнейшую дискуссию. Это довольно плохо сказалось на вашей репутации.'
        $ setRep(2,-10)
    $ move(curloc)
    
label event_loc_class4_0_no7:
    show class4
    python:
        st1 = getChar('female','corrmax')
    show expression 'pic/locations/school/class4/no7.jpg' at top as tempPic
    '[st1.fname] уселась на парты, и с интересом наблюдает за вами.'
    if st1.getCorr() > 50:
        'Потом встаёт, и направляется к выходу.'
        show expression 'pic/locations/school/class4/no7a.png':
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        'Вы не удерживаетесь от любопытства, заглядываете ей под юбочку, чтобы узнать причину столь внимательного взгляда. И вашему взгляду предстают пара проводочков выходящих из под трусиков девочки.'
        player.say '"Ну тут два варианта. Либо это бабаробот, либо [st1.name] - очень развратная девушка!"'
        $ st1.incLust(25)
    $ move(curloc)
    
    
label event_loc_class4_0_no8:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incFun(10)
        st2.incFun(10)
    show expression 'pic/locations/school/class4/no8.jpg' at top as tempPic
    '[st1.fname] уснула на коленях у своей подруги. Такое чувство, что у меня в школе ученики вообще не занимаются, а только дрыхнут! Стоило конечно разбудить девочку, но человек способный разбудить спящего, способен вообще на любую подлость!'
    $ move(curloc)
    
label event_loc_class4_0_no9:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incFun(10)
        st2.incFun(10)
        setRep(2,10)
    show expression 'pic/locations/school/class4/no9.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] высунулись в окно, и дышат свежим воздухом.'
    'Вы делаете им замечание, чтобы они слишком далеко не высовывались.'
    $ move(curloc)
    