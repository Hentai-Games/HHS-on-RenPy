label event_loc_entrance_20_StartClubPanties:
    show entrance
    python:
        global is_pantiesClub
        if is_pantiesClub != 0:
            skipEvent()
        st1 = getChar('female','corrmax')
    player.say 'Хммм...'
    'Вы слышите странное кряхтение неподалёку.'
    st1.say 'Ну снимайся же, давай! Эх, надо было на размер больше брать!'
    show expression 'pic/locations/school/entrance/pantiesClub.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Вы заходите за школу и видите, как [st1.name] пытается снять свои трусики!'
    if player.getCorr() < 40:
        player.say 'Это что ещё за разврат на голом месте! А ну немедленно прекрати, пока никто не видит!'
        st1.say 'Да уже поздно, вы всё равно увидели... - вздыхает ученица, но всё таки натягивает трусики назад.'
        player.say 'В наказание останешься после уроков!'
        st1.say 'Ясно... - вздыхает ученица и направляется к школе.'
        $ addDetention(st1)
    else:
        player.say 'Это чем это ты занимаешься, позволь спросить?'
        st1.say 'Я ну просто... Это... - неудачно пытается выкрутиться ученица.'
        player.say 'Только не говори, что тебе доставляет эстетическое удовольствие сидеть голой задницей на стуле.'
        st1.say 'Нет, конечно нет... Мы их продаём.'
        player.say 'Продаёте? ВЫ? То есть ты не единственная, кто сегодня носится по школе без нижнего белья?'
        st1.say 'Упс... - прикрывая свой рот шепчет девочка.'
        player.say 'И кому же вы их, простите, продаёте?'
        'Спустя мгновение на вас обрушивается сбивчивый рассказ о том, что девчёнки выискали в интернете сайт с извращенцами, которые покупают поношенные трусики. Ну разумеется им не пришло в голову ничего лучше, как начать встречаться с ними и продавать своё нижнее бельё. Вы решаете взять дело в свои руки.'
        player.say 'Так, хватит шляться по подворотням и продавать свои трусы!'
        '[st1.fname] понуро опускает голову.'
        player.say 'Теперь вы будете делать это организованно! Мы создадим клуб, и вы, каждый день будете отдавать мне свои трусики, продажу я беру на себя, а барыши делим пополам, согласна?'
        st1.say 'Конечно! - радостно улыбается ученица.'
        player.say 'Отлично! Тогда снимай и кидай своё добро мне в сумку.'
        '[st1.fname] снимает свои трусики под вашим пристальным взором и отдаёт их вам.'
        python:
            global is_pantiesClub
            player.addItem(clubPanties)
            st1.removeItems(studpantiesF.name)
            st1.club = 'pants'
            is_pantiesClub = 1
    $ move(curloc)

label event_loc_entrance_0_new1:
    show entrance
    python:
        if 'skimpy' != school.uniform:
            skipEvent()
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLoy(10)
        st2.incLoy(10)
    show expression 'pic/locations/school/entrance/sexy1.jpg' at top as tempPic
    player.say '"Да, весьма неплохо! И груди выпирают, и юбки ничего не прикрывают. Даже отсутствие трусиков..."'
    'Вы размышляли о красоте введённой вами формы лёжа прямо на земле. И какой только балбес раскидывает здесь банановые кожурки?'
    '[st1.name] и [st2.fname] помогли вам подняться, извиняясь за то, что намусорили.'
    player.say '"Всё таки не балбес а балбески..."'
    $ move(curloc)
    
label event_loc_entrance_0_1:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st3 = getChar('female')
        st4 = getChar('female')
    show expression 'pic/locations/school/entrance/no1.jpg' at top as tempPic
    '[st2.name] подаёт подруге зонтик с отстранённым видом. Всем понятно, что делает он это не просто так, но вот 2 девчёнки, которые подглядывают за этим, явно завидуют.'
    if player.getCorr() > 50:
        show expression 'pic/locations/school/entrance/no1a.jpg' at top as tempPic
        player.say '"Надёюсь ему перепадёт сегодня не только улыбка!"'
        'У вас аж голова закружилась, от мыслей, чего [st1.fname] и [st2.fname] могут вытворять вместе!"'
        $ player.incLust(5)
    $ st1.incCorr(1)
    $ st2.incCorr(1)
    $ move(curloc)
    
label event_loc_entrance_0_2:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/school/entrance/no2.jpg' at top as tempPic
    'Упс. Мимоветерок случайно поднял юбочку девчёнки! Как мило!'
    if player.getCorr() > 50:
        player.say '"И как развратно!"'
        $ player.incLust(5)
    $ setFun(10,5)
    $ setLust(10,10)
    $ move(curloc)
    
label event_loc_entrance_0_3:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/school/entrance/no3.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] похоже опаздывают в школу! Заметив вас, [st2.fname] делает испуганное лицо.'
    if player.getCorr() > 50:
        player.say 'Ну, ну, милая, я не кусаюсь!'
        $ st2.incLoy(5)
    $ st1.incFun(-5)
    $ st2.incFun(-5)
    $ move(curloc)
    
label event_loc_entrance_0_4:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/school/entrance/no4.png' at top as tempPic
    '[st1.fname] и [st2.fname] радостно приветствуют вас! Хотя вот [st2.fname] приветствует как то менее радостно...'
    if player.getCorr() > 50:
        player.say 'Солнышко, ну чего ты надулась? Иди сюда, я тебя обниму! - и вы нежно обнимаете ученицу.'
        $ st2.incLoy(5)
    $ st1.incFun(5)
    $ st2.incFun(5)
    $ move(curloc)
    
label event_loc_entrance_0_5:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
    show expression 'pic/locations/school/entrance/no5.jpg' at top as tempPic
    '[st1.fname] ещё смотрит на Вас с улыбкой, [st3.fname] уже спешит Вам на помощь, [st2.fname] сейчас случайно зарядит вам портфелем по лиц... БУМ... '
    player.say '"Мда, жаль, это была многообещающий день, если бы не портфель." - подумали вы лёжа на земле'
    $ player.incEnergy(-100)
    $ move(curloc)
    $ setFun(3,5)
    $ move(curloc)
    
label event_loc_entrance_5_6:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/school/entrance/no6.png' at top as tempPic
    '[st1.fname] и [st2.fname] похоже нашли друг друга. Какая милая картина, видеть их держащимися за руку!'
    if player.getCorr() > 50:
        player.say '"Хотя я бы лучше посмотрела на них вдвоём в постели..."'
        show expression 'pic/locations/school/entrance/no6a.jpg' at top as tempPic
        player.say '"Или вдвоём на парте... Да, вдвоём, да на школьной парте они смотрелись бы великолепно!"'
        player.say '"Особенно его толстенный член в её узенькой киске!"'
        $ player.incLust(10)
    $ st1.incCorr(1)
    $ st2.incCorr(1)
    $ move(curloc)
    
label event_loc_entrance_0_7:
    show entrance
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/entrance/no7.png' at top as tempPic
    'Вы с удовольствием отметили короткость юбки и белизну трусиков школьницы. Будем надеяться, что не только у вас глаз намётан!'
    $ player.incLust(5)
    $ setFun(10,5)
    $ move(curloc)
    
label event_loc_entrance_0_8:
    show entrance
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/entrance/no8.png' at top as tempPic
    'Поднимаясь по лестнице к школе, и бросив случайный взгляд наверх, у вас резко потеплело в трусиках. Да, такой симпатичный видок не каждый день открывается!'
    $ player.incLust(5)
    $ setFun(10,5)
    $ move(curloc)
    
label event_loc_entrance_0_9:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
    show expression 'pic/locations/school/entrance/no9.png' at top as tempPic
    'Вы видите, как [st1.fname] и [st2.fname] мило беседуют, кушая принесённую из дома еду.'
    if player.getCorr() > 50:
        show expression 'pic/locations/school/entrance/no9a.jpg' at top as tempPic
        player.say '"Интересно, успел ли сегодня [st1.fname] накормить киску подружки своим молочком?"'
        player.say '"Я бы посмотрела на такую кормёжку!"'
        $ player.incLust(10)
    $ st1.incFun(10)
    $ st2.incFun(10)
    $ move(curloc)
    
label event_loc_entrance_30_1:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.incLust(10)
    'Проходя мимо входа, вы услышали часть разговора за углом школы.'
    st2.say 'Конечно!, - всегда хотел это попробовать!'
    show expression 'pic/locations/school/entrance/lo1.png' at top as tempPic
    'Вам стало интересно кто и что хотел попробовать. Вы вышли из за угла и увидели что это [st1.fname] и [st2.fname].'
    'Улыбнувшись, [st1.fname] положила член между грудей и сжала его ими. Его член попал в мягкий нежный плен из которого ему совсем не хотелось выбираться. Начав двигаться, она принялась трахать его своими сиськами.'
    player.say '"Чёрт, и правда как в  порнофильмах, что я смотрела!"'
    '[st1.fname] убыстряла свои движения, лаская головку языком когда она показывалась между сисек. [st2.fname] напрягся и мне показалось что он щас кончит.'
    st2.say '[st1.fname]! Я сейчас кончу! Я хочу кончить тебе в сиськи!'
    '[st1.fname] лишь сжала их сильней и, улыбаясь, смотрела на него.'
    st1.say 'Давай, [st2.fname], кончи в мои большие сиськи!'
    'И вот он разрядился несколькими мощными выбросами и его сперма показался между ложбинок ее грудей,когда ее стало много она потекла вниз. Некоторые особо густые капли ненадолго задерживались на ее соске.'
    'Парень стоял над ней и смотрел на её сиськи покрытые его спермой. Ученица же принялась размазывать сперму по всей груди, как бы втирая её в кожу. Судя по его лицу он даже в самых своих смелых мечтах не мог представить подобного!'
    menu:
        'Оставить их':
            'Аккуратно развернувшись, вы ушли, оставив молодых развлекаться.'
            $ hadSex(st1,st2)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_15_2:
    show entrance
    python:
        st1 = getChar('male')
        player.incLust(5)
    'Проходя мимо входа, Вы услышали часть разговора за углом школы.'
    show expression 'pic/locations/school/entrance/lo2.png' at top as tempPic
    '[st1.fname] рассказывал своим друзьям, как он вчера "классно трахнул" свою младшую сестрёнку.'
    player.say '"Врёт наверняка, но зараза, как реалистично рассказывает!"'
    '"Текущая пиздёнка", "хлюпание", "стоны". У вас перед глазами промелькнула картина того, как это могло выглядеть. Весьма так возбуждающе!'
    'Вы решили не наказывать ученика, так как всё равно не поверили ему.'
    $ setLust(5,15)
    $ move(curloc)
    
label event_loc_entrance_30_3:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(10)
    'Услышав странные звуки за углом школы, вы выглянули посмотреть, что же там происходит?'
    show expression 'pic/locations/school/entrance/lo3a.png' at top as tempPic
    'К вашему удивлению, вы увидели как [st2.fname] стоит на коленях, засунув себе в рот член своего одноклассника!'
    st2.say 'Мффф, чафффф, мфффф, мы так не договаривались!'
    st1.say 'Ты же сама сказала, что сделаешь всё что угодно, если я дам тебе списать? Вот и отрабатывай!'
    'Парень вновь засунул свой член меж полных губ одноклассницы.'
    menu:
        'Смотреть дальше':
            show expression 'pic/locations/school/entrance/lo3b.png' at top as tempPic
            'Вы решили не вмешиваться. Дело то житейское, и с удовольствием продолжили наблюдать за любительским исполнением минета. Чавканье ненадолго прерывалось судорожным вздохом, и продолжалось снова.'
            'Наконец парень подался вперёд, выдохнул, и в уголках рта девушки показались белые капли. [st1.fname] не отпускал её, пока не закончил кончать.'
            st2.say 'Кхе, кхе!'
            'Девушка закашлялась, пытаясь продышаться.'
            st2.say 'Чтобы я ещё раз! Тьфу!'
            'Отплёвываясь и глубоко дыша, [st2.fname] вытерлась и стала подниматься. Вы решили исчезнуть, пока ученики случайно не застукали своего директора.'
            $ hadSex(st1,st2)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_30_4:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(10)
    st2.say 'Не останавливайся, только не останавливайся!'
    'Вы услышали тихий девичий голос неподалёку. Недоумённо оглянувшись, вы заметили какие то тени возле подсобки.'
    show expression 'pic/locations/school/entrance/lo4.png' at top as tempPic
    'Аккуратно приблизившись, вы увидели, как [st2.fname] буквально самоудовлетворяется рукой своего парня.'
    st1.say 'Тихо, нас могут услышать!'
    'Зашептал [st1.fname] на ушко девушке, поглядывая по сторонам. Благо вы неплохо замаскировались в кустах.'
    st2.say 'Ах, ах, даааа!!!'
    '[st2.fname] задрожала и обмякла в руках одноклассника.'
    st1.say 'Пошли, я не хочу чтобы [player.name] нас застукала!'
    '[st1.fname] одёрнул однокласснице юбку, и потащил девочку в школу.'
    $ move(curloc)
    
label event_loc_entrance_20_6:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(5)
    show expression 'pic/locations/school/entrance/lo6a.png' at top as tempPic
    'Вы видите, что двух учеников вдруг обуяла страсть на глазах у всех. [st1.fname] жадно целуется со своей подругой, и проходящие мимо ученики любопытно посматривают на них.'
    menu:
        'Смотреть дальше':
            show expression 'pic/locations/school/entrance/lo6b.png' at top as tempPic
            player.say 'Как мило наблюдать первые любовные порывы!'
            'Начинаете вы было свою речь, как вдруг замечаете, что рука парня вдруг оказывается между ног школьницы, и начинает там незамысловатые движения. Бёдра девушки начинают подаваться навстречу, и до вас долетает тихий стон, сорвавшийся с её губ. Похоже простыми поцелуями они не ограничатся.'
            menu:
                'Всё таки наказать их':
                    $ scoldWho = [st1,st2]
                    jump scoldAll
                'Заткнуться и смотреть' if getPar(studs, 'corr') > 40:
                    show expression 'pic/locations/school/entrance/lo6c.png' at top as tempPic
                    'Движения парня под юбкой всё ускорялись. Девушка уже не стесняясь во всю стонала. Ученики вокруг остановились как вкопанные и наблюдали за разворачивающимся перед ними действом.'
                    st2.say 'Мммм, Аааах, ААААаааААААааа!!!'
                    'Школьница задрожала, и в руку парня выплеснулась горячая влага женского оргазма.'
                    'Не обращая ни на кого внимания, [st1.fname] и [st2.fname] поцеловались ещё раз, и взявшись за руки отправились в школу.'
                    $ hadSex(st1,st2)
                    $ setLust(10, 20)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_15_7:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(5)
    show expression 'pic/locations/school/entrance/lo7.png' at top as tempPic
    player.say '"Оппа. Какая попа! То есть, кхм, какого чёрта [st2.fname] показывает свои текущие прелести этому парню в окне?"'
    menu:
        'Не вмешиваться':
            player.say '"Хотя показывает и показывает. Чем бы дитя не тешилось!"'
            'Вот и [st1.fname] имеет весьма довольный, хотя и удивлённый вид. Хотя родителям это решение явно не будет по душе.'
            python:
                st2.incRep(-5)
                st2.incCorr(5)
                setLust(5,10)
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_13_8:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(5)
    show expression 'pic/locations/school/entrance/lo8.png' at top as tempPic
    'Лёгкий ветерок приоткрыл прелести ученицы. Интересно, это повальная мода, или [st2.fname] одна такая? И стоит ли прилюдно наказать её, или фиг бы с ней?'
    menu:
        'Не вмешиваться':
            player.say '"В конце концов погода тёплая, ничего себе не простудит. Может стоит вообще задуматься об обязательности ношении трусов?"'
            python:
                st2.incCorr(2)
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_25_9:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        setLust(20,15)
        setCorr(20,1)
        player.incLust(5)
    show expression 'pic/locations/school/entrance/lo9.png' at top as tempPic
    'Хмм. Какая любопытная униформа! Настолько оригинальная, что кажется как будто [st1.fname], [st2.fname] и [st3.fname] попросту забыли до конца одеться.. Да и остальные в вашем поле зрения одеты точно так же. Новый флэшмоб? Какой то протест? Сейчас я Вам устрою протест!'
    menu:
        'Не обращать внимания':
            player.say '"А хотя если это такой способ самовыражения, то пусть."'
            'В конце концов именно за это Вы и ратуете на школьном совете. Надо только ещё раз проверить, не пишут ли родители гневных писем на Ваш адрес.'
            python:
                st1.incRep(-5)
                st2.incRep(-5)
                st3.incRep(-5)
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll

    
label event_loc_entrance_15_11:
    show entrance
    python:
        st1 = getChar('female')
    menu:
        'Вы слышите шевеление в кустах.'
        'Проверить':
            show expression 'pic/locations/school/entrance/lo11.png' at top as tempPic
            'Увидев шевеление в кустах, вы застали там ученицу со спущенными трусиками. Похоже  [st1.fname] собиралась пописать, но Вы прервали её уединение. Мда, неудобно получилось.'
            $ st1.incLoy(-10)
        'Не проверять':
            player.say '"Я слишком тороплюсь, чтобы проверять каждый куст с кошкой по пути!"'
    $ move(curloc)
    
label event_loc_entrance_25_12:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
        st1.incLoy(-5)
        st1.incRep(5)
        addDetention(st1)
    show expression 'pic/locations/school/entrance/lo12.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    player.say '[st1.fname]! - окликнули вы девушку и дождались, пока она подойдёт своей странной походкой, - Я даже не спрашиваю, [st1.fname], куда подевались твои трусики, но что, прости меня пожалуйста, стекает по твоей ляжке, можешь объяснить?'
    'Ученица смотрит на вас, потом ниже на свои ноги, тихо ойкает, и краснеет.'
    player.say 'В общем иди подмойся, и ты сегодня наказана!'
    'Вы отсылаете ученицу и продолжаете наблюдать за учениками.'
    $ move(curloc)
    
label event_loc_entrance_10_13:
    show entrance
    python:
        st1 = getChar('female')
        if school.uniform != 'usual':
            skipEvent()
    show expression 'pic/locations/school/entrance/lo13.png' at top as tempPic
    'У школьного входа стоит [st1.fname]. Похоже, что ваш указ о свободной одежде она поняла немного по своему...'
    'В принципе, если подумать, то длину ее рубашки можно принять за мини юбку , вернее за микро юбку...'
    $ move(curloc)

label event_loc_entrance_10_14:
    show entrance
    python:
        st1 = getChar('male')
    show expression 'pic/locations/school/entrance/lo14.png' at top as tempPic
    '[st1.fname], буквально у вас на глазах, заглядывает под юбку задремавшей учительнице!'
    menu:
        'Не вмешиваться':
            player.say '"Младший школьничек, мальчик молодой, все хотят потанце..."'
            player.say '"Кхм, нет, в любом случае неважно, образование штука многогранная, никогда не знаешь, где убудет, а где прибудет."'
            python:
                st1.incCorr(2)
        'Наказать':
            $ scoldWho = [st1]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_40_1:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
        player.incLust(10)
    st1.say '[st2.fname], он не войдёт!'
    'Услышали вы из ближайших кустов, и сразу же решили полюбопытствовать, что же там не входит.'
    show expression 'pic/locations/school/entrance/mid1.png' at top as tempPic
    ' Аккуратно раздвинув ветви, Вы увидели, что [st1.fname] готовится принять член парня в место не совсем для этого подходящее.'
    st2.say 'Сейчас, чёрт, больно! - ругнулся парень, а девушка тихо ойкнула.'
    show expression getCharImage(player,'dialog') as temp1
    player.say 'А ты плюнь и смажь, - вышли вы из кустов перед обалдевшей парочкой.'
    st2.say 'Ой, мы тут это, - начал запинаться ученик.'
    player.say 'От запора лечитесь, я вижу, а ну марш на занятия! - крикнули вы на них, и с чистой совестью отправились дальше.'
    $ move(curloc)
    
label event_loc_entrance_55_1:
    show entrance
    python:
        st1 = getChar('female')
        st2 = mustangovich
        hadSex(st1,st2)
        player.incLust(10)
    show expression 'pic/locations/school/entrance/hi1.png' at top as tempPic
    'Заметив шебуршение у забора, Вы заглянули в кусты. Мда, а Ахмед то времени не теряет в школе... Вон и спортивную форму себе прикупил, и девочку соблазнил. Какой прекрасный вид на киску, как будто физрук специально для вас приоткрыл створки этой раковинки.'
    'Ну да ладно, все уже не маленькие, сами знают что и как делать. Вы выползаете их кустов, пока никто вас не заметил.'
    $ move(curloc)

label event_loc_entrance_50_2:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.coverSperm('лицо')
        hadSex(st1,st2)
    menu:
        'Вы слышите шевеление в кустах.'
        'Проверить':
            show expression 'pic/locations/school/entrance/hi2.png' at top as tempPic
            'Ваше любопытство вас погубит. Или нанесёт непоправимый вред репутации. Услышав стоны из кустов возле забора, вы знали что там увидите. Но не догадывались, что ваша голова высунется прямо под парочкой во время оргазма.'
            'В итоге на вашем лице оказалась большая часть эякулята вытекающего из киски. Хорошо что хоть [st1.fname] и [st2.fname] вас не засмеяли, а лишь улыбнулись, и пообещали найти место поукромней, чтобы больше вас не пачкать.'
        'Не проверять':
            player.say '"Я слишком тороплюсь, чтобы проверять каждый куст с кошкой по пути!"'
    $ move(curloc)
    
label event_loc_entrance_65_3:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st3 = getChar('female')
        st4 = getChar('male')
        player.incLust(10)
        hadSex(st1,st2)
        hadSex(st3)
    show expression 'pic/locations/school/entrance/hi3.png' at top as tempPic
    '[st1.fname] и [st2.fname] без всякого стеснения занимаются сексом прямо на школьном крыльце. Ученица громко стонет в то время, как её одноклассник вгоняет в её узенькое влагалище свой крепкий член.'
    'Мимо проходящие [st3.fname] и [st4.fname] тоже не отличаются обилием целомудрия. Интересно, это вообще удобно ходить, когда пальцы парня в твоём влагалище? Вы чувствуете возбуждение от созерцания происходящего.'
    $ move(curloc)
    
label event_loc_entrance_70_4:
    show entrance
    python:
        st1 = getChar('female')
        setLust(10,-20)
        setFun(10,10)
    show expression 'pic/locations/school/entrance/hi4.png' at top as tempPic
    'Ученица сидит на лавочке у школьного входа, предлагая каждому обладателю мужского достоинства минет.'
    player.say '[st1.fname], с тобой всё в порядке? - участливо спрашиваете вы девушку.'
    st1.say 'Конечно, просто биологичка дала мне задание собрать побольше семенного образца, вот я и собираю, - сплюнув сперму изо рта в руки ответила девочка, - всё в порядке, идите.'
    player.say 'Понятненько... - задумчиво говорите вы и отправляетесь дальше по своим делам.'
    $ move(curloc)
    
label event_loc_entrance_70_5:
    show entrance
    python:
        st1 = getChar('futa')
        st2 = getChar('female')
        st3 = getChar('female')
        hadSex(st1,st2)
        setFun(5,10)
        setLust(10,10)
    show expression 'pic/locations/school/entrance/hi5.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    st2.say 'Ну же, давай же, дай мне своего молочка!'
    '[st2.fname] активно скакала на члене своей одноклассницы - футы, неподалёку от школьного входа.'
    st1.say 'М-м-м, я сейчас, м-м-м.'
    '[st1.fname] напрягала бёдра, двигаясь в такт движениям своей любовницы.'
    st2.say 'Ну же, ну! Докажи что ты не хуже моего парня! Я так люблю писькино молочко!'
    '[st2.fname] опустилась, полностью поглотив член своей щёлкой и начала круговые движения попкой.'
    'Вас немного удивило обилие зрителей, как будто не все верят, что мужской причиндал девушки способен выдать сперму.'
    show expression 'pic/locations/school/entrance/hi5a.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    st1.say 'Ммммм-олочко! - вдруг застонала [st1.fname] и резко задвигала попой в оргазме.'
    st2.say 'Да, да! Я чувствую!'
    '[st2.fname] вытащила член из себя, и успела заметить последний фонтанчик вырвавшийся из головки.'
    'Класс! Я всё засняла! - похвасталась [st3.fname], - Теперь твоему парню нечего будет противопоставить футе! Она такая же как и он, только лучше!'
    player.say '"Мда, они уже выбирают что лучше, девочка с мужским органом или парень..."'
    $ move(curloc)
    
label event_loc_entrance_60_6:
    show entrance
    python:
        st1 = getChar('female')
        st2 = mustangovich
        hadSex(st1,st2)
        setFun(5,10)
        setLust(5,10)
    show expression 'pic/locations/school/entrance/hi6.png' at top as tempPic
    st1.say 'Да, [st2.name], в меня!!!'
    '[st1.fname] визжит в крепких руках физрука, пока тот изливает свою сперму глубоко в её матку.'
    player.say '"Вот ведь кобель!", - с негодованием смотрите вы, как очередная девушка пала жертвой его мускулистого торса и красных трусов.'
    $ move(curloc)