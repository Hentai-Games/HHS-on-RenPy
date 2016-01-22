label event_loc_changeRoom_0_no1:
    show changeRoom
    python:
        st1 = getChar('female')
        st1.incLoy(5)
        st1.incFun(5)
    show expression 'pic/locations/school/changeRoom/no1.jpg' at top as tempPic
    '[st1.fname] одевается после бассейна. Судя по всему она не собирается снимать купальник. Может быть планирует вернуться?'
    'Вы немного поговорили с ней о том, что стоит носить нормальное нижнее бельё в школе, а не купальник. Похоже, что обсуждение нижнего белья немного повысило лояльность к вам.'
    $ move(curloc)

label event_loc_changeRoom_0_no2:
    show changeRoom
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st1.incLoy(5)
        st1.incFun(10)
        st2.incLoy(5)
        st2.incFun(10)
        st3.incEdu(-2)
        st3.incFun(-10)
    show expression 'pic/locations/school/changeRoom/no2.jpg' at top as tempPic
    'Школьницы [st1.fname], [st2.fname] и [st3.fname] переодеваются на занятия плаванием. Похоже, что [st3.fname] забыла сегодня купальник дома.'
    if player.getCorr() > 20:
        player.say '"Интересно, что же она будет делать? Надеюсь, что пойдёт голой. Это было бы так сексуально..."'
        $ player.incCorr(1)
        $ player.incLust(10)
    $ move(curloc)

label event_loc_changeRoom_0_no3:
    show changeRoom
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st1.incLoy(5)
        st1.incFun(10)
    show expression 'pic/locations/school/changeRoom/no3.jpg' at top as tempPic
    '[st1.fname] переодевается после бассейна. Судя по всему занятие было неудачным, и она чем то расстроена. Вы поболтали с ней, чтобы немного утешить. Всё это время [st1.fname] так и стояла с открытой грудью.'
    if player.getCorr() > 20:
        'Хотя в основном Вы болтали только ради того, чтобы подольше насладится видом этих сисечек.'
        $ player.incCorr(1)
        $ player.incLust(10)
    $ move(curloc)    

label event_loc_changeRoom_0_no4:
    show changeRoom
    python:
        st1 = getChar('female')
        player.incLust(10)
    show expression 'pic/locations/school/changeRoom/no4.png' at top as tempPic
    '[st1.fname] Примеряет свой новый бикини. Хмм, по моему Вы ещё не разрешали плавать в бикини.'
    menu:
        'Указать на недопустимость бикини':
            'Вы отчитали ученицу за такой наряд, попросив в будущем не одеваться так на занятия'
            python:
                st1.incFun(-10)
                st1.incEdu(10)
                st1.incLoy(-5)
        'Не обращать внимания':
            'Вы решили не обращать внимания на подобный наряд. Родители ученицы будут явно не в восторге, если узнают.'
            python:
                st1.incFun(10)
                st1.incEdu(-10)
                st1.incLoy(5)                          
    $ move(curloc)

label event_loc_changeRoom_0_no5:
    show changeRoom
    python:
        st1 = getChar('female')
        st1.incLoy(5)
        st1.incFun(10)
    show expression 'pic/locations/school/changeRoom/no5.jpg' at top as tempPic
    '[st1.fname] похоже обнаружила, что она больше не девочка, и у неё появилась грудь.'
    if player.getCorr() > 20:
        'Вот бы её потискать, эту новую грудь, которой не так давно и в помине не было!'
        $ player.incCorr(1)
        $ player.incLust(10)
    $ move(curloc)    

label event_loc_changeRoom_0_no6:
    show changeRoom
    python:
        st1 = getChar('female') #ну допустим их там трое, пускай все и получают плюшки :)
        st2 = getChar('female')
        st3 = getChar('female')
        st1.incLoy(5)
        st1.incFun(10)
        st2.incLoy(5)
        st2.incFun(10)
        st3.incLoy(5)
        st3.incFun(10)        
        player.incCorr(1)
        player.incLust(10)

    show movie
    play movie "pic/locations/school/changeRoom/no6.gif.webm" loop
    player.say '"Это я удачно зашла!", - подумали вы, глядя на раздевающихся девочек. Благодаря вашему полу, никто не обратил на Вас особого внимания.'
    stop movie
    hide movie
    $ move(curloc)    

label event_loc_changeRoom_20_low1:
    show changeRoom
    python:
        st1 = getChar('female')
        st1 = getChar('female')
        st1 = getChar('female')
        st1.incLoy(10)
        st1.incFun(10)
        st1.incLoy(10)
        st1.incFun(10)
        st1.incLoy(10)
        st1.incFun(10)
        player.incCorr(1)
        player.incLust(10)        
    show expression 'pic/locations/school/changeRoom/lo1.jpg' at top as tempPic
    'Три киски очевидно лучше чем одна! - подумали вы, заходя в раздевалку и наблюдая за тем, как ваши ученицы переодеваются.'
    'Очень странный способ, но в конце концов школьными правилами он не оговаривается.'
    $ move(curloc)

label event_loc_changeRoom_20_low2:
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
        'Наказать': # в оригинале было "Смотреть" но по коду учеников наказывают
            'Под вашим пристальным взглядом задор мальчишек как то скукожился и увял, и они, извинившись перед школьницами по быстренькому свалили.'
            'Жаль, вы были готовы насладиться небольшим шоу. Хотя девушки сердечно поблагодарили вас за своевременное появление.'
            python:
                st1.incLoy(5)
                st2.incLoy(5)
                st3.incLoy(5)

                scoldWho = [st4,st5,st6,st7,st8,st9]
                st4.incFun(-10)
                st4.incLoy(-5)
                st5.incFun(-10)
                st5.incLoy(-5)
                st6.incFun(-10)
                st6.incLoy(-5)
                st7.incFun(-10)
                st7.incLoy(-5)
                st8.incFun(-10)
                st8.incLoy(-5)
                st9.incFun(-10)
                st9.incLoy(-5)
        'Уйти':
            python:
                st1.incLoy(-5)
                st2.incLoy(-5)
                st3.incLoy(-5)

                st4.incFun(10)
                st4.incLoy(5)
                st5.incFun(10)
                st5.incLoy(5)
                st6.incFun(10)
                st6.incLoy(5)
                st7.incFun(10)
                st7.incLoy(5)
                st8.incFun(10)
                st8.incLoy(5)
                st9.incFun(10)
                st9.incLoy(5)                       
    $ move(curloc)

label event_loc_changeRoom_50_Mid1:
    show changeRoom
    python:
        st1 = getChar('female')
        st1.incLoy(10)
        st1.incFun(10)
        st1.incCorr(2)
        player.incCorr(2)
        player.incLust(15)        
    show expression 'pic/locations/school/changeRoom/mid1.jpg' at top as tempPic
    'Бросив случайный взгляд к дальней стенке раздевалки Вы заметили одну из учениц. [st1.fname] эротично стояла на носочках, слегка раздвинув ножки.'
    'Смущало не отсутвие на ней трусиков, всё таки мы в раздевалке, всякое случиться может. А густые капли спермы стекающие из её киски прямо по бёдрам. Особо крупная капля потянулась из её влагалища, прямо до пола.'
    player.say '[st1.fname], что то нехорошее случилось? - заботливо спросили вы, наблюдая за выражением лица девочки.'
    st1.say 'Нет, ну что Вы [player.name], просто у меня родители сегодня дома остались, вот мы с моим парнем и решили домой не ходить.'
    player.say 'Потнятно... - протянули вы, - Ну хорошо... В случае чего, это лучше делать в гостинице, хорошо?'
    '[st1.fname] радостно кивнула, сделала неуклюжий реверанс и скрылась в душе.'

    $ move(curloc)    

label event_loc_changeRoom_50_Mid2:
    show changeRoom
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.incLust(15)
        player.incCorr(2)
    show expression 'pic/locations/school/changeRoom/mid2.jpg' at top as tempPic
    'Вы вроде бы хотели переодеться, но теперь не знаете, насколько это удобно, переодеваться перед столь страстно трахающейся парочкой.'
    '[st1.fname] и [st2.fname] не ображая ни на кого внимания, предаются страстным ласкам прямо на лавочке в раздевалке. Вам плохо видно, но кажется член парня едва помещается в узенькую киску девушки, хотя обилие выделяемой ей смазки безусловно помогает процессу.'
    menu:
        'Наказать': # в оригинале было "Смотреть" но по коду учеников наказывают
            'Под вашим пристальным взглядом задор мальчишек как то скукожился и увял, и они, извинившись перед школьницами по быстренькому свалили.'
            'Жаль, вы были готовы насладиться небольшим шоу. Хотя девушки сердечно поблагодарили вас за своевременное появление.'
            python:
                st1.incFun(-10)
                st1.incLoy(-5)
                st2.incFun(-10)
                st2.incLoy(-5)  

                scoldWho = [st1,st2]
        'Оставить их в покое':
            python:
                st1.incFun(10)
                st1.incLoy(5)
                st1.incCorr(2)
                st2.incFun(10)
                st2.incLoy(5)
                st2.incCorr(2)                    
    $ move(curloc)

label event_loc_changeRoom_75_Hi1:
    show changeRoom
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('female')
        st5 = getChar('female')
        st1.incLoy(15)
        st1.incFun(15)
        st1.incCorr(3)
        st2.incLoy(15)
        st2.incFun(15)
        st2.incCorr(3)
        st3.incLoy(15)
        st3.incFun(15)
        st3.incCorr(3)
        st4.incLoy(15)
        st4.incFun(15)
        st4.incCorr(3)                
        st5.incLoy(15)
        st5.incFun(15)
        st5.incCorr(3)
        player.incCorr(3)
        player.incLust(20)        
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
        'Наказать': # в оригинале было "Смотреть" но по коду учеников наказывают
            'Под вашим пристальным взглядом задор мальчишек как то скукожился и увял, и они, извинившись перед школьницами по быстренькому свалили.'
            'Жаль, вы были готовы насладиться небольшим шоу. Хотя девушки сердечно поблагодарили вас за своевременное появление.'
            python:
                player.incCorr(1)
                player.incLust(10)
                st1.incLoy(5)
                st2.incLoy(5)
                st3.incLoy(5)

                scoldWho = [st4,st5,st6,st7,st8,st9]
                st4.incFun(-10)
                st4.incLoy(-5)
                st5.incFun(-10)
                st5.incLoy(-5)
                st6.incFun(-10)
                st6.incLoy(-5)
                st7.incFun(-10)
                st7.incLoy(-5)
                st8.incFun(-10)
                st8.incLoy(-5)
                st9.incFun(-10)
                st9.incLoy(-5)
        'Смотреть':
            hide tempPic
            show expression 'pic/locations/school/changeRoom/hi2_1.jpg' at top as tempPic
            'Видя, что вы не собираетесь их наказывать, парни смелее берутся за дело.'
            'Левая парочка учеников концентрируется на груди и киске школьницы, [st2.fname] стоящая посередине взвизгивает, когда [st5.fname] сжимает её грудь, а [st7.fname] вводит свои пальцы во влагалище, отодвинув в сторону облегающую ткань купальника.'
            '[st3.fname] начинает шумно дышать, когда два парня справа начинают ласкать её груди.'
                
            menu:
                'Смотреть дальше': #тут скорее всего должно быть условие проыеряющее развратность директора, я не знаю с чем сверять его
                    player.say 'Ну же мальчики, не стесняйтесь, вы так и собираетесь их тискать, как первоклашки? - подзадориваете вы учеников.'
                    hide tempPic
                    show expression 'pic/locations/school/changeRoom/hi2_2.jpg' at top as tempPic    
                    'В ответ на ваши слова, парни решают слегка увлажнить девушек, сливаясь с ними в страстных поцелуях. Ну точнее кто то сливается, а кто то продолжает ласкать школьниц, не давая им ни минуты продыху.'
                    'Вы отчётливо видите, что девушки прилично возбудились, несмотря на первоначальное сопротивление. Или же оно было наигранное?'

                    menu:
                        'Наблюдать': #тут скорее всего должно быть условие проыеряющее развратность директора, я не знаю с чем сверять его
                            player.say 'Вы меня собираетесь чем нибудь удивлять, или мне до конца дня наблюдать ваши пуританские ласки? - в очередной раз подгоняете вы школьников, увлёкшихся предварительными ласками.'
                            hide tempPic
                            show expression 'pic/locations/school/changeRoom/hi2_3.jpg' at top as tempPic    
                            'Парни наконец оторвались от поцелуев, и нагнули повизгивающих то ли от возмущения, то ли от возбуждения девушек.'
                            st4.say 'Давайте, сучки, подставляйте свои пёзды! - довольно грубо крикнул первый, доставая из штанин увесистый болт.'
                            st5.say 'Да, мы уже заждались! - сказал второй, начав тереть свой член о влажную киску школьницы.'
                            'Третий не сказал ничего, а с тихим стоном засунул свой ствол крайней девушке.'

                            menu:
                                'Ну наконец то!': #тут скорее всего должно быть условие проыеряющее развратность директора, я не знаю с чем сверять его
                                    hide tempPic
                                    show expression 'pic/locations/school/changeRoom/hi2_4.jpg' at top as tempPic    
                                    'Парни яростно долбили своих одноклассниц, не обращая ни на вас, ни на их стоны никакого внимания. Девчёнки подвизгивали от удовольствия, и из их кисок стекала смазка вперемешку с потом.'
                                    'Вся раздевалка была наполнена хлюпанием, стонами и криками, заводящими вас до ужаса. Ваша рука невольно опустилась к киске и начала её ласкать.'
                                    'Наконец парни синхронно издали победные хрипы, и их члены наполнили матки девушек спермой. Постанывая после оргазмов школьницы, опустились на пол, не в силах двигаться.' 
                                    $ player.incLust(20)
                                    $ player.incCorr(3)

                                    if player.getCorr > 60:
                                        'Ваше внимание привлекли топорщащиеся джинсы оставшейся троицы, которые так и не получили сладкого.'
                                        'Вы не смогли сдержать свою страсть, и не отрывая взгляда от топорщащихся штанов, при нялись раздеваться. Глядя на вас, ученики быстро смекнули в чём дело, и скинули с себя всю одежду тоже.'
                                        hide tempPic
                                        show movie
                                        play movie "pic/locations/school/changeRoom/hi2_5.gif.webm" loop
                                        'Вскоре вы уже с наслаждением прыгали на члене, в то время, как два остальных тёрлись о ваши груди и лицо, заводя вас всё сильнее.'
                                        'Твёрдый ствол плавно двигался в вашей киске, проникая своей, разбухшей от возбуждения головокой, всё глубже. Вы потеряли связь с реальностью, для вас существовал только этот, прекрасный член, таранящий ваше возбуждённое тело.'
                                        stop movie
                                        hide movie   
                                        show expression 'pic/locations/school/changeRoom/hi2_6.png' at top as tempPic
                                        'Одному из парней надоело бездействовать, и он затолкнул свой член вам в рот. Вы в принципе не слишком сопротивлялись, покорно заглотив угощение.' 
                                        'В это время к вашей незанятой попке пристроился третий парень и надавил головкой на анус. Вы слегка вздрогнули, когда его член плавно вошёл, расширяя попку. Ощущение заполненности всех отверстий одновременно буквально свело вас с ума, и вы принялись кончать, беспорядочно ёрзая на пронзивших вас членах, доставляя им и себе ни с чем не сравнимое удовольствие.'
                                        'Не успев отойти от первого оргазма, вас немедленно накрыл второй, когда дырочки начали заполняться спермой. Потом третий, когда члены вытащили и из дырочек начало вытекать заполнявшее их семя.'
                                        'Вы пришли в себя спустя несколько минут, удивляясь тому, что позволили себе заняться сексом аж с тремя парнями сразу.'
                                        $ player.incCorr(5)
                                        $ player.incLust(-100)
                                        $ player.incFun(10)
                                        $ player.incEnergy(-200)
                                        $ player.coverSperm('лицо','рот','попа','вагина','ноги')

                                'Уйти':
                                    python:
                                        player.incCorr(2)
                                        player.incLust(15)

                                        st1.incLoy(-10)
                                        st2.incLoy(-10)
                                        st3.incLoy(-10)

                                        st4.incFun(15)
                                        st4.incLoy(10)
                                        st5.incFun(15)
                                        st5.incLoy(10)
                                        st6.incFun(15)
                                        st6.incLoy(10)
                                        st7.incFun(15)
                                        st7.incLoy(10)
                                        st8.incFun(15)
                                        st8.incLoy(10)
                                        st9.incFun(15)
                                        st9.incLoy(10) 

                        'Уйти':
                            python:
                                player.incCorr(2)
                                player.incLust(15)

                                st1.incLoy(-10)
                                st2.incLoy(-10)
                                st3.incLoy(-10)

                                st4.incFun(15)
                                st4.incLoy(10)
                                st5.incFun(15)
                                st5.incLoy(10)
                                st6.incFun(15)
                                st6.incLoy(10)
                                st7.incFun(15)
                                st7.incLoy(10)
                                st8.incFun(15)
                                st8.incLoy(10)
                                st9.incFun(15)
                                st9.incLoy(10)

                'Уйти':
                    python:
                        player.incCorr(2)
                        player.incLust(15)

                        st1.incLoy(-10)
                        st2.incLoy(-10)
                        st3.incLoy(-10)

                        st4.incFun(15)
                        st4.incLoy(10)
                        st5.incFun(15)
                        st5.incLoy(10)
                        st6.incFun(15)
                        st6.incLoy(10)
                        st7.incFun(15)
                        st7.incLoy(10)
                        st8.incFun(15)
                        st8.incLoy(10)
                        st9.incFun(15)
                        st9.incLoy(10) 

        'Уйти':
            python:
                player.incCorr(1)
                player.incLust(10)

                st1.incLoy(-5)
                st2.incLoy(-5)
                st3.incLoy(-5)

                st4.incFun(10)
                st4.incLoy(5)
                st5.incFun(10)
                st5.incLoy(5)
                st6.incFun(10)
                st6.incLoy(5)
                st7.incFun(10)
                st7.incLoy(5)
                st8.incFun(10)
                st8.incLoy(5)
                st9.incFun(10)
                st9.incLoy(5)         
    $ move(curloc)    