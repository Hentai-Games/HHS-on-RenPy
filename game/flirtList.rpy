init python:
    def getFlirtReaction(user):
        if user.getWill() > player.getCorr():
            user.incLoy(-1)
            if user.body.sex() == 'male':
                return user.name +' скептически посмотрел на Вас, явно не одобряя вашего поведения. Его лояльность к вам серьёзно упала.'
            else:
                return user.name +' скептически посмотрела на вас, явно не одобряя подобного поведения. Её лояльность к вам серьёзно упала.'
        else:
            user.incLoy(1)
            user.incCorr(0.2)
            return user.name + ' активно включается в ваш флирт, рассказывая какую то свою весьма нескромную историю. '

            
            
label flirt_male_0_1:
    show expression 'pic/events/flirt/m1.jpg' at top zorder 1 as tempPic
    'Вы наклоняетесь, так, чтобы он прекрасно видел ваши груди, и начинаете лёгкий флирт.'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_male_0_2:
    show expression 'pic/events/flirt/m2.jpg' at top zorder 1 as tempPic
    'Вы присаживаетесь, и начинаете поправлять свою обувь. Присаживаетесь так, чтобы [user.name] смог хорошо оценить ваши ножки.'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_male_0_3:
    show expression 'pic/events/flirt/m3.jpg' at top zorder 1 as tempPic
    'Вы "случайно" подвернули ногу, и припали на одно колено. Неплохой вид на трусики открылся для взора вашего собеседника.'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_male_20_3:
    show expression 'pic/events/flirt/m6.jpg' at top zorder 1 as tempPic
    'Ой, вы "случайно" упали. И у вас "случайно" задралась юбка до пояса. Какой конфуз!'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_male_20_4:
    show expression 'pic/events/flirt/m7.jpg' at top zorder 1 as tempPic
    'Вы постарались выбрать наиболее выгодную позу, которая одновременно подчёркивает вашу стройность, а так же открывает неплохой вид на короткие чулочки и попку!'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_male_20_5:
    show expression 'pic/events/flirt/m10.jpg' at top zorder 1 as tempPic
    'Вы совершенно случайно роняете ручку, и наклоняетесь, чтобы поднять её. Старо как мир, но действенно!'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_male_20_6:
    show expression 'pic/events/flirt/m11.jpg' at top zorder 1 as tempPic
    'Вы якобы совершенно случайно роняете тетрадку, и наклоняетесь, чтобы поднять её. В это время юбка задирается открывая взору ученика ваше белье. Старо как мир, но действенно!'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_male_20_7:
    show expression 'pic/events/flirt/m4.jpg' at top zorder 1 as tempPic
    'Вы буквально легли грудью на близлежащую поверхность, соблазняя его своим телом.'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_male_50_8:
    show expression 'pic/events/flirt/m8.jpg' at top zorder 1 as tempPic
    if user.age < 20:
        'Вы не стали терять время на ухаживания, а просто влезли своим языком в рот юноши, и положили его руку себе на грудь.'
    else:
        'Вы рассказали, что недавно позволили себе весьма фривольно повести себя с учеником! Не хочет ли ваш собеседник повторить опыт счастливца?'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_male_50_9:
    show expression 'pic/events/flirt/m12.jpg' at top zorder 1 as tempPic
    player.say '- А ты никогда не мечтал о сексе с директором?'
    $ pSize = user.body.parts['пенис'].size
    'Вы аккуратно кладёте руку на его ширинку, ощущая там [pSize] сентиметровый член.'
    player.say 'Я вот когда училась в школе, просто мечатала, чтобы наш директор оттрахал меня!'
    'Вы слегка сжимаете свою руку.'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_female_0_1:
    show expression 'pic/events/flirt/f1.jpg' at top zorder 1 as tempPic
    'Вы рассказываете, как недавно купили купальник, который после стирки сел так, что едва прикрывал ваши интимные места.'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_female_0_2:
    show expression 'pic/events/flirt/f4.jpg' at top zorder 1 as tempPic
    'Вы как бы невзначай намекаете, что не особо любите бюстгалтеры, и как раз сегодня не стали надевать его.'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_female_0_3:
    show expression 'pic/events/flirt/f6.jpg' at top zorder 1 as tempPic
    'Вы признаётесь, что иногда любите примерять свой школьный купальник. Правда вы из него давно выросли, поэтому груди вы оставляете оголёнными. Это выглядит так сексуально!'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_female_20_4:
    show expression 'pic/events/flirt/f2.jpg' at top zorder 1 as tempPic
    'Вы доверительно рассказываете, что есть у вас фетиш, как будто к вам пристаёт другая женщина. Не то, чтобы бы на что-то намекаете...'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_female_20_5:
    show expression 'pic/events/flirt/f3.jpg' at top zorder 1 as tempPic
    $ anyChar = getChar('female')
    'Вы рассказываете про то, что недавно переодеваясь в кабинете, вас заметил [anyChar.name]. Это было очень неловко, но в тоже время весьма интригующе!'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_female_20_6:
    show expression 'pic/events/flirt/f5.jpg' at top zorder 1 as tempPic
    $ anyChar = getChar('female')
    'Вы рассказываете, что любите делать снимки самой себя в зеркале топлесс, и интересуетесь, нет ли у вашей собеседницы подобного хобби?'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_female_20_7:
    show expression 'pic/events/flirt/f9.jpg' at top zorder 1 as tempPic
    $ anyChar = getChar('female')
    'Вы прозрачно намекаете на то, что отнюдь не всегда надиваете трусики на работу!'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat
    
label flirt_female_50_7:
    show expression 'pic/events/flirt/f7.jpg' at top zorder 1 as tempPic
    $ anyChar = getChar('female')
    'Вы признаётесь, что мастурбируя вы иногда представляете, что у вас есть член. И отдыхая после оргазма, капаете на себя лубрикантом, чтобы создать ощущения спермы на своём животике.'
    $ answer = getFlirtReaction(user)
    '[answer]'
    hide tempPic
    call screen show_stat