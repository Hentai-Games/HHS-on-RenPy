label event_loc_class3_0_no1:
    show class3
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/school/class3/no1.jpg' at top as tempPic
    'Сегодня выдался жаркий денёк. [st1.fname] обмахивает тетрадкой свою подругу.'
    if player.getCorr() > 60:
        player.say '"Да, жарковато сегодня... В такой то жаркий денёк неплохо было бы раздеться и утолить жажду похоти своей подруги..."'
        show expression 'pic/locations/school/class3/no1a.jpg' at top as tempPic
        player.say '"Да-а-а, снять с неё и себя трусики, слиться в долгом поцелуе, потереться влажной киской о нежную кожу бедра..."'
        player.say '"Потом достать огромный дилдо и... Кхм... Что то я отвлеклась..."'
        show expression 'pic/locations/school/class3/no1.jpg' at top as tempPic
        'Несмотря на ваши мечтания, [st2.fname] продолжает наслаждаться ветерком от тетрадки.'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_class3_0_no2:
    show class3
    python:
        st1 = frigidovna
    show expression 'pic/locations/school/class3/no2.jpg' at top as tempPic
    '[st1.name] подготавливает доску для следующего занятия. У неё сконцентрированное и задумчивое лицо.'
    if 'dildo' in school.furniture:
        show expression 'pic/locations/school/class3/no2a.jpg' at top as tempPic
        player.say '"Ага, как будто она представляет, словно докупила ко всем вибраторам и вагинам вибрационное седло, и активно испытывает его лично!"'
        'Вы ещё немного посмаковали в воображении картинку Фригидовны в чудо-седле, как она медленно насаживается на эти резиновые члены, и её внутренности сотрясаются в наслаждении...'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_class3_0_no3:
    show class3
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLoy(10)
        st2.incLoy(10)
    show expression 'pic/locations/school/class3/no3.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] развлекаются игрой на гитаре. Вы немного послушали их лирическую песни о солдате пропадающем в каком-то Афганистане, смахнули слезу, и вышли.'
    'Ученицам польстило, что вам понравилось их пение.'
    $ move(curloc)
    
label event_loc_class3_0_no4:
    show class3
    python:
        setRep(5,5)
    show expression 'pic/locations/school/class3/no4.jpg' at top as tempPic
    'Обычная перемена в обычной школе. Кто то ссориться, кто то разговаривает, кто то смотрит на вас заинтересованно, кто то не очень.'
    'Сделав ссорящейся парочке замечание, вы удаляетесь.'
    $ move(curloc)
    
label event_loc_class3_5_no5:
    show class3
    python:
        st1 = getChar('futa','lustmax')
        st1.setLust(70)
        st2 = getChar('male')
    show expression 'pic/locations/school/class3/no5.jpg' at top as tempPic
    'Вы появляетесь в середине разговора.'
    st1.say 'А ещё у меня член под юбкой!'
    'Вместо ответа, [st2.fname] шокированно смотрит на одноклассницу.'
    if st1.getCorr() > 20:
        st1.say 'Хочешь посмотреть?'
        show expression 'pic/locations/school/class3/no5a.png' at top as tempPic
        'Не дождавшись ответа одноклассника, [st1.fname] встаёт из за парты и всем становится отчётливо виден торчащий под юбкой член.'
        player.say '[st1.name]! А ну немедленно прекрати!'
        '[st2.name] смотрит на вас с благодарностью.'
        $ st2.incLoy(10)
    $ move(curloc)
    
label event_loc_class3_0_no6:
    show class3
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLust(30)
        st1.incCorr(5)
    show expression 'pic/locations/school/class3/no6.jpg' at top as tempPic
    '[st1.fname] внимательно читает какой-то любовный роман, машинально накручивая на палец локон спящей рядом подружки. Не желая нарушать идиллию, вы тихо выходите, пока вас не заметили.'
    $ move(curloc)
    
label event_loc_class3_5_no7:
    show class3
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class3/no7.jpg' at top as tempPic
    'Грустная картина. Похоже на то, что [st1.fname] порвала со своим парнем, и теперь жалеет об этом.'
    'Вы подходите, и жалеете бедную девочку, успокаивая её тем, что это наверняка не последняя любовь в ее жизни.'
    $ st1.incLoy(5)
    if player.getCorr() > 60:
        show expression 'pic/locations/school/class3/no7a.jpg' at top as tempPic
        'Увлёкшись утешением, вы рассказываете девушке про то, что она ещё найдёт парня, который после школы будет нежно тыкаться горячей писькой в её молодую киску. Про то, как они сладко сольются в жарких обьятьях и будут любить друг друга с утра до самого вечера.'
        player.say 'А может быть вы потом и поженитесь!'
        if st1.getCorr() < 20:
            'Вы наконец обращаете внимание на шокированное лицо девушки. Похоже, что вы слегка перегнули палку.'
            $ st1.incLoy(-15)
        else:
            'Девушка благодарно улыбается вам. Похоже, что от вашего рассказа, она не только успокоилась, но и слегка развратилась!'
            $ st1.incLoy(5)
            $ st1.incCorr(5)
    $ move(curloc)
    
label event_loc_class3_0_no8:
    show class3
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('male','lustmax')
    show expression 'pic/locations/school/class3/no8.jpg' at top as tempPic
    player.say '"Да что же такое! Как не зайду в этот кабинет, так кто либо плачет, либо грустит. Карма тут нехорошая."'
    player.say 'У тебя что то случилось, [st1.fname]? - аккуратно интересуетесь вы.'
    'Её подруга [st2.fname] рассказывает ей, что сегодня на уроке Секспросвета [st1.fname] не смогла найти пенис на анатомическом атласе человека. Вы несколькими словами утешаете ученицу.'
    if player.getCorr() > 70:
        'А потом вам в голову приходит замечательная мысль, показать всё более наглядно.'
        show expression getCharImage(player, 'dialog') as temp1
        player.say 'Эй, [st3.name]! Подойди ка сюда!'
        show expression getCharImage(st3, 'dialog') as temp2
        st3.say 'А?'
        player.say 'Садись рядом, нам нужно кое что показать девчёнкам!'
        'Ничего не подозревающий парень, садится к вам за парту, и вы умелым движением расстёгиваете его ширинку, и достаёте наружу член.'
        hide temp1
        hide temp2
        show expression 'pic/locations/school/class3/no8a.png' at top as tempPic
        player.say 'Вот!'
        'Вы радостно потряхиваете достоинством парня, с улыбкой наблюдая за реакцией учеников. На задворках сознания вы понимаете, что вот так сразу член встать не мог, и вы достали его уже довольно возбуждённым, даже с небольшой влагой на кончике. Но всё таки продолжаете потряхивать им.'
        st3.say '[player.name], простите, я больше не могу!'
        player.say 'Что?'
        show expression 'pic/locations/school/class3/no8b.png' at top as tempPic
        'В ответ на невинное "что", член задрожал сам по себе и вам в ладонь выплеснулась накопленная за день сперма.'
        player.say 'А, ну счас мы можем наблюдать типичную эякуляцию, да... - мгновенно сориентировались вы.'
        'Девушки шокированно взирают на устроенный вашей шаловливой ручкой беспорядок.'
        player.say '"Ну по крайней мере теперь они знают не только где этот мужской половой пенис находится..."'
        'Вы быстренько собираетесь и, пряча заляпанную спермой руку за спиной, покидаете перешёптывающихся учеников.'
        python:
            st3.setLust(0)
            st1.incLust(20)
            st2.incLust(20)
            st1.incCorr(5)
            st2.incCorr(5)
            st3.incCorr(5)
            player.coverSperm('руки')
            player.incLust(15)
    $ move(curloc)
        
label event_loc_class3_10_no9:
    show class3
    python:
        st1 = getChar('female','corrmax')
        st1.incCorr(5)
    show expression 'pic/locations/school/class3/no9.jpg' at top as tempPic
    '[st1.fname] вытирает тряпочкой случайно пролившийся крем для рук.'
    player.say '"Ок. Расставим все палки над Й:\n1. Это не крем для рук.\n2. И не тряпочка."'
    player.say '"Это развратная [st1.fname] вытирает лубрикант своими трусиками."'
    $ move(curloc)
        
label event_loc_class3_0_no10:
    show class3
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class3/no10.jpg' at top as tempPic
    '[st1.fname] грустно стоит около открытого окна, и занавески нежно обмахивают её. Весьма поэтичная картина. Чего только не увидишь!'
    if player.getCorr() > 40:
        show expression 'pic/locations/school/class3/no10a.jpg' at top as tempPic
        player.say '"Хотя с моей точки зрения, она лучше бы смотрелась у доски с чьим то членом в заднице. Тоже было бы весьма поэтично!"'
        player.say '"Ну как минимум достойно бессмертных произведений Луки Мудищева!"'
        $ player.incLust(5)
    $ move(curloc)


    
label event_loc_class3_30_lo1:
    show class3
    python:
        st1 = getChar('futa','corrmax')
    show expression 'pic/locations/school/class3/lo1.jpg' at top as tempPic
    player.say 'Святая Дева Мария! - воскликнули вы, когда на вас приземлились потоки спермы, исторгнутые членом ученицы.'
    '[st1.fname], всё ещё постанывая, стискивает свой член, виновато разглядывая капли спермы.'
    menu:
        'Заставить убрать':
            player.say 'И кто это теперь будет убирать? - сурово сдвинув брови, спросили вы.'
            st1.say 'Ддавайте я...'
            show expression 'pic/locations/school/class3/lo1a.png' at left as tempPic
            'Ученица с готовностью подошла, тут же начав слизывать капли с вашего забрызганного лица.'
            player.say 'Подожди, что ты делаешь? - попытались вы отодвинуть виноватую школьницу.'
            st1.say 'Ничего, всё в порядке, пальцами только размажете, - c этими словами она всосала ещё одну капельку.'
            if player.getCorr() > 50:
                show movie
                play movie "pic/locations/school/class3/lo1b.gif.webm" loop
                player.say '[st1.fname], [st1.fname]... Куда ты? - испуганно спросили вы ученицу, когда та вдруг подняла вашу юбочку, и залезла языком прямо в киску'
                st1.say 'По моему туда тоже попало, [player.name], - ученица всерьёз занялась клитором, заставив вас испустить стон удовольствия.'
                player.say 'Да, пожалуй ты права, там ещё глубже чуть чуть, - закрыв глаза от наслаждения вы полностью отдались ласкам ученицы.'
                stop movie
                hide movie
                show expression 'pic/locations/school/class3/lo1c.jpg' at top as tempPic
                player.say 'Да, да, ДА! - закричали вы в оргазме , плотнее прижимаясь к лицу маленькой футанари своей киской'
                'Её язычок активней заработал над трепещущимся бугорком, и вы вдруг ощутили как пульсирующая киска начала исторгать большой объём жидкости прямо на личико девочки.'
                player.say 'А ты хороша! - улыбнулись вы ученице, - только вот не до конца всё слизала, ну да ладно, иди.'
                st1.say 'Спасибо за всё, [player.name], - поклонилась девушка и вышла из класса. Интересно, что же на неё нашло?'
                $ st1.incLoy(10)
                $ st1.incCorr(10)
                $ player.setLust(0)
            else:
                player.say 'Всё, достаточно, дальше я сама, - вы выгнали расстроенную ученицу из класса.'
                $ st1.incLoy(-10)
                $ player.coverSperm('ноги','грудь')
        'Выгнать и заняться чисткой одежды':
            'Вы негодующе посмотрели на ученицу, жалея что не наказали её, и, выгнав из класса, стали рассматривать размеры катастрофы с одеждой. А они велики, потому что посмотревшись в зеркальце,  вы обнаружили пару капель даже на своём лице.'
            player.say '"Мда уж, полна [st1.fname] неожиданностей!"'
            $ player.coverSperm('лицо','ноги','грудь')
            $ st1.incLoy(5)
        'Наказать':
            $ player.coverSperm('лицо','ноги','грудь')
            $ scoldWho = [st1]
            jump scoldAll
    $ move(curloc)
    
label event_loc_class3_40_mid1:
    show class3
    python:
        st1 = getChar('male')
        st2 = getChar('male')
        st3 = getChar('female')
        player.incLust(5)
    st1.say 'Мне так неприятно!'
    show expression 'pic/locations/school/class3/mid1.jpg' at top as tempPic
    'И действительно, [st3.name] делала ему весьма непрофессиональную работу ножками, от чего приятного было мало.'
    st3.say 'Не ври мне! Всё должно быть хорошо!'
    '[st3.fname] с силой водила по оголённой головке ногами. Вас аж передёрнуло от этого зрелища.'
    menu:
        'Наказать их':
            $ scoldWho = [st1,st3]
            jump scoldAll
        'Пусть сами учатся':
            $ hadSex(st1,st3)
        'Вмешаться в процесс' if player.getCorr() > 70:
            $ player.incCorr(5)
            $ player.coverSperm('ноги')
            $ player.incLust(20)
            player.say 'Нет, ну кто так делает! Иди сюда! - [st2.fname] проходивший по коридору был затянут вами в класс.'
            show expression 'pic/locations/school/class3/mid1a.jpg' at top as tempPic
            player.say 'Смотри и учись! - вы умело обхватили пальчиками ног орган ученика и начали его аккуратно массировать, - Чего замерла? Повторяй!'
            '[st3.fname] неуверенно начала повторять ваши движения и [st1.fname] застонал от её движений, благодарно посмотрев на вас.'
            player.say 'Давай же, родной, давай!'
            'Вы поглядывали на ученика, активно массируя его головку ступнями, кинув взгляд на ученицу, вы замечаете, что она тоже ускорилась вслед за вами.'
            show expression 'pic/locations/school/class3/mid1b.jpg' at top as tempPic
            st1.say 'Д-а-а-а!'
            st2.say 'О-о-о!'
            'Хрип кончающих парней cлился воедино, и ваши с ученицей ножки оказались забрызганы их семенем.'
            player.say 'Чудненько же! [st3.fname], надеюсь в следующий раз ты будешь более аккуратна!'
            'Покрасневшая школьница кивнула вам в ответ'
    $ move(curloc)
    
label event_loc_class3_50_mid2:
    show class3
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        hadSex(st1,st2)
        player.incLust(10)
    show movie
    play movie "pic/locations/school/class3/mid2.gif.webm" loop
    '[st1.fname] и [st2.fname] яростно заканчивают спаривание прямо у Вас на глазах. Вы не можете назвать это действие ничем иным, потому что ученик двигается буквально как зверь внутри одноклассницы.'
    menu:
        'Наказать их':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Подождать, пока они закончат':
            play movie "pic/locations/school/class3/mid2b.gif.webm" loop
            'Наконец [st2.fname] кричит: "Сновааа!", и вы видите как её сокращающееся в оргазме влагалище выплёскивает из себя потоки спермы прямо на яйца ученика.'
    stop movie
    hide movie
    $ move(curloc)

label event_loc_class3_50_mid3:
    show class3
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        hadSex(st1,st2)
        player.incLust(10)
    show expression 'pic/locations/school/class3/mid3.jpg' at top as tempPic
    st2.say 'Да, да, да, да!'
    'Вы с любопытством наблюдаете как [st1.fname], положив одноклассницу на стол, с силой хлопает своим животом по её бёдрам.'
    st2.say 'Сильнее, даааа!'
    'C каждым движением парня [st2.fname] выделяет больше смазки, которая стекает по её бёдрам прямо на стол и и капает на пол.'
    st2.say 'Кончаю!'
    'Девушка затряслась, и выгнувшись дугой, вырвалась из рук одноклассника, конвульсируя в оргазме.'
    st2.say 'Извини, в следующий раз займёмся тобой!'
    '[st2.fname] чмокнула одноклассника в щёчку и стала поправлять одежду.'
    if player.getLust() > 80:
        player.say 'Позволь мне им занятся, коль ты уже устала!'
        hide tempPic
        'Вы отодвигаете девушку в сторонку, скидываете с себя одежду, и занимаете место "уставшей" ученицы.'
        show expression 'pic/locations/school/class3/mid3a.png' at top as tempPic
        'Не долго взвешивая все за и против того, стоит ли трахать своего директора. Даже не задумываясь об этом! Парень резко вставил измазанный соками одноклассницы член в ваше хлюпающее влагалище.'
        player.say 'О-о-ох!'
        'Вы резко выдохнули, наслаждаясь сильным проникновением. Вы так долго ждали, пока вас кто то заполнит, что нетерпеливо принялись елозить попой по столу, ритмично вгоняя в себя скользкий член.'
        st1.say 'Ка-а-айф! - протянул парень, - [player.name], только я так долго не протяну!'
        player.say 'Кончай! Давай! Я разрешаю! Я и так этого долго ждала!'
        show expression 'pic/locations/school/class3/mid3b.png' at top as tempPic
        'Парень ускорился ещё сильнее, и вскоре два голоса закричали в экстазе. Лишь [st2.fname] сидела одиноко в сторонке, с ревностью взирая на ваше неистовое соитие.'
        player.say 'Вообще то, когда я кричала "кончай", я не имела в виду "кончай прямо в меня!" - вы с неудовольствием рассматриваете капли спермы, капающие из вашей киски на пол.'
        player.say 'А, ладно, один раз живём!'
        hide tempPic
        'На этой житейской мудрости вы расстались с юной парой, слыша, как за вашей спиной разгорается скандал.'
        $ player.coverSperm('вагина')
        $ player.setLust(0)
        $ hadSex(st1,player)
        $ st1.incLoy(10)
        $ st2.incLoy(-10)
    $ move(curloc)

label event_loc_class3_55_mid5:
    show class3
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        st3 = getChar('male')
        hadSex(st1,st2,st3)
    show expression 'pic/locations/school/class3/mid5.jpg' at top as tempPic
    player.say '"Кого то только что страстно отжарили..."'
    'Вы разглядываете до сих пор вздрагивающую в оргазме девушку. Парень ушёл, а посторгазменные конвульсии отстались. Хотя кого жарили и так понятно, имя этой преносчицы чужой спермы - [st2.fname], а вот кто её заполнял - это вопрос.'
    'Вы насилу привели в себя девушку, и выяснили, что развлекалась она сразу с двумя парнями. Теперь вы знаете кого наказать и за что.'
    menu:
        'Наказать их':
            $ scoldWho = [st1,st2,st3]
            jump scoldAll
        'Дело молодое, женщин на всех не хватает..':
            $ setLoy(3,10)
    $ move(curloc)
    
label event_loc_class3Learn_0_1:
    if getPar(studs, 'fun') < 30:
        $ skipEvent()
    show expression 'pic/locations/school/class1/learn2.jpg' at top as tempPic
    player.say '"Боже! Какой бардак! Они тут что, все с ума посходили?"'
    'Студентам слишком весело, чтобы тратить свою жизнь на такое скучное дело как занятия. Они решили поднять бунт и в данный момент крушат всё, что попадается под руку.'
    menu:
        'Помочь преподавателю успокоить их':
            $ frigidovna.incLoy(10)
            $ setFun(10,-5)
        'Не вмешиваться':
            'Видя вашу пассивность, ученики бунтуют всё сильнее, пока наконец учитель не находит в себе силы гаркнуть что есть мочи и успокоить их. Но урок всё равно провален.'
            $ frigidovna.incLoy(-5)
            $ setFun(10,5)
            $ setCorr(10,1)
            $ setEdu(10,-5)
    $ move(curloc)
    
label event_loc_class3Learn_0_2:
    show class3
    python:
        st1 = getChar('female','classroom')
    show expression 'pic/locations/school/class3/learn1.jpg' at top as tempPic
    st1.say '[player.name], можно мне выйти, а то [frigidovna.name] не разрешает...'
    menu:
        'Разрешить':
            player.say 'Иди конечно, я поговорю с учительницей об этом!'
            $ frigidovna.incLoy(-5)
        'Запретить':
            $ frigidovna.incLoy(5)
            player.say 'Слово учителя - закон! По крайней мере в школе.'
            st1.say 'Но мне очень надо!'
            player.say 'Нет!'
            if rand(1,3) == 1:
                st1.say 'Ну правда!'
                player.say 'Я всё сказала! Сиди и занимайся!'
                show expression 'pic/locations/school/class3/learn1_1.jpg' at top as tempPic
                'Ученица всё равно подрывается, но не успевает сделать и пару шагов от парты, как падает на пол и весь класс наблюдает, как под ней растекается лужа. [st1.fname] поднимает глаза и смотрит на вас с ненавистью.'
                $ st1.incLoy(-30)
            else:
                st1.say 'Ну и ладно, не очень то и хотелось!'
                player.say 'Я про это и говорила!'
                '[frigidovna.name] смотрит на вас с одобрением.'
    $ move(curloc)
    
label event_loc_class3Learn_0_3:
    show class3
    python:
        st1 = getChar('female','classroom')
        st2 = getChar('male','classroom')
    show expression 'pic/locations/school/class3/learn3.jpg' at top as tempPic
    '[st2.name] показывает своё отношение к соседке спереди весьма традиционным способом. Дёргая её за косичку. Уж не мстит ли он ей?'
    if player.getCorr() > 40:
        show expression 'pic/locations/school/class3/learn3_1.jpg' at top as tempPic
        player.say '"Хотя за что ему мстить ей? Разве что за то, что она не успела додёргать его член до звонка?"'
        'Вы с удовольствием представили, как [st1.fname], стоя в корридоре на перемене, засовывает член своего парня прямо в рукав школьного пиждака, и начинает его массировать. Да, на её бы месте даже вы не стали бы доводить мужчину до оргазма, так как ходить весь день в мокром от спермы пиджаке приятного мало.'
    $ move(curloc)
    
label event_loc_class3Learn_60_4:
    show class3
    python:
        if 'dildo' not in school.furniture:
            skipEvent()
        st1 = getChar('female','classroom')
        st2 = getChar('female','classroom')
        st3 = getChar('female','classroom')
        setLust(10,40)
        st1.incCorr(2)
        st2.incCorr(2)
        st3.incCorr(2)
    show expression 'pic/locations/school/class3/learn4.jpg' at top as tempPic
    'В тот момент, когда вы заходите в класс, [frigidovna.name] заканчивает объяснять, как надо использовать вибраторы с ДУ.'
    'Вас радует, что она решила использовать учеников, как материал для демонстрации своих слов. Тем более, по довольным лицам учениц понятно, что они как бы и не против.'
    $ move(curloc)
    
label event_loc_class3Learn_15_5:
    show class3
    python:
        if frigidovna.getCorr() < 20 or 'naked' == school.uniform:
            skipEvent()
        st1 = getChar('female','classroom')
        st2 = getChar('female','classroom')
        st1.incEdu(5)
        st2.incEdu(5)
    show expression 'pic/locations/school/class3/learn5_1.jpg' at top as tempPic
    '[frigidovna.name] заметила как девушки передавали записку друг другу. Не потерпев такой вольности на своём уроке, она выхватывает её из руг обалдевшей школьницы.'
    frigidovna.say 'Так, что у нас тут? "Я сегодня без трусиков!" и дальше "И я тоже!". Интересно. Ну раз вам не стыдно приходить в школу без трусов, то должно быть и не стыдно весь урок простоять с голой задницей перед всем классом!'
    show expression 'pic/locations/school/class3/learn5.jpg' at top as tempPic
    'С этими словами она забирает юбки у побагровевших учениц и ставит школьниц прямо напротив доски, чтобы любой мог полюбоваться их блестящими попками. Через 10 минут вы не выдерживаете.'
    player.say '[frigidovna.name], ну пожалейте вы их. Они так и урок не выучат, и пару приставал вдобавок получат.'
    'Немного подумав, [frigidovna.fname] соглашается, и, отдав юбки, отпускает учениц обратно за парту. Что любопытно, слушать они стали гораздо внимательнее.'
    $ move(curloc)
    
label event_loc_class3Learn_55_6:
    show class3
    python:
        st1 = getChar('male','classroom')
        st2 = getChar('male','classroom')
        st1.setLust(0)
        setFun(5,15)
        setLust(10,20)
    show expression 'pic/locations/school/class3/learn6.jpg' at top as tempPic
    'Зайдя, вы увидели как [st1.fname] сидит на столе, и несколько объятый страстью учениц, жадно ласкают его член. На фоне на цыпочках скачет [frigidovna.name] и что то кричит.'
    frigidovna.say 'Резинка, дуры!!! Я сказала, что это занятие не по насасываю членов, а по надеванию резинки! Тьфу! Он уже кончил и счас станет бесполезным... [st2.name], ты следующий! Может с тобой получится провести этот урок.'
    $ move(curloc)
    