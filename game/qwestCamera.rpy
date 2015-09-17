init:
    screen showSeller: # скрин, который должен добавиться на текущую локацию
        fixed:
            imagebutton:
                idle im.MatrixColor('pic/events/shop/seller.png', im.matrix.opacity(0.5))
                hover im.MatrixColor('pic/events/shop/seller.png', im.matrix.opacity(1.0)) 
                action [Jump('getCam')] xalign 1.0 yalign 1.0

label qwest_loc_shop_cameraQwest: # дублирующая локация
    if is_camera in [1,2]:
        show shop
        show screen showSeller
        call screen shop
    $ renpy.jump(curloc)

label getCam: # Сам эвент
    $clrscr()
    $ p = player
    show shop as bg
    if is_camera == 1:
        'Вы подходите к продавцу, как вам и посоветовала ваша ученица.'
        show expression 'pic/events/shop/seller.png' at right as char1
        show expression getCharImage(player,'dialog') as char2
        p.say 'Мне говорили, что вы торгуете "особым" товаром...'
        seller 'Я торгую многими вещами, пройдёмте, это не разговор для лишних ушей и глаз.'
        'Продавец идёт в подсобное помещение, маня вас за собой.'
        show expression im.Scale('pic/events/shop/2.jpg',1200,768) as bg
        show expression 'pic/events/shop/seller.png' at right as char1
        show expression getCharImage(player,'dialog') as char2
        seller 'Так что именно вы хотели приобрести?'
        p.say 'Камеру. Камеру скрытого наблюдения.'
        seller 'Тоже любите подглядывать, а?'
        'Нахальный парень подмигивает вам.'
        seller 'В общем я просто так товар не продам ни за какие деньги. Мне нужно что то взамен, какая то гарантия... Скажем ролик с вами.'
        p.say 'Какого рода ролик? - удвилённо приподнимаете вы одну бровь.'
        seller 'Самого, что ни на есть копроментирующего толка! В наше время знаете ли довольно трудно достать действительно качественный материал по вуеризму!'
    else:
        show expression 'pic/events/shop/seller.png' at right as char1
        show expression getCharImage(player,'dialog') as char2
        p.say 'Я вернулась...'
        seller 'Ну я же говорил, сладкая! Пойдём! Моё предложение остаётся в силе!'
        show expression im.Scale('pic/events/shop/2.jpg',1200,768) as bg
    hide char1
    hide char2
    menu:
        'Э-э-э'
        'Согласиться сняться на камеру':
            'Вы нехотя соглашаетесь помастурбировать, но только с одним условием - не снимая трусов. Извращенец радостно соглашается, и расстилает матрац перед вами.'
            show expression 'pic/events/shop/1.jpg' at top as tempPic
            'Вам немного неловко, но эти камеры нужны позарез, так что вы снимаете с себя всё, кроме трусиков, и начинаете ласкать себе груди. Постепенно возбуждаясь, вы забываете о парне, который снимает вас на камеру, и запускаете руку в свои мокрые трусики.'
            p.say '"И когда они только успели?" - мимолётом думаете вы.'
            'Постепенно сознание затмевается пеленой похоти, и вот вы уже судорожно сжимая ножки кончаете прямо перед извращенцем.'
            hide tempPic
            show expression 'pic/events/shop/seller.png' at right as char1
            seller 'Спасибо за устроенное шоу, крошка! - улыбается извращенец, а вы видите, что на его штанах расплывается мокрое пятно.'
            seller 'Камеры можешь взять в любое время в соседнем помещении, я покажу. Но товар дорогой - по 2000 за штучку!'
            hide char1
            'Вам вдруг становится противно от того, что вы сделали, но по крайней мере Вы теперь можете купить эти чёртовы камеры.'
            'Остаётся надеятся, то это видео для личного просмотра, иначе вашей репутации не поздоровится.'
            python:
                is_camera = 3
                setRep(rand(1,10),-10)
                p.setCorr(2)
                p.setLust(-100)
        'Предложить отсосать ему':
            show expression 'pic/events/shop/seller.png' at right as char1
            show expression getCharImage(player,'dialog') as char2
            p.say 'Что то я не особо уверена в твоей добропорядочности и в том, что ты не выложишь это видео в сеть.'
            seller 'Я? Да за кого вы меня принимаете?'
            p.say 'За извращенца. Так что давай лучше я тебе прям счас отсосу без камер и без свидетелей.'
            seller 'Я? То есть мне? Да!'
            hide char1
            hide char2
            'Парень торопливо расстёгивает свои штаны, вываливая наружу волосатый член.'
            show expression 'pic/events/shop/3.jpg' at top as tempPic
            'Как только вы приближаетесь к его паху, в нос ударяет сильный запах немытых яиц и мускуса.'
            p.say '"Мда, у этого парня давно ничего не было", - мелькает у вас мысль, перед погружением члена в рот.'
            'После начала его движений у вас остаётся только одно желание - не задохнуться. Причём не задохнуться не только от запаха, но и от того, что его скакун достаёт чуть ли не до желудка.'
            'Парень с силой вгоняет свой орган Вам в рот, постанывая при этом от удовольствия.'
            seller 'Да, детка, да, соси его сильнее, крошка, - шепчет он в пылу страсти.'
            show expression 'pic/events/shop/4.jpg' at top as tempPic
            'Наконец долгое воздержание оказывает своё действие, парень отстраняется, и начинает буквально заливать вас своей спермой как из брасбойта.'
            'Лицо, рот, очки, груди. Ничто не могло укрыться от его выстрелов. Вам уже было ни до чего, широко разевая рот вы пытались отдышаться.'
            show expression 'pic/events/shop/seller.png' at right as char1
            seller 'Спасибо за инициативу, крошка! - улыбается извращенец, вытирая свой член о ваши волосы.'
            seller 'Камеры можешь взять в любое время в соседнем помещении, я покажу. Но товар дорогой - по 2000 за штучку!'
            'Вам вдруг становится противно от того, что вы сделали, но по крайней мере теперь чёртовы камеры доступны к покупке.'
            python:
                is_camera = 3
                p.setCorr(5)
                p.coverSperm('лицо','рот','грудь')
                move(curloc)
        'Указать ему его место' if player.getCorr() > 35:
            'todo'
            jump getCam
        'Уйти':
            p.say 'Да пошёл ты к чёрту!'
            seller 'Ты ещё вернёшься, сладкая! Вы всегда возвращаетесь! - кричит вам парень вслед.'
            $ is_camera = 2
    $ move(curloc)
        