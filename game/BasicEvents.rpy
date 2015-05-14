init:
    image cleanFace = "pic/events/bodyclean/face1.jpg"
    image cleanMouth = "pic/events/bodyclean/mouth1.jpg"
    image cleanBody = "pic/events/bodyclean/body1.jpg"
    image cleanHands = "pic/events/bodyclean/hands1.jpg"
    image cleanFeet = "pic/events/bodyclean/feet1.jpg"
    image cleanPussy = "pic/events/bodyclean/pussy1.jpg"
    image cleanAss = "pic/events/bodyclean/ass1.jpg"
    $ complains = ''

label shower:
    hide screen stats_screen
    $ rands = renpy.random.randint(1, 8)
    show expression ("pic/events/bathroom/%d.jpg" % rands) at top

    if player.stats.dirty == 0:
        'Вы искупались, хотя и не были особо грязными. Как же Вам нравится стоять под нежными струями воды или принимать ванну... Ох, это особое чувство чистоты!'
    else:
        'Вы смыли с себя запах немытого тела. Как же Вам нравится стоять под нежными струями воды или принимать ванну... Ох, это особое чувство чистоты!'

    if player.isSperm() > 0:
        $temp = player.printSperm()
        'Теперь [temp] больше не в сперме.'

    $changetime(15)
    $player.cleanAll()
    $move(curloc)

label cleanFace:
    hide screen stats_screen #скрываем интерфейс
    show cleanFace at top #Показываем картинку
    'Ваше лицо перемазано в сперме. Густые её капли покрывают щеки, носик, губки, пару капель застряли в полосах'
    menu: #меню всё делает за вас
        'Чем бы вытереть эту липкую жидкость?' #текст под меню
        'Вытереть салфетками' if player.hasItem('Салфетка') == True: #показывается, если салфетки ещё есть
            'Вы вытерли салфетками Ваше лицо. Теперь оно сияет прежним внутренним светом!'
            if player.apply('Салфетка') == False:
                'ОШИБКА!!!'#Убираем одну салфетку
            $ player.clean('лицо') #чистим лицо
        'Попытаться вытереть руками':
            $changetime(10) #увеличиваем время
            if rand(1,3) == 1: #Вызываем кастомный рандом
                'На удивление Вам удалось аккуратными движениями пальчиков снять семя с лица, и незаметно стряхнуть её на землю. Личико опять чистое!'
                $ player.clean('лицо') #чистим лицо
            else:
                'Вы лишь ещё сильнее размазали сперму по лицу, вдобавок испачкав руки.'
                $ player.coverSperm('руки') #Заляпываем ещё и руки
        'Да мне и так хорошо!':
            pass #просто пропуск
    $ move(curloc) #Возврат на последнюю локацию

label cleanMouth:
    hide screen stats_screen #скрываем интерфейс
    show cleanMouth at top #Показываем картинку
    'Ваш рот полон спермы. Вы чувствуете её густую терпкость на своём языке.'
    menu:
        'Мне надо избавиться от неё'
        'Выплюнуть':
            $ player.clean('рот')
            'Вы незаметно сплевываете в сторонку. Теперь у Вас чистый ротик'
        'Проглотить' if player.stats.corr > 20:
            'Вы проглатываете тягучую сперму, и ощущаете как Ваш желудок наполняется соками Вашего последнего любовника. Вы чувствуете небольшое возбуждения и развратность этого действия.'
            $ player.stats.lust += 10
            $ player.stats.corr += 1
            $ player.clean('рот')
        'Ммм Ффф ммм ууу!':
            pass
    $ move(curloc) #Возврат на последнюю локацию

label cleanBody:
    hide screen stats_screen
    show cleanBody at top
    'После обильного семяизвержения Ваше тело перемазано в сперме, капли виднеются повсюду.'
    menu:
        'Чем бы вытереть эту липкую жидкость?'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Вы быстрыми движениями вытерли салфетками тягучие капли и очистили себя!'
            $ player.apply('Салфетка')
            $ player.clean('грудь')
        'Попытаться вытереть руками':
            $changetime(10)
            if rand(1,3) == 1:
                'На удивление Вам удалось аккуратными движениями пальцев снять сперму с тела, и стряхнуть её. Вроде бы получилось незаметно!'
                $ player.clean('грудь')
            else:
                'Вы лишь ещё сильнее размазали сперму, вдобавок испачкав руки.'
                $ player.coverSperm('руки')
        'Да вроде бы и так неплохо выглядит!':
            pass
    $ move(curloc)

label cleanHands:
    hide screen stats_screen
    show cleanHands at top
    'Ваши руки перемазаны в сперме. Густые капли маслянистой жидкости приятны на ощупь.'
    menu:
        'Чем бы вытереть эту липкую жидкость?'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Вы вытерли салфетками руки.'
            $ player.apply('Салфетка')
            $ player.clean('руки')
        'Облизать' if player.stats.corr > 40:
            'Вы облизали свои руки от спермы. Это было одновременно приятно и возбуждающе.'
            $ player.stats.lust += 10
            $ player.stats.corr += 2
            $ player.clean('руки')
        'Само высохнет и отвалится!':
            pass
    $ move(curloc)

label cleanFeet:
    hide screen stats_screen
    show cleanFeet at top
    'На Ваших ножках виднеются тягучие белые пятна. Это привлекает очень много ненужного внимания!'
    menu:
        'Чем бы вытереть эту липкую жидкость?'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Вы аккуратными движениями вытерли салфетками ноги. Ножки как ножки, только красивые!'
            $ player.apply('Салфетка')
            $ player.clean('ноги')
        'Попытаться вытереть руками':
            $changetime(10)
            if rand(1,3) == 1:
                'На удивление Вам удалось аккуратными движениями пальцев снять сперму с ножек, и незаметно стряхнуть её. Ножки как ножки, только красивые!'
                $ player.clean('ноги')
            else:
                'Вы лишь ещё сильнее размазали сперму по ногам, вдобавок испачкав руки.'
                $ player.coverSperm('руки')
        'Да вроде и так красиво!':
            pass
    $ move(curloc)

label cleanPussy:
    hide screen stats_screen
    show cleanPussy at top
    'Ваша киска полна спермы. Вы чувствуете её влажное хлюпанье при каждом движении.'
    menu:
        'Ммм. Надо что то сделать с этим.'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Отойдя в сторонку и немного присев, Вы выдавили из своей киски всю сперму прямо на салфетку. Еще раз протерев всё начисто, Вы удовлетворились результатом.'
            $ player.apply('Салфетка')
            $ player.clean('вагина')
        'Попытаться достать её руками' if player.stats.corr > 50:
            $changetime(10)
            'Отойдя в сторонку, вы запустили свои шаловливые пальчики, и принялись доставать из вашей киски сгустки спермы и стряхивать их на пол. Ритмичные движения пальцев в вашей щёлки не добавляют спокойствия.'
            'Через 10 минут работа была закончена, но руки оказались перемазаны в ваших соках и чужой сперме.'
            $ player.clean('вагина')
            $ player.coverSperm('руки')
            $ player.stats.lust += 10
            $ player.stats.corr += 2
        'Это может и подождать.':
            pass
    $ move(curloc)

label cleanAss:
    hide screen stats_screen
    show cleanAss at top
    'Внутри Вашей попки полно семени. Вы чувствуете её влажное хлюпанье при каждом движении.'
    menu:
        'Не самое приятное чувство.'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Отойдя в сторонку Вы аккуратно протёрли салфетками попу. Теперь все чисто.'
            $ player.apply('Салфетка')
            $ player.clean('анус')
        'Попытаться достать её руками' if player.stats.corr > 60:
            $changetime(10)
            'Отойдя в сторонку, вы присели на корточки и запустили свой палец в вашу заднюю дырочку. Неожиданный спазм заставил выделиться из попки не только сперму.'
            if player.hasItem('Салфетка') == True:
                'Хорошо, что у вас оказались салфетки, которыми вы протёрли всё начисто. И стоило заморачиваться с пальцем? - подумали Вы.'
            else:
                'К сожалению вытереть новый конфуз оказалось не чем, и теперь от вас попахивает.'
                $ player.stats.dirty += 1
            $ player.clean('анус')
        'Это может и подождать! Да! Наверное...':
            pass
    $ move(curloc)

label sleep:
    hide screen stats_screen
    python:
        # Изнашивание одежды, если спите в ней.
        for x in player.wear:
            if rand(1,2) == 1:
                x.durability -= 1
                player.checkDur()
                
        global hour, ptime, last_sleeped
        
        if weekday != 5 and weekday != 6:
            hour_up = 7
        else:
            hour_up = 12
            
        if hour >= 0:
            start_hour = hour - 24
        else:
            start_hour = hour
        sleeped = 0
        while player.stats.energy < player.stats.health and start_hour < hour_up and sleeped < 12:
            changetime(60)
            last_sleeped = ptime
            start_hour += 1
            player.stats.energy += player.getHealth()/10
            sleeped += 1
        player.reset()
        if rand(1,3) > 2:
            tryEvent('loc_dreams')
        renpy.jump('loc_dreams')

label loc_dreams:
    hide screen show_stats
    $ rands = rand(1,11)
    show expression ("pic/locations/home/dream/no%d.jpg" % rands) at top
    'В это раз Вам ничего не снилось и, провалившись в ласковые объятия сна, Вы отлично выспались.'
    $ move('loc_bedroom')

label naked:
    if player.getClothPurpose('swim'):
        show expression ("pic/events/various/bikini.png") at top
    else:
        show expression ("pic/events/various/naked.jpg") at top

    player.say 'Я не могу выходить на улицу в таком виде!!!'
    $ move(prevloc)

label loc_swim:
    show beach
    if player.stats.energy < 200:
        player.say 'Я слишком устала, чтобы плавать... Пора возвращаться домой.'
    elif player.getClothPurpose('swim') == False:
        player.say 'Я не могу плавать в одежде!'
    else:
        hide screen show_stats
        $ rands = rand(1,5)
        show expression ("pic/events/beach/swim_norm%d.jpg" % rands) at top
        'Вы поплавали часок, и немного устали. По крайней мере Ваша физическая форма улучшилась.'
        $ changetime(60)
        $ player.stats.energy -= rand(100,300)
        $ player.stats.health += rand (10,20)
        $ player.cleanAll()
    $ move('loc_beach')
    
label loc_taxi:
    show expression 'pic/locations/taxi.jpg'
    $ money = player.money
    menu:
        'Куда поедем? Городочек маленький, проезд в любую сторону всего по 50.'
        'Пляж' if curloc != 'loc_beach' and money >= 50:
            $ player.money -= 50
            $ changetime(10)
            $ move('loc_beach')
        'Домой' if curloc != 'loc_street' and money >= 50:
            $ player.money -= 50
            $ changetime(10)
            $ move('loc_home')
        'На торговую' if curloc != 'loc_shopStreet' and money >= 50:
            $ player.money -= 50
            $ changetime(10)
            $ move('loc_shopStreet')
        'К школе' if curloc != 'loc_entrance' and money >= 50:
            $ player.money -= 50
            $ changetime(10)
            $ move('loc_entrance')
        'Я передумала' if money >= 50:
            $ move (curloc)
        'Простите, но у меня нет денег' if money < 50:
            $ move (curloc)

label unconsciousSchool:
    show expression 'pic/events/uncon/1.jpg' at top
    'Вы упали без сознания от переутомления. Вы пролежали пару часов, пока Вас не нашли случайные ученики.'
    'Проснувшись, Вы обнаружили, что Вас обыскивали, верхняя одежда снята, на теле синяки.'
    if player.money > 200:
        $ player.money -= rand(100,200)
    $ setRep(2,-2)
    $ player.setEnergy(200)
    $ changetime(rand(100,200))
    $ move(curloc)
    
label unconsciousOther:
    show expression 'pic/events/uncon/2.jpg' at top
    'Вы упали без сознания от переутомления прямо на улице. Вы пролежали пару часов, пока Вас не нашли случайные люди.'
    'Проснувшись, Вы обнаружили свежее пятно спермы на одежде.'
    $ player.body.parts['грудь'].sperm = True
    if player.money > 200:
        $ player.money -= rand(100,200)
    $ setRep(10,-2)
    $ player.setEnergy(200)
    $ changetime(rand(100,200))
    $ move(curloc)

label stolen:
    show office
    show computer at top
    $ temp = school.baseIncome*rand(1,5)
    $ player.money += temp
    'Проведя пару фиктивных сделок, вы смогли вывести [temp] монет со счёта школы.'
    'Надо быть осторожней, и чаще подчищать следы, чтобы меня не поймали.'
    $ changetime(120)
    $ move(curloc)
    
label catched:
    show office
    show computer at top
    'У вас не получилось безопасно вывести деньги, и ваши махинации засекли.'
    'Проследив всю цепочку, инспекторы выписали вам штраф в 5 МРОТ за каждый обнаруженный инцидент, и сделали в вашем личном деле внеочередную пометку о неблагонадёжности.'
    python:
        setRep(50,-school.caughtChance)
        player.money -= school.caughtChance*school.baseIncome*5
        school.caughtChance = 0
        changetime(120)
        move(curloc)
        
label cover:
    show office
    show computer at top
    if player.getEdu() < school.caughtChance*10 and school.caughtChance > 1:
        'У вас не получилось полностью скрыть следы. Надо пробовать ещё.'
        $ school.caughtChance -= 1
    else:
        'Вы скрыли следы своего преступления'
        $ school.caughtChance = 0
    $ changetime(120)
    $ move (curloc)

label increaseIncome:
    show office
    show computer at top
    if stat_edu*100 > school.baseIncome:
        $ temp = stat_edu*100 - school.baseIncome
        $ school.baseIncome += temp
        'Вы успешно выбили себе повышение на [temp] монет за каждый рабочий день.'
    else:
        'Вам не удалось достаточно замотивировать Министерсто Образования.'
        'Они отклонили вашу просьбу о повышении, мотивируя это недостаточно высоким уровнем образования в школе.'
    $ changetime(120)
    $ move(curloc)
    
label working:
    show office
    show computer at top
    'Вы поработали, заполняя различные документы, подписывая акты и выполняя прочую бумажную работу. На сегодня работа закончена.'
    if rand(1,3) == 1:
        'В одном из документов Вы натолкнулись на интересную тему для изучения, и слегка повысили свой уровень образования.'
        $ player.setEdu(1)
    $ changetime(120)
    $ move(curloc)
    
label income:
    show expression 'pic/events/income/income.png' at top as tempPic
    python:
        global complains
        temp = school.myIncome()
        player.money += temp
        checkJail()
        complains = ''
        school.workedDays = 0
        for x in studs:
            if x.getRep()<10:
                complains += x.name
                complains += ', '
        if complains != '':
            complains = complains[:-2] + '.'
    'Вам позвонили из бухгалтерии министерства образования.'
    'Зарплата в размере [temp] была зачислена на ваш счёт.'
    if complains != '':
        'Вас так же уведомили, что вами недовольны родители следующих учеников:\n[complains]'
    $ move(curloc)
    
label jail:
    show expression 'pic/events/various/jail1.png' at top as tempPic
    'Ваc уволили. Репутация как минимум у родителей одного ученика упала почти до нуля. Было инициировано расследование, по результатам которого всплыли все Ваши грязные методы образования и закрытие глаз на вертеп, творящейся в вашей школе.'
    'Суд был непреклонен и Вас отправили в самую грязную тюрьму в стране.'
    'Там Вас заставляли есть собачий корм и ходить под себя. Спустя месяц это сломало вас.'
    show expression 'pic/events/various/jail2.png' at top as tempPic
    show text 'Спустя пол года' at truecenter 
    with dissolve
    pause 1
    hide text
    with dissolve
    'Свою первую нормальную еду Вы получили только после того, как переспали с одним их посетителей.'
    'Оказывается начальница зарабатывала тем, что сдавала сломавшихся девушек в прокат на пару часов. По сути обычный бордель.'
    'Обещание еды, заставило сокращаться вашу киску гораздо сильнее, чем когда либо, и довльный клиент потребовал продолжения, и её, и снова...'
    'До тех пор пока Вы в полубессознательном состоянии наконец то не закричали от оргазма.'
    show expression 'pic/events/various/jail3.png' at top as tempPic
    show text 'Спустя год' at truecenter 
    with dissolve
    pause 1
    hide text
    with dissolve
    'Вскоре многие клиенты подпольного борделя захотели испробовать вашу задницу. И начальница лично занялась этим вопросом, планомерно расширяя Ваш анал до тех пор, пока в него не смог поместиться её кулак.'
    'Вам было всё равно, Вы хотели жрать, потому что на время тренировки клиентов к Вам не подпускали.'
    show expression 'pic/events/various/jail4.png' at top as tempPic
    show text 'Спустя ещё месяц' at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    'Вы с радостью трахали всех, кого Вам поставляли. Один, два, трое, без разницы! Чем больше чем лучше! Ваши отверстия привыкли принимать в себя любое количество и любой размер, пока хватало сил.'
    'А когда силы кончались, Вас просто трахали как игрушку.'
    show expression 'pic/events/various/jail5.png' at top as tempPic
    show text 'Спустя 5 лет' at truecenter 
    with dissolve
    pause 1
    hide text
    with dissolve
    '[player.fname], сегодня день твоего освобождения, ты готова уйти? - спросила Вас в одну утро начальница.'
    player.say 'Устройте мне праздник, госпожа! Найдите самый большой член в городе! - неожиданно попросили Вы.'
    'Конечно, как пожелаешь! - улыбнулась начальница и спустя пол часа, Вас уже яростно таранил огромный член незнакомца, раздвигая стенки вашего раздолбанного влагалища.'
    player.say 'Еби меня! Еби! - кричали Вы в экстазе, понимая, что никуда Вы больше не уйдёте отсюда, всё что Вам надо это жрать, спать и трахаться. Трахаться так, как никогда в жизни. И так всю оставшуюся жизнь.'
    centered 'Конец Игры'
    $ renpy.quit(relaunch = True)
    return
    
label death:
    show expression 'pic/events/various/death.jpg' at top as tempPic
    'Вы умерли от истощения. Иногда, кто нибудь из учеников приходит на вашу могилу, и тихо вспоминает вас.'
    show text 'Конец Игры' at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    $ renpy.quit(relaunch = True)
    
label scoldAll:
    show expression 'pic/locations/school/class1/lo1b.jpg' at top as tempPic
    'Яростным свистом в свой директорский свисток, Вы прервали разворачивающиеся перед вашими глазами непотребство, и приказали всем участникам остаться после уроков. Раздасованные ученики понурив головы, пообещали Вам придти.'
    python:
        for x in scoldWho:
            x.setLoy(-1)
            x.setRep(1)
            addDetention(x)
        move(curloc)