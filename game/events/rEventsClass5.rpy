label event_loc_class5_0_no1:
    show class5
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class5/no1.jpg' at top as tempPic
    'Зайдя в кабинет, вы видите, что [st1.fname] решила сесть на диету или просто тренирует свою силу воли. Хотя её лицо говорит о том, что от силы воли остались лишь мелкие крохи.'
    if player.getEnergy() < 500:
        'Не желая больше мучить ученицу, вы накинулись на сладости и, к вашему удивлению, всё умяли. Ученица смотрит на вас с благодарностью.'
        $ player.incEnergy(200)
    $ move(curloc)

label event_loc_class5_0_no2:
    show class5
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        st3 = getChar('female')
        setFun(10,5)
    show expression 'pic/locations/school/class5/no2.jpg' at top as tempPic
    'Кто-то бегает, вот [st1.fname] спит,  [st2.fname] и [st3.fname] общаются о чём-то в сторонке. Обычный день в школе.'
    $ move(curloc)
    
label event_loc_class5_0_no3:
    show class5
    python:
        st1 = getChar('female')
        setFun(10,10)
    show expression 'pic/locations/school/class5/no3.jpg' at top as tempPic
    'Это вы удачно зашли! Похоже, что [st1.fname] справляет свой день рождения! Вы говорите ей свои дежурные поздравления и оставляете учеников праздновать дальше.'
    $ move(curloc)
    
label event_loc_class5_5_no4:
    show class5
    python:
        st1 = getChar('futa')
        st2 = getChar('female')
    show expression 'pic/locations/school/class5/no4.jpg' at top as tempPic
    'Войдя в класс, вы заметили, что [st1.fname] одёргивает юбку так, словно секунду назад она была поднята.'
    st1.say 'Это не то, о чём вы подумали, - со страхом говорит [st1.fname].'
    player.say 'А о чём я подумала?'
    st1.say 'Ну как будто я всем показывала свой, своего... - ученица замолкает.'
    player.say 'Они тебе не верили, да? Не переживай, я знаю, что такие иногда рождаются, - быстро всё поняв, утешаете вы ученицу.'
    if player.getCorr() > 50:
        player.say 'А вы не смейтесь! - окрикиваете вы расшалившихся учеников.'
        show expression 'pic/locations/school/class5/no4a.jpg' at top as tempPic
        player.say 'Настанет время, и, может быть, даже ты, [st2.fname], будешь с трепетом касаться её члена, направляя его в свою узенькую дырочку!'
        player.say '"Да... Огромный член в её маленькой дырочке..."'
        'Вы оставляете немного шокированных вашими словами учеников.'
    $ move(curloc)
    
label event_loc_class5_0_no5:
    show class5
    python:
        st1 = getChar('futa','lustmax')
        st2 = getChar('female')
    show expression 'pic/locations/school/class5/no5.jpg' at top as tempPic
    '[st1.name] вцепилась в волосы своей одноклассницы и куда-то ведёт её.'
    menu:
        'Сделать замечание':
            'Вы сделали замечание ученице, и [st1.fname] отпустила волосы. [st2.fname] смотрит на вас с благодарностью.'
            $ st1.incLoy(-10)
            $ st2.incLoy(15)
        'Не обращать внимания':
            $ st1.incLoy(10)
            $ st2.incLoy(5)
            'Вы решили не обращать внимания на эту странную парочку. Остаётся надеятся, что ничего страшного не случится.'
        'Проследить за ними' if getPar(studs,'corr') > 25 or development == 1:
            $ hadSex(st1,st2)
            show expression 'pic/locations/school/class5/no5a.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            'Девушки уединяются в свободном кабинете, и вы замечаете, что [st1.name] не совсем девушка. Усевшись на парту, она приспускает трусики и из под юбки выпрыгивает крепкий член.'
            st1.say 'Подрочи мне, как всегда, - требовательно произносит молодая фута.'
            '[st2.fname] кладёт свои ручки на подрагивающий пенис и начинает медленно ласкать уздечку.'
            show expression 'pic/locations/school/class5/no5b.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            st1.say 'Да... Вот так хорошо! Продолжай!'
            'С кончика члена девушки начинает стекать небольшая струйка преэякулята, смазывая шаловливые пальчики подружки. Она берёт член покрепче и продолжает ласкать уздечку своей влажной ладошкой.'
            show expression 'pic/locations/school/class5/no5c.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            'Наконец, [st1.fname] издаёт громкий стон, и в потолок бьёт маленький фонтанчик спермы.'
            st2.say 'Мне уже можно идти?'
            '[st2.fname] с беспокойством разглядывает перемазанные в семени руки.'
            st1.say 'Ага! Завтра я тебя снова найду!'
            player.say '"Однако интересные отношения завязываются в моей школе..."'
            $ player.incLust(10)
    $ move(curloc)
    
label event_loc_class5_0_no6:
    show class5
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        st1.incFun(10)
        st2.incFun(15)
    show expression 'pic/locations/school/class5/no6.png' at top as tempPic
    st1.say 'Ну короче, выхожу я вчера на мид, а кэрри в лесу. Ну я ему кричу, мол какого хера, кто мид пушить будет, я саппорт!'
    '[st1.fname] рассказывает подружке, как он вчера до 2 часов ночи рубал с друзьями в Шмоту. Вы бы не сказали, что [st2.name] в восторге от этих разговоров, но что-то в этом мальчике ей определённо нравится.'
    if player.getCorr() > 60:
        show expression 'pic/locations/school/class5/no6a.jpg' at top as tempPic
        player.say '"А может быть ей нравится его упругий член, который каждый день, по ночам, терзает её хрупкий анус?"'
        'Вы отчётливо представили, как [st1.fname], закончив свои ночные бои в Шмоте, заходит в спальню к подружке и, перевернув её попкой к верху, медленно вводит член в неподатливое колечко сфинктера. У вас аж всё сжалось от реалистичности картинки предоставленной воображением.'
        $ player.incLust(10)
    $ move(curloc)
    

label event_loc_class5_10_no7:
    show class5
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/school/class5/no7.jpg' at top as tempPic
    player.say '"Ого, сколько учебников приходится таскать в школу нашим ученикам!"'
    'Хотя не видно, чтобы [st1.fname] сильно напрягалась от переноски такой стопки. Вот он, скрытый спортивный потенциал! В любом случае неплохо было бы помочь донести их.'
    menu:
        'Помочь':
            'Вы помогли донести учебники до парты. [st1.fname] благодарит вас.'
            $ st1.incLoy(10)
        'Подрядить ученика на это дело':
            $ hadSex(st1,st2)
            player.say 'Эй, [st2.fname]! Подойди пожалуйста, помоги девочке с тяжёлыми книжками!'
            'Парень, постоянно подтягивая спадающие треники, кивает вам и бросается на помощь однокласснице. Вы с удовлетворённым видом отворачиваетесь, как внезапно слышите глухой удар и крик девушки за спиной.'
            show expression 'pic/locations/school/class5/no7a.jpg' at top as tempPic
            'Нет, вы, конечно, читали в объяснительных, мол шёл, упал на девушку, случайно изнасиловал, но вживую подобную ситуацию видите впервые. Стремительно бегущий парень в конце концов запутался в своих трениках, и врезался в школьницу. Со спущенными штанами. Со стоящим членом. Врезался так, что вдавил членом трусики глубоко ей во влагалище.'
            show expression 'pic/locations/school/class5/no7b.jpg' at top as tempPic
            st1.say 'В-в-выйди из меня, пожалуйста! - шепчет девушка, стоя на подрагивающих ногах и поддерживаемая в вертикальном положении глубоко сидящим в ней членом.'
            st2.say 'Я ненаро... О боже, подожди, НЕ ДВИГАЙСЯ!!!'
            'Девушка активно заёрзала, пытаясь выбраться из щекотливой ситуации. Парень же, в свою очередь, вовсю пытался минимизировать эти движения. В итоге все эти действия со стороны смотрелись как банальные фрикции.'
            st2.say 'Ч-ч-чёрт! Прости!'
            show expression 'pic/locations/school/class5/no7c.jpg' at top as tempPic
            'Когда парень, наконец-то, достал свой член из влажных трусиков, за ним протянулась густая белая капля спермы. [st1.fname] слегка застонала, видимо не совсем понимая, что сейчас произошло.'
            player.say 'Эмм, давайте я лучше закрою глаза на то, что сейчас произошло. Боюсь, что даже если я расскажу, мне всё равно никто не поверит.'
            'Школьники согласно закивали головами. Хотя [st1.name] ещё не в себе. Будем надеятся, что она тоже никому не расскажет.'
            $ player.incLust(5)
    $ move(curloc)

label event_loc_class5_0_no8:
    show class5
    python:
        st1 = getChar('female')
        st1.incFun(-10)
    show expression 'pic/locations/school/class5/no8.png':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Похоже, что [st1.fname] потеряла свою школьную обувь и ищет её. Выражение её лица говорит вам о том, что ищет [st1.fname] уже давно.'
    if player.getCorr() > 60:
        show expression 'pic/locations/school/class5/no8a.jpg' at top as tempPic
        player.say '"Такая задница! Да, эта попа прекрасно бы смотрелась залитой спермой из парочки членов!"'
    $ move(curloc)
    
label event_loc_class5_0_no9:
    show class5
    python:
        setFun(5,20)
    show expression 'pic/locations/school/class5/no9.jpg' at top as tempPic
    'Школьная рок группа репетирует песню "Стрела в колене" из своего нового альбома "Молодые сливки 5". Казалось бы, причём тут драконы? Вы не стали мешать репетиции и ушли.'
    $ move(curloc)
    
label event_loc_class5Learn_0_1:
    if getPar(studs, 'fun') < 30:
        $ skipEvent()
    show expression 'pic/locations/school/class1/learn2.jpg' at top as tempPic
    player.say '"Боже! Какой бардак! Они тут что, все с ума посходили?"'
    'Студентам слишком весело, чтобы тратить свою жизнь на такое скучное дело как занятия. Они решили поднять бунт и в данный момент крушат всё, что попадается под руку.'
    menu:
        'Помочь преподавателю успокоить их':
            $ dikovna.incLoy(10)
            $ setFun(10,-5)
        'Не вмешиваться':
            'Видя вашу пассивность, ученики бунтуют всё сильнее, пока, наконец, учитель не находит в себе силы гаркнуть что есть мочи и успокоить их. Но урок всё равно провален.'
            $ dikovna.incLoy(-5)
            $ setFun(10,5)
            $ setCorr(10,1)
            $ setEdu(10,-5)
    $ move(curloc)
    
label event_loc_class5Learn_0_2:
    show class3
    python:
        st1 = getChar('female','classroom')
    show expression 'pic/locations/school/class5/learn1.jpg' at top as tempPic
    '[st1.fname] сидит и слушает плеер на уроке. В то время, пока [dikovna.name] внедряет учебный материал в юные головы учеников, кто-то не вовлечён в процесс. Вас это немного возмущает.'
    menu:
        'Сделать замечание':
            'Вы бесцеремонно вытаскиваете наушники из ушей ученицы и молча указываете на преподавателя. Всем своим видом показывая, чем нужно заниматься на уроке.'
            $ st1.incLoy(-5)
            $ st1.incEdu(5)
        'Ничего не делать':
            player.say '"В конце концов, не я их учитель, и не мне решать, чем ученики должны заниматься на уроках."'
            $ st1.incLoy(5)
            $ st1.incEdu(-5)
    $ move(curloc)
    
label event_loc_class5Learn_0_3:
    show class3
    python:
        if 'usual' not in school.uniform:
            skipEvent()
        st1 = getChar('female','classroom')
        st1.incEdu(3)
    show expression 'pic/locations/school/class5/learn3.jpg' at top as tempPic
    'В классе довольно жарко. [st1.fname] сидит и потеет над уроком не только в метафизическом, но и вполне реальном смысле.'
    if rand(1,3) == 1:
        show expression 'pic/locations/school/class5/learn3_1.jpg' at top as tempPic
        $ st1.incLust(50)
        'Неожиданно девушка приоткрывает свой сарафанчик, чтобы впустить хоть немного ветерка поближе к телу, и вы замечаете эротичный оттопыренный сосок.'
        player.say '"Однако, я считала, что соски у женщин встают только по двум причинам. И очевидно, что на этот раз причина "холод" тут не подходит."'
    $ move(curloc)
    
label event_loc_class5Learn_0_4:
    show class3
    if dikovna.getLust() < 60:
        $ skipEvent()
    $ setLust(10,10)
    show expression 'pic/locations/school/class5/learn4.jpg' at top as tempPic
    dikovna.say 'Записывайте дети и не отставайте!'
    dikovna.say 'A cock - петушок.'
    dikovna.say 'A pussy - киска.'
    dikovna.say 'Wet, wetter, wettest - влажный, влажнее, влажнейший.'
    dikovna.say 'Hot, hotter, hottest - горячий, горячее, горячейший.'
    player.say '"Вот вроде бы всё в порядке, но этот подбор слов и отчётливая выпуклость на юбке как бы намекают, что урок проходит не вполне обычно."'
    $ move(curloc)
    
label event_loc_class5Learn_10_5:
    show class3
    python:
        st1 = getChar('male','classroom')
    show expression 'pic/locations/school/class5/learn5.jpg' at top as tempPic
    'В классе очень жарко, многие ученицы расстёгивают свою форму, чтобы немного проветрится. Вы, в принципе, солидарны с ними и тоже слегка расстёгиваетесь, чем привлекаете взгляды. Особенно выделяется [st1.name], который пытается одновременно и смотреть, и нет.'
    if player.getCorr() > 40 and player.getBeauty() > 90:
        show expression 'pic/locations/school/class5/learn5_1.jpg' at top as tempPic
        'Вы решаете немного поиграть с ним. Вы достаёте свою ручку и начинаете медленно облизывать её так, словно это не совсем ручка. Точнее совсем не ручка. В общем, все понимают, что вы там облизываете, поглядывая на школьника, включая его самого.'
        'Спустя пару мгновений вашей невинной игры, член парня начинает отчётливо выпирать, оттопыривая его штаны.'
        show expression 'pic/locations/school/class5/learn5_2.jpg' at top as tempPic
        'Вы включаете на полную всю свою харизму и начинаете вытворять с ручкой такое, что игнорировать это смог бы только разложившийся до стадии скелета труп. Ваш язычок порхает по колпачку, с уголка рта стекает блестящая капелька слюны, вы даже немного постанываете. Наконец, парень не выдерживает этой игры, и вы отчётливо видите, как на его штанах растекается влажное пятно.'
        player.say '"Хе-хе-хе. Всё таки могу ещё!"'
    else:
        'Вы слегка подмигиваете ему и продолжаете заниматься своими делами.'
    $ move(curloc)

