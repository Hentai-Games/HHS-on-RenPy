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
    
label event_loc_class4Learn_0_1:
    if getPar(studs, 'fun') < 30:
        $ skipEvent()
    show expression 'pic/locations/school/class1/learn2.jpg' at top as tempPic
    player.say '"Боже! Какой бардак! Они тут что, все с ума посходили?"'
    'Студентам слишком весело, чтобы тратить свою жизнь на такое скучное дело как занятия. Они решили поднять бунт и в данный момент крушат всё, что попадается под руку.'
    menu:
        'Помочь преподавателю успокоить их':
            $ bissektrisovna.incLoy(10)
            $ setFun(10,-5)
        'Не вмешиваться':
            'Видя вашу пассивность, ученики бунтуют всё сильнее, пока наконец учитель не находит в себе силы гаркнуть что есть мочи и успокоить их. Но урок всё равно провален.'
            $ bissektrisovna.incLoy(-5)
            $ setFun(10,5)
            $ setCorr(10,1)
            $ setEdu(10,-5)
    $ move(curloc)
    
label event_loc_class4Learn_0_2:
    show class3
    python:
        st1 = getChar('male','classroom')
    show expression 'pic/locations/school/class4/learn1.jpg' at top as tempPic
    bissektrisovna.say 'Так, [st1.fname]! Ну ка быстро назови мне первые 9 цифр чисел Фибоначчи!'
    st1.say 'Эээ, ноль... Один... Один... Ддальше идёт... Идёт дальше...'
    $ temp = ''
    if player.getIntel() > 70:
        $ temp = ' (интеллект)'
    menu:
        'Подсказать числа (2,3,4,5,6,7)':
            'Вы тихонько нашёптываете числа ученику.'
            bissektrisovna.say 'Неправильно! Садись! Два!'
            'Парень с огорчением смотрит на вас. Наверняка он думает, что вы нарочно подсказали ему неверный ответ.'
            $ st1.incLoy(-10)
        'Подсказать числа (2,2,4,6,10,14)':
            'Вы тихонько нашёптываете числа ученику.'
            bissektrisovna.say 'Неправильно! Садись! Два!'
            'Парень с огорчением смотрит на вас. Наверняка он думает, что вы нарочно подсказали ему неверный ответ.'
            $ st1.incLoy(-10)
        'Подсказать числа (2,3,5,8,13,21)[temp]':
            'Вы тихонько нашёптываете числа ученику.'
            bissektrisovna.say '[player.name]! Прекратите ему подсказывать! Ладно, [st1.fname], садись, четыре.'
            'Парень с благодарностью смотрит на вас.'
            $ st1.incLoy(10)
        'Не подсказывать ничего':
            'Помекав ещё минуту и дойдя до пятого числа, нерадивый ученик сел с тройкой за парту. [bissektrisovna.name] благодарна вам, что вы не вмешивались в учебный процесс.'
            $ bissektrisovna.incLoy(5)
    $ move(curloc)
    
label event_loc_class4Learn_5_3:
    show class3
    python:
        st1 = getChar('female','classroom')
    show expression 'pic/locations/school/class4/learn3.jpg' at top as tempPic
    '[st1.name] сидит на уроке и внимательно слушает, что там вещает сегодня преподаватель математики. Вроде бы придраться не к чему. Разве что вас терзают сомнения, не забыла ли она сегодня дома трусики...'
    if st1.getCorr() > 20:
        $ st1.incCorr(3)
        $ player.incLust(5)
        show expression 'pic/locations/school/class4/learn3_1.jpg' at top as tempPic
        'Видя ваше внимание, [st1.fname] раздвигает свои ноги, окончательно развеяв все сомнения. Она прекрасно помнит, что не надела трусики, и более того, не против продемонстрировать свою бритую киску вам!'
        player.say '"Ну и что с ней делать? Не снимать же с себя трусы, чтобы ей отдать?"'
        'Вы решаете оставить девушку в покое. По крайней мере отсутствие нижнего белья не мешает ей внимательно слушать преподавателя.'
    $ move(curloc)
    
label event_loc_class4Learn_45_4:
    show class3
    python:
        st1 = getChar('female','classroom')
        st2 = getChar('male','classroom')
        hadSex(st1,st2)
    show expression 'pic/locations/school/class4/learn4.jpg' at top as tempPic
    'Зайдя в класс, вы видите, что несмотря на то, как на доске стремительно разворачиваются формулы логарифмического исчисления, под столом у одной парочки разворачиваются совсем другие действия. Если быть точнее, [st1.fname], накинув свои весёленькие трусики на член парня, ловко играет пальчиками с его головкой.'
    player.say '"Вот ведь чертовка! И какой интересный выход нашла, чтобы руку не запачкать! Или может это просто [st2.fname] у нас такой фетишист?"'
    $ move(curloc)
    
label event_loc_class4Learn_40_5:
    show class3
    python:
        st1 = getChar('male','classroom')
    show expression 'pic/locations/school/class4/learn5.jpg' at top as tempPic
    '[bissektrisovna.name] нашла интересный способ наказания учеников и одновременно выяснения реального уровня их знаний. Прикрепив небольшой вибратор прямо к члену одного из парней, она проводит блиц опрос. Провалившийся оказывается с мокрыми штанами. Вы не думаете, что выиграть вообще возможно.'
    bissektrisovna.name 'Докажи, что уравнение  xy = 2006 (x+y) имеет решения в целых числах.'
    st1.say 'Э-э-э, н-у-у-у'
    show expression 'pic/locations/school/class4/learn5_1.jpg' at top as tempPic
    bissektrisovna.name 'Неправильно!'
    'На минуту класс наполняется жужжанием и ученик краснеет. Наконец жужжание смолкает.'
    show expression 'pic/locations/school/class4/learn5.jpg' at top as tempPic
    bissektrisovna.name 'Три шара радиуса R касаются друг друга и плоскости  α, четвертый шар радиуса R положен сверху так, что касается каждого из трех данных  шаров. Определи высоту «горки» из четырех шаров.'
    st1.say 'Э-э-э, н-у-у-у'
    show expression 'pic/locations/school/class4/learn5_1.jpg' at top as tempPic
    bissektrisovna.name 'Неправильно!'
    'Жужжание снова наполнет класс, и ученик даже не пытается скрывать, насколько ему хорошо. Разве что не достал свой член.'
    player.say '"Он вообще точно не представляет как решать задачи, или притворяется?"'
    show expression 'pic/locations/school/class4/learn5.jpg' at top as tempPic
    bissektrisovna.name 'В прямоугольник 20 x 25 бросают 120 квадратов 1 x 1. Докажи, что в прямоугольник можно поместить круг с диаметром, равным 1, не имеющий общих точек ни с одним из квадратов.'
    st1.say '8'
    bissektrisovna.name 'Что 8?'
    st1.say 'Ответ...'
    show expression 'pic/locations/school/class4/learn5_1.jpg' at top as tempPic
    bissektrisovna.name '[st1.fname], ты дурак?'
    'И снова парень опростовосился и вибратор, прикрепленный к его уздечке снова приступил к работе. Только на этот раз спустя минуту он не отключился.'
    st1.say 'А можно ещё один вопрос?'
    bissektrisovna.name 'Нет!'
    st1.say 'Я сейчас это... О чёрт!'
    show expression 'pic/locations/school/class4/learn5_2.jpg' at top as tempPic
    'Парень вздрогнул всем телом, и на его штанах начала растекаться пятно спермы.'
    bissektrisovna.name 'А теперь достань его сам, и положи на стол. Следующий!'
    $ move(curloc)