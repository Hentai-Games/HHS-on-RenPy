init:
    image cleanFace = "pic/events/bodyclean/face1.jpg"
    image cleanMouth = "pic/events/bodyclean/mouth1.jpg"
    image cleanBody = "pic/events/bodyclean/body1.jpg"
    image cleanHands = "pic/events/bodyclean/hands1.jpg"
    image cleanFeet = "pic/events/bodyclean/feet1.jpg"
    image cleanPussy = "pic/events/bodyclean/pussy1.jpg"
    image cleanAss = "pic/events/bodyclean/ass1.jpg"
    image centeredText = ParameterizedText(xalign=0.5, yalign=0.5, style = 'navigation_button_text')
    $ complains = ''

label shower:
    hide screen stats_screen
    show expression ('pic/events/bathroom/shower%d.png' %rand(1,2)) at Move((0.0, 0.0), (0.0, -1.1), 10.0, repeat = True, bounce = True, xanchor="left", yanchor="top")
    if player.stats.dirty == 0:
        'Вы искупались, хотя и не были особо грязными. Как же вам нравится стоять под нежными струями воды или принимать ванну... Ох, это особое чувство чистоты!'
    else:
        'Вы смыли с себя запах немытого тела. Как же вам нравится стоять под нежными струями воды или принимать ванну... Ох, это особое чувство чистоты!'

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
            'Вы вытерли салфетками ваше лицо. Теперь оно сияет прежним внутренним светом!'
            if player.apply('Салфетка') == False:
                'ОШИБКА!!!'#Убираем одну салфетку
            $ player.clean('лицо') #чистим лицо
        'Попытаться вытереть руками':
            $changetime(10) #увеличиваем время
            if rand(1,3) == 1: #Вызываем кастомный рандом
                'На удивление вам удалось аккуратными движениями пальчиков снять семя с лица, и незаметно стряхнуть её на землю. Личико опять чистое!'
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
            'Вы незаметно сплевываете в сторонку. Теперь у вас чистый ротик'
        'Проглотить' if player.stats.corr > 20:
            'Вы проглатываете тягучую сперму, и ощущаете как ваш желудок наполняется соками вашего последнего любовника. Вы чувствуете небольшое возбуждения и развратность этого действия.'
            $ player.stats.lust += 10
            $ player.stats.corr += 1
            $ player.clean('рот')
        'М-м-м Ф-ф-ф м-м-м у-у-у!':
            pass
    $ move(curloc) #Возврат на последнюю локацию

label cleanBody:
    hide screen stats_screen
    show cleanBody at top
    'После обильного семяизвержения ваше тело перемазано в сперме, капли виднеются повсюду.'
    menu:
        'Чем бы вытереть эту липкую жидкость?'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Вы быстрыми движениями вытерли салфетками тягучие капли и очистили себя!'
            $ player.apply('Салфетка')
            $ player.clean('грудь')
        'Попытаться вытереть руками':
            $changetime(10)
            if rand(1,3) == 1:
                'На удивление вам удалось аккуратными движениями пальцев снять сперму с тела, и стряхнуть её. вроде бы получилось незаметно!'
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
    'На ваших ножках виднеются тягучие белые пятна. Это привлекает очень много ненужного внимания!'
    menu:
        'Чем бы вытереть эту липкую жидкость?'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Вы аккуратными движениями вытерли салфетками ноги. Ножки как ножки, только красивые!'
            $ player.apply('Салфетка')
            $ player.clean('ноги')
        'Попытаться вытереть руками':
            $changetime(10)
            if rand(1,3) == 1:
                'На удивление вам удалось аккуратными движениями пальцев снять сперму с ножек, и незаметно стряхнуть её. Ножки как ножки, только красивые!'
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
            'Отойдя в сторонку и немного присев, вы выдавили из своей киски всю сперму прямо на салфетку. Еще раз протерев всё начисто, вы удовлетворились результатом.'
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
    'Внутри вашей попки полно семени. Вы чувствуете её влажное хлюпанье при каждом движении.'
    menu:
        'Не самое приятное чувство.'
        'Вытереть салфетками' if player.hasItem('Салфетка') == True:
            'Отойдя в сторонку вы аккуратно протёрли салфетками попу. Теперь все чисто.'
            $ player.apply('Салфетка')
            $ player.clean('анус')
        'Попытаться достать её руками' if player.stats.corr > 60:
            $changetime(10)
            'Отойдя в сторонку, вы присели на корточки и запустили свой палец в вашу заднюю дырочку. Неожиданный спазм заставил выделиться из попки не только сперму.'
            if player.hasItem('Салфетка') == True:
                'Хорошо, что у вас оказались салфетки, которыми вы протёрли всё начисто. И стоило заморачиваться с пальцем? - подумали вы.'
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
    show expression ("pic/locations/home/dream/no%d.jpg" % rand(1,11)) at top
    'В это раз вам ничего не снилось и, провалившись в ласковые объятия сна, вы отлично выспались.'
    $ move(curloc)

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
        show expression ("pic/events/beach/swim_norm%d.jpg" % rand(1,5)) at top
        'Вы поплавали часок, и немного устали. По крайней мере ваша физическая форма улучшилась.'
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
    'Вы упали без сознания от переутомления. Вы пролежали пару часов, пока вас не нашли случайные ученики.'
    'Проснувшись, вы обнаружили, что вас обыскивали, верхняя одежда снята, на теле синяки.'
    if player.money > 200:
        $ player.money -= rand(100,200)
    $ setRep(2,-2)
    $ player.setEnergy(200)
    $ changetime(rand(100,200))
    $ move(curloc)
    
label unconsciousOther:
    show expression 'pic/events/uncon/2.jpg' at top
    'Вы упали без сознания от переутомления прямо на улице. Вы пролежали пару часов, пока вас не нашли случайные люди.'
    'Проснувшись, вы обнаружили свежее пятно спермы на одежде.'
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
    $ school.budget -= stolenMoney
    $ player.money += stolenMoney
    'Проведя пару фиктивных сделок, вы смогли вывести [stolenMoney] монет со счёта школы.'
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
        'Вам не удалось достаточно замотивировать Министерство Образования.'
        'Они отклонили вашу просьбу о повышении, мотивируя это недостаточно высоким уровнем образования в школе.'
    $ changetime(120)
    $ move(curloc)
    
label working:
    show office
    show computer at top
    'Вы поработали, заполняя различные документы, подписывая акты и выполняя прочую бумажную работу. На сегодня работа закончена.'
    if rand(1,3) == 1:
        'В одном из документов вы натолкнулись на интересную тему для изучения, и слегка повысили свой уровень образования.'
        $ player.setEdu(1)
    $ changetime(120)
    $ move(curloc)
    
label invest:
    show office
    show computer at top
    python:
        investment = renpy.input('Вы решили инвестировать в школу часть своих средств.\nВведите сумму, которую вы собираетесь инвестировать.', default= player.money, allow='{1234567890}')
        investment = int(investment)
    if investment > player.money:
        player.say 'Я не могу инвестировать больше средств, чем имею!'
        jump invest
    else:
        python:
            player.money -= investment
            school.budget += investment
            changetime(120)
            move(curloc)
    
label income:
    show expression 'pic/events/income/income.png' at top as tempPic
    python:
        global complains
        temp = school.myIncome()
        player.money += temp
        school.budget -= temp
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
    if school.budget < 0:
        'Несмотря на то, что в результате на счету школы образовалась задолженность.'
    if complains != '':
        'Вас так же уведомили, что вами недовольны родители следующих учеников:\n[complains]'
    $ move(curloc)
    
label jail:
    show expression 'pic/events/various/jail1.png' at top as tempPic
    'Ваc уволили. Репутация как минимум у родителей одного ученика упала почти до нуля. Было инициировано расследование, по результатам которого всплыли все ваши грязные методы образования и закрытие глаз на вертеп, творящейся в вашей школе.'
    'Суд был непреклонен и вас отправили в самую грязную тюрьму в стране.'
    'Там вас заставляли есть собачий корм и ходить под себя. Спустя месяц это сломало вас.'
    show expression 'pic/events/various/jail2.png' at top as tempPic
    show centeredText 'Спустя пол года' at truecenter 
    with dissolve
    pause 1
    hide centeredText
    with dissolve
    'Свою первую нормальную еду вы получили только после того, как переспали с одним их посетителей.'
    'Оказывается начальница зарабатывала тем, что сдавала сломавшихся девушек в прокат на пару часов. По сути обычный бордель.'
    'Обещание еды, заставило сокращаться вашу киску гораздо сильнее, чем когда либо, и довольный клиент потребовал продолжения, и её, и снова...'
    'До тех пор пока вы в полубессознательном состоянии наконец то не закричали от оргазма.'
    show expression 'pic/events/various/jail3.png' at top as tempPic
    show centeredText 'Спустя год' at truecenter 
    with dissolve
    pause 1
    hide centeredText
    with dissolve
    'Вскоре многие клиенты подпольного борделя захотели испробовать вашу задницу. И начальница лично занялась этим вопросом, планомерно расширяя ваш анал до тех пор, пока в него не смог поместиться её кулак.'
    'Вам было всё равно, вы хотели жрать, потому что на время тренировки клиентов к вам не подпускали.'
    show expression 'pic/events/various/jail4.png' at top as tempPic
    show centeredText 'Спустя ещё месяц' at truecenter
    with dissolve
    pause 1
    hide centeredText
    with dissolve
    'Вы с радостью трахали всех, кого вам поставляли. Один, два, трое, без разницы! Чем больше чем лучше! Ваши отверстия привыкли принимать в себя любое количество и любой размер, пока хватало сил.'
    'А когда силы кончались, вас просто трахали как игрушку.'
    show expression 'pic/events/various/jail5.png' at top as tempPic
    show centeredText 'Спустя 5 лет' at truecenter 
    with dissolve
    pause 1
    hide centeredText
    with dissolve
    '[player.fname], сегодня день твоего освобождения, ты готова уйти? - спросила вас в одну утро начальница.'
    player.say 'Устройте мне праздник, госпожа! Найдите самый большой член в городе! - неожиданно попросили вы.'
    'Конечно, как пожелаешь! - улыбнулась начальница и спустя пол часа, вас уже яростно таранил огромный член незнакомца, раздвигая стенки вашего раздолбанного влагалища.'
    player.say 'Еби меня! Еби! - кричали вы в экстазе, понимая, что никуда вы больше не уйдёте отсюда, всё что вам надо это жрать, спать и трахаться. Трахаться так, как никогда в жизни. И так всю оставшуюся жизнь.'
    show centeredText 'Конец Игры' at truecenter 
    with dissolve
    pause 5
    hide centeredText
    with dissolve
    $ renpy.quit(relaunch = True)
    
label death:
    show expression 'pic/events/various/death.jpg' at top as tempPic
    'Вы умерли от истощения. Иногда, кто нибудь из учеников приходит на вашу могилу, и тихо вспоминает вас.'
    show centeredText 'Конец Игры'
    with dissolve
    pause 5
    hide centeredText
    with dissolve
    $ renpy.quit(relaunch = True)
    
label scoldAll:
    show expression 'pic/locations/school/class1/lo1b.jpg' at top as tempPic
    'Яростным свистом в свой директорский свисток, вы прервали разворачивающиеся перед вашими глазами непотребство, и приказали всем участникам остаться после уроков. Раздосадованные ученики понурив головы, пообещали вам придти.'
    python:
        for x in scoldWho:
            x.setLoy(-1)
            x.setRep(1)
            addDetention(x)
        move(curloc)
        
        
label inhib1:
    show expression 'pic/events/inhibLow/arh.jpg' at top as tempPic
    'Покопавшись в интернете, вы довольно быстро нашли какой-то эрофотоархив, и быстренько распечатали фотографии. Пройдясь по всем классам, вы попрятали эти фотографии в разных неожиданных местах. Будем надеяться, что нежданные картинки порадуют учеников!'
    'Ещё раз оглядев плоды своих трудов, вы с чистой совестью направились к выходу.'
    python:
        inhibLowTime = ptime
        inhibLow = 1
        player.setEnergy(-100)
        changetime(60)
        move('loc_entrance')
        
label inhib2:
    show expression 'pic/events/inhibLow/porn.jpg' at top as tempPic
    'Покопавшись в интернете, вы довольно быстро нашли порно сайт, и распечатали с него наиболее развратные фотки. Пройдясь по всем классам, вы попрятали эти фотографии в разных неожиданных местах. Наверняка ученики захотят обсудить друг с другом свои находки!'
    'Ещё раз оглядев плоды своих трудов, вы с чистой совестью направились к выходу.'
    python:
        inhibLowTime = ptime
        inhibLow = 2
        player.setEnergy(-100)
        changetime(60)
        move('loc_entrance')
        
label inhib3:
    show expression 'pic/events/inhibLow/cam.jpg' at top as tempPic
    'Вы распечатываете сегодняшние фотографии на своём принтере, и раскладываете их по школе и по партам. Разумеется вы предварительно замазали лица, чтобы не было понятно, где именно сняты эти фотографии. Будем надеяться, что неожиданные картинки порадуют школьников!'
    'Ещё раз оглядев плоды своих трудов, вы с чистой совестью направились к выходу.'
    python:
        inhibLowTime = ptime
        inhibLow = 3
        player.setEnergy(-100)
        changetime(60)
        move('loc_entrance')
        
label inhib4:
    $ rands = renpy.random.randint(1, 8)
    show expression ('pic/events/inhibLow/mast%d.jpg' % rands) at top as tempPic
    'Чувствуя своё возбуждение, вы решили немного помастурбировать. Но не как обычно, дома или в офисе, а прямо в классах! Зная, что в школе в это время никого уже не бывает, сняв свои трусики и оставив их в кабинете, вы стали ходить из класса в класс, то трясь своей киской об угол стола, то просто присаживаясь на чей нибудь стул, оставляя на нём след и запах своей влажной дырочки. '
    'Закончили вы свой маленький вояж в спортзале, где никого не стесняясь, испытали сильнейший оргазм, исторгнув из своей киски струю пахучих выделений!'
    'Ещё раз оглядев плоды своих трудов, вы с чистой совестью направились к выходу.'
    python:
        inhibLowTime = ptime
        inhibLow = 4
        player.setEnergy(-300)
        changetime(120)
        move('loc_entrance')
        
label madness_home:
    $ clrscr()
    show expression 'pic/events/madness/1.png' at top as tempPic
    'Не в силах больше сдерживать сексуальное напряжение, вы опускаете свою руку вниз и начинаете яростно теребить свою киску. Волны удовольствия начинают прокатываться по напряженному телу.'
    'Вы пытаетесь совладать с вашими пальцами, но они уже начали жить своей собственной жизнью, посылая всё дальше к вершинам удовольствия.'
    show expression 'pic/events/madness/2.png' at top as tempPic
    'Вы стесняетесь своего текущего во всех смыслах слова состояния, но ничего не можете с собой поделать - ваше тело просто не слушается вас.'
    'Пальчики сами по себе порхают вокруг истекающей киски, вы и не подозревали, что способны так управляться со своим естеством. Как будто развратная суккубка направляет ваши движения. Попку вверх, пальчиками к анусу, попку вниз, пальчиками к бугорку удовольствия.'
    'Вы понимаете, что приближаетесь к мощному оргазму, ваши коленки начинают дрожать, киска сокращается, как будто по ней пустили электрический ток. Ваше тело изгибается в предоргазменном состоянии. Вы начинаете терять сознание от удовольствия.'
    show expression 'pic/events/madness/3.png' at top as tempPic
    'Вы уплываете в горизонт на парусах оргазма. Ваш разум уже не с вами. Киска и попка безумно сокращаются, из них льются соки похоти. С трудом очнувшись, вы поднимаететесь, и нехотя, на подрагивающих ногах, идёте в ванную.'
    'Несмотря на такую концовку, по вашему лицу блуждает развратная улыбка, и вы с нетерпением ждёте повторения опыта'
    $ player.setLust(-100)
    $ player.setCorr(0.5)
    $ player.setEnergy(-100)
    $ move('loc_home')
    
label madness_school:
    $clrscr()
    show expression 'pic/events/madness/school.jpg' at top as tempPic
    'Вы внезапно понимаете, что ещё чуть чуть, и за вами будет оставаться мокрый след от вашей киски. Не разбирая направления, заскакиваете в женский туалет и стремительно избавляетесь от одежды, разбросав её по полу.'
    'Вы почувствовали иррациональное желание засунуть себе что нибудь во все доступные для удовлетворения дырочки. И не нашли ничего лучше, чем заполнить их пальцами.'
    'Насаживаясь одновременно на обе свои руки, вы принялись интенсивно двигать бёдрами. Так, что сначала пальцы одной руки полностью заполняли вашу киску, и обратным движением, пальцы другой заполняли анус.'
    'Ваши соки текли по бёдрам, отлично смазывая обе дырочки. Киска и анус сильно сжали ваши пальцы, и вы почувствали, что скоро так долго продолжаться не может.'
    show expression ('pic/events/madness/orgasm%d.png' rand(1,15)) at top as tempPic
    if lt() > 0:
        'Ваше тело сотрясалось в оргазме, вы пытались стиснуть зубы, и сдержать крик, но ничего не получается, и по коридорам школы разнёсся  громкий, полный страсти, стон. Пережив сладостные мгновения и опомнившись, вы стали собирать одежду с пола.'
        'Одевшись, вы обнаружили несколько пятен на одежде, да и, судя по всему, ваш крик тоже наверняка не останется незамеченным.'
        python:
            setRep(10,-2)
            player.setEnergy(-100)
            player.setLust(-100)
            player.setCorr(1)
            player.setDirty(1)
    else:
        'Ваше тело сотрясалось в оргазме, вы пытались стиснуть зубы, и сдержать крик, но ничего не получается, и по коридорам школы разнёсся  громкий, полный страсти, стон. Пережив сладостные мгновения и опомнившись, вы стали собирать одежду с пола.'
        'Одевшись, вы обнаружили несколько пятен на одежде, хорошо, что сейчас неучебное время, и никто ничего не заметит!'
        python:
            player.setEnergy(-100)
            player.setLust(-100)
            player.setCorr(0.5)
            player.setDirty(1)
    $ move('loc_wcf')
    
label beauty_intro:
    show expression im.FactorScale('pic/locations/shopBeauty/2.png',0.8) at right as tempPic
    show expression Image(player.picto, xalign=0.1, yalign= 1.0, yanchor = 'center')
    'Не успеваете вы войти в салон, как к вам подлетает медсестра и начинает зачитывать список предоставляемых в салоне услуг с такой скоростью, словно она участвует в соревнованиях по скороговоркам.'
    med 'Добрый день, уважаемая [player.name]! - начинает тараторить она.'
    player.say 'Здрас...'
    med 'Наш салон, единственный во всём городе предлагает следующие услуги, химическую завивку волос, депиляцию волос, очистку кожи по самым современным технологиям, а так же маникюр и педикюр!'
    player.say 'Я тольк...'
    med 'Химическая завивка волос увеличит вашу красоту и привлекательность, в принципе как и все услуги предоставляемые в нашем заведении! Эта супер стойкая завивка продержится целую неделю без каких либо действий с вашей стороны! Даже душ, ванна и цунами не смогут повредить ей!'
    player.say 'Хотела...'
    med 'Депиляция кожи удалит с вашей кожи все те волоски, о которых вы не подозревали, а так же даже те, о которых вы даже не задумывались! Разумеется лишь до тех пор, пока они не отрастут снова. Это произойдёт примерно через две недели.'
    player.say 'Я...'
    med 'Чистка кожи очистит кожу вашего лица, чтобы она была глаже попки младенца, и упруже попки старшеклассницы! К сожалению, через месяц процедуру стоит повторить!'
    player.say 'Спросить мож...'
    med 'Маникюр и педикюр делают безусловно лучшие мастера нашего города! Разнорабочий Ашот, и фрезеровщик 6-го разряда Валентин! Шутка конечно! Ха-ха-ха!'
    player.say 'Тьфу! - плюёте вы с досады то того, что на ваши потуги вставить хоть словечко, совсем не обращают внимания.'
    med 'Кстати недавно у нас открылась новое направление - пластическая хирургия! Просто в наш город приехал дровосек из Нового Орлеана... Да не смотрите вы так! Это просто прозвище такое, потому что из любого бревна конфетку сделает! Правда и за услуги берёт недёшево...'
    'Медсестричка заразительно хихикает, заканчивает она свой бесконечный монолог, и убегает встречать следующую посетительницу.'
    $ move(curloc)
    
label beauty_depilation:
    $clrscr()
    med 'Отличный выбор! Вам давно следовало позаботиться о своей коже! - радостно говорит медсестричка, и провожает Вас в кабинет для депиляции.'
    'Спустя пол часа, депиляция закончена, кожа немного зудит, но в целом всё стало гораздо лучше, чем было!'
    python:
        player.money -= 1000
        changetime(30)
        depilation = 14
        move(curloc)
        
label beauty_him_zavivka:
    $clrscr()
    med 'Отличный выбор! Вам давно следовало позаботиться о своих волосах! - радостно говорит медсестричка, и провожает Вас в кабинет по завивке волос.'
    'Спустя пол часа, ваши волосы завиты и находятся в прекрасной форме!'
    python:
        player.money -= 500
        changetime(30)
        him_zavivka = 7
        move(curloc)
        
label beauty_skin_care:
    $clrscr()
    med 'Отличный выбор! Вам давно следовало позаботиться о своём лице! - радостно говорит медсестричка, и провожает Вас в кабинет для чистки кожи.'
    'Спустя полчаса чистка закончена, кожа немного зудит, но в целом всё стало гораздо лучше, чем было!'
    python:
        player.money -= 5000
        changetime(30)
        skin_care = 30
        move(curloc)
        
label beauty_manicure:
    $clrscr()
    med 'Отличный выбор! Вам давно следовало позаботиться о своих ногтях! - радостно говорит медсестричка, и провожает Вас в кабинет для маникюра.'
    'Спустя полчаса маникюр высыхает, Ваши ногти красивы, как никогда!'
    python:
        player.money -= 100
        changetime(30)
        manicure = 3
        move(curloc)
        
label beauty_pedicure:
    $clrscr()
    med 'Отличный выбор! Вам давно следовало позаботиться о своих ногтях! - радостно говорит медсестричка, и провожает Вас в кабинет для педикюра.'
    'Спустя полчаса педикюр высыхает, Ваши ногти красивы, как никогда!'
    python:
        player.money -= 200
        changetime(30)
        pedicure = 6
        move(curloc)
        
label beauty_operation:
    $clrscr()
    med 'Великолепно! Прекрасно! Я Вас уже предупредила, что операция и краткий курс восстановления займёт примерно сутки? Вы согласны?'
    menu:
        player.say 'Э-м-м-м...'
        'Да!':
            python:
                player.money -= 50000
                player.setBeauty(30)
                if player.stats.beauty > 100:
                    player.stats.beauty = 100
                changetime(24*60)
                player.setHealth(-100)
            'На следующий день, Вас уже выписали. Посмотревшись в зеркало, Вы цокнули языком от удивления, вроде бы стало немного лучше, чем было. правда после наркоза всё побаливает, и сердечко заходится в неровном ритме.'
        'Нет, не сейчас':
            player.say 'Нет, я пока не готова.'
            med 'Ну как хотите, если что, обращайтесь!'
    $ move(curloc) 