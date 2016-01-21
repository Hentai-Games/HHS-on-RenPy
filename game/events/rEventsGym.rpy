label event_loc_gym_0_no1:
    show gym
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st1.incLoy(5)
        st1.incFun(10)
        st2.incLoy(-5)
        st2.incFun(-10)
    show expression 'pic/locations/school/gym/no1.jpg' at top as tempPic
    '[st1.fname] больно получила мячом по бедру. Вы утешили ее, и помогли ей подняться. А вот [st2.fname] получил втык за подобное поведение.'
    st1.say 'Ну, [st1.fname], я тебе покажу ещё!'
    if player.getCorr() > 40:
        show expression 'pic/locations/school/gym/no1_1.jpg' at top as tempPic
        player.say '"Какой злобный взгляд! Интересно, как она его накажет? В самый ответственный момент не даст, заставив обкончать свой собственный живот?"'
        'Вы прикрыли глаза и представили себе эту сцену... Изнемогающий от желания погрузиться во влажную темноту [st2.fname], и [st1.fname], безжалостно заставляющая парня обкончать её руку...'
        $ player.incCorr(1)
        $ player.incLust(10)
    $ move(curloc)

label event_loc_gym_0_no2:
    show gym
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incEdu(2)
        st1.incFun(5)
        st2.incEdu(2)
        st2.incFun(10)
    show expression 'pic/locations/school/gym/no2.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] играют в баскетбол. Хоть бы переоделись в форму для занятий.'
    if player.getCorr() > 30:
        show expression 'pic/locations/school/gym/no2_1.jpg' at top as tempPic
        player.say '"А то вспотеют, промокнут, форма прилипнет к телу, будет облегать, ммм..."'
        'Вы отчётливо представили, как [st2.fname] приподнимает свой топ, чтобы хоть немного остудить разгорячённое тело.'
        python:
            player.incLust(10)
            player.incCorr(1)
    $ move(curloc)

label event_loc_gym_0_no3:
    show gym
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/gym/no3.png' at center as tempPic
    '[st1.fname] делает упражнения по лёгкой атлетике. Вообще для занятий подобным придумали пуанты, но [st1.fname] их почему то не носит.'
    if player.getCorr() > 30:
        show expression 'pic/locations/school/gym/no3_1.jpg' at center as tempPic
        player.say '"Хотя жаль, что она только пуанты не носит во время занятий гимнастикой."'
        'Вы мгновенно представили, как это юное тело смотрелось бы совсем без одежды. Весьма схематично, но места интересов ваше воображение прорисовало хорошо.'
        python:
            player.incLust(10)
            player.incCorr(1)
    python:
        st1.incEdu(3)
        st1.incFun(10) 
    $ move(curloc)
    
label event_loc_gym_0_no4:
    show gym
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
    show expression 'pic/locations/school/gym/no4.jpg' at top as tempPic
    '[st1.fname]? Нет, [st2.fname]? Нет, [st3.fname]? Да, точно, [st3.fname]! Теперь когда девочка лежит в нокауте от волейбольного мяча, Вы наконец то смогли её идентифицировать. Ну чтож, волейбол суровая игра, и в неё надо уметь играть!'
    if player.getCorr() > 50:
        show movie
        play movie "pic/locations/school/gym/no4_1.gif.webm" loop
        player.say '"Уж лучше бы она сыграла с подругой в "Доведи парня до оргазма". Очень такая любопытная игра получилась бы. Две киски, зажатый между ними член и активное трение. Самая интрига в том, чтобы угадать кто же первый кончит?"'
        player.say '"И травм, опять таки меньше. Разве что моральная, от преждевременного проигрыша."'
        stop movie
        hide movie
        python:
            player.incLust(10)
            player.incCorr(1)
    python:
        st3.incEdu(3)
        st3.incFun(10) 
    $ move(curloc)
    
label event_loc_gym_0_no5:
    show gym
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/school/gym/no5.jpg' at top as tempPic
    'Так так, [st1.fname] и [st2.fname] похоже затеяли ссору!'
    st1.say 'Ты виновата!'
    st2.say 'Нет ты!'
    st1.say 'Нет ты! Я почти его не трогала!'
    'Видя, что вы смотрите на них, девушки замолкают.'
    menu:
        'Разнять их':
            'Вы отчитали обеих учениц, за недостойное поведение, и пообещали сообщить обо всём их родителям.'
            $ scoldWho = [st1, st2]
            python:
                st1.incFun(-10)
                st2.incFun(-10)   
        'Вы решили не обращать внимания на выходки учеников. В конце концов кто давал Вам право вмешиваться в их личные дела? Хотя в случае чего, их родители будут безусловно другого мнения.':
            python:
                st1.incFun(10)
                st2.incFun(10)
                st1.incRep(-5)
                st2.incRep(-5)
        'Узнать, в чём собственно дело' if st1.getCorr() + st2.getCorr() > 100 or development == 1:
            'Девушки начинают рассказывать:'
            show movie
            play movie "pic/locations/school/gym/no5_1.gif.webm" loop
            st1.say 'Ну мы вчера с одним парнем, ну в общем вдвоём с ней решили попробовать.'
            st2.say 'Ага, ну сняли, повели в кровать, целовали там, всякое разное, потом стали член ручками ласкать.'
            st1.say 'Да, вместе схватились, и нежно так поглаживали, ну я то нежно, а она как вцепилась!'
            st2.say 'Сама ты вцепилась! Это я едва его касалась!'
            st1.say 'Да ты!!!!'
            player.say 'Так стоп, случилось то что?'
            play movie "pic/locations/school/gym/no5_2.gif.webm" loop
            st1.say 'Известно что, [st2.fname] так увлеклась, что парень кочил! Прям БАХ! И всё в сперме!'
            st2.say 'Сама ты увлеклась! Я то вообще за ствол держалась! А он у парней и не чувствует ничего!'
            st1.say 'Да? А кто ему яйца сдавливал и ушко лизал? Я?'
            player.say 'Так стоп! Ну кончил он и чего?'
            st2.say 'Известное дело, домой пошёл...'
            st1.say 'Это ты виновата!'
            st2.say 'Нет ты!'
            player.say 'СТОП Я СКАЗАЛА! Никто не виноват, девочки. Просто парень вам бракованный попался. Бывают такие, чуть коснулся, и он уже храпит. Не теряйте надежду и вам в конце концов повезёт найти общего любимого!'
            player.say '"И что я им несу? Сама себе репутационную могилу рою!"'
            stop movie
            hide movie
            'Девушки задумались, но потом согласились с вами и улыбнулись друг другу. Вам почему то кажется, что они стали немного увереннее в себе. Но вот их родители - наоборот.'
            $ st1.incCorr(5)
            $ st2.incCorr(5)
            $ st1.incRep(-5)
            $ st2.incRep(-5)
    $ move(curloc) 

label event_loc_gym_0_no6:
    show gym
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/gym/no6.jpg' at top as tempPic
    '[st1.fname] как раз закончила делать растяжку, и немного смущена тем, что заметила как вы за ней наблюдаете.'
    if player.getCorr() > 30:
        show expression 'pic/locations/school/gym/no6_1.jpg' at top as tempPic
        player.say '"И чего тут смущаться? Вот помню, будучи ещё школьницей, я пригласила покататься на аттракционе парня, и в самый ответственный момент ощутила причину его согласия. Вот это было смущение!"'
        python:
            player.incLust(5)
            player.incCorr(1)
            st1.incLoy(-5)
    python:
        st1.incEdu(3)
        st1.incFun(10) 
    $ move(curloc)

label event_loc_gym_0_no7:
    show gym
    python:
        st1 = getChar('male')
        st2 = getChar('male')
    show expression 'pic/locations/school/gym/no7.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] отдыхают после тренировки.'
    if player.getCorr() > 30:
        player.say 'Какие горячие парни! Так бы и скинула всё с них, и... Хотя при таком обилии школьниц, эта идея уже не кажется мне особо привлекательной.'
        python:
            player.incLust(10)
            player.incCorr(1)
    python:
        st1.incEdu(3)
        st1.incFun(10)
        st2.incEdu(3)
        st2.incFun(10)    
    $ move(curloc)   
    
label event_loc_gym_0_no8:
    show gym
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/gym/no8.jpg' at top as tempPic
    'Ого! [st1.name] похоже решила всерьёз попасть на олимпийские игры! Заметившие прыжок одноклассницы шокированы великолепно исполненным прыжком.'
    if mile_qwest_1_stage > 0:
        show expression 'pic/locations/school/gym/no8_1.jpg' at top as tempPic
        'Глядя на прыгающую девочку, вам внезапно вспомнился [mustangovich.name]. Уж больно тот любил прыгающих на его члене девочек!'
        python:
            player.incLust(10)
    python:
        st1.incEdu(3)
        st1.incFun(10) 
    $ move(curloc)    
    
label event_loc_gym_0_no9:
    show gym
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/gym/no9.jpg' at top as tempPic
    '[st1.name] решила попробовать свои силы в лёгкой атлетике. Ну чтож, у неё неплохо получается.'
    if player.getCorr() > 40:
        show expression 'pic/locations/school/gym/no9_1.jpg' at top as tempPic
        player.say '"Уж лучше бы попробовала силы в лёгком порно. Почему то мне кажется, что неё тоже неплохо бы получилось... И тут шесты и там шесты. И тут счастье в конце и там..."'
        $ player.incLust(10)
    python:
        st1.incEdu(3)
        st1.incFun(10) 
    $ move(curloc) 

label event_loc_gym_0_no10:
    show gym
    python:
        st1 = getChar('female','brustmax')
    show expression 'pic/locations/school/gym/no10.jpg' at top as tempPic
    '[st1.fname] делает растяжку.  [st1.fname] растяжку делает.  Делает растяжку [st1.fname]. Я готова сколь угодно долго переставлять слова, но суть от этого не меняется - [st1.fname] делает растяжку.'
    if player.getCorr() > 50:
        show movie
        play movie "pic/locations/school/gym/no10_1.gif.webm" loop
        player.say '"Мне вот интересно, чтобы отрастить такие буфера тоже надо какую то специальную растяжку делать? В душе там, с парнем... Ну не то, что с парнем, я так полагаю, что любой член сойдёт!"'
        stop movie
        hide movie
        python:
            player.incLust(10)
            player.incCorr(1)
    python:
        st1.incEdu(3)
        st1.incFun(10) 
    $ move(curloc)
    
label event_loc_gym_0_no11:
    show gym
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st2.incLoy(5)
    show expression 'pic/locations/school/gym/no11.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] помогает своей подруге сесть на шпагат.'
    player.say 'Очень, очень впечатляюще [st2.fname]!!! Можно гордиться - растяжка превосходна!'
    if player.getCorr() > 30:
        player.say 'Как и молодые тела юных барышень. Мммм... Вы буквально чувствуете как намокают ваши трусики...'
        python:
            player.incLust(15)
            player.incCorr(1)
    python:
        st1.incEdu(1)
        st1.incFun(10) 
    $ move(curloc)
    
label event_loc_gym_20_low1:
    show gym
    python:
        st1 = getChar('female')
        st1.incLust(-10)
        st1.incFun(-10)
        st1.incCorr(3)
        player.incLust(10)
    show expression 'pic/locations/school/gym/lo1.jpg' at top as tempPic
    '[st1.fname] запуталась в сетке, отбивая подачу на волейболе. Всё бы ничего, но самостоятельные попытки выбраться привели к некоторому обнажению некоторых частей тела.'
    $ move(curloc)
    
label event_loc_gym_50_mid1:
    show gym
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('female')
        st5 = getChar('female')
    show expression 'pic/locations/school/gym/mid1.jpg' at top as tempPic
    'Девушки проводят внеклассные теринировки под интригующим названием "разомни свою киску". Это уникальное занятие улучшает мышечный тонус, поднимает настроение, и стимулирует выделение естественной влагалищной смазки. По крайней мере с последним пунктом Вы безусловно согласны. Смазки выделяется будь здоров!'
    'На вопрос, кто их начил этому упражнению, все пальчики показали на красного, под цвет своих трусов, физрука. Вы не придумали ничего лучше, чем махнуть рукой на такие занятия. По крайней мере у некоторых девстсвенная плева видна невооружённым глазом. И на осмотре гинеколога можно сэкономить.'
    python:
        st1.incCorr(5)
        st1.incCorr(1)
        st2.incCorr(5)
        st2.incCorr(1)
        st3.incCorr(5)
        st3.incCorr(1)
        st4.incCorr(5)
        st4.incCorr(1)
        st5.incCorr(5)
        st5.incCorr(1)
        player.incLust(30)
        player.incCorr(3)
        player.incWill(4)
    $ move(curloc)
    