label event_loc_teacherRoom_0_1:
    show teacherRoom
    python:
        if hour < 15 or hour > 20:
            skipEvent()
    'Вы вошли как раз в тот момент, когда учителя проводили внутреннее совещание по вопросам финансирования школы и распределения бюджетных средств на ближайший месяц.'
    player.say '"Это может затянуться... Если уйду - потеряю лояльность. Если останусь - потеряю время. Диллема."'
    menu:
        'Уйти':
            'Выбрав как то дурацкий предлог, вы покидаете собрание, которое без вашего участия довольно скоро заканчивается.'
            $ choice(teachers).incLoy(-5)
            $ choice(teachers).incLoy(-5)
            $ changetime(20)
        'Остаться':
            'Вы высиживаете невыносимо долгие 4 часа на очередном бессмысленном собрании. По крайней мере кому то из учителей ваше участие помогло...'
            $ choice(teachers).incLoy(5)
            $ choice(teachers).incLoy(5)
            $ changetime(4*60)
    $ move(curloc)
    
label event_loc_teacherRoom_0_new1:
    show teacherRoom
    $ player.incLust(5)
    show expression 'pic/locations/school/teacherRoom/new1.png' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    player.say 'Э-э-э, [bissektrisovna.name]?'
    bissektrisovna.say 'Что? Меня просто обрызгал какой то мужлан на своём геленвагене, и мне необходимо переодеться. Не обращайте внимания!'
    if player.getCorr() > 20:
        player.say '"Легко сказать! "Не обращайте внимания". Как тут можно не обращать?"'
        'И вы продолжили наслаждаться шикарным видом на тело переодевающейся учительницы.'
    else:
        hide tempPic
        'И вы поспешно отворачиваетесь, стараясь прогнать увиденное из головы.'
    $ move(curloc)
    
label event_loc_teacherRoom_0_new2:
    show teacherRoom
    $ player.incLust(10)
    show expression 'pic/locations/school/teacherRoom/new2.png' at top as tempPic
    if danokova.getLoy() < 30:
        danokova.say '[player.fname]! Не могли бы вы перестать изучать меня только внимательно?'
        player.say 'А, собственно, что вы делаете?'
        danokova.say 'Переодеваюсь. По моему это очевидно.'
        player.say 'А почему не в туалете?'
        danokova.say 'А по почему вы не писаете на подоконнике?'
        player.say 'Что?'
        danokova.say 'У каждого помещения своё предназначение. В туалете писают, в ванной моются, в учительской - переодеваются.'
        player.say '"Не думаю, что я смогу переубедить её."'
    else:
        danokova.say '[player.name], если вы решили полюбваться, то на здоровье, просто не делайте это столь прямо.'
        player.say 'Конечно, конечно...'
    $ move(curloc)
    
label event_loc_teacherRoom_0_new3:
    show teacherRoom
    $ player.incLust(10)
    show expression 'pic/locations/school/teacherRoom/new3.png' at top as tempPic
    frigidovna.say 'Просите, что застаёте меня в таком виде, просто мне необходимо переодеться в нормальную одежду. Я, надеюсь, вы не против?'
    player.say 'Ну о чём вы, [frigidovna.name]! Для вас - в любой момент!'
    frigidovna.say 'Что, простите?'
    player.say 'Ничего - ничего! Переодевайтесь, меня тут уже нет!'
    $ move(curloc)
    
label event_loc_teacherRoom_0_new4:
    show teacherRoom
    $ player.incLust(10)
    show expression 'pic/locations/school/teacherRoom/new4.png' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    kupruvna.say 'Ой! Простите! Я сейчас!'
    player.say 'Да ничего, я уже привыкла, что тут раздевалка, а не учительская. Не торопитесь.'
    $ move(curloc)
    
label event_loc_teacherRoom_0_new5:
    show teacherRoom
    python:
        if dikovna.getCorr() < 30:
            skipEvent()
        player.incLust(10)
        dikovna.incLoy(5)
    show expression 'pic/locations/school/teacherRoom/new5.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    dikovna.say 'What? Oh! It\'s You! I thought... Простите, я не думала, что кто то войдёт, а в туалете все места были заняты... Простите, I will clean in shortly!'
    'Вы шумно сглатываете, разглядывая огромный болт в руках учительницы.'
    player.say 'Да, будьте так добры, приберитесь немножко. И постарайтесь не забыть запереть дверь в следующий раз!'
    $ move(curloc)
    
label event_loc_teacherRoom_0_new6:
    show teacherRoom
    $ player.incLust(10)
    show expression 'pic/locations/school/teacherRoom/new6.png' at top as tempPic
    dikovna.say 'Oh! It\'s you! Я тут подумала, что it will be a little uneasy, to change прямо в школьной раздевалке, и решила переодеться прямо тут! Правда я не думала, что кто то войдёт...'
    'Учительница стояла прямо перед вами, и её полувставший член слегка подрагивал на уровне вашего пояса. Точнее чуть пониже. Вы прикрыли глаза, стараясь прогнать наваждение.'
    player.say 'Да, пожалуй, это не худшее решение. Не все смогут понять...'
    $ move(curloc)
    
label event_loc_teacherRoom_0_new7:
    show teacherRoom
    python:
        if mustangovich.getCorr() < 30:
            skipEvent()
        player.incLust(20)
    show expression 'pic/locations/school/teacherRoom/new7.png' at top as tempPic
    player.say '[mustangovich.name]????'
    mustangovich.say 'Я тут это...'
    player.say 'Не надо! Я не уверена, что хочу знать!'
    if mile_quest_1 == 2 and player.getLust() > 70:
        player.say '"Чёрт! Как я его хочу!"'
        $ tryEvent('loc_ahmedSex')
    $ move(prevloc)
    
label event_loc_teacherRoom_0_ask1:
    show teacherRoom
    if is_teacher_room_1 == 1:
        $ skipEvent()
    show expression getCharImage(player,'dialog') as temp1
    show expression getCharImage(bissektrisovna,'dialog') as temp2
    if is_teacher_room_1 == 0:
        bissektrisovna.say 'Нам нужны новые книги!'
        player.say 'По какому предмету и с какой целью?'
        bissektrisovna.say 'По математике конечно! - удивлённо поднимает брови [bissektrisovna.fname], - Старые совсем износились, да и в педагогическом плане порядком устарели.'
        player.say 'Откуда же по вашему я возьму на них деньги? - приподнимаете вы брови'
        bissektrisovna.say 'Ничего не знаю! Предыдущий директор как то сам решал этот вопрос! - начинает распаляться учительница'
        player.say 'Ага, и именно поэтому теперь вместо него - я. Хорошо, я подумаю над этим вопросом, но ничего не обещаю, - отвечаете вы и даёте понять, что разговор закончен.'
    else:
        $ speech = rand(1,5)
        if speech = 1: 
            bissektrisovna.say 'Грызуны сгрызли все мои учебники! - сокрушается [bissektrisovna.fname], - нам необходимо закупить новые!'
        if speech = 2: 
            bissektrisovna.say 'Прорвало трубу, и все учебники залило! - сокрушается [bissektrisovna.fname], - нам необходимо закупить новые!'
        if speech = 3: 
            bissektrisovna.say 'Ученики разлили какие то химикаты на мои учебники! - сокрушается [bissektrisovna.fname], - нам необходимо закупить новые!'
        if speech = 4: 
            bissektrisovna.say 'Кто то запустил кота, и он обоссал все мои учебники! - сокрушается [bissektrisovna.fname], - нам необходимо закупить новые!'
        if speech = 5: 
            bissektrisovna.say 'Учебники были некачественные, и на них уже выцвели буквы! - сокрушается [bissektrisovna.fname], - нам необходимо закупить новые!'
    hide temp2
    menu:
        'Закупить обычные учебники (1000 монет)' if school.budget >= 1000:
            $ school.budget -= 1000
            $ setEdu(50,5)
            'Вы закупили обычные учебники. Образование в школе выросло.'
            $ is_teacher_room_1 = 1
        'Закупить лучшие учебники (2000 монет)' if school.budget >= 2000:
            $ school.budget -= 2000
            $ setEdu(50,10)
            'Вы закупили лучшие учебники. Образование в школе сильно выросло.'
            $ is_teacher_room_1 = 1
        'Закупить экспериментальную партию под соавторством Де Сада(5000 монет)' if school.budget >= 5000:
            if bissektrisovna.getCorr() < 40:
                'Вы закупили экспериментальную партию учебников по математике под соавторством Де Сада. Увидев их, учительница тут же выбросила их на мусорку. Вам с трудом удалось сбагрить эти книги по заниженной цене.'
                $ school.budget -= 1000
            else:
                'Вы закупили экспериментальную партию учебников по математике под соавторством Де Сада. Образованию они не помогли, но что то в школе изменилось. Вы чувствуте, что даже пахнуть стало немного по другому. Как то развратнее.'
                $ is_teacher_room_1 = 1
                $ setCorr(50,5)
        'Не закупать ничего':
            'Вы приняли решение не закупать ничего. Это явно отразится на образованности ваших учащихся и на лояльности математички.'
            $ setEdu(50,-2)
            $ bissektrisovna.incLoy(-5)
    $ move(curloc)
    
label event_loc_teacherRoom_0_ask2:
    show teacherRoom
    if is_teacher_room_2 == 1:
        $ skipEvent()
    show expression getCharImage(player,'dialog') as temp1
    show expression getCharImage(dikovna,'dialog') as temp2
    if is_teacher_room_2 == 0:
        dikovna.say 'I am afraid, but..'
        player.say 'Что? - прерываете вы учительницу по английскому языку.'
        dikovna.say 'I am sorry, то есть простите, но наша библиотека уж давно не обновлялась, - снова начинает [dikovna.name]'
        player.say 'На ремонт денег у меня нет, даже в том случае, если завтра все книги будут похоронены под слоем отвалившейся от старости штукатуркой - снова прерываете вы её.'
        dikovna.say ' No, я не про это. Наполнение библиотеки слишком бедно, чтобы удовлетворить страсть наших учеников к изучению английского языка - явно преувеличивает [dikovna.fname].'
        player.say 'И при чём тут я? - удивляетесь вы.'
        dikovna.say 'Ну я подумала, что может быть вы могли бы издать decree on закупке новых книг? - заискивающе смотрит вам в глаза учительница.'
        player.say 'Я могу даже издать указ о закупке здании парламента для нужд школы. Только кто даст мне на это денег? - начинаете вы возмущаться.'
        dikovna.say 'А разве в бюджете больше ни копеечки не осталось?'
        player.say 'Ладно, я подумаю, что можно сделать.'
    else:
        $ speech = rand(1,4)
        if speech = 1: 
            dikovna.say 'Tief! Tief! Вор! У нас кто то украл почти всю нашу библиотеку! - возмущается [dikovna.name], - может быть купим новые книжки?'
        if speech = 2: 
            dikovna.say 'Maybe закупим ещё книжек для библиотеки? - заискивает [dikovna.name]'
        if speech = 3: 
            dikovna.say 'Students растащили по домам половину нашей библиотеки! - сокрушается [dikovna.name], - может быть купим новые книжки?'
        if speech = 4: 
            dikovna.say 'Somebody burned my books! Даже "451 градус по Фаренгейту"! - недоумевает [dikovna.name], - может быть купим новые книжки?'
        player.say '"Да когда же это закончится!"'
    hide temp2
    menu:
        'Закупить обычные учебники (1000 монет)' if school.budget >= 1000:
            $ school.budget -= 1000
            $ setEdu(50,5)
            'Вы закупили обычные учебники. Образование в школе выросло.'
            $ is_teacher_room_2 = 1
        'Закупить лучшие учебники (2000 монет)' if school.budget >= 2000:
            $ school.budget -= 2000
            $ setEdu(50,10)
            'Вы закупили лучшие учебники. Образование в школе сильно выросло.'
            $ is_teacher_room_2 = 1
        'Закупить экспериментальную партию под соавторством Де Сада(5000 монет)' if school.budget >= 5000:
            if dikovna.getCorr() < 40:
                'Вы закупили экспериментальную партию учебников по математике под соавторством Де Сада. Увидев их, учительница тут же выбросила их на мусорку. Вам с трудом удалось сбагрить эти книги по заниженной цене.'
                $ school.budget -= 1000
            else:
                'Вы закупили экспериментальную партию учебников по математике под соавторством Де Сада. Образованию они не помогли, но что то в школе изменилось. Вы чувствуте, что даже пахнуть стало немного по другому. Как то развратнее.'
                $ is_teacher_room_2 = 1
                $ setCorr(50,5)
        'Не закупать ничего':
            'Вы приняли решение не закупать ничего. Это явно отразится на образованности ваших учащихся и на лояльности математички.'
            $ setEdu(50,-2)
            $ dikovna.incLoy(-5)
    $ move(curloc)
    
label event_loc_teacherRoom_0_ask3:
    show teacherRoom
    if is_teacher_room_3 == 1:
        $ skipEvent()
    show expression getCharImage(player,'dialog') as temp1
    show expression getCharImage(danokova,'dialog') as temp2
    if is_teacher_room_3 == 0:
        danokova.say 'Эмм. - начинает разговор [danokova.name].'
        'Вы устремляете на неё удивлённый взгляд, ожидая продолжения.'
        danokova.say 'Мда, - говорит учительница, и разворачивается. Вы видите, что она собирается уходить.'
        player.say 'Вы что то хотели? - окликиваете вы уходящую учительницу биологии.'
        danokova.say 'А? Вы со мной? - делает она немного глупое выражение лица.'
        player.say 'Конечно, это же вы ко мне первой подошли... Вы что то хотели спросить?'
        danokova.say 'Ах, да, жуки! - говорит она и смотрит на вас с ожиданием.'
        'В этот момент в вашей голове проносятся все виды жуков, начиная от скорпионов, и кончая собственными тараканами в голове.'
        player.say 'Эммм, что жуки? - не понимая спрашиваете вы.'
        danokova.say 'Ну или гады там, змеи, ящерицы. - продолжает загонять вас в тупик биологичка.'
        player.say 'Что с ними? - задаёте вы наводящий вопрос, пытаясь понять мысли учительницы'
        danokova.say 'Они бегают! - немного радостоно сообщает преподавательница. Вы почему то уже совершенно не удивлены этим ответом'
        player.say 'А что же им ещё делать? - недоумеваете вы, отчаявшись понять куда клонит [danokova.fname].'
        danokova.say ' Сидеть конечно же. В клетках, в моём кабинете. - снисходительно смотрит на вас биологичка, как будто вы умственно отсталый ребёнок.'
        player.say 'Вы хотите посадить животных в клетки в вашем кабинете? - ухватываете вы нить её мысли.'
        danokova.say 'Нет, - улыбка слетает с её лица. - Я хочу, чтобы вы их купили.'
        player.say '"Ок. Она странная. Она хочет, чтобы я купила разных зверюшек в её кабинет. Наверно для наглядного примера. Да, её сложно понять, но мне с ней работать."'
    else:
        danokova.say 'Он убежал, или пропал. Скорее первое, чем второе - с отстранённым видом говорит [danokova.name]'
        player.say 'Ок, я всё поняла, можешь не продолжать, - скороговоркой говорите вы, пока вас не начали погружать в пучину неадеквата.'
        player.say '"Как она детей то учит?"'
    hide temp2
    menu:
        'Купить хомячкa (200)' if player.money >= 200:
            $ player.money -= 200
            $ setLoy(50,2)
            player.say 'Хо-мя-чок, - по слогам говорите вы, но [danokova.fname] уже опять впала в своё полукоматозное состояние.'
            $ is_teacher_room_3 = 1
        'Купить ящерицу(1000)' if player.money >= 1000:
            $ player.money -= 1000
            $ setLoy(50,5)
            player.say 'Пусть будет ящерица, - тихо бурчите вы, но вас уже не слышат.'
            $ is_teacher_room_3 = 1
        'Купить змею(5000)' if player.money >= 5000:
            $ player.money -= 5000
            $ setLoy(50,10)
            $ is_teacher_room_3 = 1
            player.say 'Питон, он всем людям знаком - пытаетесь вы хохмить, но понимаете, что в этом обществе вашу хохму не оценят.'
        'Не закупать ничего':
            'Вы приняли решение не закупать ничего. Вам не кажется, что кто то расстроится, если у него вдруг не появится карманного питона.'
    $ move(curloc)