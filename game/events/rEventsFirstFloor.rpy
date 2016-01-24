label event_loc_firstFloor_0_no1:
    show firstFloor
    show expression 'pic/locations/school/firstFloor/no1.jpg' at top as tempPic
    'Внезапно во всей школе погас свет. Коридор вдруг приобрёл какой-то мистический оттенок.'
    if player.getCorr() > 50 and player.getLust() > 50 or development == 1:
        show expression 'pic/locations/school/firstFloor/no1a.png' at center as tempPic1
        player.say '"Что?"'
        hide tempPic1
        'На секунду вам показалось, что две девушки только что предавались ласкам прямо перед вами! Проморгавшись, вы поняли, что воображение играет с вами шутки.'
    'Через минуту свет дали, и всё стало по прежнему.'
    $ move(curloc)
    
label event_loc_firstFloor_5_no2:
    show firstFloor
    python:
        st1 = getChar('futa')
        st2 = getChar('male')
        st1.incFun(-10)
        st1.incCorr(2)
        st1.incLoy(10)
    show expression 'pic/locations/school/firstFloor/no2.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Поднимаясь по лестнице, вы увидели, что [st1.fname] чем-то очень расстроена. Хотя, если судить по кружочкам над её головой, ей просто безответно нравится [st2.fname].'
    'Вы решили немного поговорить с девочкой и вселили в неё небольшую надежду на ответные чувства.'
    if player.getCorr() > 20:
        $ st1.incLust(20)
        'Пытаясь утешить, вы приобняли девицу, и неожиданно в ваше бедро упёрлось то, чего у девочек быть не может.'
        player.say '"Однако... Чего это она там себе нафантазировала?"'
        show expression 'pic/locations/school/firstFloor/no2a.jpg' as tempPic:
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
        player.say '"Может быть как она будет издеваться над парнем, если он её не примет и уйдёт к другой?"'
        player.say '"Не думаю... Это слишком жестоко, для такой милой девочки!"'
    $ move(curloc)
    
label event_loc_firstFloor_0_no3:
    if is_cherleaderClub != 0:
        $ skipEvent()
    show firstFloor
    'В коридоре вам встретились две девушки, и чуть ли не насильно затащили в класс.'
    jump event_loc_class2_0_1
    
label event_loc_firstFloor_0_no4:
    show firstFloor
    python:
        if hour < 14:
            skipEvent()
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st1.incEdu(10)
        st2.incEdu(10)
        st3.incEdu(10)
    show expression 'pic/locations/school/firstFloor/no4.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Ученицы [st1.fname], [st2.fname] и [st3.fname] собираются на дополнительные занятия.'
    if player.getCorr() > 50:
        show expression 'pic/locations/school/firstFloor/no4a.jpg' as tempPic:
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        'Потакая своей развратной натуре, вы надеетесь, что это будут дополнительные занятия по сексуальному просвещению, в области "Совместное использование двойных дилдо количеством трёх человек и более."'
        player.say '"Да, это был бы интересный опыт, посмотреть как девушки делят один дилдо на троих... Например [st2.fname] и [st3.fname] сверху тренируют свои дырочки, а [st1.fname] соблазняет зрителя своей розовой киской."'
        player.say '"А потом они меняются, и так вплоть до того, пока оргазм не разлучит их!"'
        'Вы вздыхаете, прокручивая картинку вероятного будущего в голове, и отправляетесь дальше по своим делам.'
    $ move(curloc)
    
label event_loc_firstFloor_0_no5:
    show firstFloor
    python:
        st1 = getChar('female')
        st1.incFun(10)
    show expression 'pic/locations/school/firstFloor/no5.jpg' at top as tempPic
    'В коридоре вы видите, что [st1.fname] разговаривает с кем-то по телефону. Ну чтож, телефоны не запрещены, пускай себе болтает.'
    if st1.getCorr() > 60 or development == 1:
        'Услышав инетересные слова, вы всё таки решаете прислушаться.'
        st1.say 'Ну па-а-п! Ну купи мне ыФон 376 UltraLux! Ну купи!'
        st1.say 'Не, ну так нечестно! Давай как вчера, я тебе киску покажу, ты подрочишь и купишь мне!'
        show expression 'pic/locations/school/firstFloor/no5a.jpg' as tempPic:
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        'У вас в голове возникла вполне правдобная картинка того, как это всё могло происходить.'
        player.say '"Вот сидит такая [st1.fname] перед отцом, да без трусиков, а тот наяривает свой здоровенный член, и сипло шепчет любимой дочке ласковые слова..."'
        player.say '"А теперь ещё и ыФон купит последний..."'
        player.say '"Хех, да после таких слов от доченьки, я думаю он и бузить особо не будет в случае чего!"'
        $ st1.incRep(25)
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_firstFloor_0_no6:
    show firstFloor
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('male')
        st1.incFun(10)
        st2.incFun(10)
        player.incFun(5)
    show expression 'pic/locations/school/firstFloor/no6.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] возвращаются с занятий смеясь о чём то. Вам радостно наблюдать эту молодую весёлость. Совсем недавно вы были такой же.'
    if st1.getCorr() > 40 or development == 1:
        $ hadSex(st1,st3)
        $ setLust(3, 30)
        $ player.incLust(10)
        'До вас долетают обрывки их разговора.'
        show expression 'pic/locations/school/firstFloor/no6a.jpg' at top as tempPic
        st2.say 'И что, ты ему прямо в классе отсосала?'
        st1.say 'Ага!'
        st2.say 'И чё, [st3.fname] вообще большой там или как?'
        st1.say 'Ага!'
        st2.say 'А как ты вообще, сложно было?'
        st1.say 'Ага! Еле в рот поместился! Только до половины вошёл, и уже в глотку упёрся. Но зато я языком смогла почти до его яиц дотянуться!'
        st2.say 'Ого! Ты с высунутым языком сосала что ли? Как шлюха? Класс! Я тебе завидую!'
        player.say '"Однако..."'
        'Смеясь и раздвигая руки как рыбаки, девушки скрылись за углом.'
    $ move(curloc)
    
label event_loc_firstFloor_0_no7:
    show firstFloor
    python:
        bissektrisovna.incLoy(5)
        player.incFun(5)
    show expression 'pic/locations/school/firstFloor/no7.jpg' at top as tempPic
    'Скользкий пол, неуклюжий шаг, и вот уже [bissektrisovna.name] обнаруживает вас у себя между ног. Конфуз то какой!'
    'Хотя, после того, как вы поднялись, никаких обид не возникло и вы вместе посмеялись над этим случаем.'
    $ move(curloc)
    
label event_loc_firstFloor_0_no8:
    show firstFloor
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        setFun(10,10)
    show expression 'pic/locations/school/firstFloor/no8.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] несут принадлежности для черчения. Всё бы хорошо, но только такой предмет в вашей школе пока не преподают.' 
    'Вы интересуетесь у девочек, зачем им столько бумаги и узнаёте, что они готовят сюрприз для мальчишек.'
    $ move(curloc)
    
label event_loc_firstFloor_0_no9:
    show firstFloor
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLoy(-5)
        st2.incLoy(-5)
    show expression 'pic/locations/school/firstFloor/no9.jpg' at top as tempPic
    'До тех пор, пока вы быстрым шагом не ворвались на этаж, [st1.fname] и [st2.fname] что то обсуждали друг с другом. Теперь же они просто смотрят на вас и молчат.'
    'Аккуратно ступая, вы удаляетесь.'
    $ move(curloc)
    
label event_loc_firstFloor_0_no10:
    show firstFloor
    python:
        player.incLust(5)
        setRep(5,-2)
    show expression 'pic/locations/school/firstFloor/no10.jpg' at top as tempPic
    'Эмм, это было неожиданно. Точнее неожиданного было много. Сначала неожиданно недавно помытый пол, потом неожиданно оставленный кем-то портфель. Далее, насколько вы можете припомнить, была неожиданно не свойственная для вас невнимательность. Как следствие - неожиданный вид, представший перед вашими глазами.'
    $ move(curloc)
    
label event_loc_firstFloor_0_no11:
    show firstFloor
    python:
        st1 = getChar('female')
        player.incLust(5)
    show expression 'pic/locations/school/firstFloor/no11.png' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] взбегает на второй этаж, явно куда-то опаздывая. Её развевающаяся юбочка и стройные ножки радуют ваши глаза.'
    $ move(curloc)
    
label event_loc_firstFloor_0_no12:
    show firstFloor
    python:
        setFun(10,10)
    show expression 'pic/locations/school/firstFloor/no12.png' at top as tempPic
    'Обычный день в обычной школе. Все высыпали в коридор и занимаются своими делами. Хотелось бы кого нибуь наставить на путь истинный, но вроде всё и так в порядке. Ваше вмешательство не требуется.'
    $ move(curloc)
    
    
label event_loc_firstFloor_20_lo1:
    show firstFloor
    python:
        if school.uniform not in ['sexy','usual']:
            skipEvent()
        setCorr(5,5)
        setLust(10,10)
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        player.incLust(5)
    show expression 'pic/locations/school/firstFloor/lo1.jpg' at top as tempPic
    'Поднимаясь по лестнице, вы заметили, что ваш недавний указ о свободной форме одежды трактуется довольно вольно. [st1.fname] и пара других девушек решили попросту не надевать сегодня трусиков в школу и всё!'
    if is_pantiesClub == 1:
        player.say '"Хотя может быть девушки из моего секретного клуба? На всякий пожарный не буду кричать на них, а то буду попросту глупо выглядеть в их глазах."'
    else:
        menu:
            'Оставить всех после уроков':
                $ scoldWho = [st1,st2,st3]
                jump scoldAll
            'Не обращать внимания':
                player.say '"В конце концов это не моё дело, что ученицы прячут под юбками. Хотя, конечно, слухи пойдут..."'
                $ setRep(5,-5)
    $ move(curloc)
    
label event_loc_firstFloor_15_lo2:
    show firstFloor
    python:
        st1 = getChar('male')
        setLust(5,15)
        st1.incCorr(5)
    show expression 'pic/locations/school/firstFloor/lo2.jpg' at top as tempPic
    'Идя по коридору, вы услышали как группа парней вовсю обсуждают недавнюю историю приключившуюся с одним из них. Якобы [st1.fname] смог уломать свою сестрёнку на настоящий минет! Количество "Ух ты", и "Ах ты", а так же увеличивающиеся количество сантиметров во рту у девочки по мере рассказа, окончательно уверили вас в том, что это всего лишь влажные фантазии лоликонщиков.'
    if player.getCorr() > 40:
        $ player.incLust(10)
        player.say '"Мечты мечтами, а я бы на это посмотрела!"'
    $ move(curloc)
    
label event_loc_firstFloor_20_lo3:
    show firstFloor
    python:
        st1 = getChar('female','lustmax')
        hadSex(st1)
        player.incLust(10)
    show expression 'pic/locations/school/firstFloor/lo3.jpg' at top as tempPic
    'Случайно глянув в приткрытую дверь в коридоре, вы заметили, что [st1.fname] занимается вещами далёкими от учебников и ручек. Её ладошка плавно скользила по мокрым от возбуждения трусикам, и вязкие капли её сока медленно стекали по ноге к парте'
    menu:
        'Продолжать смотреть':
            show expression 'pic/locations/school/firstFloor/lo3a.jpg' at top as tempPic
            player.say 'Упс!'
            'Вы поспешно хлопнули дверью, поняв, что [st1.name] заметила вас. Вряд ли это укрепит ваши с ней отношения.'
            $ st1.incLoy(-10)
        'Уйти':
            'Немного насладившись видом мастурбирующей девочки, вы аккуратно прикрыли дверь и отправились дальше.'
    $ move(curloc)
    
label event_loc_firstFloor_15_lo4:
    show firstFloor
    python:
        st1 = getChar('futa')
        st2 = getChar('female')
        player.incLust(5)
        hadSex(st1)
    show expression 'pic/locations/school/firstFloor/lo4.jpg' at top as tempPic
    'Вы подслушали, как [st1.fname] по секрету рассказывала своей подружке, о нестандартном использовании плюшевого мишки. Судя по горящим глазам девочки, [st2.fname] уже придумывала, чтобы такого приделать к своему мишке.'
    $ move(curloc)
    
label event_loc_firstFloor_25_lo5:
    show firstFloor
    python:
        st1 = getChar('female')
        player.incLust(10)
        hadSex(st1)
    show expression 'pic/locations/school/firstFloor/lo5.jpg' at top as tempPic
    'Кинув взгляд на приоткрытую дверь во второй кабинет, вы застыли как вкопанная.'
    '[st1.fname] похоже немного зачиталась любовным романом, и, пользуясь тем, что все покинули класс, решила поиграть сама с собой. Её напряжённые соски, капельки пота, и призывно открытый вход в маленькую пещерку намекал на то, что мастурбирует она в классе не в первый раз.'
    menu:
        'Наказать':
            $ scoldWho = [st1]
            jump scoldAll
        'Не обращать внимания':
            player.say '"Ну не убудет же от неё в самом деле! К тому же в классе никого нет!"'
            'Вам как то даже не пришло в голову, что не вы одна можете заглянуть в приоткрытую дверь.'
            $ setLust(5,20)
            $ setRep(2,-10)
    $ move(curloc)
    
label event_loc_firstFloor_30_lo6:
    show firstFloor
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('male')
        st1.incCorr(5)
        st2.incCorr(5)
        st3.incLust(50)
        player.incLust(5)
    show expression 'pic/locations/school/firstFloor/lo6.jpg' at top as tempPic
    'Войдя в коридор первого этажа, вы поражённо застыли. [st1.fname] и [st2.fname] хвастались парню тем, что вчера побрили свои киски! И этот показ похоже неплохо возбудил их! [st3.fname] задумчиво разглядывал открывшиеся перед ним прелести, как будто выбирая.'
    player.say 'Какого богавашуматерь тут происходит?'
    'Заметив вас, девчёнки быстро натянули трусики и, хихикая, свалили. Вы решили не гнаться за ними. В конце концов ничего страшного не произошло.'
    $ move(curloc)
    
label event_loc_firstFloor_20_lo7:
    show firstFloor
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        hadSex(st1,st2)
        player.incLust(5)
    show expression 'pic/locations/school/firstFloor/lo7.jpg' at top as tempPic
    'Вы видите, как [st1.fname] и [st2.fname] предаются оральным утехам у подоконника напротив окна. Целуются то есть.'
    show expression 'pic/locations/school/firstFloor/lo7a.png':
        xalign 1.0 yalign 0.0
    player.say '"Хотя, судя по интенсивности, с которой [st1.fname] лезет подружке в трусики, тут и до полного контакта кисок недалеко."'
    menu:
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Не обращать внимания':
            player.say '"Чем бы дитя не тешилось!"'
            'Хотя родители учениц вряд ли согласятся с вашим мнением.'
            $ setLust(5,20)
            $ setRep(2,-5)
        'Посмотреть':
            show movie
            play movie "pic/locations/school/firstFloor/lo7a.gif.webm" loop
            'Вы наблюдаете за тем, как девочки ловко играют со своими язычками, нежно обсасывая их, и поглаживая.'
            player.say '"Интересно, они пельмешки так же лижут?"'
            stop movie
            hide movie
            $ player.incLust(15)
            $ player.incCorr(3)
            if rand(1,3) == 1:
                'Кто то заметил, как вы подглядываете за учениками. По школе поползли нехорошие слухи.'
                $ setRep(5,-5)
    $ move(curloc)
    
label event_loc_firstFloor_30_lo8:
    show firstFloor
    python:
        st1 = getChar('female')
        setLust(5,15)
        st1.incCorr(5)
        player.incLust(5)
    show expression 'pic/locations/school/firstFloor/lo8.jpg' at top as tempPic
    '[st1.fname] хвастается подружкам, что сегодня не одела трусики под юбочку. Подружки восхищённо ахают. Вы тоже ахаете, но не от восхищения, а от шока, что такую красивую киску не скрывают красивые трусики.'
    if is_pantiesClub == 1:
        player.say '"Возможно она из клуба поношенных трусиков. Не стоит заострять внимание."'
    else:
        menu:
            'Наказать':
                $ scoldWho = [st1,st2]
                jump scoldAll
            'Не обращать внимания':
                pass
    $ move(curloc)
    
label event_loc_firstFloor_30_lo9:
    show firstFloor
    python:
        st1 = getChar('female')
        st1.incCorr(3)
        player.incLust(5)
    show expression 'pic/locations/school/firstFloor/lo9.jpg' at top as tempPic
    '[st1.fname] похоже забыла натянуть нижнее бельё. Вы не видите другого объяснения тому, что она сидит с голой попой, и трусиками болтающимся на ноге. Не писать же она в коридоре собралась?'
    'Заметив вас, ученица громко ойкает, и убегает, оставляя в неведении относительно её намерений. Ну хоть на киску посмотрели!'
    $ move(curloc)
    
label event_loc_firstFloor_20_lo10:
    show firstFloor
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.incLust(5)
        hadSex(st1,st2)
    show expression 'pic/locations/school/firstFloor/lo10.jpg' at top as tempPic
    'Из окна вы увидели, как [st1.fname] и  [st2.fname] страстно целуются.'
    player.say '"Надо бы им сказать пару ласковых, но кричать на улицу не хочется, а идти далеко. Пусть себе молодёжь развлекается!"'
    $ move(curloc)
    
label event_loc_firstFloor_0_lo11:
    show firstFloor
    python:
        if school.uniform not in ['sexy','usual','uniform']:
            skipEvent()
        st1 = getChar('female')
        st2 = getChar('male')
    'Вы замечаете какую то блестяшку под лестницей. Подойдя ближе, вы заметили, что это всего лишь крышка от баночки газировки. Вы слышите смех и гомон над вами.'
    menu:
        'Идти дальше':
            pass
        'Посмотреть наверх' if player.getCorr() > 25:
            $ player.incLust(20)
            show expression 'pic/locations/school/firstFloor/lo11.png' at top as tempPic
            'Вы постояли немного под лестницей, наблюдая как девушки одна за одной, проходят мимо, оставляя в вашей памяти следы их прекрасных трусиков. Пожалуй, это были одни из самых лучших минут в вашей жизни. '
            if rand(1,3) == 1:
                'Кто заметил, как вы стояли под лестницей. Ваша репутация упала.'
                $ setRep(3,-5)
    $ move(curloc)
    
label event_loc_firstFloor_50_mid1:
    show firstFloor
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incCorr(5)
        st2.incCorr(5)
        setLust(4,20)
        player.incLust(15)
    show expression 'pic/locations/school/firstFloor/mid1.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] хвастаются перед подругами своими новыми гаджетами! Вам немного не по себе от того места, куда они их засунули...'
    menu:
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Ну и ладно, хоть не беременны!':
            'Пока вы находили себе оправдание тому, чтобы не вмешиваться, [st1.fname] вдруг задрожала, и сползла по стенке, заливая пол своими выделениями.'
            player.say '"Всё таки кончила!", - подумали вы, и пошли дальше по своим делам.'
    $ move(curloc)
    
label event_loc_firstFloor_60_mid2:
    show firstFloor
    python:
        if school.uniform != 'naked':
            skipEvent()
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st1.incCorr(5)
        st2.incCorr(5)
        st3.incCorr(5)
        player.incLust(10)
    show expression 'pic/locations/school/firstFloor/mid2.jpg' at top as tempPic
    '"Сегодня день небритой киски чтоли?" - думали вы, глядя на [st1.fname], [st2.fname] и [st2.fname] стоящих у окна в коридоре.'
    $ move(curloc)
    
label event_loc_firstFloor_40_mid3:
    show firstFloor
    python:
        st1 = getChar('female')
        st2 = getChar('male','lustmax')
        hadSex(st1,st2)
    show expression 'pic/locations/school/firstFloor/mid3.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
    st1.say ' Да ты охренел чтоли?'
    '[st1.fname] возмущённо оборачивается, когда подошедший сзади парень, вдруг достал свой член и окропил её своим семенем.'
    st2.say 'А нечего жопу так оттопыривать!'
    'И парень залепил ещё смачный шлепок по заляпанной спермой заднице.'
    st1.say 'Да я счас тебя!'
    menu:
        'Наказать его':
            $ scoldWho = [st2]
            jump scoldAll
        'И действительно, чего это она оттопырила попу?':
            player.say 'Стоять! Не заниматься рукоприкладством. [st1.name], не удивляйся вниманию, если надеешься его привлечь! Спрячь задницу и никто к тебе не подойдёт!'
            player.say 'А ты, [st2.name], не распускай, кхм, руки на то, что ещё не твоё!'
            'Разняв учеников, вы отправились дальше.'
            $ st1.incLoy(10)
            $ st2.incLoy(10)
    $ move(curloc)
    
label event_loc_firstFloor_45_mid4:
    show firstFloor
    python:
        st1 = getChar('female','lustmax')
        hadSex(st1)
        incLust(10,25)
        incFun(10,10)
        player.incLust(15)
    show expression 'pic/locations/school/firstFloor/mid4.jpg' at top as tempPic
    'Не найдя себе парня, [st1.fname] принялась удовлетворять себя посреди коридора, буквально на ваших глазах. Она медленно опустилась на коленки, её пальчики нащупали под юбкой влажную киску, и медленно погрузились в неё. Девочка громко застонала, ощущая заполненность киски.'
    menu:
        'Наказать её':
            $ scoldWho = [st1]
            jump scoldAll
        'Попросить уйти в другое место':
            player.say '[st1.fname], будь так добра, найди более укромное местечко, тут всё таки люди ходят.'
            player.say 'А ты тут растопырилась на пути.'
            'Согласившись, что немного мешает движению, ученица с тихим всхлипом вытащила свои пальчики, и с понурым видом пошла по коридору.'
    $ move(curloc)
    
label event_loc_firstFloor_80_hi1:
    show firstFloor
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st2 = getChar('male')
        st2 = getChar('male')
        hadSex(st1,st2,st3,st4)
        player.incLust(20)
    show expression 'pic/locations/school/firstFloor/hi1.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] радостно принимала в себя сразу 3 члена, прямо на полу в коридоре. Похоже делала она это уже некоторое время, потому что [st2.fname] яростными рывками в её влагалище выталкивал оттуда сперму своего предшественника.'
    player.say 'Ты хоть предохраняшься, шлюшка? - спросили вы стонущую в очередном оргазме ученицу.'
    st1.say 'М-м-м-м, чаф-ф, М-М-М-М, Д-а-а-а-а-а!'
    'Ученица простонала что то утвердительное в перерывах между сосанием членов, что вы приняли за положительный ответ и пошли дальше.'
    menu:
        'Хотя, если подумать...'
        'Орднунг убер аллес! (Наказать)':
            $ scoldWho = [st1,st2,st3,st4]
            jump scoldAll
        'Всё таки уйти':
            pass
    $ move(curloc)
    