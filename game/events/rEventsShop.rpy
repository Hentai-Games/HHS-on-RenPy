label event_loc_shop_0_no1:
    show shop
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')

        setFun(3,5)
    show expression 'pic/locations/shop/no1.jpg' at top as tempPic
    'Вы видите как [st1.fname], [st2.fname] и [st3.fname] сидят у магазина и читают какой-то модный журнал.'
    if st1.getCorr() > 25 or development == 1:
        'Ммм, как они облизывают эти мороженные...'
        $ player.incLust(5)
    $ move(curloc)
    
label event_loc_shop_0_no2:
    show shop
    python:
        st1 = getChar('female')
        st2 = getChar('female')

        st1.incFun(5)
        st2.incFun(5)
    show expression 'pic/locations/shop/no2.jpg'  as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] и [st2.fname] в отделе игрушек, судя по всему, выбирают подарок для младшего братишки.'
    if st1.getCorr() > 25 or development == 1:
        ' Только судя по заинтерисованному взгляду девочки, она не совсем о ракетах думает...'
        $ player.incLust(5)
    $ move(curloc)
    
label event_loc_shop_0_no3:
    show shop

    show expression 'pic/locations/shop/no3.jpg' at top as tempPic
    'Вы нескромно обращаете внимание на маму одного из своих подопечных. Выбирая себе сумку, она подарила посетителям магазина очень возбуждающую картину.'
    if st1.getCorr() > 25 or development == 1:
        ' Эта юбка так обтягивает ее ягодицы, что видно нижнее белье. Вы буквально чувствуете как между ножек становится все более влажно.'
        $ player.incLust(7)
    $ move(curloc)
    
label event_loc_shop_0_no4:
    show shop
    python:
        st1 = getChar('male')

        st1.incFun(5)
    show expression 'pic/locations/shop/no4.jpg' at top as tempPic
    '[st1.fname] пошёл за покупками с братом! Какой же он молодец!'

    $ move(curloc)

label event_loc_shop_0_no5:
    show shop
    python:
        st1 = getChar('female')

        st1.incFun(5)
    show expression 'pic/locations/shop/no5.jpg' at top as tempPic
    '[st1.fname] выбирает печенье. Вы не уверены в том, что видите рядом с ней. Нет, не в кошке, а в том, что рядом. По моему вы просто не выспались.'

    $ move(curloc)

label event_loc_shop_0_no6:
    show shop
    python:
        st1 = getChar('female')

    show expression 'pic/locations/shop/no6.jpg' at top as tempPic
    'Вы усмотрели как [st1.fname] выбрала новый томик манги, но едва дотягивается до верхней полки. Ой какие мы стали сердитые...'
    if st1.getCorr() > 25 or development == 1:
        ' Вы немного(секунд на двадцать) подвисли, опустив взгляд ей под юбочку...'
        $ player.incLust(5)

    menu:
        'Помочь ей':
            player.say '[st1.fname], давай попробую я, - с этими словами Вы, легко достаете мангу и протягиваете ее ученице.'
            st1.say 'Спасибо Вам!! Я едва дотягивалась до верхней полки, - [st1.fname] мило улыбнулась и побежала дальше. Следом неспешным шагом двинулись и вы. Приятно делать добрые дела!'
            
            $ st1.incLoy(5)
            $ st1.incFun(5)
        'Проигнорировать':
            'Вы делаете вид, как будто ничего не заметили. [st1.fname], попрыгав у полки, так и не достав книжку, с недовольным видом ушла вглубь магазина.'
            $ st1.incFun(-5)    
    $ move(curloc)

label event_loc_shop_0_no7:
    show shop
    python:
        st1 = getChar('female')
        st2 = getChar('male')

        st1.incFun(5)
        st2.incFun(5)
    show expression 'pic/locations/shop/no7.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] вместе покупают продукты. У девочки почему то повязка на глазу, интересно, это не [st2.fname] ей вдарил? Надо как нибудь поговорить с ним о поведении.'
    if st1.getCorr() > 25 or development == 1:
        ' "Покупают вместе, наверно и живут вместе. Живут вместе, наверное и трахаются вместе. А вот я и живу одна, и трахаюсь пока одна."'
        $ player.incLust(10)
    $ move(curloc)    

label event_loc_shop_0_no8:
    show shop
    python:
        st1 = getChar('female')

        st1.incFun(5)
    show expression 'pic/locations/shop/no8.jpg' at top as tempPic
    '[st1.fname] закупается выпечкой. Какая милая девочка!'
    if st1.getCorr() > 25 or development == 1:
        'Главное чтобы не располнела на этой выпечке, будет печально мять эти телеса, коли у меня всё таки найдётся к ней подход.'
        $ player.incLust(5)
    $ move(curloc)    

label event_loc_shop_0_no9:
    show shop
    python:
        st1 = getChar('female')
        st2 = getChar('male')

        st1.incFun(5)
        st2.incFun(5)
    show expression 'pic/locations/shop/no9.jpg' at top as tempPic
    'Интересная картина. [st1.fname] занимается уничтожением продуктов, а [st2.fname] занимается их оплатой. Мини конвеер просто, на зависть Генри Форду!'

    $ move(curloc)    

label event_loc_shop_0_no10:
    show shop
    python:
        st1 = getChar('female')
        st1.incFun(5)
    show expression 'pic/locations/shop/no10.jpg' at top as tempPic
    '[st1.fname] выбирает книги для покупки в книжном отделе. Вы подошли к ней, и поболтали немного о любимых рассказах.'
    if st1.getCorr() > 25 or development == 1:
        player.say '[st1.fname], обрати внимание - Камасутра, 10 дней Содома, 50 оттенков серого - это замечательные книги для прочтения!'
        
        $ player.incCorr(1)
        $ st1.incCorr(1)
        $ st1.incRep(-1)
    $ player.incLust(5)
    $ move(curloc)   

label event_loc_shop_0_no11:
    show shop
    $ st1 = getChar('female')
    show expression 'pic/locations/shop/no11.jpg'  as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Среди витрин Вы углядели молодую маму с кучей детей. Ей можно только посочувствовать, дети не дают ни минуты покоя.'
    
    if st1.getCorr() > 25 or development == 1:
        'Понаблюдав за ней, вы поняли, что детей еще не хотите, а вот такие трусики... Может быть!'
        $ player.incLust(5)

    $ move(curloc)    

label event_loc_shop_0_no12:
    show shop
    python:
        st1 = getChar('female')

        st1.incFun(5)
        st1.incLust(5)
        st1.incCorr(1)
    show expression 'pic/locations/shop/no12.jpg' at top as tempPic
    'Проходя мимо витрины с печатной эротической продукцией, вы заметили странно одетую девочку. За мгновение вы поняли зачем она одела очки и большой шарф, в котором вы ее раньше не видели.'
    'Эх, [st1.fname], [st1.fname]... Гормоны судя по всему разошлись не на шутку, а информации для их удолетворения взять неоткуда. Ну чтож, вы ее понимаете.'
    if st1.getCorr() > 25 or development == 1:
        'Облизнувшись, Вы подумали о том, что могли бы обучить ее сами. Кхм... неплохая мысль!'
        $ player.incLust(5)

    $ move(curloc)  

label event_loc_shop_0_no13:
    show shop
    python:
        st1 = getChar('female')

        st1.incFun(5)
    show expression 'pic/locations/shop/no13.jpg' at top as tempPic
    'Прямо на Ваших глазах [st1.fname] залезла в холодильник и уплетает сосиску. Неужели она настолько голодна?! Вы приостанавливаетесь в задумчимости : стоит ли указать на недопустимость подобного поведения, все таки за продукты сначала необходимо заплатить.'
    if st1.getCorr() > 25 or development == 1:
        'Какая у нее короткая юбочка... Мммммм... А чулочки судя по всем из маминого гардероба...'
        $ player.incLust(5)

    menu:
        'Мягко пожурить':
            'Вы незаметно подошли к ученице и тихим шепотом пояснили что так делать нельзя. [st1.fname] проглотила последний кусочек сосиски и кивнула Вам.'
            st1.say 'Простите, я уж очень проголодалась. А за сосиску я сейчас заплачу, - и девочка побежала в сторону касс, в то время как ваш взгляд провожал ее юбочку.'
        'Проигнорировать':
            'Вы делаете вид, как будто ничего не произошло, и вы ничего не заметили. Ученица с благодарностью смотрит на вас, и тянется за следующей сосиской. Вы незаметно уходите от холодильника.'
            $ st1.incLoy(5)    
    $ move(curloc)  