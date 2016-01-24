label event_loc_changeRoom_0_no1:
    show changeRoom
    python:
        st1 = getChar('female')
        st1.incLoy(10)
        st1.incFun(5)
    show expression 'pic/locations/school/changeRoom/no1.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] одевается после бассейна. Судя по всему она не собирается снимать купальник. Может быть планирует вернуться?'
    'Вы немного поговорили с ней о том, что стоит носить нормальное нижнее бельё в школе, а не купальник. Похоже, что обсуждение нижнего белья немного повысило лояльность к вам.'
    $ move(curloc)

label event_loc_changeRoom_0_no2:
    show changeRoom
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        setFun(3,5)
        setLust(5,10)
    show expression 'pic/locations/school/changeRoom/no2.jpg' at top as tempPic
    'Школьницы [st1.fname], [st2.fname] и [st3.fname] переодеваются на занятия плаванием. Похоже, что [st3.fname] забыла сегодня купальник дома.'
    if player.getCorr() > 20:
        show expression 'pic/locations/school/changeRoom/no2_1.jpg' as tempPic:
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        player.say '"Интересно, что же она будет делать? Надеюсь, что пойдёт голой. Это было бы так сексуально..."'
        'Вы с удовольствем смакуете в воображении, как обнажённая [st3.fname] выходит из бассейна.'
        $ player.incCorr(1)
        $ player.incLust(10)
    $ move(curloc)

label event_loc_changeRoom_8_no3:
    show changeRoom
    python:
        st1 = getChar('female')
        st1.incLoy(5)
        st1.incFun(10)
    show expression 'pic/locations/school/changeRoom/no3.jpg' at top as tempPic
    '[st1.fname] переодевается после бассейна. Судя по всему, занятие было неудачным, и она чем то расстроена. Вы поболтали с ней, чтобы немного утешить. Всё это время [st1.fname] так и стояла с открытой грудью.'
    if player.getCorr() > 30:
        show expression 'pic/locations/school/changeRoom/no3_1.jpg' at top as tempPic
        'Она так долго стояла с открытой грудью, что вы всерьёз начали жалеть, что ещё не видели момента, как эта грудь зажимает чей то член и своей мягкостью и теплотой доводдит его до оргазма.'
        player.say '"Эх, такие сиськи без дела висят!"'
        $ player.incCorr(1)
        $ player.incLust(10)
    $ move(curloc)    

label event_loc_changeRoom_10_no4:
    show changeRoom
    python:
        st1 = getChar('female')
        player.incLust(10)
    show expression 'pic/locations/school/changeRoom/no4.png' at top as tempPic
    '[st1.fname] Примеряет свой новый бикини. Хмм, по моему вы ещё не разрешали плавать в бикини.'
    if 'naked' == school.uniform:
        player.say '[st1.fname]! Зачем тебе бикини, когда все уже плавают голыми, а?'
        show expression 'pic/locations/school/changeRoom/no4_1.png' at top as tempPic
        'Ученица соглашается с вами и полностью раздевается, складывая свой красивый купальник в шкафчик.'
    else:
        menu:
            'Указать на недопустимость бикини' if school.uniform in ['usual','strict','uniform']:
                'Вы отчитали ученицу за такой наряд, попросив в будущем не одеваться так на занятия'
                python:
                    st1.incFun(-10)
                    st1.incCorr(-5)
                    st1.incRep(5)
            'Не обращать внимания':
                'Вы решили не обращать внимания на подобный наряд. Родители ученицы будут явно не в восторге, если узнают.'
                python:
                    st1.incFun(10)
                    if rand(1,3) == 1:
                        st1.incRep(-5)
                    st1.incLoy(5)                          
    $ move(curloc)

label event_loc_changeRoom_5_no5:
    show changeRoom
    python:
        st1 = getChar('female')
        st1.incLoy(5)
        st1.incFun(10)
        player.incLust(5)
    show expression 'pic/locations/school/changeRoom/no5.jpg' as tempPic:
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
    '[st1.fname] похоже обнаружила, что она больше не девочка, и у неё появилась грудь.'
    if player.getCorr() > 25:
        show expression 'pic/locations/school/changeRoom/no5_1.jpg' at top as tempPic
        player.say '"То то она удивится, когда обнаружит, что к этой груди прилагаются места куда более интересные!"'
        'Вы вспомнили себя в её возрасте, когда впервые обнаружили, что киска выделяет влагу не только, когда хочется писать, но и когда первый раз смотришь порно...'
        player.say '"Я, по моему, в ту самую ночь раз шесть кончила!"'
        $ player.incCorr(1)
        $ player.incLust(10)
    $ move(curloc)    

label event_loc_changeRoom_0_no6:
    show changeRoom
    python:
        st1 = getChar('female')
        setLust(5,15)
        player.incLust(10)
    show movie
    play movie "pic/locations/school/changeRoom/no6.gif.webm" loop
    player.say '"Это я удачно зашла!", - подумали вы, глядя на раздевающихся девочек. Благодаря вашему полу, никто не обратил на вас особого внимания.'
    stop movie
    hide movie
    $ move(curloc)    

label event_loc_changeRoom_15_low1:
    show changeRoom
    python:
        player.incLust(15)
        setCorr(3,5)
    show expression 'pic/locations/school/changeRoom/lo1.jpg' at top as tempPic
    'Три киски очевидно лучше чем одна! - подумали вы, заходя в раздевалку и наблюдая за тем, как ваши ученицы переодеваются.'
    player.say '"Очень странный способ, но в конце концов школьными правилами он не оговаривается!"'
    $ move(curloc)

label event_loc_changeRoom_40_low2:
    show changeRoom
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')

        st4 = getChar('male')
        st5 = getChar('male')
        st6 = getChar('male')
        st7 = getChar('male')
        st8 = getChar('male')
        st9 = getChar('male')
        player.incLust(10)
        player.incCorr(1)
    show expression 'pic/locations/school/changeRoom/lo2.jpg' at top as tempPic
    'Войдя в раздевалку, вы увидели как группа парней домогается до девушек. Причём очень так активно домогается. [st1.fname], [st2.fname] и [st3.fname] пытаются вырваться из их "чутких" объятий.'
    menu:
        'Смотреть':
            'Под вашим пристальным взглядом задор мальчишек как то скукожился и увял, и они, извинившись перед школьницами, по быстренькому свалили.'
            'Жаль, вы были готовы насладиться небольшим шоу. Хотя девушки сердечно поблагодарили вас за своевременное появление.'
            python:
                st1.incLoy(15)
                st2.incLoy(15)
                st3.incLoy(15)
                scoldWho = [st4,st5,st6,st7,st8,st9]
                for x in scoldWho:
                    x.incLoy(-5)
                    x.incRep(5)
                    addDetention(x)
        'Уйти':
            python:
                hadSex(st1,st2,st3,st4,st5,st6,st7,st8,st9)
    $ move(curloc)

label event_loc_changeRoom_40_mid1:
    show changeRoom
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
        player.incLust(15)
    show expression 'pic/locations/school/changeRoom/mid1.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Бросив случайный взгляд к дальней стенке раздевалки Вы заметили одну из учениц. [st1.fname] эротично стояла на носочках, слегка раздвинув ножки.'
    'Смущало не отсутвие на ней трусиков, всё таки мы в раздевалке, всякое случиться может. А густые капли спермы стекающие из её киски прямо по бёдрам. Особо крупный сгусток потянулся из её влагалища, прямо до пола.'
    menu:
        'Спросить, что случилось':
            player.say '[st1.fname], что то нехорошее случилось? - заботливо спросили вы, наблюдая за выражением лица девочки.'
            st1.say 'Нет, ну что вы [player.name], просто у меня родители сегодня дома остались, вот мы с моим парнем и решили домой не ходить.'
            player.say 'Понятно... - протянули вы, - Ну ладно... В случае чего, это лучше делать в гостинице, хорошо?'
            '[st1.fname] радостно кивнула, сделала неуклюжий реверанс и скрылась в душе.'
            $ st1.incLoy(10)
        'Наказать':
            $ scoldWho = [st1]
            jump scoldAll
    $ move(curloc)    

label event_loc_changeRoom_50_mid2:
    show changeRoom
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.incLust(15)
        player.incCorr(2)
    show expression 'pic/locations/school/changeRoom/mid2.jpg' at top as tempPic
    'Вы вроде бы хотели переодеться, но теперь не знаете, насколько это удобно, переодеваться перед столь страстно трахающейся парочкой.'
    '[st1.fname] и [st2.fname] не обращая ни на кого внимания, предаются страстным ласкам прямо на лавочке в раздевалке. Вам плохо видно, но кажется член парня едва помещается в узенькую киску девушки, хотя обилие выделяемой ей смазки безусловно помогает процессу.'
    menu:
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Оставить их в покое':
            python:
                hadSex(st1,st2)
    $ move(curloc)

label event_loc_changeRoom_75_Hi1:
    show changeRoom
    python:
        player.incLust(20)
        setCorr(10,5)
        setLust(10,15)
    show expression 'pic/locations/school/changeRoom/hi1.jpg' at top as tempPic
    'Похоже в Ваше отсутвие тут проходит соревнование на самую красивую попку школы! Вот парни и не сдержались и поставив девчёнок, принялись выбирать победительницу. Судя по равномерно заляпанным спермой задницам, победила дружба!'
    $ move(curloc)

label event_loc_changeRoom_75_Hi2:
    show changeRoom
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')

        st4 = getChar('male')
        st5 = getChar('male')
        st6 = getChar('male')
        st7 = getChar('male')
        st8 = getChar('male')
        st9 = getChar('male')
        
    show expression 'pic/locations/school/changeRoom/lo2.jpg' at top as tempPic
    'Войдя в раздевалку, вы увидели как группа парней домогается до девушек. Причём очень так активно домогается. [st1.fname], [st2.fname] и [st3.fname] пытаются вырваться из их "чутких" объятий.'
    menu:
        'Наказать':
            python:
                st1.incLoy(15)
                st2.incLoy(15)
                st3.incLoy(15)
                scoldWho = [st4,st5,st6,st7,st8,st9]
            jump scoldAll
                
        'Смотреть':
            $ player.incLust(25)
            $ player.incCorr(5)
            show expression 'pic/locations/school/changeRoom/hi2_1.jpg' at top as tempPic
            'Видя, что вы не собираетесь их наказывать, парни смелее берутся за дело.'
            'Левая парочка учеников концентрируется на груди и киске школьницы, [st2.fname] стоящая посередине взвизгивает, когда [st5.fname] сжимает её грудь, а [st7.fname] вводит свои пальцы во влагалище, отодвинув в сторону облегающую ткань купальника.'
            '[st3.fname] начинает шумно дышать, когда два парня справа начинают ласкать её груди.'
            player.say 'Ну же мальчики, не стесняйтесь, вы так и собираетесь их тискать, как первоклашки? - подзадориваете вы учеников.'
            show expression 'pic/locations/school/changeRoom/hi2_2.jpg' at top as tempPic    
            'В ответ на ваши слова, парни решают слегка увлажнить девушек, сливаясь с ними в страстных поцелуях. Ну точнее кто то сливается, а кто то продолжает ласкать школьниц, не давая им ни минуты продыху.'
            'Вы отчётливо видите, что девушки прилично возбудились, несмотря на первоначальное сопротивление. Или же оно было наигранное?'
            player.say 'Вы меня собираетесь чем нибудь удивлять, или мне до конца дня наблюдать ваши пуританские ласки? - в очередной раз подгоняете вы школьников, увлёкшихся предварительными ласками.'
            show expression 'pic/locations/school/changeRoom/hi2_3.jpg' at top as tempPic    
            'Парни наконец оторвались от поцелуев, и нагнули повизгивающих то ли от возмущения, то ли от возбуждения девушек.'
            st4.say 'Давайте, сучки, подставляйте свои пёзды! - довольно грубо крикнул первый, доставая из штанин увесистый болт.'
            st5.say 'Да, мы уже заждались! - сказал второй, начав тереть свой член о влажную киску школьницы.'
            'Третий не сказал ничего, а с тихим стоном засунул свой ствол крайней девушке.'
            show expression 'pic/locations/school/changeRoom/hi2_4.jpg' at top as tempPic    
            'Парни яростно долбили своих одноклассниц, не обращая ни на вас, ни на их стоны никакого внимания. Девчёнки подвизгивали от удовольствия, и из их кисок стекала смазка вперемешку с потом.'
            'Вся раздевалка была наполнена хлюпанием, стонами и криками, заводящими вас до ужаса. Ваша рука невольно опустилась к киске и начала её ласкать.'
            'Наконец парни синхронно издали победные хрипы, и их члены наполнили матки девушек спермой. Постанывая после оргазмов школьницы, опустились на пол, не в силах двигаться.' 
            if player.getLust() > 70:
                'Ваше внимание привлекли топорщащиеся джинсы оставшейся троицы, которые так и не получили сладкого.'
                'Вы не смогли сдержать свою страсть, и не отрывая взгляда от топорщащихся штанов, при нялись раздеваться. Глядя на вас, ученики быстро смекнули в чём дело, и скинули с себя всю одежду тоже.'
                hide tempPic
                show movie
                play movie "pic/locations/school/changeRoom/hi2_5.gif.webm" loop
                'Вскоре вы уже с наслаждением прыгали на члене, в то время, как два остальных тёрлись о ваши груди и лицо, заводя вас всё сильнее.'
                'Твёрдый ствол плавно двигался в вашей киске, проникая своей, разбухшей от возбуждения головокой, всё глубже. Вы потеряли связь с реальностью, для вас существовал только этот, прекрасный член, таранящий ваше возбуждённое тело.'
                stop movie
                hide movie   
                show expression 'pic/locations/school/changeRoom/hi2_6.jpg' at top as tempPic
                'Одному из парней надоело бездействовать, и он затолкнул свой член вам в рот. Вы в принципе не слишком сопротивлялись, покорно заглотив угощение.' 
                'В это время к вашей незанятой попке пристроился третий парень и надавил головкой на анус. Вы слегка вздрогнули, когда его член плавно вошёл, расширяя попку. Ощущение заполненности всех отверстий одновременно буквально свело вас с ума, и вы принялись кончать, беспорядочно ёрзая на пронзивших вас членах, доставляя им и себе ни с чем не сравнимое удовольствие.'
                'Не успев отойти от первого оргазма, вас немедленно накрыл второй, когда дырочки начали заполняться спермой. Потом третий, когда члены вытащили и из дырочек начало вытекать заполнявшее их семя.'
                'Вы пришли в себя спустя несколько минут, удивляясь тому, что позволили себе заняться сексом аж с тремя парнями сразу.'
                $ player.incCorr(5)
                $ player.incLust(-100)
                $ player.incFun(10)
                $ player.incEnergy(-200)
                $ player.coverSperm('лицо','рот','попа','вагина','ноги')
            $ hadSex(st1,st2,st3,st4,st5,st6,st7,st8,st9,player)
            $ changetime(30)
    $ move(curloc)    