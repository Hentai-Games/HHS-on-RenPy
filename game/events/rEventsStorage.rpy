label event_loc_storage_0_no1:
    show storage
    python:
        st1 = getChar('futa')
        st1.incLoy(5)
        st1.incFun(5)
    show expression 'pic/locations/school/storage/no1.jpg' at top as tempPic
    '[st1.fname] похоже потеряла брошку и не может её найти. Вы с радостью согласились ей помочь, попутно оценив оригинальность спортивного костюма.'
    if player.getCorr() > 30:
        'А так же то, что в штанишках у неё похоже немного больше, чем она рассказывает. Надо будет как нибудь проверить, что она там прячет.'
        $ player.incLust(10)
        $ player.incCorr(1)
    $ move(curloc)

label event_loc_storage_0_no2:
    show storage
    python:
        st1 = getChar('female')
        st1.incLoy(-5)
        st1.incFun(-5)
    show expression 'pic/locations/school/storage/no2.jpg' at top as tempPic
    'Вы заходите в кладовку, видите что [st1.fname] кого то ждёт, и искренне надеясь что не вас, выходите.'
    $ move(prevloc)

label event_loc_storage_0_no3:
    show storage
    python:
        st1 = getChar('female','lustmax')
        st1.incLoy(-5)
        st1.incFun(-5)
    show expression 'pic/locations/school/storage/no3.jpg' at top as tempPic
    '[st1.fname] похоже кого то ждёт в кладовке. Вы немного поболтали с ней, но судя по её удивлённому виду, ждала она не вас.'
    if player.getCorr() > 30:
        'А судя по позе возможно хотела предаться в дали от глаз более приятным занятием, чем пустое ожидание. Не стоило с ней разговаривать. Стоило подсмотреть сначала. Но кто же знал?'
        $ player.incLust(-10)
        $ player.incCorr(-1)
    $ move(curloc)

label event_loc_storage_0_no4:
    show storage
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/storage/no4.jpg' at top as tempPic
    '[st1.fname] подвернула ногу, пытаясь дотянуться до верхней полки со спорт инвентарём. Хорошо, что Вы вовремя зашли!'
    menu:
        'Помочь' if player.money >= 50:
            'Вы отправили девочку на такси домой. Сама она ходить по сути не может. Это Вам встало всего в 50 монет. Слухи о вашей доброте разнеслись по школе.'
            $ player.money -= 50
            $ st1.incLoy(5)

        'Не обращать внимания':    
            'Вы решили не обращать внимания ранение ученицы. В конце концов Вы директор, а не нянька.'
            $ st1.incLoy(5)

    $ move(curloc)

label event_loc_storage_0_no5:
    show storage
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLoy(5)
        st1.incFun(5)
        st2.incLoy(5)
        st2.incFun(5)
    show expression 'pic/locations/school/storage/no5.jpg' at top as tempPic
    '[st1.fname]  судя по всему притомилась, и уснула на коленях у своей подруги. Какая же милота! Вы решили не тревожить их. Время всё равно не учебное.'

    $ move(curloc)

label event_loc_storage_30_low1:
    show storage
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLoy(10)
        st1.incFun(10)
        st1.incCorr(1)
        st2.incLoy(10)
        st2.incFun(10)
        st2.incCorr(1)

        player.incLust(10)
        player.incCorr(1)
        player.incWill(2)
    show expression 'pic/locations/school/storage/lo1.jpg' at top as tempPic
    'Молодые, влажные киски, нежно трущиеся друг об друга. Их неспешное перемешивание соков, и эротичное хлюпание. Эта картинка буквально застыла у Вас в глазах и голове.'
    'И пока Вы её переваривали, [st1.fname] и [st2.fname] быстренько пробежали мимо Вас, скрывшись в недрах школы. Какое огорчение, что они постеснялись вас...'

    $ move(curloc)

label event_loc_storage_30_low2:
    show storage
    python:
        st1 = getChar('female')
        st2 = getChar('male')

    'Зайдя в кладовку, Вы услышали тихий разговор. Аккуратно спрятавшись за какой то тумбой, Вы выглянули, чтобы рассмотреть участников.'
    show expression 'pic/locations/school/storage/lo2.jpg' at top as tempPic
    st1.say '[st2.fname], я искренне надеюсь, что это в последний раз, когда ты не выучил урок'
    'Вы увидели, как [st1.fname], староста одного класса, уверенными движенями своей ножки массирует небольшой член школьника.'
    st2.say 'Прости пожалуйста, ммм, я постараюсь выступить лучше в следующий раз! - ученик немного смешно дёргается, под ступнёй старосты.'
    st1.say 'Ты понимаешь, что подвёл не только меня, но и весь класс, не выучив урок? - нажим ножки усилился, вдавливая член в живот, и из него начали сочиться капельки предоргазменной смазки.'
    'С одной стороны вроде кого то воспитывают. С другой стороны как то это неправильно...'
    
    menu:
        'Всё таки лучше учить хоть как, чем никак.' if player.getCorr > 40:
            hide tempPic
            show expression 'pic/locations/school/storage/lo2a.jpg' at top as tempPic
            st2.say '[st1.fname], я сейчас кончу! - сильнее заворочался парень, пытаясь выскользнуть из под ноги ученицы.'
            st1.say 'Как тебе тогда это? - староста вдруг раздвинула свой балахончик, показывая молодое тело школьнику, - Мне тоже уже надоело с тобой возится, и это уже в третий раз! Кончай давай.'
            'С этими словами из уст мальчишки раздался стон, и белая жидкость начала разбрызгиваться по животу, заливая пальчики девочки. Вы постарались незаметно уйти, пока никто Вас не заметил.'
            $ hadSex(st1,st2)
            $ player.incLust(10)
            $ player.incCorr(1)
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)

label event_loc_storage_30_low3:
    show storage
    python:
        st1 = getChar('female')

    show expression 'pic/locations/school/storage/lo3.jpg' at top as tempPic
    'Зайдя в кладовку, Вы увидели ученицу, ласкающую себя маленьким вибратором прямо на матах.'
    player.say '[st1.fname]? - удивлённо спросили Вы её.'
    st1.say '[player.name]! Я! Ммммм! - девушка не выдержала вибрации между ног, и Вы отчётливо увидели, как её влагалище начало сокращаться в оргазме.'

    menu:
        'Всё в порядке.' if player.getCorr > 40:
            hide tempPic
            show expression 'pic/locations/school/storage/lo3a.jpg' at top as tempPic
            player.say 'Всё в порядке, - улыбнулись Вы девушке, - Каждый этим занимается..'
            st1.say 'Я, я, я снова-а-а-а! - затряслась девушка, и раздвинула пальчиками свою маленькую вагину, из которой начали плескать её соки.'
            player.say '"Ну вот, теперь маты менять" - подумали вы, оставляя оргазмирующую ученицу за собой.'
            $ st1.incLoy(10)
            $ st1.incFun(10)
            $ st1.incCorr(1)

            $ player.incLust(10)
            $ player.incCorr(1)
            $ player.incWill(2)

        'Наказать':
            $ st1.incLoy(-5)
            $ st1.incFun(-5)
            $ st2.incLoy(-5)
            $ st2.incFun(-5)
            $ scoldWho = [st1]    

    $ move(prevloc)

label event_loc_storage_30_low4:
    show storage
    python:
        st1 = getChar('female')
        st1.incLoy(10)
        st1.incFun(10)
        st1.incCorr(1)
    show expression 'pic/locations/school/storage/lo4.jpg' at top as tempPic
    player.say '[st1.fname]? - строго спрашиваете Вы судорожно натягивающую трусики девушку.'
    st1.say 'Я, я... Пёрышко из мата просто в трусики попало... - ученица быстро собралась и убежала, оставляя Вас в раздумьях: "Откуда в войлочных патах перья?"'

    $ move(curloc)

label event_loc_storage_50_mid1:
    show storage
    python:
        st1 = getChar('female')
        st2 = getChar('male')

        player.incLust(15)
        player.incCorr(2)
        player.incWill(3)

    show movie
    play movie "pic/locations/school/storage/mid1.gif.webm" loop
    '[st2.fname] сильными толчками вгнял свой член в одноклассницу, стонавшую под его неистовым напором. Явно, что ученики сильно спешили отдаться друг другу, так как даже не успели снять одежду. [st1.fname] громко стонала, ощущая как стенки её влагалища таранит молодой член парня. Парочка настолько завелась, что совершенно не обращает на Вас внимания!'
    'Твёрдый ствол плавно двигался в вашей киске, проникая своей, разбухшей от возбуждения головокой, всё глубже. Вы потеряли связь с реальностью, для вас существовал только этот, прекрасный член, таранящий ваше возбуждённое тело.'
    stop movie
    hide movie   

    menu:
        'Наказать':
            $ st1.incLoy(-10)
            $ st1.incFun(-10)
            $ st2.incLoy(-10)
            $ st2.incFun(-10)
            $ scoldWho = [st1, st2] 
        'Уйти':
            'Насладившись неистовством молодости, вы с небольшим сожалением выходите из кладовки.'
            $ st1.incLoy(10)
            $ st1.incFun(10)
            $ st1.incCorr(1)
            $ st2.incLoy(10)
            $ st2.incFun(10)
            $ st2.incCorr(1)            
            $ hadSex(st1, st2)

    $ move(curloc)

label event_loc_storage_50_mid2:
    show storage
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = mustangovich
        
        st1.incLoy(10)
        st1.incFun(10)
        st1.incCorr(1)
        st2.incLoy(10)
        st2.incFun(10)
        st2.incCorr(1) 

        hadSex(st1,mustangovich)
        hadSex(st2,mustangovich) # не знаю можно ли так сделать

        player.incLust(15)
        player.incCorr(2)
        player.incWill(3) 
        
    show expression 'pic/locations/school/storage/mid2.png' at top as tempPic  
    '[st3.fname] [st3.lname] проводит особые тренировки в кладовке. Очень особые. Непосредственно в данный момент его член активно погружается в хлюпающую вагину одной из учениц. [st1.fname], так кажется её зовут.'
    'Вы даже слегка удивились, как она может принять такой пенис в свою отнюдь не титаническую щёлку. Но как то принимала. И даже получила от этого неслабое удовольствие. Отдельной темой была [st2.fname].'
    'Вы не знаете, когда и как она присоединилась к очередной тренировке, но свою роль она играет хорошо. Вон как её пальчики выкручивают соски одноклассницы, просто загляденье! Да и про себя девочка не забывает, резко елозя своей промежностью по лицу физрука.'
    'Внезапно [st1.fname] застонала, и было от чего! Похоже что семяизвержение мужчины наконец то спровоцировало её собственный оргазм, и девочку, откинувшуюся на свою подругу, начали сотрясать спазмы удовольствия. Настолько сильные, что член выскочил из её киски, заливая всё вокруг своей спермой, а сама ученица, не удержавшись, исторгла мощную струю из своей уретры.'
    'Наказать бы их всех примерно, но вроде как не на людях, да и не будут никому рассказывать. Наверное...'

    $ move(curloc)