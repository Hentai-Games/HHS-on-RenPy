label mileQwest1:
    $ clrscr()
    $ st1 = getChar('female')
    $ st2 = getChar('female')
    $ st3 = getChar('futa')
    $ hadSex(st1,mustangovich)
    $ t = mustangovich
    show hall as bg
    show expression 'pic/events/mile_1/1.png' at top as tempPic
    'Вы замечаете плачущую ученицу и подходите к ней. Она сидит на полу и рыдает. Переодически её руки прижимаются к нижней части живота, как будто у неё что то болит'
    player.say 'Что случилось? Тебя мальчишки обидели?'
    st1.say 'Меня изнасиловал наш физрук [t.name]! Его огромный член трахал меня с такой силой, что он по моему мне всё порвал!'
    'Несмотря на её слова, крови не видно, и вряд ли у неё всё так серьёзно, как она говорит. Скорее всего в ней говорит больше обида, чем боль.'
    player.say 'Что он с тобой сделал? - спрашиваете вы, успокаивая и поглаживая её по плечам'
    show storage as bg
    show expression 'pic/events/mile_1/2.jpg' at top as tempPic
    st1.say 'Он попросил меня принести мяч из кладовки, и когда я наклонилась, чтобы взять его из корзины, он схватил меня сзади, прижал к козлам, и...'
    'Не в силах продолжать свой рассказ, [st1.name] захлёбывается в рыданиях.'
    player.say 'Ты уверена, что это был он?'
    show hall as bg
    show expression 'pic/events/mile_1/1.png' at top as tempPic
    st1.say 'Ну а у кого ещё в нашей школе 30 сантиметровый член?'
    'Увидев ваши брови, которым высота вашего лба стала резко недостаточной для восхождения, ученица смущённо замолкает.'
    player.say 'Та-а-ак, и сколько же членов ты уже перемерила???, - удивлённо вопрошаете вы, но ученица не дождавшись окончания реплики, убегает, невзирая на "боль и унижение".'
    hide tempPic
    player.say 'Мне надо всерьёз поговорить с физкультурником на эту тему. Иш ты, горячий горный парень, решил совместить физкультуру с сексуальным образованием! Да и не может у человека быть член в 30 сантиметров. Ну не бывает таких просто!'
    show gym as bg
    'Вы направляетесь в спортзал, но тут никого нет. Странно, обычно на перемене тут полно народу. Интересно, где виновник вашего визита, [t.name]?'
    menu:
        'И где он прячется?'
        'Посмотреть в раздевалке':
            'Подходя к раздевалке, вы услышали странные стоны.'
            show changeRoom as bg
            show expression 'pic/events/mile_1/3.png' at top as tempPic
            $penis = int(st3.body.parts['пенис'].size)
            player.say 'Ага, вот ты и попался, грязный извращенец! - закричали вы открывая дверь, и с удивлением уставились на [penis] сантиметровый член ученицы [st3.fname].'
            '"Что за чёрт?" - успели вы подумать, прежде чем белая струя спермы ударила прямо в лицо.'
            $ player.coverSperm('лицо','грудь')
            show expression 'pic/events/mile_1/4.png' at right as tempPic
            'Вы как стояли с открытым, так и стоите. Только теперь рот полон спермы, уж не нарочно ли ученица умудрилась? Да и ученица ли?'
            st3.say 'Простите меня пожалуйста, я не хотела!'
            '"Что за невезучий день, сначала [t.fname], теперь ещё и это."'
            player.say 'Давно ли этот инструмент у тебя? - интересуетесь вы с улыбкой.'
            st3.say 'Поговаривают, что существуют препараты, которые делают девчёнок такими, но я родилась с членом.'
            'Школьница смущённо опускает глаза на свой приборчик.'
            st3.say 'Сначала родители хотели от меня отказаться, но колдунья сказала, что я принесу им счастье.'
            player.say 'Не знаю как родителей, но меня ты сегодня осчастливила конечно... Кстати, не подскажешь, где наш физрук?'
            st3.say '[t.name]? Он в кладовке, с моей подругой [st2.fname].'
            hide tempPic
            player.say '"Вся школа чтоли уже в курсе? Я директор в конце концов или нет?"'
            'Не долго думая, вы слегка отряхиваетесь и направляетесь в кладовку.'
            jump mileQwest1_storage
        'Посмотреть в кладовке':
            jump mileQwest1_storage

label mileQwest1_storage:
    show gym as bg
    'Подходя к кладовке вы услышали как, тихие голоса разговаривают о чём то. Вы решили подсмотреть, что же там происходит? Вдруг [t.name] просто объясняет студентке как выполнить сложное упражнение? Хотя кого я обманываю?'
    show storage as bg
    show movie
    play movie 'pic/events/mile_1/5.gif.webm' loop
    'Посмотрев в дверную щель, Вы отшатнулись. Да, Вы в чём то оказались правы. [t.fname] действительно объяснял студентке упражнение. Только оно было не совсем спортивным. Спортивным конечно, но не совсем. За те секунды, что вы провели у двери, вы успели заметить не только тщательность выполнения трюка, но и размеры учителя.'
    player.say '"Японская богоматеринница! Да как же он у него в трусах то умещается? Телескопический что ли?"'
    'Вне зависимости от вашего желания, вы почувствали, что в трусах стало жарко и влажно. Прижавшись к стене, вы стали думать о том, что следует сделать дальше. Учитывая ваше состояние, лучше наверно было бы подождать пока они закончат.'
    $ player.incLust(10)
    $ st2.incCorr(1)
    stop movie
    hide movie
    show gym as bg
    menu:
        'Что делать? Что делать? ЧТО ДЕЛАТЬ?'
        'Подсматривать':
            show storage as bg
            $ player.incCorr(1)
            show expression 'pic/events/mile_1/6.png' at top as tempPic
            'Заглянув во второй раз, Вы увидели, что ситуация поменялась, теперь [st2.fname] сидела на попе, призывно раздвинув киску, а её ножки скользили по влажному от её соков члену учителя.'
            '[t.name] постанывал и совершал импульсивные движения бёдрами. Несмотря на то, что только недавно он надругался над другой ученицей, его эрекция была всё ещё тверда, и член подрагивал от каждого прикосновения юной ступни, готовясь вот-вот извергнуть семя.'
            show gym as bg
            hide tempPic
            show movie
            play movie 'pic/events/mile_1/7.gif.webm' loop
            'Вы и сами не заметили, как ваши пальчики оказались в трусах. Волны удовольствия прокатывались по вашему телу, и трепет оргазма захватил вас почти с первого прикосновения.'
            player.say 'М-м-м, не хватало ещё кончить одновременно с этим, о-о-ох.'
            'Уже не обращая внимания на разврат творящийся в соседней комнате, вы полностью сконцентрировались на ощущениях в ващей похотливой киске. Пальчики порхали всё быстрее, вверх - вниз, провести по губкам, опять к клитору, вниз - вверх.'
            play movie 'pic/events/mile_1/8.gif.webm' loop
            'Вас с головой накрыл оргазм, и, судя по мужским стонам из кладовки, не только вы побывали на эвересте наслаждения.'
            stop movie
            hide movie
            show storage as bg
            show expression 'pic/events/mile_1/9.png' at top as tempPic
            'Немного отдышавшись, вы посмотрели в приоткрытую дверь, и увидели, что измазанные в сперме ножки ученицы до сих пор покоятся на члене физрука. Вы не верите своим глазам, но похоже 30 сантиметровый гигант и не собирается опадать!'
            'Разглядывая перемазанные в сперме ножки ученицы и трепыхающийся в неспадающем возбуждении член, вы ощущаете, как предвкушение наслаждения снова охватывает ваше тело.'
            player.say '"Нет, с этим надо заканчивать!" - Вы решительно берётесь за руччку двери и открываете её.'
            $ lastMastur = ptime
            jump mileQwest1_storageIn
        'Войти':
            jump mileQwest1_storageIn

label mileQwest1_storageIn:
    show storage as bg
    show expression 'pic/events/mile_1/10.png' at top as tempPic
    'Войдя Вы видите, что [t.name] опять сажает школьницу на себя.'
    player.say 'Да ты с ума сошёл, кобель! Здесь что по твоему, школа или бордель??? - орёте вы на физрука.'
    '[st2.fname] в панике собирает вещи, и пытается улизнуть.'
    player.say 'Ты кем себя возомнил? Быком осеменителем высшего разряда? - продолжаете вы неиствоствовать.'
    if player.isSperm() != 2:
        show expression getCharImage(t,'dialog') as temp1
        '[t.name] мямлит что то невразумительное, ученица шмыгает за дверь.'
        show expression getCharImage(player,'dialog') as temp1
        player.say 'Какие бабушкины лекарства, что ты мелешь?'
        show expression getCharImage(t,'dialog') as temp1
        '[t.name] в панике объясняет вам, что он ничего не может с собой поделать. Его стояк не прекращается с самого утра, с того самого момента, как он перепутал свои стероиды с бабушкиным лекарством от сердца. Домой в таком состоянии он возвращаться не может, так как там только одна комната и одна бабушка.'
        show expression getCharImage(player,'dialog') as temp1
        player.say 'А какого чёрта ты на ученицу полез? - всё ещё не понимаете вы.'
        show expression getCharImage(t,'dialog') as temp1
        t.say 'Да если бы я сам! Она сама на меня запрыгнула! Вон, спросите у неё сами!'
        'Тут [t.name] замечает, что ученица уже улизнула.'
        t.say 'Вот ведь дрянь маленькая!'
        'Отведя взгляд, вы замечаете, что физрук до сих пор сидит без штанов, а его многосантиметровое достоинство ,подрагивая, смотрит вам прям в лицо.'
        show expression getCharImage(player,'dialog') as temp1
        player.say 'Кажется я знаю, как решить твою проблему с обоюдным удовольствием, - хищно улыбаясь, говорите Вы, облизывая острым язычком губы.'
        show expression 'pic/events/mile_1/11.png' at top as tempPic
        'Несмотря на то, что судя по влажности и температуре между ног у вас там тропические джунгли, вы решаете сначала попробовать на вкус то, что запихнёте в себя позже.'
        'Вы оголяете свои груди и вставляете между ними просто царский пенис. Одно только это действие заставило его выделить приличную порцию эякулята, смазывающего ложбинку в которой уместился член.'
        player.say 'Дааа, таблеточки то непростые, - замечаете вы.'
        t.say 'Нгггг, - стонет в ответ физрук.'
        player.say 'Ты уже готов кончить? Как же ты смог удовлетворить тех девчёнок с такой то скорострельностью???'
        'Не желая терять ни капли спермы из этого монстра, Вы обхватываете его губами, и он спустя секунду орошает вам глотку густым и пахучим веществом.'
        'Улыбаясь, вы поднимаете голову к своему любовнику, как вдруг чувствуете на себе чей то взгляд.'
        hide tempPic
        show expression getCharImage(st2,'dialog') as temp1
        st2.say 'Я смотрю Вы мою игрушку решили отобрать? Могли бы и попросить, я бы дала Вам попользоваться. Ну что, дальше - втроём?'
        '[st2.fname] игриво склонила голову набок и ждёт вашего ответа.'
        'Судорожно сглотнув сперму, вы ощущаете как она пожаром прокатывается по вашему пищеводу, и на вас резко накатывает неукротимое желание продолжить свой род во что бы то не стало.'
        player.say '"Ой-ой. Похоже в семени содержалось довольно много действущего вещества из таблеточек." - в панике проносится у вас в голове, пока вы безуспешно пытаетесь совладать с растущим возбуждением.'
        player.say 'Да что ТЫ СЕБЕ ПОЗВОЛЯЕШЬ! Я против! Да уж лучше я сама...'
        'Очередной приступ скручивает вашу матку, и из киски вырывается тонкая струйка влаги, обильно смазывающая вашу промежность.'
        player.say 'Хотя чёрт с ним, только родителям о проишествии - молчок!'
        show expression getCharImage(player,'dialog') as temp2
        st2.say'Конечно! - радостно восклицает ученица, и вы обе поворачиваетесь к притихшему физруку'
        hide temp1
        hide temp2
    else:
        '[t.name] в панике объясняет вам, что он ничего не может с собой поделать. Его стояк не прекращается с самого утра, с того самого момента, как он перепутал свои стероиды с бабушкиным лекарством от сердца. Домой в таком состоянии он возвращаться не может, так как там только одна комната и одна бабушка. '
        hide tempPic
        'Пока вы заняты этими объяснениями, ученица совершает обходной маневр. Аккуратно подойдя к вам, она вдруг лижет вас в щёку.'
        st2.say 'Мммм, [st3.fname], - мечтательно закатывая глаза шепчет она.'
        player.say 'Что???'
        'Вы с ужасом понимаете, что со всеми этими делами совсем забыли привести себя в порядок.'
        st2.say 'Я просто помогала учителю сбросить напряжение, причём даже без секса как такового. К тому же, и Вы тоже без дела не сидели. Ваши стоны за дверью не слышали разве что в Чикаго. Ну что, может быть продолжим втроём?'
        'Перед вашими глазами пролетают "ученица" в раздевалке, то, что вы увидели в кладовке, ноздри щекотит острый аромат секса. Ваша киска сжимается в сладкой неге от предвкушения того, как её может заполнить до сих пор торчащий между ног физрука предмет.'
        player.say '"А ну его всё к чёрту! Один раз живём!" - пролетает у вас в голове.'
        player.say 'А что, давай, - улыбаетесь вы, - Только родителям - молчок! Договорились?'
        show expression getCharImage(st2,'dialog') as temp1
        show expression getCharImage(player,'dialog') as temp2
        st2.say'Конечно! - радостно восклицает ученица, и вы обе поворачиваетесь к притихшему физруку'
        hide tempPic
        hide temp1
        hide temp2
    show movie
    play movie 'pic/events/mile_1/12.gif.webm' loop
    'Началась бесконечная оргия. Вы прыгали на неунывающем члене физрука, а [st2.fname] уселась ему на лицо. Ваши языки переплетались, и вас трясло от вожделения.'
    play movie 'pic/events/mile_1/13.gif.webm' loop
    'Спустя пару часов и пару оргазмов Вы всё ещё прыгали на его члене. [st2.fname] тоже подустала, но не слазила со своего насеста, постоянно ощущая, как неутомимый язык физрука ласкал её лоно.'
    stop movie
    hide movie
    show expression 'pic/events/mile_1/16.jpg' at top as tempPic
    'Оргазм! Очередной оргазм! Множественный оргазм! Боже, да [t.fname] просто неутомим! Похоже действие этих таблеток так легко не прекратить.'
    show movie
    play movie 'pic/events/mile_1/14.gif.webm' loop
    'Мдаа, Вам уже не 16 лет. Утомившись, вы предоставили инициативу по отсосу напарнице.'
    stop movie
    hide movie
    show expression 'pic/events/mile_1/15.jpg' at top as tempPic
    '[st2.fname] продолжает сосать член, вы нехотя полизываете его. Боже, у вас уже всё болит от этих скачек. Губы опухли, язык не слушается, между ног тоже не всё в порядке. Пора с этим заканчивать.'
    show expression 'pic/events/mile_1/17.jpg' at top as tempPic
    '[st2.fname] в полубессознательном состоянии висит на руках физрука, в то время как вы, вытащив его член из вагины, вгрызаетесь в него зубами.'
    t.say 'AAAAAA, ты что, обезумела? - кричит от боли [t.name], - Зачем ты это сделала???'
    player.say 'Смотри, - показываете вы рукой вниз на опадающий член. Хех, не в стоячем состоянии он выглядит не таким грозным!'
    t.say 'Фух, спасибо, кажется отпускает. Да и возбуждения больше не чувствуется. - радуется физрук'
    player.say 'Твою мать! Ты трахал нас 7 часов, а всё решалось так просто!, - возмущаетесь Вы -  [st2.fname], а ты что об этом всём думаешь?'
    st2.say 'Ммммннннмммннндаааа, - в полубессознательном состоянии вырвалось у неё.'
    show expression 'pic/events/mile_1/18.jpg' at top as tempPic
    'Спустя некоторое время, попив чай, отдонув и приведя себя в порядок, вы раздаёте указания.'
    player.say 'Значит так, - начинаете вы, - [t.fname], ты доставляешь ученицу домой в целости и сохранности. Надеюсь мы сбили твой стояк. Если нет - сбивай его хоть кирпичём. Понятно?'
    t.say 'Угу, - мямлит поникший физрук.'
    player.say '[st2.fname], ты ведёшь себя нормально, сегодня был обычный день, устала ты потому, что сегодня был кросс на 5 км последним уроком. Уяснила?'
    st2.say ' Ага! - радостно восклицает она, - а мы ещё как нибудь повторим?'
    player.say 'Может быть, радость моя, может быть, - ласково говорите вы.'
    player.say 'И да, [t.name], теперь ты будешь голосовать за любые мои предложения на педсовете. Ясненько?'
    t.say 'А как же иначе! Может быть сразу за секс на физкультуре проголосуем?'
    'Лицо физрука принимает мечтательное выражение.'
    player.say 'Но но! Разогнался. Для начала хотя бы форму этим, - Вы киваете на ученицу, - поменяем.'
    python:
        mile_quest_1 = 1
        t.incLoy(20)
        t.incCorr(20)
        t.incLust(-100)
        t.incFun(10)
        st2.incLoy(20)
        st2.incCorr(20)
        st2.incLust(-100)
        st2.incFun(10)
        player.incCorr(20)
        player.incLust(-100)
        player.incFun(10)
        player.incEnergy(-700)
        changetime(8*60)
        player.coverSperm('лицо','рот','попа','вагина','ноги')
        move('loc_home')

label ahmed_sex_selector:
    menu:
        'Вы видите, как трусы Ахмеда призывно оттопыриваются, когда вы подходите ближе.'
        'Удовлетворить':
            $ tryEvent('loc_ahmedFootjob')
        'Заняться сексом':
            $ tryEvent('loc_ahmedSex')
        'Отсососать':
            $ tryEvent('loc_ahmedSuck')

label event_loc_ahmedFootjob_0_1:
    $ mile_quest_1 = 2
    show expression 'pic/events/sex/ahmed/footjob1.jpg' at top as tempPic
    player.say 'Ну что же вы, [mustangovich.name]! - сказали вы, аккуратно трогая пальчиком выпирающее достоинство физрука.'
    player.say 'Вы мне так всех учениц распугаете! Признавайтесь, опять бабушкиных таблеточек от сердца бахнули? - ваша ладошка обхватывает толстый ствол члена сквозь ткань плавок.'
    mustangovich.say 'Я, ну оно так, как то само... - оправдывается [mustangovich.fname].'
    player.say 'Надо с этим что то сделать, не так ли? - заходите Вы за физрука, проводя рукой по его мускулистой груди.'
    mustangovich.say 'Это, ну наверное да...'
    'Вы оказываетесь у него за спиной, и небольшим ударом под коленку, укладываете физрука на себя. Ваши ножки плотно обхватывают крепкое мужское тело и скользят по нему в направлении оттопыренных плавок.'
    player.say 'Сейчас мы займёмся вашим хозяйством! - с этими словами вы оттянули большими пальцами резинку трусов, заставив 30 сантиметровый член выпрыгнуть наружу.'
    'Ваши ступни уверенно обхватили головку, и двигаясь вниз, сняли с неё крайнюю плоть.'
    player.say 'Какой же Вы негодник, [mustangovich.name]! Ну нельзя же себя до такого доводить! - подразнили вы застонавшего физрука, разглядывая набухший венами член.'
    'Однако делу время, а потехе час, и ваши ножки пришли в движение, уверенно массируя здоровенную палку учителя. [mustangovich.fname] всеми силами старался Вам помочь, двигаясь навстречу бёдрами и трахая ваши ступни. Учитывая его возбуждение, скоро он брызнул фонтаном спермы, забрызгивая себя и ваши ножки.'
    player.say 'Так то получше будет! - чмокнули Вы удовлетворённого мужчину в щёку, и начали подниматься.'
    'Воля физрука уменьшилась.'
    python:
        mustangovich.sayCount -= 5
        player.incLust(10)
        player.incCorr(4)
        mustangovich.incWill(-5)
        mustangovich.incCorr(5)
        player.coverSperm('ноги')
        changetime(10)
        move(curloc)

label event_loc_ahmedFootjob_0_2:
    $ mile_quest_1 = 2
    show expression 'pic/events/sex/ahmed/footjob2.jpg' at top as tempPic
    player.say 'Это что ещё такое? - оттягивая ткань трусов пальчиком, уставились Вы на приведённое в боевую готовность оружие массового поражения.'
    mustangovich.say 'Я, тут, это у меня, как то само, - разводит руками [mustangovich.fname].'
    player.say 'Само только кошки родятся! Фууу, вы вообще мылись сегодня, [mustangovich.name]? - Вы брезгливо убираете свой пальчик, заставляя резинку громко шлёпнуть по мускулистому животу физрука.'
    mustangovich.say 'Ну как бы тренировки, я пока не успел...'
    player.say 'Нет, в таком виде я Вас в душ отпустить не могу, случайное движение и мне там плитку разобьёте, садитесь! - волевым движением вы усаживаете физрука на пол.'
    'В очередной раз наморщив носик от исходящего от мужчины амбре, вы спустили с него плавки, и ухватили член своими ножками.'
    player.say 'И даже не надейся, что я дотронусь до этого руками! - предупредили вы было напрягшегося физрука, и начали двигать своими лапками, ощущая между ними горячую твёрдость. Член приятно скользил между ваших ступней, вызывая приливы желания внизу живота. [mustangovich.fname] был черезвычайно перевозбуждён и вскоре Вы ощутили предоргазменное трепетание.'
    player.say 'Ну давай уже, не томи, спускай!'
    'Вы сжали член покрепче, и ускорили движения. Физрук схватил ваши ноги своими лапищами и начал резко загонять свой член между ними, орошая пальчики своей спермой.'
    player.say 'А теперь можно и в душ! - хихикнули вы поднимаясь.'
    python:
        mustangovich.sayCount -= 5
        player.incLust(10)
        player.incCorr(4)
        mustangovich.incWill(-5)
        mustangovich.incCorr(5)
        player.coverSperm('ноги')
        changetime(10)
        move(curloc)

label event_loc_ahmedSex_0_1:
    $ player.incLust(30)
    player.say '"Чёрт, как же хочется повторить!"'
    if len(player.getCover()) != 0:
        'Вы скидываете с себя одежду, и подзываете физрука к себе.'
    else:
        'Ложась на спину и раздвигая ноги подзываете вы к себе физрука.'
    show expression 'pic/events/sex/ahmed/sex1.png' at top as tempPic
    player.say 'О, да! - выдыхаете Вы когда ощущаете как что то огромное заполняет вас изнутри.'
    'Ощутив упругое сопротивление вашего влагалища, [mustangovich.fname] начинает двигаться, доставая до матки и пытаясь продавить свой член дальше.'
    'Вы стонете и мечетесь на полу, пока физрук насаживает вас на кол по всем заветам графа Дракулы. Его член становится всё больше, видимо приятная узость киски тоже нехило его заводит. Хотя для такого причиндала и ведро покажется узкой щёлкой. Яростные движения продолжаются всего лишь пару десятков секунд, но вы уже близки к оргазму. Впрочем [mustangovich.fname] похоже тоже.'
    mustangovich.say 'Я счас кончу, - захрипел физрук, останавливая свои движения глубоко внутри вас.'
    if player.getLust() > 70:
        player.say 'В меня, кончай в меня! - стиснули вы своим влагалищем заполнявший вас ствол, и содрогаясь, ощутили как он запульсировал и начал наполнять вашу киску спермой.'
    else:
        player.say 'Только не в меня! - Вы упёрлись ногами в физрука, и вытащили его из своего влагалища.'
        'На ваших глазах, член запульсировал и начал заливать Ваше тело и ноги спермой. Когда первые горячие капли упали на Ваш живот, Вы ощутили что ваша киска начала сокращаться, и из за отсутствия в ней члена, оргазм получился смазанным.'
    'Вы оба встали привели себя в относительный порядок.'
    if player.getLust() > 70:
        python:
            player.coverSperm('вагина')
            player.setLust(0)
            mustangovich.setLust(0)
            player.incCorr(2)
            mustangovich.incCorr(5)
            mustangovich.incWill(10)
        'Воля физрука увеличилась.'
    else:
        python:
            player.coverSperm('грудь','ноги')
            player.setLust(0)
            mustangovich.setLust(0)
            player.incCorr(2)
            mustangovich.incCorr(5)
            mustangovich.incWill(-10)
        'Воля физрука уменьшилась.'
    $ changetime(15)
    $ hadSex(player, mustangovich)
    $ move(curloc)

label event_loc_ahmedSex_0_2:
    $ player.incLust(30)
    player.say 'Чёрт, как же я тебя хочу!'
    show expression 'pic/events/sex/ahmed/sex2.png' at right as tempPic
    if len(player.getCover()) != 0:
        'Вы толкаете физрука и, усаживаясь сверху, направляете его член в себя.'
    else:
        'Вы скидываете с себя одежду и, усаживаясь сверху, направляете его член в себя.'
    player.say 'Класс! - шепчете вы, когда член наполняет вашу вагину. Вы начинаете быстро скакать на физруке, лаская его разбухшую головку стенками своего влагалища.'
    mustangovich.say 'Я так долго не продержусь! - [mustangovich.fname] кладёт свои руки вам на талию, почти полностью обхватывая её своими лапищами.'
    player.say 'И... Не... На...До... - по слогам выкрикиваете вы, ритмично тараня членом свою матку.'
    mustangovich.say 'Нггг, - кончаю!!! - физрук резко подался вам навстречу, вызывая лёгкую боль своим размером.'
    if player.getLust() > 70:
        player.say 'В меня, кончай в меня! - стиснули вы своим влагалищем заполнявший его ствол, и, содрогаясь, ощутили как он запульсировал и начал наполнять вашу киску спермой.'
    else:
        player.say 'Поняв, что вас сейчас наполнят спермой как последнюю шлюшку, вы быстро соскочили с члена, и тугие струи спермы ударили по вашим ногам.'
    'Вы оба встали привели себя в относительный порядок.'
    if player.getLust() > 70:
        python:
            player.coverSperm('вагина')
            player.setLust(0)
            mustangovich.setLust(0)
            player.incCorr(2)
            mustangovich.incCorr(5)
            mustangovich.incWill(10)
        'Воля физрука увеличилась.'
    else:
        python:
            player.coverSperm('ноги')
            player.setLust(0)
            mustangovich.setLust(0)
            player.incCorr(2)
            mustangovich.incCorr(5)
            mustangovich.incWill(-10)
        'Воля физрука уменьшилась.'
    $ changetime(15)
    $ hadSex(player, mustangovich)
    $ move(curloc)

label event_loc_ahmedSex_0_3:
    show expression getCharImage(mustangovich,'dialog') as temp1
    show expression getCharImage(player,'dialog') as temp2
    player.say 'Кажется тебе нужна небольшая помощь с этим? - вы потыкали пальчиком в оттопырившиеся трусы.'
    mustangovich.say 'Ну да... Не помешало бы... - поглаживая свой орган проговорил [mustangovich.fname].'
    player.say 'ВСПЫШКА СЛЕВА!'
    hide temp1
    hide temp2
    show expression 'pic/events/sex/ahmed/sex3.png' at top as tempPic
    'Физрук, как любой человек прошедший армию принял единственно верное решение - сначала грохнулся на пол и только потом подумал, что он делает. Не дав ему опомниться, вы быстрым движением достали его член и направили себе в киску.'
    '"Хлюп" - и член уже погрузился почти на всю длину, вынудив вас застонать от удовольствия.'
    player.say 'Как же хорошо! - вскрикнули вы, скользя вдоль достойного достоинства физрука.'
    mustangovich.say '[player.fname], вы лучшая! - прошептал физрук, и начал двигать своими бёдрами, облегчая вам задачу. Вскоре он полностью захватил инициативу, и ваше тело лишь безвольно подпрыгивало на его бёдрах и пенисе.'
    player.say 'Ммм... А... Умм... - стонали вы, ощущая быстрые движения внутри себя.'
    mustangovich.say 'Да, да, ДА! - насаживал вас физрук, ухватив своими лапищами ваши груди, - Кончаю, кончаю!'
    'Сквозь пелену удовольствия, вы ощутили, как ваша киска начинает наполняться чем то горячим. Струи спермы, ударившие в вашем влагалище, были последней каплей, и громко закричав, вы начали кончать. Вы очнулись спустя минуту, подрагивая и всхлипывая на груди мужчины.'
    python:
        player.coverSperm('вагина')
        player.setLust(0)
        mustangovich.setLust(0)
        player.incCorr(2)
        mustangovich.incCorr(5)
        mustangovich.incWill(10)
    'Воля физрука увеличилась.'
    $ changetime(15)
    $ hadSex(player, mustangovich)
    $ move(curloc)

label event_loc_ahmedSex_0_4:
    show expression getCharImage(mustangovich,'dialog') as temp1
    show expression getCharImage(player,'dialog') as temp2
    player.say '[mustangovich.name], не желаете ли избавиться от некоторого стеснения в трусах? - потянули вы резинку его трусов вниз, обнажая устрашающий член.'
    mustangovich.say 'Я как бы никогда! - радостно ответил порозовевший физрук и ловко выпрыгнул из трусов'
    player.say 'Экий торопыжка! - погрозили пальчиком физруку и слились с ним губами, заваливая его на спину.'
    hide temp1
    hide temp2
    show expression 'pic/events/sex/ahmed/sex4.png' at top as tempPic
    'В вашу задницу отчётливо упёрся его разбухший орган, вызывая прилив желания. Не долго думая, вы ввели его в свою киску, шумно выдохнув воздух, вытесняемый заполняющим киску объёмом. По крайней мере так вам показалось. Вы начали медленно двигать тазом, наслаждаясь как пенис приятно подрагивает в глубине влагалища у самой матки.'
    player.say 'Это волшебно! - вы вновь впились губами в физрука, наращивая темп.'
    'Спустя пару минут вы уже полубезумно скакали на его достоинстве, используя его в качестве секс игрушки. Ваши груди летали вверх и вниз, вслед за вашими движениями, а попа громко шлёпала по бёдрам мужчины.'
    player.say 'Да, да, ДА! - ваши волосы развевались и киска сильно сжалась в оргазме, полностью ощущая фактуру и плотность заполнявшего вас члена. Не успели вы кончить, как ощутили яростные движения начинавшего кончать физрука.'
    player.say 'Но но! - вы быстро соскочили с физрука и его собственная струя спермы ударила ему прямо в лицо.'
    'Хихикнув, вы начали приводить себя в порядок.'
    python:
        player.setLust(0)
        mustangovich.setLust(0)
        player.incCorr(2)
        mustangovich.incCorr(5)
        mustangovich.incWill(-10)
    'Воля физрука уменьшилась.'
    $ changetime(15)
    $ hadSex(player, mustangovich)
    $ move(curloc)

label event_loc_ahmedSex_0_5:
    player.say '[mustangovich.fname], мне кажется я знаю, куда ты можешь пристроить эту штуку! - показали вы на оттопыренные трусы и отвернулись к стене, призывно выпятив попу.'
    show expression 'pic/events/sex/ahmed/sex5.png' at left as tempPic
    'Физрук не заставил себя упрашивать два раза. Проведя по вашим губкам головкой, физрук без прелюдий вторгся в горячее лоно, заставляя вас встать на носочки. Схватив вашу за руку, он всадил свой член ещё глубже, заставив попой прижаться к его животу.'
    player.say 'Оооох, - только и смогли выдохнуть вы, когда [mustangovich.fname] всё таки начал неторопливые движения.'
    'Вам казалось, что киска сейчас буквально порвётся, но эта боль была сладка, и вскоре исчезла, оставив приятное чувство полностью заполненного влагалища.'
    mustangovich.say 'Вот так вот, вот так, - приговаривал учитель, двигаясь в глубине вашей киски, - Вот, ещё чуть чуть, ДА!'
    'Ваша матка чуть не выпрыгнула во время вашего одновременного оргазма. Как только горячее семя начало заполнять пульсирующие влагалище, вы чуть не потеряли сознание от удовольствия, повизгивая и подрагивая на держащем вас на весу члене.'
    'Немного отойдя, вы начали одеваться.'
    python:
        player.coverSperm('вагина')
        player.setLust(0)
        mustangovich.setLust(0)
        player.incCorr(2)
        mustangovich.incCorr(5)
        mustangovich.incWill(10)
    'Воля физрука увеличилась.'
    $ changetime(15)
    $ hadSex(player, mustangovich)
    $ move(curloc)

label event_loc_ahmedSuck_0_1:
    show movie
    play movie "pic/events/sex/ahmed/suck1.gif.webm" loop
    'Не говоря ни слова, вы медленно опустились перед удивлённым физруком на колени, и приспустив его плавки, взяли огромную елду в рот. Разумеется вся она не помещалась, но вы решили удовлетвориться обсасыванием его головки. Проведя по ней язычком, вы принялись ритмично двигать головой, крепко сжимая ствол губами.'
    'В ответ физрук застонал, наслаждаясь ощущаниями горячих губ на его члене. Долго эту пытку он выдержать не мог, и вскоре в вашу глотку выплеснулась первая струя спермы, вторая, третья. Вы бросили считать на этом моменте и просто дождались пока рот не наполнится горьковатой субстанцией.'
    stop movie
    hide movie
    python:
        player.coverSperm('рот')
        player.incLust(10)
        mustangovich.setLust(0)
        player.incCorr(2)
        mustangovich.incCorr(2)
        mustangovich.incWill(10)
    'Воля физрука увеличилась.'
    $ changetime(15)
    $ move(curloc)

label event_loc_ahmedSuck_0_2:
    show expression 'pic/events/sex/ahmed/suck2.png' at top as tempPic
    'Покрывая поцелуями тело физрука, вы опускались всё ниже, пока наконец не дошли до самой интересной части тела молодого мужчины.'
    player.say 'М-м-м, - замычали вы, засунув сразу половину члена в свой рот и ощущая как он упёрся в вашу горло.'
    mustangovich.say 'Ка-а-айф! - протянул физрук, откинув голову.'
    'Вы продолжали обрабатывать его член, зажав основание между грудей. Возникло желание попробовать запихнуть его ещё глубже, чтобы дотянуться языком до яиц, но вас остановили две вещи. Во первых ваша глотка была отнюдь не бездонной, и не была предназначена для того, чтобы в неё запихивать брёвна и прочие пиломатериалы, а во вторых, всё место вдруг неожиданно стало занято густой спермой, брызнувшей из члена учителя.'
    player.say 'Пф-ф-ф, кхе, кху, - закашлялись вы, выплёвывая всё наружу. Часть капель попала на вашу грудь. Поднимаясь, вы с укоризной смотрите на изображающего расскаяние физрука.'
    python:
        player.coverSperm('рот')
        player.incLust(10)
        mustangovich.setLust(0)
        player.incCorr(2)
        mustangovich.incCorr(2)
        mustangovich.incWill(10)
    'Воля физрука увеличилась.'
    $ changetime(15)
    $ move(curloc)

label event_loc_ahmedSuck_0_3:
    show expression 'pic/events/sex/ahmed/suck3.jpg' at left as tempPic
    'Вы опутились перед физруком на колени, и не объясняя ничего, достали толстый член из его плавок. Физрук было дёрнулся, чтобы немедля заправить его вам в рот, но вы цыкнули на него, и принялись медленно водить языком вдоль его ствола, то заигрывая с уздечкой, то посасывая волосатые яйца.'
    'Вы не давали мужчине не минуты продыху, но и не ласкали его слишком сильно. Как раз так, чтобы он медленно приближался к пику возбуждения.'
    'Через 15 минут Ахмед всё таки не выдержал, и несмотря на то, что вы не трогали головку, начал спускать на лицо и на руки. Вы дождались финала этой мощной эякуляции, и тщательно облизали член, стараясь не пропустить ни одной драгоценной капли.'
    python:
        player.coverSperm('рот')
        player.incLust(10)
        mustangovich.setLust(0)
        player.incCorr(2)
        mustangovich.incCorr(2)
        mustangovich.incWill(10)
    'Воля физрука увеличилась.'
    $ changetime(15)
    $ move(curloc)
