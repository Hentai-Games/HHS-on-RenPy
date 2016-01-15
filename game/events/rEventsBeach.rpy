label event_loc_beach_0_1:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/beach/no1.jpg' at top as tempPic
    'Вы видите, как на пляже отдыхают [st2.fname] и его подружка [st1.fname]. Какие же симпатичные у неё ножки и пальчики!'
    if player.getCorr() > 60:
        show expression 'pic/locations/beach/no1a.jpg' at top as tempPic
        player.say '"Так и представляю, как эти пальчики выгибаются в экстазе, когда [st2.fname] загоняет ей в задницу свой здоровенный член!"'
        player.say '"Да-а-а!"'
        'Вы мечтательно закатываете глаза, смакуя эту картину.'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_beach_0_2:
    show beach
    python:
        st1 = getChar('female','lustmax')
    show expression 'pic/locations/beach/no2.jpg' at top as tempPic
    'Вы заметили, что [st1.fname] ведёт себя несколько странно. Вы не уверены, но, кажется, она очень сильно возбуждена. Надо взять это на заметку!'
    $ move(curloc)
    
label event_loc_beach_0_3:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/no3.jpg' at top as tempPic
    'Нет, Вы посмотрите как проказница [st1.fname] играет с мячом! Кстати купальника такого фасона я никогда не видела!'
    if player.getCorr() > 40:
        player.say '"Интересно, позирует ли она перед старшим братиком в своём купальнике?"'
        show expression 'pic/locations/beach/no3a.jpg' at top as tempPic
        player.say '"А может быть и вообще без него?"'
        player.say 'Вы мечтательно закрываете глаза, представляя, как [st1.fname] задирает свой купальник, показывая братику влажную киску...'
    $ move(curloc)
    
label event_loc_beach_5_4:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
    show expression 'pic/locations/beach/no4.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Девчёнки [st1.fname], [st2.fname] и [st3.fname] позируют перед фотографом. Ээх, мне бы толику их веселья!'
    $ setFun(3,5)
    $ move(curloc)
    
label event_loc_beach_10_5:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('male','lustmax')
        st3 = getChar('female')
    show expression 'pic/locations/beach/no5.jpg' at top as tempPic
    '[st1.fname] чего то испугалась, и жмётся к своей подружке. Может быть на пляже водятся скорпионы? Или просто кто то решил пощеголять без плавок? Вы оборачиваетесь, и видите, как [st2.fname] что то прячет в трусы. Судя по довольному виду, [st3.fname] ничуть не смущена.'
    $ setFun(3,5)
    $ move(curloc)

label event_loc_beach_0_6:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('male','lustmax')
    show expression 'pic/locations/beach/no6.jpg' at top as tempPic
    'Вот ведь [st1.fname] умничка! Пока все предаются сладкой неге, она осваивает новые виды водного спорта! Так держать!'
    if player.getCorr() > 50:
        player.say '"Хотя в мире есть столько видов спорта!"'
        show expression 'pic/locations/beach/no6a.jpg' at top as tempPic
        player.say '"Могла бы и занятся более приятным водным спортом..."'
        player.say '"Вон, тот же [st2.name] стоит с оттопыренными плавками! Он бы наверняка составил ей компанию на горячем, прибойном песочке!"'
        'Вы прикрыли глаза, отчётливо представляя, как [st2.name] своим возбуждённым членом таранит беззащитное лоно ученицы.'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_beach_10_7:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/beach/no7.jpg' at top as tempPic
    'Хехе, [st1.fname] и [st2.fname] нацепили кошачьи ушки и пытаются поиграть с мальчишками в войнушку водяными пистолетами. Интересно, куда у первой хвост то крепится?'
    if player.getCorr() > 50:
        show expression 'pic/locations/beach/no7a.jpg':
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        'Вы прикрыли глаза, и представили, как маленькая развратница крепит свой хвостик в попке.'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_beach_0_8:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/no8.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] сладко подтягивается, пока её бойфренд ушёл ещё за другим коктейлем.'
    $ move(curloc)
    
label event_loc_beach_0_9:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/no9.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Девчёнки решили переодеться, не стоя в очереди в раздевалку. Увидев, что их заметили, [st1.fname] показывает вам язык! Немножко жаль, что вы не застали их пораньше.'
    $ move(curloc)
    
label event_loc_beach_0_10:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/no10.jpg' at top as tempPic
    '[st1.fname] пришла сегодня с младшей сестрой. Судя по её недовольному виду, она ожидала другого времяпровождения.'
    if player.getCorr() > 50:
        show expression 'pic/locations/beach/no10a.png' at top as tempPic
        player.say '"Да, наверняка она бы лучше отдалась трём горячим парням из параллельного класса прямо в раздевалке!"'
        player.say '"Обсасывала их горячие члены, ласкала юные тела, тёрлась бы киской об их торчащие естества!"'
        player.say '"ДА! Определённо это было бы более приятным времяпровождением!"'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_beach_5_11:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('female')
    show expression 'pic/locations/beach/no11.jpg' at top as tempPic
    '[st1.fname], [st2.fname], [st3.fname] и [st4.fname] играют в какую то игру на пляже. Но вот [st4.fname] как то слишком нежно приобнимает свою подружку.'
    if player.getCorr() > 40:
        show expression 'pic/locations/beach/no11a.jpg' at top as tempPic
        player.say '"Наверняка [st4.fname] подала бы ей дружескую руку помощи в раздевалке, на случай, если [st3.fname] переломает свои!"'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_beach_0_12:
    show beach
    python:
        st1 = getChar('futa')
        player.incLust(5)
    show expression 'pic/locations/beach/no12.jpg' at top as tempPic
    'Гм, [st1.fname] раскинулась в шезлонге и отдыхает. Вы невольно бросаете взгляд на её юбочку, и видите, что лёгкая ткань буквально облегает её совсем не женский и совсем не детский орган. Вы чувствуете небольшое возбуждение от увиденного.'  
    $ move(curloc)
    
label event_loc_beach_8_14:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/no14.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] сегодня решила надеть свой школьный купальный костюм. Надо бы ей намекнуть, что он ей уже немного маловат, и слишком сильно обтягивает её попку. Хотя может быть именно этого она и добивается?'
    $ setLust(3,15)
    $ move(curloc)
    
label event_loc_beach_0_15:
    show beach
    show expression 'pic/locations/beach/no15.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Ученицы весело играет с водяными пистолетами. А кто то прыгает со скалы в воду, врезаясь в неё с громким плюхом. Будем надеятся, что спасатели не дремлют! Не хотелось бы потерять своих учеников вот так глупо.'
    $ setFun(5,10)
    $ move(curloc)
    
label event_loc_beach_0_16:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/no16.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] фотографируется на пляже. Ей немного не удобно от того, что пришлось надеть свой школьный купальник, но другого, судя по всему, у неё нет.'
    $ move(curloc)
    
label event_loc_beach_0_17:
    show beach
    show expression 'pic/locations/beach/no17.jpg' at top as tempPic
    '[danokova.name] приветствует вас, и приглашает позагорать вместе. Вы отвечаете, что ей пора бы уже прекратить принимать солнечные ванны, судя по отчётливому красноватому оттенку кожи. Учительница смотрит на себя, ойкает и убегает.'
    $ danokova.incLoy(5)
    $ move(curloc)
    
label event_loc_beach_0_18:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/no18.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    player.say '"У матросов нет вопросов, у матросов нет проблем"'
    'Всплыли у Вас в голове слова старой песенки, когда мимо прошла [st1.fname] в своём новом купальнике.'
    $ move(curloc)
    
label event_loc_beach_0_19:
    show beach
    python:
        setFun(3,10)
    show expression 'pic/locations/beach/no19.jpg' at top as tempPic
    'Пока одни строят песочные корабли, другие решили покататься на волнах. Тоже неплохое развлечение, и для фигуры полезно.'
    $ move(curloc)
    
label event_loc_beach_5_20:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/no20.jpg' at top as tempPic
    'Увидя Вас, [st1.fname] немного застеснялась из за того, что одела своё новенькое бикини.'
    menu:
        'Сказать, что это нормально, носить бикини':
            'Вы улыбнулись, и как бы невзначай заметили, что и сами иногда не против надеть бикини, что в ношении такого купальника нет ничего зазорного.'
            'Несмотря на всю убедительность Ваших слов, [st1.fname] засмущалась ещё сильнее.'
            $ st1.incCorr(-5)
        'Сделать вид, что не обратили внимания':
            'Вы делаете вид, что ничего особенного не происходит. [st1.fname] явно стала чувствовать себя более раскованно.'
            $ st1.incCorr(5)
    $ move(curloc)
    
label event_loc_beach_5_21:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/beach/no21.jpg' at top as tempPic
    'Случайно проходя, вы обратили внимание на то, что [st1.fname] и [st2.fname] зачем то прячутся за полотенцем. И услышали злобный шопот:'
    st1.say 'Блин, вон [player.name] идёт, надо было дождаться очереди в раздевалку!'
    menu:
        'Подойти к ним':
            show expression 'pic/locations/beach/no21a.jpg' at top as tempPic
            'Вы подошли к ученицам, и как по заказу, порыв ветра вырвал полотенце из рук девочки.'
            st1.say '[player.name]! Это вовсе не то, о чём вы подумали! - начинает причитать ученица, - мы просто переодевались!'
            'Видя, что [st1.fname] говорит правду, вы, окинув взглядом прелестные тела смущённых девушек, вернули полотенце и пошли дальше.'
            $ st1.incCorr(-2)
            $ st2.incCorr(-2)
            $ st1.incLoy(-5)
            $ st2.incLoy(-5)
        'Сделать вид, что не обратили внимания':
            'Вы делаете вид, что ничего не слышали, и уходите. Голоса сзади успокаиваются. Наверное даже хорошо, что вы не стали черезчур смущать девушек. В следующий раз они будут более охотно переодеваться вне раздевалок.'
            $ st1.incCorr(2)
            $ st2.incCorr(2)
            $ st1.incLoy(5)
            $ st2.incLoy(5)
    $ move(curloc)
    
label event_loc_beach_5_22:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/no22.jpg' at top as tempPic
    '[st1.fname] фотографируется у моря. Кстати у неё неплохая грудь в этом купальнике!'
    menu:
        'Стоять и смотреть':
            'Вы досмотрели фото-сессию до конца, но ничего интересного не произошло. Мда, могли бы и лучше провести время, хотя грудь всё таки ничего!'
            $ st1.incCorr(1)
        'Уйти':
            'Вам не особо интересна эта фото-сессия, и Вы уходите. Хотя уходя вы услышали вскрик, и дружный хохот.'
            show expression 'pic/locations/beach/no22a.jpg' at top as tempPic
            'Обернувшись, причина веселья стала понятна. Мда, с неплохой грудью вы конечно немного переборщили. Тут надо бочку капусты слопать, чтобы что то исправить!'
            $ setFun(5,15)
    $ move(curloc)
    
label event_loc_beach_5_23:
    show beach
    python:
        st1 = getChar('female')
        st1.incRep(5)
    show expression 'pic/locations/beach/no23.jpg' at top as tempPic
    'Вам встретилась мама одной из учениц. Вы немного с ней поболтали, немного улучшив отношение к себе.'
    $ move(curloc)
    
label event_loc_beach_0_24:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/no24.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] устала, или её просто разморило на солнышке. Вы немного полюбовались на спящую девочку, и пошли дальше.'
    $ move(curloc)
    
label event_loc_beach_0_25:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLoy(5)
        st2.incLoy(5)
    show expression 'pic/locations/beach/no25.jpg' at top as tempPic
    player.say 'Ух ты!'
    'Вы улыбнулись, когда увидели, что [st1.fname] и [st2.fname] решили устроиться отдыхать рядом с вами.'
    $ move(curloc)
    
label event_loc_beach_15_1:
    show beach
    python:
        st1 = getChar('futa')
        player.incLust(10)
        st1.incCorr(1)
    show expression 'pic/locations/beach/lo1.jpg' at top as tempPic
    'Гм, [st1.fname] раскинулась в шезлонге и отдыхает. Вы невольно бросаете взгляд на неё, и видите, что её бикини лишь подчёркивает её достоинства. Вы чувствуете небольшое возбуждение от увиденного.'
    menu:
        'Полюбоваться ещё немного':
            show expression 'pic/locations/beach/lo1a.jpg' at top as tempPic
            'Заметив ваше пристальное внимание, [st1.fname] начала возбуждаться, и её встающий член довольно сильно натянул и так мало что скрывающие трусики.'
            'К сожалению Ваше внимание заметила не только девушка, и вы потеряли немного репутации.'
            $ setRep(5,-1)
            $ player.incCorr(2)
        'Уйти':
            'Вы делаете вид, что что ничего не заметили, и идёте дальше по своим делам.'
    $ move(curloc)
    
label event_loc_beach_15_2:
    show beach
    python:
        st1 = getChar('female')
        player.incLust(5)
    show expression 'pic/locations/beach/lo2.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] судя по всему совсем запарилась на жаре, и приспустила трусики, попивая холодную колу. И как ей только не стыдно? Хотя кроме вас её никто и не замечает.'
    $ move(curloc)
    
label event_loc_beach_0_kup1:
    show beach
    python:
        st1 = kupruvna
        if kupruvna.getCorr() < 30:
            skipEvent()
    show expression 'pic/locations/beach/lo3.jpg' at top as tempPic
    '[st1.name] просит вас намазать её спину кремом от загара.'
    menu:
        'Намазать':
            'Вы неспешно намазали спину учительницы, немного захватив даже её груди. Потом вы немного посидели и поболтали. Ваши отношения улучшились. Хотя многие родители видели, как тщательно вы ласкали свою сотрудницу, что вряд ли сослужит вам хорошую службу.'
            $ setRep(5,-5)
            $ st1.incLoy(10)
            $ st1.incCorr(5)
        'Отказаться':
            'Отказываетесь, и указываете учительнице на то, что загорать топлесс - слишком вызывающе для преподавателя. [st1.name] смущается, и одевает свой лифчик от купальника. Кстати ваш довольно гневный монолог услышали многие родители, что положительно скажется на вашей репутации.'
            $ setRep(5,5)
            $ st1.incLoy(-10)
            $ st1.incCorr(-5)
    $ move(curloc)
    
label event_loc_beach_20_4:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/lo4.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Вы идёте в дальний конец пляжа, и видите, что [st1.fname] снимается на фоне моря в своём новом бикини. Немолодой уже фотограф просит девушку раздеться, для "большей экспрессии и артистичности снимка".'
    menu:
        'Остановить девушку и закончить фото-сессию':
            'Вы подходите к фотографу, и со словами: "А ну пошёл отсюда, старый извращенец!", прогоняете его. [st1.fname] смотрит на вас с недоумением и обидой. Похоже она всерьёз собиралась раздеться перед этим старичком.'
            $ st1.incLoy(-10)
            $ setRep(2,5)
        'Стоять и смотреть':
            show expression 'pic/locations/beach/lo4a.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            'Вы видите, как [st1.fname] скидывает с себя своё бикини и усаживается в ту же позу.'
            'Фотограф крутиться вокруг неё, стараясь сфотографировать самые интимные места. Удивительно, насколько неплохие груди она прятала под своим бикини! Вы чувствуете нарастающее возбуждение.'
            $ st1.incCorr(5)
            $ player.incLust(10)
            if st1.getCorr() > 50:
                show expression 'pic/locations/beach/lo4b.png' at top as tempPic
                'Не успели вы моргнуть и глазом, как перевозбуждённая от фото-сессии нимфа стягивает с фотографа штаны и с громким стоном осёдлывает возбуждённого старичка.'
                'Несмотря на то, что считается, мол ранняя эякуляция проблема молодости, старость похоже тоже подвержена этой болезни. Так или иначе, не успела [st1.fname] начать двигаться, как её лоно оказалось заполнено густой спермой.'
                'Впрочем, непохоже на то, что ваша ученица расстроилась, так как её киска начала сокращаться в унисон с пульсирующим внутри членом, и протяжный крик оргазма огласил окрестности.'
                player.say '"Надеюсь она от него не залетела..."'
                $ st1.incCorr(5)
                $ player.incLust(10)
    $ move(curloc)
    
label event_loc_beach_15_5:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        player.incLust(10)
        incLust(5,10)
    show expression 'pic/locations/beach/lo5.jpg' at top as tempPic
    '[st1.fname] тщательно намазывает свою подругу кремом от загара.'
    player.say '"Я бы даже сказала через чур тщательно, потому что [st2.fname] уже начинает постанывать от прикосновений, которые то теребят её соски, то опускаются вниз, и через тонкую ткань купальника ласкают там что то."'
    $ move(curloc)
    
label event_loc_beach_20_6:
    show beach
    python:
        st1 = getChar('female')
        setLust(10,5)
    show expression 'pic/locations/beach/lo6.jpg' at top as tempPic
    'Проходя мимо шезлонгов, вы заметили, что [st1.fname] загорает топлесс.'
    menu:
        'Сделать ей замечание':
            'Вы подходите к ученице, и просите её накинуть лифчик от купальника. [st1.fname] смущается, и выполняет ваше указание. Другие отдыхающие с одобрением смотрят на вас.'
            $ setRep(5,1)
            $ st1.incCorr(-5)
            $ st1.incLoy(-5)
        'Не обращать внимания':
            'Вы решаете не обращать внимания на подобные выходки. В самом деле, ваши подопечные уже почти взрослые люди, и только им решать, как себя вести.'
    $ move(curloc)
    
label event_loc_beach_0_biss1:
    show beach
    python:
        st1 = bissektrisovna
        if st1.getCorr() < 30:
            skipEvent()
    show expression 'pic/locations/beach/lo7.jpg' at top as tempPic
    'Гуляя по пляжу, Вы видите, как [st1.name] идёт купаться в очень откровенном наряде.'
    menu:
        'Сделать ей замечание':
            'Вы подходите к учительнице, и просите её либо переодеться во что нибудь подобающее, либо покинуть пляж. [st1.fname] хмыкает, и уходит. Другие отдыхающие с одобрением смотрят на вас.'
            $ setRep(10,1)
            $ st1.incCorr(-5)
            $ st1.incLoy(-5)
        'Не обращать внимания':
            'Вы решаете не обращать внимания на подобные выходки. В самом деле, ваши преподаватели уже достаточно взрослые люди, чтобы знать как себя вести.'
    $ move(curloc)
    
label event_loc_beach_15_8:
    show beach
    python:
        st1 = getChar('female')
        st1.incLust(40)
        st1.incCorr(5)
    show expression 'pic/locations/beach/lo8.jpg' at top as tempPic
    '[st1.fname] охлаждается кубиками льда. Судя по её лицу, это не только охлаждает, но даже напротив, распаляет её.'
    'Кубики блуждают по животу, иногда оказываясь совсем рядом с киской, а её левая рука судорожно сжимает маленькую грудь.'
    $ move(curloc)
    
label event_loc_beach_30_9:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        hadSex(st1,st2)
    show expression 'pic/locations/beach/lo9.jpg' at top as tempPic
    'Вы случайно заметили, что [st1.fname] с довольно недвусмысленными намерениями тянется, а точнее тянет к себе свою подругу.'
    menu:
        'Смотреть что будет дальше':
            show expression 'pic/locations/beach/lo9a.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            'Вы видите, как их губы слились в страстном поцелуе, [st2.fname] начала тяжелее дышать, груди обеих оголились от страстных обьятий, и они стали потираться сосками друг об друга.'
            'Понимая, куда это всё ведёт, вы не выдерживаете, и прерываете их прелюдию, прося по крайней мере отойти в какое нибудь более укромное место. [st1.fname] и [st2.fname] соглашаются с вами, и взявшись за руки уходят в ближайшие кустики.'
            $ setRep(10,1)
            $ player.incLust(10)
        'Уйти':
            'Вы решаете не стоит счас мешать девочкам, у них наверняка и без вас есть чем заняться. Хотя по недовольным лицам окружающих, понятно, что от вас ожидали более решительных действий по отношению к вашим воспитанникам.'
            $ setRep(10,-1)
    $ move(curloc)
    
label event_loc_beach_20_10:
    show beach
    python:
        st1 = getChar('female')
        player.incLust(10)
        setLust(10,10)
    show expression 'pic/locations/beach/lo10.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] пришла сегодня на пляж в довольно откровенном наряде. Судя по тому, что она держит верёвочки своего лифчика в зубах, загорать она собирается топлесс, да и способ, которым она наносит крем на своё молодое тело, не оставляет вас и окружающих равнодушными.'
    $ move(curloc)
    
label event_loc_beach_30_11:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/lo11.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] похоже хочет снять свой купальник, но заметив Вас, останавливается, и держит его одной рукой, глядя на Вас с ожиданием.'
    menu:
        'Кивнуть ей, показав что вы не против':
            show expression 'pic/locations/beach/lo11a.jpg' at top as tempPic
            'Видя, что Вы не против, [st1.fname] снимает с себя топ, и идёт к морю. Погрузив свои груди в воду, она кокетливо оглядывается на Вас, и развязывает узелочки на своих трусиках.'
            'Вы ошарашенно смотрите на открывшуюся для вашего взгляда дырочку её ануса. Судя по недовольному перешёптыванию за вашей спиной, не только вы заметили перформансы ученицы.'
            $ setRep(5,-5)
            $ setLust(5,15)
            $ st1.incCorr(5)
            $ player.incLust(10)
        'Покачать головой, показав, что вы против':
            'Видя, что Вы отрицательно относитесь к публичному оголению, [st1.fname] вздыхает, и начинает завязывать шнурочки на своём купальнике.'
            $ st1.incLoy(-5)
            $ st1.incCorr(-5)
    $ move(curloc)
    
label event_loc_beach_40_12:
    show beach
    python:
        st1 = getChar('male')
        st1.incRep(20)
        player.incLust(15)
    show expression 'pic/locations/beach/lo12.jpg' at top as tempPic
    'Вы видите, как [st1.fname] втирает в тело своей мамы крем. Очень оригинально втирает, всем телом. Особенно бёдрами между полупопий, как будто у него на трусах тоже есть крем. И судя по ритмичным, и ускоряющимся движениям, втирает уже не первую минуту.'
    'Заметив Вас, мама ученика подмигнула вам, и продолжила наслаждаться ласками сына. Мда, ну по крайней мере эта мама на Вас стучать не будет... Если только ревновать не начнёт.'
    $ move(curloc)

label event_loc_beach_20_13:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('female')
        st1.incCorr(5)
        st2.incCorr(5)
        st3.incCorr(5)
        st4.incCorr(5)
    show expression 'pic/locations/beach/lo13.jpg' at top as tempPic
    'Девчёнки примеряют свои новые бикини. Да, очевидно не всем ещё удобно ходить почти без одежды. Но по крайней мере нормы приличий соблюдены. Особенно стесняется [st1.fname], у неё наверное такое чувство, словно она оказалась голой посреди площади.'
    $ move(curloc)
    
label event_loc_beach_35_14:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
        setRep(5,-5)
    show expression 'pic/locations/beach/lo14.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Ваше внимание привлекли странные движения, которые совершала [st1.fname]. Какая то резиновая игрушка, которой ученица ритмично била по земле не вызывала у Вас никаких ассоциаций.'
    'Но как только из игрушки вырвалась первая струя белой жидкости, всё сразу встало на свои места. Вам остаётся надеяться, что всё поняли только вы, и подобные действия ваших учеников не отразятся на вашей репутации.'
    $ move(curloc)
    
label event_loc_beach_30_15:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/lo15.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] похоже хочет снять свой топ, но заметив вас, останавливается, глядя с ожиданием.'
    menu:
        'Кивнуть ей, показав что вы не против':
            show expression 'pic/locations/beach/lo15a.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            'Видя, что Вы не против, [st1.fname] снимает с себя абсолютно всё, и ложиться отдыхать на шезлонг. Мда, возможно вы погорячились с согласием.  [st1.fname], своим шикарным телом, привлекла к себе не только ваш взгляд.'
            $ setRep(5,-5)
            $ setLust(5,15)
            $ st1.incCorr(5)
            $ player.incLust(10)
        'Покачать головой, показав, что вы против':
            'Видя, что Вы отрицательно относитесь к публичному оголению, [st1.fname] вздыхает, и начинает завязывать шнурочки на своём купальнике.'
            $ setRep(5,5)
            $ st1.incCorr(-5)
    $ move(curloc)
    
label event_loc_beach_30_16:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/lo16.jpg' at top as tempPic
    '[st1.fname] устроила фото-сессию себя любимой. Она стоит в волнах прибоя, и меняет позы, пока какой то парень её фотографирует.'
    menu:
        'Смотреть дальше':
            show expression 'pic/locations/beach/lo16a.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            'Внезапно налетевшая волна прибоя срывает купальник с ученицы. [st1.fname] продолжает фото-сессию, как ни в чём не бывало.'
            'Точнее в чём мать родила. Хотя вот парень, который щёлкал её, судя по всему начал искать запасную плёнку у себя в трусах, наверное в фотоаппарате закончилась.'
            $ setRep(5,-2)
            $ setLust(5,15)
            $ st1.incCorr(5)
            $ player.incLust(10)
        'Уйти':
            'Не желая смотреть очередную бессмысленную фото-сессию своей ученицы, вы поворачиваетесь и уходите.'
    $ move(curloc)
    
label event_loc_beach_35_17:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        hadSex(st1,st2)
    show expression 'pic/locations/beach/lo17.jpg' at top as tempPic
    'Ваше внимание привлекли [st1.fname] и [st2.fname]. Они стоят в волнах, и страстно, прижимаясь грудьми, целуются друг с другом. Судя по всему Вы застали девушек в самый ответственный момент, потому что [st1.fname] уже начинает стягивать топ с подруги, а [st2.fname] всерьёз взялась за трусики.'
    'Вы подходите к ним, и прозрачно намекаете, что и стоит скрыться с глаз долой, пока их не заметило слишком много народа. Девчёнки хихикают, и быстренько удаляются в ближайшие кустики.'
    $ move(curloc)
    
label event_loc_beach_20_18:
    show beach
    python:
        st1 = getChar('female')
        st1.incCorr(1)
    show expression 'pic/locations/beach/lo18.jpg' at top as tempPic
    'Проходя мимо шезлонгов, вы заметили, что на них отдыхает [st1.fname]. Выглядит она вроде бы прилично, но вот только распущенная ширинка на её джинсовых шортах отчётливо показывает, что [st1.fname] сегодня решила не надевать трусиков. Выглядит весьма эротично.'
    $ move(curloc)
    
label event_loc_beach_5_19:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/lo19.jpg' at top as tempPic
    'Вы заметили, что [st1.fname] лежит, и нежится в волнах, одетая в закрытый купальник.'
    menu:
        'Сказать ей, что в такой солнечный день можно было бы надеть что нибудь полегче' if st1.getCorr() > 30:
            'Вы заводите разговор с ученицей, и говорите ей, что можно было бы надеть что нибудь полегче в такой солнечный день. К тому же и загар будет лучше и ровнее. А если кто то стесняется, так можно пройти в отдалённый конец пляжа, где почти никого не бывает, и загорать там как угодно!'
            show expression 'pic/locations/beach/lo19a.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            'Ученица видимо не совсем так Вас поняла, потому что спустя пару секунд, она лежала в той же позе, но уже совсем без купальника, привлекая к себе кучу восторженных взглядов.'
            python:
                st1.incCorr(3)
                player.incLust(5)
                setLust(10,15)
                setRep(5,-5)
        'Ничего не говорить':
            'Вы решаете, что всё и так в порядке, и удаляетесь.'
    $ move(curloc)
    
label event_loc_beach_35_20:
    show beach
    python:
        st1 = getChar('female')
        hadSex(st1)
        player.incLust(15)
    show expression 'pic/locations/beach/lo20.jpg' at top as tempPic
    'Вы заметили, что жара влияет не на всех одинаково. Вот например [st1.fname] не иначе как от жары, одной рукой наминает себе грудь, а другой путешествует по своему девичьему телу, периодически заходя в гости в трусики.'
    'Постепенно правая рука окончательно прописывается в трусиках, и оттуда начинают раздаваться хлюпающие звуки. На трусиках ученицы начинает расползаться влажное пятно, а лицо становится всё краснее.'
    'Наконец [st1.fname] выгибается с тихим стоном, и начинает мелко подрагивать. Вы надеетесь, что хотя бы ученице стало прохладней, потому что вам отнюдь нет.'
    $ move(curloc)
    
label event_loc_beach_40_21:
    show beach
    python:
        incRep(3,15)
    show expression 'pic/locations/beach/lo21.jpg' at top as tempPic
    'Зайдя в дальний уголок пляжа, вы натыкаетесь на трёх мамочек, которые решили позагорать не то, что топлесс, а вообще голыми. Так как это их не особо смущает, вы заводите с ними светскую беседу, и зарабатываете немного репутации.'
    'Хотя видит бог, это было тяжело, учитывая насколько хорошо сохранились родители ваших учеников. Эти полные груди, и гладко выбритые киски наверняка будут сниться вам не одну ночь.'
    $ move(curloc)
    
label event_loc_beach_35_22:
    show beach
    python:
        st1 = getChar('female')
    show expression 'pic/locations/beach/lo22.jpg' at top as tempPic
    'Вас зовёт [st1.fname] и просит намазать её кремом. А то все её подруги убежали купаться, забыв про неё.'
    menu:
        'Помочь ей':
            show expression 'pic/locations/beach/lo22a.jpg' at top as tempPic
            'Вы соглашаетесь, и пока Вы выдавливали крем на руку, [st1.fname] уже полностью разделась, и смотрит на Вас с ожиданием. Вы шокированно смотрите на голую ученицу, призывно приподнявшую свою попу, и не знаете что Вам теперь делать, и как выкрутиться из этой щекотливой ситуации.'
            'Оглянувшись, и поняв что на вас никто не обращает внимания, вы начинаете массировать своими руками тело старшеклассницы. Вы проводите рукой по её плечам, талии. Спускаетесь ниже, к попе и ногам, потом возвращаетесь выше, к грудям. Убедившись ещё раз, что всем всё равно, вы становитесь немного смелее.'
            'Вы начинаете поглаживать груди ученицы, пропуская её соски между своих пальцев. Другой рукой спускаетесь ниже, к её киске. Проведя по ней рукой, вы понимаете, что ученица там уже чем то намазана. Судя по запаху - её собственными соками.'
            'Вы смачиваете в них свои пальчики, вызывая у ученицы сладострастный стон, и засовываете указательный палец в тугое колечко её ануса, а средний в её текущую щель. Начав движения рукой, вы без удивления обнаруживаете, что [st1.fname] вовсю вам подмахивает, и с её губ постоянно срываются стоны. Чтобы не привлекать излишнего внимания, вы зажимаете ей рот свободной рукой, а левой ускоряете движения в её дырочках.'
            'После пары минут отчаянного хлюпания, вы чувствуете что ваши пальчики начали ритмично сжимать стенки её влагалища и сфинктер ануса. Ученица выгнулась в оргазме, пытаясь вытолкнуть вас, и прикусила зубами ваши пальцы на правой руке. От неожиданности вы отдёрнули от неё свои руки, и сладострастный крик удовольствия разнёсся по пляжу.'
            'Не желая становиться объектом внимания, вы быстренько собираетесь и уходите.'
            $ st1.incLoy(10)
            $ hadSex(st1,player)
        'Не помогать':
            'Вы говорите, что у вас нет желания пачкать руки в креме, и уходите.'
            $ st1.incLoy(-5)
    $ move(curloc)
    
label event_loc_beach_20_23:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        setLust(10,15)
        setRep(5,-1)
    show expression 'pic/locations/beach/lo23.jpg' at top as tempPic
    'Ваше внимание привлекли [st1.fname] и [st2.fname]. Они вроде бы одели закрытые купальники. Но вроде бы и не одели. Вроде бы всё прикрыто, но настолько прозрачно, что голый человек привлекал бы меньше внимания, чем эти двое. Хотя вам нравится.'
    $ move(curloc)
    
label event_loc_beach_5_24:
    show beach
    python:
        st1 = frigidovna
        if st1.getCorr() < 30:
            skipEvent()
    show expression 'pic/locations/beach/lo24.jpg' at top as tempPic
    '[st1.name] приподняла свой топ, чтобы намазать груди кремом для загара. Судя по её удивлённому лицу, она не ожидала вас увидеть.'
    menu:
        'Сделать ей замечание':
            'Вы подходите к учительнице, и просите её надеть топ, потому что все смотрят, что скажется на репутации школы. [st1.fname] извиняется, и начинает в спешке натягивать лифчик. Удивительно, как такая скромная учительница умудрилась раздеться до трусов перед публикой.'
            $ st1.incLoy(-10)
            $ setRep(5,5)
            $ st1.incCorr(-5)
        'Не обращать внимания':
            'Вы решаете не обращать внимания на подобные выходки. В самом деле, ваши преподаватели уже достаточно взрослые люди, чтобы знать как себя вести.'
            $ st1.incLoy(10)
    $ move(curloc)
    
label event_loc_beach_41_2:
    show beach
    python:
        st1 = getChar('female')
        setLust(10,10)
        setFun(10,10)
        setRep(10,-2)
        st1.incCorr(5)
        player.incLust(10)
    show expression 'pic/locations/beach/mid2.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Фурор. Именно фурор произвела [st1.fname], появившись на пляже вроде и в купальнике, а вроде и нет. Жаль только, что на следующем родительском собрании об этом фуроре спрашивать будут не ученицу, а вас.'
    $ move(curloc)
    
label event_loc_beach_35_3:
    show beach
    python:
        st1 = getChar('female')
        st1.incLoy(10)
        st1.incCorr(5)
        player.incLust(15)
    'Заметив неподалёку кабинку с незамысловатой надписью WC, Вы без задней мысли толкнули дверь, чтобы справить малую нужду.'
    show expression 'pic/locations/beach/mid3.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    st1.say 'Я КОНЧАЮ-У-У-У, - встретил вас крик девушки, и её дёргающееся в конвульсиях оргазма тело, начало сползать с унитаза.'
    'В этом небольшом, дёргающимся тельце на полу, вы узнали одну из своих учениц. Бедем надеятся, что никто ничего не услышал, подумали вы, поднимая полубессознательную девочку и усаживая её обратно. [st1.fname] устало улыбается вам.'
    $ move(curloc)
    
label event_loc_beach_45_4:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        hadSex(st1,st2)
        player.incLust(5)
    show expression 'pic/locations/beach/mid4.jpg' at top as tempPic
    'Гуляя по пляжу, вы обратили внимание на двух своих учениц, они невозмутимо загорали, сверкая своими обнажёнными телами.'
    'А ну немедленно оденьтесь! - закричал какой то ханжа'
    st1.say 'Да пошёл ты в жопу! Мы и в школе так ходим!'
    'Девочки захихикали и продолжили болтать'
    if rand(1,3) == 1:
        'Слишком многие обратили внимание на их высказывание, и ваша репутация пострадала.'
        $ setRep(5,-5)
    $ move(curloc)
    
label event_loc_beach_50_5:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
        player.incLust(10)
    show expression 'pic/locations/beach/mid5.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Вы обратили внимание на аномально высокую концентрацию ног в пляжной раздевалке. Аккуратно заглянув, вы увидели, как [st2.fname] посасывает грудь девушки с параллельного класса. Его член призывно тёрся о небритый лобок девушки намекая на более личное знакомство.'
    player.say '"Чёрт, а это возбуждает!" - подумали вы, оставляя парочку наедине.'
    $ move(curloc)
    
label event_loc_beach_35_6:
    show beach
    python:
        st1 = getChar('female')
        st1.incCorr(5)
        player.incLust(10)
    show expression 'pic/locations/beach/mid6.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] решила не заморачиваться с бикини и купальником и отдыхать как есть. Всё хорошо, и груди сочные и лобок выбрит и даже загар требуется.'
    'Есть только одна проблема - пляж то не нудисткий...'
    $ move(curloc)
    
label event_loc_beach_60_1:
    show beach
    python:
        st1 = getChar('female')
        hadSex(st1)
        st1.incCorr(5)
        player.incLust(15)
    show expression 'pic/locations/beach/hi1.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Прогуливаясь по пляжу, вы зашли в укромное местечко, где маленькая [st1.fname], уединившись от взрослых взглядов, устроила себе маленькое развлечение в надувном бассейне.'
    'Вы как раз увидели её в тот момент, когда её киска плотно обхватив пальчики, начала сокращаться в оргазме. Что было отчётливо видно по пульсирующему кольцу ануса.'
    'Немного полюбовавшись на картинку, вы пошли дальше'
    $ move(curloc)
    
label event_loc_beach_70_2:
    show beach
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/beach/hi2.jpg' at top as tempPic
    'Подойдя к скоплению народа, чтобы посмотреть, чего же все там так столпились, вы обнаружили трахающуюся у всех на глазах парочку. И с ужасом узнали в них ваших учеников.'
    '[st2.fname] яростно сношал свою подругу, совершенно не обращая внимания на то, что за ним наблюдают десятки глаз, и даже пара камер. Пожалуй от этого он возбуждался ещё сильнее. И его крепкий член всё активнее вторгался в пещерку школьницы.'
    player.say '"Что то мне хочется, чтобы меня связали с этой парочкой. Надо поскорее сваливать!"'
    $ move(curloc)