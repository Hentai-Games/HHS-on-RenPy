label event_loc_pool_0_no1:
    show pool
    python:
        t = getChar('female','teacher')
        t.incLoy(1.5)
        player.incCorr(0.5)

    show expression 'pic/locations/school/pool/no1.jpg' at top as tempPic
    '[t.fname] [t.lname] отдыхает в бассейне лёжа на надувном матраце. Ну чтож, учителям тоже не чужд отдых.'
    if player.getCorr() > 30:
        player.say '"Тем более такими формами можно совратить не то что юного ученика, даже умирающий старец обзавёлся бы нешуточной эрекцией."'
        'Между делом Вы немного поболтали с учительницей, чем привлекли много взглядов к её фигуре.'

    $ move(curloc)
    
label event_loc_pool_0_no2:
    show pool
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLoy(5)
        st2.incLoy(5)
        st1.incFun(5)
        st2.incFun(5)

    show expression 'pic/locations/school/pool/no2.jpg' at top as tempPic
    '[st1.fname] и [st2.fname]  устроили водный бой! Путь повеселяться, девочки заслужили.'

    $ move(curloc)
    
label event_loc_pool_0_no3:
    show pool
    python:
        st1 = getChar('female')
        st1.incLoy(5)
        st1.incFun(5)

    show expression 'pic/locations/school/pool/no3.jpg' at top as tempPic
    '[st1.fname] плавает на своей надувной акуле. Вы перекинулись с ней парой фраз.'
    if player.getCorr() > 30:
        'Совершенно не заостряя внимание на том, что плавник акулы можно использовать не только как средство удержания на воде, но и несколько другими способами.'
        $ player.incCorr(0.5)
        $ player.incLust(5)

    $ move(curloc)
    
label event_loc_pool_0_no4:
    show pool
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLoy(5)
        st2.incLoy(5)
        st1.incFun(5)
        st2.incFun(5)

    show expression 'pic/locations/school/pool/no4.jpg' at top as tempPic
    '[st1.fname] сейчас расплачется, из за того, что проиграла водную гонку своей подруге. Вы замечаете, что [st1.fname] похоже не сильно обрадована своим выигрышем.'
    if player.getCorr() > 30:
        'А ещё Вы замечаете, что [st1.fname] похоже надела купальник немного меньшего, чем следовало размера, и её нижние губки явно выделяется на форме трусиков. А ещё вы замеаете, что другие это тоже замечают. Замечательное замечание!'
        $ player.incCorr(0.5)
        $ player.incLust(5)
        $ st1.incLust(5)

    $ move(curloc)
    
label event_loc_pool_0_no5:
    show pool
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLoy(-5)
        st2.incLoy(-5)
        st1.incFun(-5)
        st2.incFun(-5)

    show expression 'pic/locations/school/pool/no5.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] решили устроить "мокрые игры". Вы пресекаете подобные игры вне бассейна. Кто то может и подскользнуться!'
    if player.getCorr() > 30:
        'А ещё кто то может перевозбудиться. Вы уже почти пожалели, что прекратили их игру.'
        $ player.incCorr(-0.5)
        $ player.incLust(-5)

    $ move(curloc)

label event_loc_pool_0_no6:
    show pool
    python:
        st1 = getChar('female')

        st1.incLoy(5)
        st1.incFun(5)
        st1.incCorr(0.5)

        player.incCorr(0.5)
        player.incLust(5)
    show expression 'pic/locations/school/pool/no6.jpg' at top as tempPic
    'Вы кинули взгляд на купающихся учеников, и увидели как [st1.fname] вылазит из бассейна. Всё бы ничего, только вот её купальник немного задрался, открывая вид на розовую щёлку. Заметив Ваш красноречивый взгляд и его причину, девочка засмущалась и убежала в раздевалку, поправляя купальник на ходу.'

    $ move(curloc)

label event_loc_pool_0_no7:
    show pool
    python:
        st1 = getChar('female')
        st1 = getChar('female')
        
        st1.incLoy(5)
        st1.incFun(5)

        st2.incLoy(5)
        st2.incFun(5)

    show expression 'pic/locations/school/pool/no7.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] играют в "кто просидит дольше под водой". И дураку понятно, что [st1.fname] не имеет никаких шансов на выигрышь. Чтобы дело не закончилось утоплением, вы выдурнули её из воды, и посоветовали не играть в подобные игры.'

    $ move(curloc)

label event_loc_pool_30_low1:
    show pool
    python:
        st1 = getChar('female')

        player.incCorr(1)
        player.incLust(10)
    show expression 'pic/locations/school/pool/low1.jpg' at top as tempPic
    '[st1.fname] отстранённо запускала свои пальчики вдали от чужих, но не от ваших глаз. Вы с удовольствием наблюдали, как её пальчики медленно скользили по влажной после бассейна киске, аккуратно проскальзывая внутрь.'

    menu:
        'Пусть себе наслаждается': # if player.getCorr > 40:
            'Вы решили не мешать ученице, и продолжили наблюдать за купающимися учениками.'
            $ st1.incLoy(10)
            $ st1.incFun(10)
            $ st1.incCorr(1)
            $ hadSex(st1)

        'Наказать':
            $ st1.incLoy(-5)
            $ st1.incFun(-5)
            $ scoldWho = [st1]
    $ move(curloc)

label event_loc_pool_30_low2:
    show pool
    python:
        st1 = getChar('female') # в оригинале был учитель

        player.incCorr(1)
        player.incLust(10)
    show expression 'pic/locations/school/pool/low2.jpg' at top as tempPic
    '[st1.fname] явно не выглядит довольной своим китайским купальником. Точнее не им, влагоустойчивостью его покраски.'

    menu:
        'Ну прозрачный, ну и что?': # if player.getCorr > 40:
            '[st1.fname] ещё долго стояла перед всем бассейном живописно описывая китайцев, красивших её купальник'
            $ st1.incLoy(10)
            $ st1.incFun(10)
            $ st1.incCorr(1)
            $ hadSex(st1)

        'Наказать':
            $ st1.incLoy(-5)
            $ st1.incFun(-5)
            $ scoldWho = [st1]
    $ move(curloc)

label event_loc_pool_30_low3:
    show pool
    python:
        st1 = getChar('female') # в оригинале был учитель

        player.incCorr(1)
        player.incLust(10)
    show expression 'pic/locations/school/pool/low3.jpg' at top as tempPic
    'Возле душевой кабинки, вы обратили внимание на ученицу, которая увлеклась мытьём своей промежности и грудей. Немного полюбовавшись на неё, вы подумали, а не вмешаться ли в происходящий процесс?'

    menu:
        'Не вмешиваться': # if player.getCorr > 40:
            '[st1.fname] буквально на ваших глазах задрожала и кончила, медленно оседая под тугими струями душа.'
            $ st1.incLoy(10)
            $ st1.incFun(10)
            $ st1.incCorr(1)
            $ hadSex(st1)

        'Наказать':
            $ st1.incLoy(-5)
            $ st1.incFun(-5)
            $ scoldWho = [st1]
    $ move(curloc)

label event_loc_pool_30_low4:
    show pool
    python:
        st1 = getChar('female')
        st2 = getChar('male')

        player.incCorr(1)
        player.incLust(10)
    show expression 'pic/locations/school/pool/low4.jpg' at top as tempPic
    '[st1.fname] озорно заигрывает со своим парнем, слегка оттягивая свой купальник, чтобы тот смог насладиться её вставшими от холода сосками.'

    menu:
        'Оставить их в покое': # if player.getCorr > 40:
            '[st1.fname] доигралась до того, что смущённый [st1.fname], пряча ото всех свой вставший член поспешил скрыться в раздевалке.'
            $ st1.incLoy(10)
            $ st1.incFun(10)
            $ st1.incCorr(1)
            $ st2.incLoy(10)
            $ st2.incFun(10)
            $ st2.incCorr(1)            
            $ hadSex(st1)

        'Наказать':
            $ st1.incLoy(-5)
            $ st1.incFun(-5)
            $ st2.incLoy(-5)
            $ st2.incFun(-5)            
            $ scoldWho = [st1, st2] # в оригинале парня не наказывали, сдесь пойдет за компанию, что бы ей скучно не было) 
    $ move(curloc)

label event_loc_pool_50_mid1:
    show pool
    python:
        st1 = kupruvna
        st2 = getChar('male')
        
        st1.incLoy(15)
        st1.incFun(15)
        st1.incCorr(2)
        st2.incLoy(15)
        st2.incFun(15)
        st2.incCorr(2)            
        hadSex(st1, st2)
        
        player.incCorr(2)
        player.incLust(15)
    show expression 'pic/locations/school/pool/mid1.jpg' at top as tempPic
    'Сначала Вы обратили внимание на необычный купальник вашей учительницы. Потом Ваше внимание привлекло то, чем она занималась со своим учеником. Это конечно было похоже на растяжку, но откровенно говоря, весьма отдалённо.'
    player.say '[st1.fname] [st1.lname], чем Вы занимаетесь? - не смогли Вы удержаться и подошли к учительнице.'
    st1.say 'Эммм, ничем, просто [st2.fname] помогает мне выправить вывихнутое плечо, правда, [st2.fname]? - умоляюще смотрит она на парня.'
    st2.say 'Даааа, - как то слишком протяжно отвечает тот и слегка вздрагивает. Он только что кончил, в этом нет сомнения, несмотря на то, что с вашей похиции это незаметно.'
    player.say 'Будте добры в следующий раз заниматься "медициной" в специально отведённом для этого месте, - бросаете Вы покрасневшей учительнице и уходите.'
    
    $ move(curloc)

label event_loc_pool_50_mid2:
    show pool
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        
        st1.incLoy(15)
        st1.incFun(15)
        st1.incCorr(2)
        st2.incLoy(15)
        st2.incFun(15)
        st2.incCorr(2)            
        hadSex(st1, st2)
        
        player.incCorr(2)
        player.incLust(15)
    show expression 'pic/locations/school/pool/mid2.png' at top as tempPic
    'Вы зашли в бассейн, но по дороге решили заглянуть в душевую. Ох, какая красота! [st1.fname] восседала на своём парне, активно елозя по его слену своей киской, но не вводя его в себя.'
    'От активного трения об свой собственный живот и бутончик девушки, [st2.fname] незамедлительно кончил, прямо на ваших глазах. Вы решили оставить студентов в душе, ведь им ещё и отмывать свои перемазанные спермой тела!'
    
    $ move(curloc)

label event_loc_pool_50_mid3:
    show pool
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        
        st1.incLoy(15)
        st1.incFun(15)
        st1.incCorr(2)
        st2.incLoy(15)
        st2.incFun(15)
        st2.incCorr(2)            
        hadSex(st1, st2)
        
        player.incCorr(2)
        player.incLust(15)
    show expression 'pic/locations/school/pool/mid3.png' at top as tempPic
    'Маленькая [st1.fname] своей маленькой ножкой маленько довела одноклассника до маленькой кульминации в душе!'
    player.say '"И как он только на это согласился?" - думаете вы, глядя на то, как ножка девушки продолжает скользить по кончающему члену парня, и одновременно с этим, она выкручивает ему соски своими руками...'
    
    $ move(curloc)

label event_loc_pool_75_hi1:
    show pool
    python:
        st1 = bissektrisovna
        st2 = getChar('futa')
        st3 = getChar('futa')

        st1.incLoy(20)
        st1.incFun(20)
        st1.incCorr(3)
        st2.incLoy(20)
        st2.incFun(20)
        st2.incCorr(3)
        st3.incLoy(20)
        st3.incFun(20)
        st3.incCorr(3)                       
        hadSex(st1, st2)
        hadSex(st1, st3) # да же и не знаю как в таких ситуациях поступать когда 3 участника
        
        player.incCorr(3)
        player.incLust(20)
    show expression 'pic/locations/school/pool/hi1.jpg' at top as tempPic
    'Вы с некоторым удивлением замечаете вашу учительницу по английскому, которая предаётся совсем не детским ласкам со своими ученицами.'
    '[st2.fname] и [st3.fname] радостно заполняют ненасытную попу и рот учительницы своими членами. Вам безумно хочется присоединится к этой оргии, но авторитет - прежде всего!'
    
    $ move(curloc)

label event_loc_pool_75_hi2:
    show pool
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('female')
        st5 = getChar('female')

        st1.incLoy(20)
        st1.incFun(20)
        st1.incCorr(3)
        st2.incLoy(20)
        st2.incFun(20)
        st2.incCorr(3)
        st3.incLoy(20)
        st3.incFun(20)
        st3.incCorr(3)
        st4.incLoy(20)
        st4.incFun(20)
        st4.incCorr(3)  
        st5.incLoy(20)
        st5.incFun(20)
        st5.incCorr(3)                                                
        hadSex(st1, st2)
        hadSex(st2, st3) 
        hadSex(st1, st4) 
        hadSex(st1, st5) # тут вообще мозг сломаешь кто кого...

        player.incCorr(3)
        player.incLust(20)
    show expression 'pic/locations/school/pool/hi2.jpg' at top as tempPic
    $ penis = int(st1.body.parts['пенис'].size)
    'Проходя мимо душевой, Вы заметили, что сразу четыре девушки издеваются над бедным парнем. Ну как издеваются, самоудовлетворяются.'
    '[st2.fname] скачет на его [penis] сантиметровом члене, подвизгивая от удовольствия. А [st3.fname] помогает ей, массируя рукой маленький клитор.'
    'Одну руку захватила [st4.fname], положив себе на грудь, другой рукой удовлетворяется [st5.fname], запихивая непослушные пальцы себе во влагалище. Сам [st1.fname] громко стонет, и вам не совсем понятно, толи пытается так вырваться, толи активно подмахивает движениям скачущей на нём школьницы.'
    
    $ move(curloc)

label event_loc_pool_90_hi3:
    show pool
    python:
        st1 = getChar('male')
        st2 = getChar('male')
        st3 = getChar('male')
        st4 = getChar('male')
        st5 = getChar('male')
        st6 = getChar('female')
        st7 = getChar('female')
        st8 = getChar('female')
        st9 = getChar('female')
        st10 = getChar('female')

        st1.incLoy(20)
        st1.incFun(20)
        st1.incCorr(3)
        st2.incLoy(20)
        st2.incFun(20)
        st2.incCorr(3)
        st3.incLoy(20)
        st3.incFun(20)
        st3.incCorr(3)
        st4.incLoy(20)
        st4.incFun(20)
        st4.incCorr(3)  
        st5.incLoy(20)
        st5.incFun(20)
        st5.incCorr(3)
        st6.incLoy(20)
        st6.incFun(20)
        st6.incCorr(3)  
        st7.incLoy(20)
        st7.incFun(20)
        st7.incCorr(3)  
        st8.incLoy(20)
        st8.incFun(20)
        st8.incCorr(3)  
        st9.incLoy(20)
        st9.incFun(20)
        st9.incCorr(3)  
        st10.incLoy(20)
        st10.incFun(20)
        st10.incCorr(3)                                                                                          
        hadSex(st1, st6)
        hadSex(st2, st7) 
        hadSex(st3, st8) 
        hadSex(st4, st9)
        hadSex(st5, st10)

        player.incCorr(3)
        player.incLust(20)
    show expression 'pic/locations/school/pool/hi3.jpg' at top as tempPic
    player.say 'Во что я превратила школу...", - думаете вы, наблюдая за разворачивающейся перед вашими глазами оргии в душевой.'
    'Куда бы Вы не кинули взгляд, всюду юные тела наслаждаются друг другом в различных позах. Кто то лежит на полу, кто то стоит раком, где то у стены,  [st6.fname] отсасывает у какого то парня. В душевой стало очень жарко, но не от горячей воды, а от пламенного секса.'
    'У Вас даже язык не поворачивается, чтобы наказать школьников за то, что они делают. В конце концов именно этого вы и добивались, не так ли?'

    $ move(curloc)