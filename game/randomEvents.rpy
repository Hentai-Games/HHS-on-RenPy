label event_loc_home_15_1:
    $ dynpicto = studs[0].picto
    studs[0].say "поймал1!"
    'пусто'
    $ move(curloc)

    
label event_loc_dreams_10_1:
    show expression ("pic/locations/home/dream/1.jpg") at top
    'На этот раз сон был о том, как вы купаетесь в деньгах с бывшей одноклассницей. Во сне вы немного перебрали шампанского, и теперь без зазрения совести позволяете себя лапать этому странному существу.'
    'Даже во сне вы умудрились смутиться, и, проснувшись, обнаружили приятную теплоту в трусиках.'
    $ player.stats.lust += 10
    $ move(curloc)

label event_loc_dreams_0_2:
    show expression ("pic/locations/home/dream/2.jpg") at top
    'Ужасный сон о красношапных, мальчиках терроризирующих пикачу, не дал вам нормально выспаться.'
    $ player.stats.energy -= 100
    $ move(curloc)
    
label event_loc_dreams_0_3:
    show expression ("pic/locations/home/dream/3.jpg") at top
    'Вам приснилась странная гравюра с японской женщиной под яблоней. Она навеяла вам воспоминания о матери.'
    'Развратные мысли немного развеялись и вы отлично выспались'
    $ player.stats.energy += 100
    $ player.stats.lust -= 10
    $ move(curloc)
    
label event_loc_dreams_5_4:
    show expression ("pic/locations/home/dream/4.jpg") at top
    'Вам приснился бывший бойфренд. Ну не то, чтобы именно он, но вы искренне надеетесь на это.'
    'Не хотелось бы думать, что эти тропические температуры в паху вызваны незнакомцем. Ооох....'
    'Ваше желание увеличилось'
    $ player.stats.lust += 10
    $ move(curloc)

label event_loc_dreams_0_5:
    show expression ("pic/locations/home/dream/5.jpg") at top
    'Замечательный сон о барбекю на пляже настроил вас на благодушный лад с утра. Только перекусить захотелось...'
    $ move(curloc)
    
label event_loc_dreams_20_6:
    show expression ("pic/locations/home/dream/6.jpg") at top
    'Вам приснилась стоящая у замёрзшего пруда странная девочка с кожанными крылышками. Маленькие ледяные олени у озера вызвали у вас только симпатию.'
    'Странный сон, оказывается суккубы способны вызывать не только желание'
    'Ваше желание немного уменьшилось'
    $ player.stats.lust -= 10
    $ move(curloc)
    
label event_loc_dreams_25_7:
    show expression ("pic/locations/home/dream/7.jpg") at top
    'Это был ужасно беспокойный и вместе с тем развратный сон. Всю жизнь вы прожили как демонолог. Причём МУЖСКОГО пола. В последнюю ночь вы решили себя побаловать маленькой суккубой!'
    'Боже, как она ласково облизывала ваш 20 сантиметровый член!'
    'Проснувшись вы с удивлением понимаете, что даже жалеете о том, что вам никогда не испытать удовольствия от пламенного язычка на головке. При воспоминании об этом соитии, у вас начинает течь по ножкам'
    'Ваше желание максимально'
    $ player.stats.lust = 100
    $ move(curloc)
    
label event_loc_dreams_40_8:
    show expression ("pic/locations/home/dream/8.jpg") at top
    'Это был пикантный и волшебный сон. В нём вы оказались маленькой колдуньей 200 лет от роду. За столь долгий период жизни, вы настолько пресытились ласками женщин и удовольствиями от мужчин, что решили наградить одну из своих любимых рабынь членом.'
    'Не в силах совладать с новыми ощущениями от одновременного вида огромной плоти и грудей, вы занимались любовью где это только было возможно. На ковре у камина, прижимаясь спиной к прохладной стенке темницы, даже сидя за роялем - не могли удержать бешенного желания!'
    'Как же было прекрасно скользить своими маленькими булочками по огромному уду рабыни. Как нежно трепетали стенки влагалища, когда в него вторгалась набухшая головка члена!'
    'Вы даже ничуть не расстроились, что вас разбудил не будильник, а конвульсии оргазма.'
    'Утренний оргазм уменьшил желание, но увеличил развращённость'
    $ player.stats.lust -= 50
    $ player.incCorr(1)
    $ move(curloc)
    
label event_loc_dreams_15_9:
    show expression ("pic/locations/home/dream/9.jpg") at top
    'Вам приснилось, что вас застукали ученики, когда вы возвращались утром с рейверской вечеринки. Непонятно почему, но стыдно до сих пор.'
    'Развратность уменьшилась.'
    $ player.decCorr(1)
    $ move(curloc)
    
label event_loc_dreams_0_10:
    show expression ("pic/locations/home/dream/10.jpg") at top
    'Вам снится, что вас уволили, и ваши ученики с радостью выпроваживают вас за ворота школы. Ужасно, просто ужасно. Вы проснулись в холодном поту.'
    $ move(curloc)
    
label event_loc_dreams_25_11:
    show expression ("pic/locations/home/dream/11.jpg") at top
    'В этом сне вы были королевой. Вызванные вами специально отобранные рабы получили совершенно неоднозначный приказ к исполнению.'
    'И вот, ваши великолепные ножки, привыкшие к ежедневным лошадиным скачкам, задраны вверх и мощная плоть раба вторгается в королевское лоно, раздвигая нежные складки, полностью заполняя собой высокородную промежность.'
    'Остальные два раба ждали своей очереди, по опыту зная, что одним колом Ваше Королевское Величество не насытится. И бесконечные оргазмы во сне были прерваны одним, но наяву.'
    'Утренний оргазм уменьшил желание, но увеличил развращённость.'
    $ player.stats.lust -= 30
    $ player.incCorr(1)
    $ move(curloc)
    
label event_loc_dreams_50_12:
    show expression ("pic/locations/home/dream/12.jpg") at top
    'Вам снится сон, в котором вы нашли огромный, перевитый венами, мужской половой орган. Он возвышался над вами, такой живой, с бархатистой кожей, блестящей головкой и она, вы знали, жаждалa прикосновений.'
    'Не выдержав, вы как смогли приласкали его, гладя ладонями, всем телом, обвиваясь вокруг этого столба. И вашей наградой был поток пряно-пахнувшей белой жидкости, его было много, безумно много и вы были счастливы.'
    'Проснувшись вы удивились странному сну, но в паху приятно покалывало.'
    $ player.stats.lust += 20
    $ move(curloc)
    
label event_loc_dreams_60_13:
    show expression ("pic/locations/home/dream/13.jpg") at top
    'Сегодня в вашем сне ученики младших классов устроили небольшие соревнования, о которых, вы уверены, они не будут рассказывать родителям. Вас это ничуть не смутило, ведь чем бы дитя не тешилось.'
    'Развращенность немного повысилась.'
    $ player.incCorr(0.5)
    $ move(curloc)
    
label event_loc_dreams_40_14:
    show expression ("pic/locations/home/dream/14.jpg") at top
    'В этом сне в женском туалете вашей школы собрались девушки, с.. кхм... довольно большими отклонениями. Особых запах заполнял все пространство, они вас явно не ждали, но даже, как вам показалось, обрадовались.'
    'Проснувшись, вы вздохнули, думая о сочетании упругих грудок и великолепного члена.'
    $ player.stats.lust += 10
    $ move(curloc)
    
label event_loc_dreams_25_15:
    show expression ("pic/locations/home/dream/15.jpg") at top
    'Вам снится компьютерная игра. Да это так: есть шкала жизней, особых ударов, имя персонажа, но вот только удары тут наносятся вполне определенные, и судя по всему, кто первый ощутит взрыв оргазма - тот и победил.'
    'Проснувшись, вы выкинули увиденное из головы. Игры играми, но жизнь гораздо интереснее.'
    $ player.stats.lust += 10
    $ move(curloc)
    
label event_loc_dreams_10_16:
    show expression ("pic/locations/home/dream/16.jpg") at top
    'Вам сниться свадьба. Парадно одетый жених, одобрительно посматривает на свою половинку в довольно интересном платье, открывающим не менее интересное положение невесты. "Надеюсь у них все будет хорошо", - и с этой мыслью сон завершается.'
    'Вы отлично выспались.'
    $ player.stats.energy += 150
    $ move(curloc)
    
label event_loc_dreams_0_17:
    show expression ("pic/locations/home/dream/17.jpg") at top
    'Вам сниться прогулка по городу в закатном свете. Чистый воздух, приятный шелест листвы, длинные тени сопровождают вас в этой прогулке и наполняют душу покоем.'
    'Вы отлично выспались.'
    $ player.stats.energy += 150
    $ move(curloc)
    
label event_loc_dreams_70_18:
    show expression ("pic/locations/home/dream/18.jpg") at top
    'В сегодняшнем сне, будучи дриадой, невинные заигрывания с сатиром привели к неожиданному финалу: поймав и уложив вас на покрытую зеленое возвышение, его пальцы снизу раздвинули половые губы, и что-то очень твердое и тупое уперлось в вашу вагину.'
    'Вы сделали последнюю попытку вырваться, понимая, что проникновение ТАКОГО члена будет непростым. Бесполезно. На ощущение собственной беспомощности и бессилия, нижнее естество отреагировало предательски - влагалище намокло горячей сладостью. И сатир ПРОНИК...'
    'Вы никогда не сталкивалась с членом такой толщины. Нижние губы обхватившие член, оказались натянутыми так, что первым ощущением от проникновения была боль. Его первое движение было глубоким и медленным. Насильник явно смаковал его.'
    'Распиравший вас член двигался все дальше и дальше вглубь, уперся в заднюю стенку матки. В первый раз показалось, что член заполнил вас всю, вы застонали, рогатый отпрянул своим тазом назад, высвобождая член, густо смазанный соками вожделения и снова загнал его внутрь, продолжая насиловать вас.'
    'Ваше желание максимально.'
    $ player.stats.lust = 100
    $ player.incCorr(1)
    $ move(curloc)
    
label event_loc_dreams_80_19:
    show expression ("pic/locations/home/dream/19.jpg") at top
    'Вам снится как шесть девушек(в числе которых и вы) нежно ублажают парня с немалым достоинством. В конечном итоге ласки прекрасных див приводят к настоящему взрыву страсти, мощным потоком оросив всех !!!'
    'Проснувшись вы почувствовали как теплая, щемящая и сладострастная волна, зародившись между ног, распространяется по всему телу. Утренний оргазм уменьшил желание, но увеличил развращённость.'
    $ player.stats.lust -= 50
    $ player.incCorr(0.5)
    $ move(curloc)
    
label event_loc_dreams_0_19:
    if player.stats.corr < 20:
        show expression ("pic/locations/home/dream/200.jpg") at top
        'В этом сне вы смиренно просили Господа избавить вас от соблазнов, одолевающих вас каждую минуту, просили отвратить от вас искушение, не вводить во грех. Вы проклинали ваше тело, которое столько чувствительно, столь притягательно, ваши округлые бедра, холмики больших грудей с выпирающими сосками. Ведь вам так трудно удержаться от собственных ласк. Молитва продолжалась долго..'
    elif player.stats.corr < 80:
        show expression ("pic/locations/home/dream/201.jpg") at top
        'Вам снилось как вы, будучи монахиней, не смогли справиться с демоном искушения, одолевающим ваше великолепное тело. Не выдержав, вы подняли подол своего платья и запустив длинные пальчики под белье вложили пальчики в полыхающее страстью отверстие. Полные груди с выпирающими под платьем сосками тяжело поднимались, бедра,  слегка  отстраненные  в предвкушении,  извивались, ваши губы вздрагивали, обнажая ряд белоснежных  зубов.'
        'Ваше желание и развращенность увеличились'
        $ player.stats.lust += 10
        $ player.incCorr(0.5)
    else :
        show expression ("pic/locations/home/dream/202.jpg") at top
        'Вам снилось как вы, будучи монахиней, потерпели сокрушительное поражения от демона соблазнов и, не избегнув искушения ласкали себя прямо в храме. Ваши глаза полуоткрыты, одной рукой вы быстро освободили грудь от одежды, а второй,  чуть раздвинув ножки, неистово ласкали свою истекающую соками промежность. Перед глазами вставали сладострастные картины, и миг блаженства приближался с неумолимостью Апокалипсиса.'
        'Утренний оргазм уменьшил желание, но увеличил развращённость.'
        $ player.stats.lust -= 50
        $ player.incCorr(0.5)
    $ move(curloc)
    
label event_loc_dreams_40_21:
    show expression ("pic/locations/home/dream/21.jpg") at top
    'В жарком Египте невольники с огромными членами неутомимо трудились над вашим царственным телом. Отдавая свое роскошное, смазанное маслом тело, вы с наслаждением насаживали себя на член раба до самого конца, чувствуя, как промежность приятно растянулась в самом толстом месте у основания его члена.'
    'Вы сами выбирали ритм, сами выбирали углы проникновения, импровизировали и торжествовали над ними.'
    'Проснувшись вы почувствовали как теплая, щемящая и сладострастная волна, зародившись между ног, распространяется по всему телу. Утренний оргазм уменьшил желание, но увеличил развращённость'
    $ player.stats.lust -= 50
    $ player.incCorr(0.5)
    $ move(curloc)
    
label event_loc_dreams_50_22:
    show expression ("pic/locations/home/dream/22.jpg") at top
    'В этом сне вы, элитная куртизанка, вызвались удовлетворять богатых купцов из Африки. За долгие дни в море они соскучились по женскому теплу и вы чувствуете их напряженное желание. Оседлав одного купца с его великолепным черным членом, вы почувствовали, как его жадные руки вцепились в вашу роскошную грудь.'
    'В алые губы устремился второй напряженный член с распухшей, как гриб, головкой, а нетерпеливые руки последнего купца развели половинки вашей упругой задницы, дабы занять свое место в третьем отверстии вашего атласного тела.'
    'Вы проснулись от адского пламени в промежности'
    $ player.stats.lust = 100
    $ move(curloc)
    
label event_loc_dreams_80_23:
    show expression ("pic/locations/home/dream/23.jpg") at top
    'На этот раз сон был о том, как вы, будучи дворянкой, всесильной в своих владениях, жили в своем поместье, развлекаясь как только могли.'
    'И вот однажды, в вашу голову пришла мысль о том, чтобы принять ванну из мужского семени, ведь это так освежает и питает кожу (по мнению британских ученых)'
    'Собрав холопов, вы улеглись в ванную и отдали приказ "НАПОЛНИТЬ!!!". Сотня мужиков поочередно изливались в емкость, наполняя ее терпким семенем.'
    'Ровные строи ложились на лицо, покрывали потоками большую грудь, ложились на ноги и лицо, проникали внутрь влагалища. Были ли вы счастливы? Вполне возможно :)'
    'Развращенность повысилась'
    $ player.incCorr(1)
    $ move(curloc)
    
label event_loc_dreams_10_24:
    show expression 'pic/locations/home/dream/24.jpg' at top as tempPic
    'В этом сне к вам пришло воспоминание из детства, когда маленький братишка боялся спать один и приходил к вам. Он уютно устраивался на вашей груди, и со счастливой улыбкой засыпал. Это было так мило...'
    'Воспоминание было очень приятным и вы отлично выспались'
    $ player.stats.energy += 150
    $ move(curloc)
    
######################################################################################################################################
#
######################################################################################################################################

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
    'Вы видите, как [st1.fname] и [st2.fname] предаются оральным утехам у подоконника. Целуются то есть.'
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
            show expression 'pic/locations/school/firstFloor/lo11.jpg' at top as tempPic
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
    show expression 'pic/locations/school/firstFloor/mid3.jpg' at top as tempPic
    st1.say ' Да ты охренел чтоли?'
    '[st1.fname] позмущённо оборачивается, когда подошедший сзади парень, вдруг достал свой член и окропил её своим семенем.'
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
    show expression 'pic/locations/school/firstFloor/hi1.jpg' at top as tempPic
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
    
######################################################################################################################################
#
######################################################################################################################################

label event_loc_hall_0_no1:
    show hall
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/school/hall/no1.jpg' at top as tempPic
    '[st2.fname] и [st1.fname]. Очевидно Вы прервали важную беседу, и вам здесь не рады.'
    $ move(curloc)
    
label event_loc_hall_0_no2:
    show hall
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st1.incLust(20)
        st2.incCorr(5)
    show expression 'pic/locations/school/hall/no2.jpg' at top as tempPic
    player.say 'Ого! Тут похоже не обошлось без любовного послания! Давненько вы таких лиц не видели!'
    $ move(curloc)
    
label event_loc_hall_0_no3:
    show hall
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st1.incLust(20)
        st2.incCorr(5)
    show expression 'pic/locations/school/hall/no3.jpg' at top as tempPic
    'Очередное любовное послание? Мило. Похоже шкафчики для обуви используют как угодно, но только не для обуви.'
    $ move(curloc)
    
label event_loc_hall_0_no4:
    show hall
    python:
        st1 = getChar('female')
        st1.incLoy(10)
    show expression 'pic/locations/school/hall/no4.jpg' at top as tempPic
    player.say '"Ну хоть кто то использует шкафчики для обуви, а не для хранения писем поклонников! Какая же [st1.fname] молодец!"'
    'Вы немного поболтали с девушкой, подняв её лояльность.'
    $ move(curloc)
    
label event_loc_hall_0_no5:
    show hall
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st2.incLust(20)
        st1.incCorr(5)
    show expression 'pic/locations/school/hall/no5.jpg' at top as tempPic
    'Что то новенькое. Раньше я встречала только парней, подкатывающих к девушкам. А вот [st1.fname] судя по всему имеет своё мнение насчёт того, кто должен начать ухаживания.'
    $ move(curloc)
    
label event_loc_hall_0_no6:
    show hall
    python:
        player.incLust(5)
        incFun(5,10)
    show expression 'pic/locations/school/hall/no6.jpg' at top as tempPic
    $ move(curloc)
    
######################################################################################################################################
#
######################################################################################################################################

label event_loc_class1_10_1:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('male','lustmax')
    show expression 'pic/locations/school/class1/no1.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Вы прервали важное обсуждение девочек о том, как [st3.name] весь день пытается скрыть свою эрекцию.'
    '[st1.name] улыбается, потому что она давно заметила вас, и молчит.'
    'Зато [st2.fname] заметила вас только посреди своей фразы:'
    st2.say 'А ещё [st3.fname] весь день пялится на мою грудь!'
    'Поэтому окончание фразы звучало как "пялится на мою гру-у-у-у-у-ой".\nВы покинули учениц, не проронив не слова.'
    $ move(curloc)
    
label event_loc_class1_0_2:
    show class1
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class1/no2.jpg' at top as tempPic
    '[st1.fname] убирается в классе, пока все остальные гуляют.'
    if player.getCorr() > 50:
        'Причём ручка швабры вам отчетливо видится стриптизёрским шестом. Вот бы посмотреть какова [st1.fname] в танце!'
        $ player.incLust(2)
    $ move(curloc)
    
label event_loc_class1_0_3:
    show class1
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class1/no3.jpg' at top as tempPic
    '[st1.fname] проветривает свои ножки на перемене. Видимо школьная обувь слишком тесна.'
    if player.getCorr() > 50:
        'Будь у вас член, у между ножек бы тоже стало тесно от такого вида. А пока стало влажно. Мммм... Тоже пора проветривать...'
        $ player.incLust(2)
    $ move(curloc)
    
label event_loc_class1_0_4:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/school/class1/no4.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] и [st2.name] готовятся к уроку. Хотя судя по мечтательному виду девочки за партой, ей не до уроков.'
    $ move(curloc)
    
label event_loc_class1_0_5:
    show class1
    show expression 'pic/locations/school/class1/no5.jpg' at top as tempPic
    'Похоже, что ваше появление помешало девочкам переодеваться к какому-то празднику. Извинившись, вы поворачиваетесь к двери.'
    if player.getCorr() > 50:
        'Хотя от вашего возбужденного взгляда не ускользнули упругие округлости!'
        $ player.incLust(5)
    $ move(curloc)
    
label event_loc_class1_0_6:
    show class1
    python:
        st2 = getChar('female')
        st1 = getChar('male')
    show expression 'pic/locations/school/class1/no6.jpg' at top as tempPic
    'Как мило! Вечно голодающий [st1.fname] кормится с рук. Мдаа, не ожидали вы что [st2.fname] легко падет перед его хулиганскими чарами.'
    if player.getCorr() > 50:
        player.say 'Уж я бы точно пала. Или уже падала? Не припомню что-то.'
        $ player.incLust(5)
    $ move(curloc)
    
label event_loc_class1_0_7:
    show class1
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class1/no7.jpg' at top as tempPic
    'Стол. Класс. Голова. [st1.fname] просто заснула, или что-то случилось?'
    'Вы подошли к девочке и потрогали её за плечо. Оказалось что с ней всё в порядке. [st1.fname] поблагодарила вас за пробуждение, и пожаловалась на своих одноклассников, которые опять бросили её досыпать после урока химии одной.'
    $ st1.incLoy(5)
    $ move(curloc)
    
label event_loc_class1_0_8:
    show class1
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class1/no8.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] отдыхает. Заметив ваш взгляд, она улыбнулась. Какая милая девочка!'
    if player.getCorr() > 50:
        player.say '"И как мило отдыхает! Жаль что мой высокий статус директора не позволяет пристроиться между её ножек, чтобы подробнее рассмотреть узор на трусиках."'
        $ player.incLust(2)
    $ move(curloc)
    
label event_loc_class1_0_9:
    show class1
    python:
        st1 = getChar('male')
        st2 = getChar('male')
    show expression 'pic/locations/school/class1/no9.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] запускают самолётики в свободное от учёбы время.'
    if player.getCorr() > 50:
        'Вы искренне надеетесь, что кроме самолётиков и дружбы между ними нет ничего общего. Уж очень вы не любите, когда при таком обилии девочек мальчики занимаются друг другом.'
    $ move(curloc)
    
label event_loc_class1_0_10:
    show class1
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class1/no10.jpg' at top as tempPic
    'Обернувшись на внезапный девичий вскрик, вы увидели, что одна из учениц, чуть не плача, сидит на полу класса. Кажется, [st1.fname] неловко запнулась и ушибла себе мягкое место.'
    menu:
        'Помочь':
            'Вы помогаете ей подняться и утешаете бедную девочку.'
            $ st1.incLoy(5)
        'Выставить её посмешищем':
            'Вы публично посмеялись над девочкой, показав всем плохой пример для подражания, чем заслужили множество неодобрительных взглядов.'
            $ setLoy(10,-2)
            $ setCorr(10,0.5)
    $ move(curloc)
    
label event_loc_class1_60_1:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('male')
    show expression 'pic/locations/school/class1/lo1.jpg' at top as tempPic
    'Проходя мимо  класса, вы заметили что [st3.fname] беспокойно ерзает на стуле, присмотревшись, вы заметили что он крайне возбужден, вы было хотели подойти и отпустить его домой, чтобы он там снял напряжение, но вас опередили две девушки, [st1.fname] и [st2.fname].'
    'Они достали его член из штанов, и, глядя на этот агрегат, начали поочередно губами плавно водить от яиц до головки, обильно смазывая слюной и массируя ручками его яйца.'
    'От такой картины ваше сердце готово было выпрыгнуть из груди от умиления.'
    $ player.incLust(10)
    menu:
        'Продолжать смотреть':
            show expression 'pic/locations/school/class1/lo1a.jpg' at top as tempPic
            '[st1.fname] тем временем заглотила его член на столько насколько могла ,а вторая стала посасывать его яички, [st3.fname] взял её за волосы и руками начал насаживать ее на свой член, стараясь проникнуть как можно глубже в горло.'
            '[st1.fname] разошлась не на шутку начав наращивать темп,я смотрела как её губы скользят по мокрому от слюны члену. После нескольких минут такого миньета, [st3.fname] прошептал что сейчас кончит, девушки слегка отстранились и он оросил их развратные лица.'
            $ setLust(3,20)
            $ setCorr(3,1)
        'Идти дальше':
            'Вы решили не мешать своим присутствием ученикам, и отправились по своим делам дальше'
            $ setLust(3,10)
            $ setCorr(3,0.5)
            $ setLoy(3,1)
        'Всех наказать':
            show expression 'pic/locations/school/class1/lo1b.jpg' at top as tempPic
            'Яростным свистом в свой директорский свисток, вы прервали разворачивающиеся перед вашими глазами непотребство, и приказали всем участникам оргии остаться после уроков. Раздосадованные ученики понурив головы, пообещали вам придти'
            $ addDetention(st1,st2,st3)
            $ setLoy(3,-2)
            $ setLust(3,-10)
            $ setCorr(3,-1)
    $ move(curloc)
    
label event_loc_class1_15_2:
    show class1
    python:
        st1 = getChar('female','lustmax')
    show expression 'pic/locations/school/class1/lo2.jpg' at top as tempPic
    'Зайдя в класс, вы увидели, как [st1.name], приподняв юбочку, яростно трётся своей киской о край стола. Похоже ей всерьёз не хватает мужской ласки.'
    $ st1.incLust(20)
    $ st1.incCorr(1)
    $ player.incLust(10)
    $ move(curloc)
    
label event_loc_class1_15_3:
    show class1
    python:
        st1 = getChar('female')
    show class1
    'Проходя мимо, вы услышали странные звуки из первого класса.' 
    menu:
        'Заглянуть':
            show expression 'pic/locations/school/class1/lo3.jpg' at top as tempPic
            'Осторожно заглянув внутрь, вы увидели как [st1.fname] раздвигает свою киску пальчиками, аккуратно поглаживая клитор.'
            'Похоже она не на шутку возбудилась! Её пальчики были уже перемазаны соками, и до вас донеслись чавкающие звуки, когда она погружала их в своё лоно.'
            st1.say 'Ооох, простите, я не, это не то, простите, - запричитала девушка, заметив вас.'
            'Быстро надев трусики, она скрылась в коридоре.'
            $ st1.incLust(20)
            $ st1.incCorr(-1)
            $ st1.incLoy(-5)
            $ player.incLust(10)
        'Не обращать внимания':
            'Вы решили не испытывать судьбу, и оставили стонающего в одиночестве. Будем надеятся, что у него или неё не инфаркт, и стонет она от удовольствия а не от боли.'
            $ st1.incLust(20)
            $ st1.incCorr(1)
    $ move(curloc)
    
label event_loc_class1_15_4:
    show class1
    python:
        st1 = getChar('futa')
    show expression 'pic/locations/school/class1/lo4.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Зайдя в класс, вы увидели, что [st1.fname] похоже только закончила онанировать. С её немаленького члена стекала вязкая капля спермы, а на полу образовалась небольшая лужица.'
    player.say 'Сделаем так. Ты убираешь следы своей бурной деятельности, а я делаю вид, что ничего не видела. Включая твой член, - приказным тоном говорите вы.'
    'Школьница понуро берётся за швабру, и начинает убираться, немного вас смущаясь.'
    $ st1.incLust(20)
    $ st1.incCorr(1)
    $ player.incLust(10)
    $ move(curloc)
    
label event_loc_class1_10_5:
    show class1
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class1/lo5.jpg' at top as tempPic
    'Приоткрыв дверь в класс, вы заметили необычные движения вашей ученицы.'
    '[st1.fname] сидела на стуле, и шевелила пальчиками в районе своей промежности.'
    'Судя по всему, она начиталась эротических романов, и не в силах стерпеть желание, решила самоудовлетвориться в классе.'
    'Вы немного подождали, пока девушка с тихим стоном, прижав книжку к лицу, закончит и вошли в класс'
    $ st1.incLust(20)
    $ st1.incCorr(1)
    $ player.incLust(10)
    $ move(curloc)
    
label event_loc_class1_20_6:
    show class1
    python:
        st1 = getChar('futa')
        psize = round(st1.body.parts['пенис'].size,1)
        player.incLust(2)
    show expression 'pic/locations/school/class1/lo6.jpg' at top as tempPic
    'Вы чуть не упали, когда увидели, как [st1.fname], достав свой член сидит, и медитирует на него. Похоже, что медитация была вполне удачна, судя по этому напряжённому фаллосу.'
    menu:
        'Возмутиться':
            player.say 'Что это ты тут устроила? - грозно спрашиваете вы, недоумевая от подобного поведения'
            st1.say 'Не знаю. Мне просто захотелось посмотреть на него. - меланхолично ответила ученица, - Можно посмотреть на ваш?'
            player.say 'Ннно у меня нет ничего подобного! - начинаете вы неожиданно обороняться, будучи застигнутой врасплох.'
            st1.say 'Ясно, - произносит [st1.fname], прячет свой член под юбочку и выходит.'
            'Что это было то сейчас? Вы не поняли, но смешки за дверь показали, что ваша репутация немного уменьшилась.'
            $ st1.incLust(20)
            $ st1.incCorr(2)
            $ setRep(3,-1)
        'Оставить её':
            'Вы решили оставить девушку в покое, в тайне надеясь, что она как нибудь сама справится со своей [psize] сантиметровой проблемой.'
            $ st1.incLust(20)
            $ st1.incCorr(1)
            $ st1.incLoy(3)
    $ move(curloc)
    
label event_loc_class1_15_7:
    show class1
    python:
        st1 = getChar('female')
        player.incLust(2)
    show movie
    play movie 'pic/locations/school/class1/lo7.gif.webm' loop
    'Довольно неожиданное применение школьному столу нашла [st1.fname].'
    'Вслед за движениями бёдер оставалась влажная полоса её выделений, покрывшая уже половину длины стола. По классу разносятся тихие стоны, и влажное хлюпание юной киски. Вы привлекаете внимание лёгким потопыванием ноги.'
    player.say '??? - вопросительно смотрите вы на девочку.'
    st1.say 'Ой, я тут это, - начинает оправдываться [st1.fname] - прочитала что запах может привлечь любимого человека, вот я и... В общем увлеклась я немного, извините.'
    player.say 'Вытирай за собой, тут не только твой любимый сидит, и после занятий останешься в школе, понятно?'
    st1.say 'Да, простите ещё раз пожалуйста, - покорно отвечает девочка и начинает вытирать следы своей любви.'
    $ st1.incLust(20)
    $ st1.incCorr(1)
    $ st1.incLoy(-5)
    $ addDetention(st1)
    stop movie
    hide movie
    $ move(curloc)
    
label event_loc_class1_25_8:
    show class1
    python:
        st1 = getChar('female')
        st1 = getChar('female')
        player.incLust(2)
    show expression 'pic/locations/school/class1/lo8.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Вы с некоторым умилением наблюдаете на страстным поцелуем девочек. Судя по стекающим каплям пота, они черезвычайно возбуждены, так, что даже не заметили вашего прихода.'
    'Понаблюдав пару минут за их ласками, вы негромко окликиваете их, и "предлагаете" остаться после занятий для улучшения поведения.'
    '[st1.fname] и [st2.fname] не могут отказаться от столь "щедрого" предложения и понуро соглашаются'
    $ setRep(2, 1)
    $ setCorr(2, 1)
    $ setLoy (2, -2)
    $ addDetention(st1,st2)
    $ move(curloc)
    
label event_loc_class1_30_9:
    show class1
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(2)
    show expression 'pic/locations/school/class1/lo9.jpg' at top as tempPic
    'Немного приоткрыв дверь в класс, вы заметили двух учеников. [st1.name] похоже принёс в школу свою "игрушку", и как то уговорил подругу поиграть с ней.'
    'Резиновая дырочка с чавканьем движется по стволу члена,  направляемая неуверенной рукой девочки. Парень помогает ей как может, в основном советами, но и не гнушается двигать бёдрами, вы как завороженная наблюдаете за действом.'
    st1.say 'А теперь немного побыстрее, - направляет девочку [st1.name]'
    st2.say 'Вот так вот? - уточняет [st2.name], немного убыстряя темп.'
    st1.say 'Да, не останавливайся пожалуйста, я скоро кончу. - шепчет ученик.'
    menu:
        'Продолжать смотреть':
            'Движения девочки становятся всё резче, похоже она находится на пределе своей скорости.'
            st1.say 'Мммм, - стонет парень, и начинает мелко трястись.'
            'Похоже кто то сегодня получил оргазм! Вы ещё немного подождали, пока закончатся поцелуйчики, подтирашки и обнимашки, и зашли в класс.'
            $ setRep(2, -1)
            $ setCorr(2, 1)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_class1_20_10:
    show class1
    python:
        st1 = getChar('female')
        player.incLust(2)
    'Услышав странные звуки из кабинета, вы заглянули, чтобы узнать их источник. Вдруг уборщица несвоевременно моет полы, или кто занимается взбиванием масла?'
    show expression 'pic/locations/school/class1/lo10.jpg' at top as tempPic
    'Маслом кабинете и не пахло. Пахло сексом. [st1.name] сидя на своём стуле, ласкала груди и нежно теребила набухшую вишенку.'
    'Пальчики нежно ласкали соски и играли с капюшончиком клитора, то оголяя его и то пряча назад.'
    'Каждое движение шаловливых пальчиков сопровождалось тихим стоном и громким хлюпаньем, которое было слышно даже в коридоре.'
    menu:
        'Уйти':
            'Вы решили не мешать девочке, в конце концов может быть у неё нет своей комнаты дома, и негде этим заняться?'
            $ st1.incLust(10)
            $ st1.incCorr(1)
        'Наказать':
            show expression 'pic/locations/school/class1/lo1b.jpg' at top as tempPic
            'Яростным свистом в свой директорский свисток, вы прервали разворачивающиеся перед вашими глазами непотребство, и приказали ученице остаться после уроков'
            python:
                setRep(5,1)
                st1.incLoy(-2)
                st1.incCorr(-1)
    $ move(curloc)
    
label event_loc_class1_50_1:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('male','corrmin')
        player.incLust(10)
    show expression 'pic/locations/school/class1/mid1.png' at top as tempPic
    'Заглянув в первый класс вы услышали тихое пыхтение за партами'
    st1.say 'Давай же, вставь его!'
    st2.say 'Не могу, он выскальзывает!'
    st1.say 'Подожди, я счас сама всё сделаю, ложись давай! Одна морока с этими сыночками-корзиночками!'
    'Какой занимательный диалог! И немного сменив угол обзора вы увидели виновников вашего повышенного внимания. Похоже [st1.fname] собирается прямо в классе лишить девственности своего одноклассника.'
    player.say '"Уж не за то ли, что она недавно сдала контрольную на пятёрку?"'
    menu:
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Подсмотреть, что и откуда там выскальзывает':
            show expression 'pic/locations/school/class1/mid1a.png' at top as tempPic
            'Вы с нарастающим возбуждением наблюдаете, как [st1.fname] ловко ухватив пальчиками член мальчика, загоняет его в свою киску и начинает медленно приседать'
            st2.say 'Оууу, ты такая узенькая! - шепчет [st2.fname].'
            st1.say 'Ну хоть ты у меня и не первый, но слава богу и не сотый, так что наслаждайся, помошник!'
            st2.say 'Мммм, ты слишком узкая... - стонет школьник, - К тому же я не дрочил с утра. Я по моему кончаю!'
            'Стой! Не в меня! - вскрикивает ученица'
            show expression 'pic/locations/school/class1/mid1b.png' at top as tempPic
            st1.say 'Ну ты и ко... Ой, [player.name], - замечает вас девушка.'
            'Мда, девочка так напугалась, что даже забыла вынуть пульсирующий член из своего влагалища. Вы в свою очередь не могли оторвать глаз от такого притягательного зрелища.'
            'Только после того, как член закончил извергаться и из молоденькой киски потекли капли спермы, вы вспомнили, что вы всё таки директор, и надо с ними что-то решать.'
            menu:
                'Наказать':
                    $ scoldWho = [st1,st2]
                    jump scoldAll
                'Путь гуляют':
                    hide tempPic
                    show expression getCharImage(player,'dialog') as temp1
                    player.say 'В следующий раз используйте кондомы, а ещё лучше, найдите место поукромнее, усекли? - строго глядя выговариваете вы ученикам.'
                    show expression getCharImage(st1,'dialog') as temp2
                    st1.say 'Да я с ним больше никогда, с этим спринтером! - пытается оправдаться [st1.fname].'
                    show expression getCharImage(st2,'dialog') as temp2
                    st2.say 'Посмотрю я на тебя, когда в следующий раз на контрольной завалишься! - начинает возбухать внезапно финишировавший.'
                    'Ещё через пару минут препираний дети наконец сваливают. Оставив вам на память прекрасные картинки и мокрые трусики.'
                    $ hadSex(st1,st2)
    $ move(curloc)
    
label event_loc_class1_25_2:
    show class1
    python:
        st1 = getChar('female')
        player.incLust(2)
    show expression 'pic/locations/school/class1/mid2.jpg' at top as tempPic
    player.say '[st1.fname], мастурбация, конечно не порок, но посередине класса? В школе? О чём ты только думаешь? - заявили вы ученице, видя её запихивающей свои пальцы в киску прямо на полу.'
    st1.say 'Мммм, я перевозбудилась, простите, я скоро, мммм.'
    menu:
        'Пусть себе. Авось хуже не будет':
            'Вы недовольно хмыкнув, отвернулись в ожидании, пока девочка закончит.'
            $ st1.incLoy(5)
            $ st1.incCorr(2)
            $ st1.incLust(-100)
        'Наказать':
            show expression 'pic/locations/school/class1/lo1b.jpg' at top as tempPic
            'Яростным свистом в свой директорский свисток, вы прервали разворачивающиеся перед вашими глазами непотребство, и приказали ученице остаться после уроков'
            python:
                setRep(5,1)
                st1.incLoy(-2)
                st1.incCorr(-1)
    $ move(curloc)
    
label event_loc_class1_50_3:
    show class1
    python:
        st1 = getChar('female')
        player.incLust(2)
    show expression 'pic/locations/school/class1/mid3.jpg' at top as tempPic
    player.say '[st1.fname]? Чем это ты тут занимаешься? - строго спросили вы ученицу, оценив её полуголый вид и подтёки спермы на промежности.'
    st1.say 'Мы тут с парнем моим... В общем не смогли сдержаться мы. А вы не любили никогда, да? Голову никогда не теряли чтоли? - переходит в наступление ученица.'
    player.say 'Успокойся, я пока просто спросила. На всякий пожарный, ты уверена, что о случившемся знают только трое, включая меня?'
    st1.say 'Я, я не уверена... Кажеться я слышала шаги, но мы вроде как спрятались. - задумчиво ответила [st1.fname]. Надо что-то решать. Если их действительно видели, ваша репутация может пострадать!'
    menu:
        'Пусть себе. Авось хуже не будет':
            'Вы недовольно хмыкнув, отвернулись в ожидании, пока девочка оденется.'
            $ st1.incLoy(2)
            $ st1.incCorr(2)
            $ st1.incLust(-100)
        'Наказать':
            'Вы решили, что репутация дороже, и приказали ученице остаться после уроков в школе в качестве наказания.'
            python:
                setRep(5,1)
                st1.incLoy(-2)
                st1.incCorr(-1)
    $ move(curloc)
    
label event_loc_class1_55_4:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.incLust(2)
    show expression 'pic/locations/school/class1/mid4.jpg' at top as tempPic
    'Вы с нарастающим возбуждением наблюдаете за тем, как член парня погружается в тугую и смазанную попку девушки. Чёрт подери, да у него немалая сила, держать её на руках и так активно долбить в задницу!'
    'А эти ножки, эти приспущенные трусики... Очевидно, что девушка не обделена некоторой красотой и шармом.'
    'Вы ещё немного понаблюдали за сочной киской и крепким членом в паре сантиметров от неё, пока не опомнились, и не поняли, что с ними надо что-то решать.'
    menu:
        'Оставить их':
            'Аккуратно развернувшись, вы покинули помещение, оставив молодых развлекаться.'
            $hadSex(st1,st2)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_class1_30_5:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.incLust(5)
    show expression 'pic/locations/school/class1/mid5.jpg' at top as tempPic
    'Увидев вас, [st1.fname] быстро спускает трусики, и показывает свою гладкую киску под юбочкой. Не успели вы насмотреться на её прелести, как она быстренько натягивает трусики назад и пытается смотаться подальше.'
    player.say 'Это что за перформанс ты устроила? - хватаете вы девчёнку за руку.'
    st1.say 'Я просто проспорила кое кому. Вы же не в обиде. Не так ли? - подмигивает вам [st1.fname].'
    menu:
        '"Отпустить" её.':
            show movie
            play movie 'pic/locations/school/class1/mid5a.gif.webm'
            player.say 'Ну хорошо, иди, - говорите вы, и вдруг впиваетесь в её губы своими.'
            'На удивление [st1.fname] вам с радостью отвечает взаимностью. Через несколько секунд поцелуя, вы всё таки отпускаете, легко хлопнув по попке.'
            stop movie
            hide movie
            $ player.incLust(20)
        'Наказать':
            player.say 'Школа - не место для подобных споров! - строго выговариваете вы ученице, и добавляете её в свой список наказанных.'
            python:
                setRep(5,1)
                st1.incLoy(-2)
                st1.incCorr(-1)
    $ move(curloc)
    
label event_loc_class1_45_6:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        player.incLust(2)
    show expression 'pic/locations/school/class1/mid6.jpg' at top as tempPic
    'Копошение у доски не могло не привлечь вашего внимания. [st1.fname] и [st2.fname] совершенно не обращая на вас внимания занимались делами несколько далёкими от учёбы. Хотя весьма близкими к биологии и сексуальному просвещению.'
    'Их гладкие киски безудержно тёрлись друг об друга порождая хлюпающие звуки и сносящий голову запах'
    menu:
        'Продолжать смотреть':
            show expression 'pic/locations/school/class1/mid6a.jpg' at top as tempPic
            'Наблюдая за девочками вы неволей опустили ручку, которую держали в руках к своей промежности и начали наглаживать свой клитор.'
            show expression 'pic/locations/school/class1/mid6.jpg' at top as tempPic
            'Школьницы совершенно не обращали на вас внимания, занимаясь своими кисками и не мешая вам заниматься своей.'
            'Вскоре их движения стали более грубыми и резкими, и сквозь туман наслаждения до вас дошла мысль, что они похоже скоро кончат и вам совсем не хочется, чтобы вас заметили тут с поднятой юбкой.'
            'Быстренько приведя себя в порядок, вы вышли в коридор.'
            $ hadSex (st1,st2)
            $ hadSex (player)
            $ player.incLust(20)
            $ move(prevloc)
        'Оставить их':
            'Аккуратно развернувшись, вы покинули помещение, оставив молодых развлекаться.'
            $ setLoy(2,5)
            $ hadSex (st1,st2)
            $ move(prevloc)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_class1_35_7:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        player.incLust(2)
    show expression 'pic/locations/school/class1/mid7.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Девочки явно не ожидали увидеть вас на своём писькотёрочном мероприятии. А им явно есть чем потереться! Хотя удивлённой выглядит только [st2.fname], [st1.fname] смотрит на вас со странной улыбкой, и, возможно, немножко даже с вызовом!'
    menu:
        'Оставить их':
            'Вы уходите, не произнося ни слова. За спиной вы слышите облегчённый вздох учениц. Похоже вашего  свистка не на шутку боятся!'
            $ setLoy(2,5)
            $ hadSex (st1,st2)
            $ move(prevloc)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_class1_50_8:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.incLust(5)
    show expression 'pic/locations/school/class1/mid8.jpg' at top as tempPic
    player.say '"Неужели это не могло подождать до дома?", думали вы, глядя на трахающуюся парочку в углу.'
    'Член ученика на ваших глазах таранил узенькое лоно школьницы, отчего в классе були слышны влажные звуки. [st1.fname] тихо постанывала, скорее отдаваясь парню, нежели помогая ему.'
    '[st2.fname] был совсем не против почувствовать себя активным партнёром, и продолжал долбить девочку с силой угрожающей не самой новой парте.'
    menu:
        'Оставить их':
            'Вы уходите, стараясь сделать это как можно бесшумней. Всё таки дело молодое, а сломанная парта не повод для печали.'
            $ hadSex (st1,st2)
            $ move(prevloc)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_class1_40_9:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.incLust(5)
    show expression 'pic/locations/school/class1/mid9.jpg' at top as tempPic
    '[st1.fname] с любопытством оттягивает член одноклассника, любуясь как головка то исчезает, то появляется из под натянутой кожицы на члене.'
    'Не похоже на то, чтобы [st2.fname] как то препятствовал этому любопытству. Кажется вы уже знаете, чем это закончится.'
    'И, судя по блестящей капельке на члене, закончится скоро.'
    menu:
        'Продолжать смотреть':
            show expression 'pic/locations/school/class1/mid9a.jpg' at top as tempPic
            'Парень вдруг застонал, и из его небольшого члена, брызнул довольно мощный поток, заливающий парту и девушку.'
            st1.say 'Ой, чего же ты не предупредил? - ойкнула ученица, и начала вытираться.'
            'Парень тяжело дышал, привалившись на парту. Вы подумали о том, что лучше бы вас не заметили, и тихонько скрылись из класса.'
            $ setCorr(2,2)
            $ setLust(2,20)
            $ move(prevloc)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_class1_75_1kupruvna:
    show class1
    python:
        if mile_qwest_2_stage != 12:
            skipEvent()
        st0 = kupruvna
        st1 = getChar('male')
        st2 = getChar('male')
        st3 = getChar('male')
        st4 = getChar('male')
        player.incLust(30)
    show expression 'pic/locations/school/class1/hi1.jpg' at top as tempPic
    'Вы зашли в класс и увидели что Валентина Купрувна очень сильно занята, у нее сложный случай - сразу у четырех учеников случилась мощная эрекция, и она, как и всякий хороший преподаватель, не могла оставить это.'
    'К сожалению вы не видели самого начала, на учительнице уже было порвано платье в весьма пикантных местах и она сидела на голом ученике, двух других она стимулировала руками время от времени помогая себе ротиком.'
    menu:
        'Продолжать смотреть':
            show expression 'pic/locations/school/class1/hi1a.jpg' at top as tempPic
            'Третий мастурбировал, глядя на остальных. Киска учительницы сочилась соком и уже была готова принять в себя член.'
            'Вдруг [st0.fname] привстала не выпуская член изо рта и медленно опустилась на пенис ученика.'
            show expression 'pic/locations/school/class1/hi1b.jpg' at top as tempPic
            'Она была настолько влажной, что он вошел во влагалище учительницы без проблем. Губки жадно обхватывали его член,а ее соки брызнули в разные стороны.'
            'Купрувна активно запрыгала на члене не забывая о учениках, она двигалась с какой то животной страстью, и ей похоже было все равно кто под ней лежит и чьи члены вокруг нее.'
            st1.say '"Шевели задницей, училка! Я скоро кончу!",- крикнул ей ученик на котором она прыгала.'
            '[st1.fname] перехватил у нее инициативу и с силой стал вгонять в нее свой член. Звук ударяющихся тел заполнил класс. Чавкающий звук члена, входящего в вагину достиг ваших ушей.'
            'Мелкая дрожь напряженных ног подсказали вам насколько Валентина близка к финалу...'
            show expression 'pic/locations/school/class1/hi1c.jpg' at top as tempPic
            'Учительница отдавалась со всей страстью. Её мышцы были напряжены до предела. Вдруг она выгнулась дугой протяжно замычав из ее влагалища брызнула сперма ученика смешанная с ее соком...'
            'Почти одновременно кончили трое остальных учеников обильно полив своим семенем лицо и грудь учительницы. Немного красная, толи от стыда, толи от возбуждения, вы покинули класс.'
            $ hadSex(st0,st1,st2,st3,st4)
            $ move(prevloc)
        'Всех наказать':
            $ scoldWho = [st1,st2,st3,st4]
            jump scoldAll
    $ move(curloc)
    
label event_loc_class1_40_2kupruvna:
    show class1
    python:
        if mile_qwest_2_stage != 12:
            skipEvent()
        st0 = kupruvna
        st1 = getChar('male')
        player.incLust(30)
    show expression 'pic/locations/school/class1/hi2.jpg' at top as tempPic
    'С небольшой завистью, вы наблюдаете за тем, как [st1.fname] насаживает свою учительницу на член.'
    'Причём трахаются они отнюдь не минуту и не две, потому что лицо Валентины Купровны густо измазано в сперме. То есть сначала был минет, а теперь они трахаются.'
    'Нет, вы посмотрите на них. Яростная парочка даже не замечает вас! И эти звуки, запах... Вас саму это так заводит... Чёрт с ними, надо сбегать и снять напряжение. Так или иначе.'
    $ hadSex(st0,st1)
    $ move(curloc)

    
label event_loc_class1_30_3kupruvna:
    show class1
    python:
        if mile_qwest_2_stage != 12:
            skipEvent()
        st0 = kupruvna
        st1 = getChar('male')
        player.incLust(30)
    show expression 'pic/locations/school/class1/hi3.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Вы заметили, что Валентина Купрувна похоже занимается смазыванием инструмента перед выступлением в музыкальном клубе. Да, инструмент надо смазывать тщательно, и как можно глубже, и сильнее. Вот уже влага показалась с обратного конца флейты.'
    player.say 'Да что я такое думаю то? Какая смазка для флейты, это же не тромбон! К чёрту!'
    'Вы выходите из кабинета, попутно захватив с собой случайно зашедшего ученика. За вашей спиной прозвучал сдавленный стон смазанной флейты.'
    $ hadSex(st0)
    $ move(prevloc)
    
label event_loc_class1_30_4kupruvna:
    show class1
    python:
        if mile_qwest_2_stage != 12:
            skipEvent()
        st0 = kupruvna
        player.incLust(2)
    show expression 'pic/locations/school/class1/hi4.jpg' at top as tempPic
    player.say '"Какая же всё таки она шлюха", - думаете вы, смотря как поток спермы вытекает из влагалища химички прямо на контрольные работы.'
    'Не надо иметь детективный нюх, чтобы понять, как именно происходит выставление оценок по этому предмету. У кого член больше, у того и оценка выше.'
    'Наш физрук был бы круглым отличником с такими учителями.'
    'С небольшим омерзением, вы захлопываете зверь и выходите из класса, давая извращенке привести себя в порядок.'
    'Выйдя в коридор, вы заметили, что случайно перепачкали руки в чьей то сперме.'
    $ player.coverSperm('руки')
    $ hadSex(st0)
    $ move(prevloc)
    
label event_loc_class1_70_5:
    show class1
    python:
        st1 = getChar('futa')
        st2 = getChar('futa')
        player.incLust(10)
    show expression 'pic/locations/school/class1/hi5.jpg' at top as tempPic
    player.say '"Какие маленькие проказницы!" - думали вы с удовольствием наблюдая за ученицами, - И ведь не в первый раз кончают, судя по забрызганному спермой полу.'
    'Да, таким девчёнкам парни без надобности...'
    'Ещё немного полюбовавшись на любовниц, вы дождались пока [st1.fname] наконец то зальёт семенем ножку своей подруги, и с чистой совестью вышли из кабинета.'
    $ hadSex(st1, st2)
    $ move(prevloc)
    
label event_loc_class1_70_6kupruvna:
    show class1
    python:
        if mile_qwest_2_stage != 12:
            skipEvent()
        st1 = kupruvna
        st2 = getChar('male')
        player.incLust(10)
    show expression 'pic/locations/school/class1/hi6.jpg' at top as tempPic
    st1.say 'Сильнее! Да! Кончаю! - кричала в оргазме [st1.name], в то время как [st2.fname] активно вгонял ей свой член во влагалище.'
    'В ответ раздался громкий шлепок ей по заднице.'
    st1.say 'Дааааа, пользуй меня как шлюху! - задрожала учительница от удовольствия.'
    player.say '[st1.fname], вы не хотите ничего объяснить? - спросили вы стонущую от удовольствия женщину.'
    'В ответ она закатила глаза и издала нечленораздельный стон. Похоже она совсем в неадеквате от количества испытанных оргазмов.'
    'Плюнув на пол от негодования, вы вышли из класса хлопнув дверью.'
    $ move(prevloc)
    
label event_loc_class1_80_7:
    show class1
    python:
        st1 = getChar('female','lustmax')
        st2 = getChar('male')
        st3 = getChar('male')
        changetime(20)
    show expression 'pic/locations/school/class1/hi7.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    st1.say '[player.name], не хотите присоединиться? - спрашивает вас текущая от возбуждения ученица.'
    menu:
        'Трахаться с учениками? Уж увольте!':
            player.say 'Ты в своём уме? - спрашиваете вы ученицу, - А ну ка быстро привела себя в порядок!'
            'Вы упираете свои руки в боки, сурово глядя на ученицу.'
            st1.say 'Ну как хотите, - странно улыбается девушка, и вы внезапно ощущаете холод наручников на своих запястьях'
            show expression 'pic/locations/school/class1/hi7a.jpg' at top as tempPic
            player.say 'Да что происходит? - удивлённо спрашиваете вы, как вдруг оказываетесь сверху девушки, прижимаясь своими грудями к её.'
            player.say 'Эй, что ты там делаешь??? - восклицаете вы, ощущая как в вашу попу проникает инородный предмет необычной формы, - Ааааааа.'
            st2.say 'Вот так, - раздаётся голос сзади, когда банан наполовину скрылся в вашей верхней дырочке, - Теперь займёмся нижней, ты не против, [st1.fname]?'
            st1.say 'Конечно, [st2.fname], засовывай! - простонала девушка под вами, и в вашу киску вдруг вторглось что-то холодное, смазанное и большое'
            player.say 'Ччччёрт! - ругнулись вы, понимая что необычная заполненность дырочек начинает заводить вас, - А ну прекратите!'
            st1.say 'Да, [st2.fname], да! - Вдруг заелозила под вами девушка, и живот парня начал ритмично вдавливать в вас дилдо и банан.'
            'Поначалу ощущения были неприятные, и вы изо всех сил пытались вырваться, но вскоре самотык согрелся в вашей киске, и вам стало приятней.'
            'Неутомимо двигаясь в заднице одноклассницы, парень положил свои руки вам на талию и начал действовать ещё активней. Частота движения предметов в ваших дырочках резко возросла, и вы почувствовали как внизу живота поднимается тёплая волна оргазма.'
            player.say 'Нет, пожалуйста, прекрати, - простонали вы и [st2.fname] плотно прижался к вам, максимально глубоко загоняя дилдо, который уткнулся в вашу матку.'
            player.say 'Кончаю-у-у-у! - закричали вы вместе с ученицей, попка которой начала наполняться спермой.'
            st2.say 'Это было волшебно! - упал на вас сверху парень, расстёгивая наручники.'
            $ hadSex(player,st1,st2)
            menu:
                'Всех наказать':
                    $ scoldWho = [st1,st2]
                    jump scoldAll
                'Спасибо':
                    player.say 'Это было незабываемо! - вздохнули вы, ощущая как проходит возбуждение, оставляя приятную теплоту между ног и в попе.'
                    'Повернувшись вы поцеловали парня и девушку, и улыбнувшись им напоследок, покинули кабинет.'
                    $ setLoy(2,5)
        'Почему бы и не разнообразить свою сексуальную жизнь?':
            show expression 'pic/locations/school/class1/hi7b.jpg' at top as tempPic
            player.say 'Один раз живём! - сказали вы, залазя на ученицу, и сливаясь с ней в долгом поцелуе.'
            'Ваши киски встретились и принялись тереться друг об друга, смешивая соки. Вы ощущали приятное нарастание возбуждения в вашем животе, ваше влагалище сокращалось от удовольствия и вы хотели большего.'
            'Неожиданно дверь приоткрылась и в класс вошли [st2.fname] и [st3.fname]'
            player.say 'Присоединитесь, мальчики? - обернувшись помахали вы своей попой.'
            show expression 'pic/locations/school/class1/hi7c.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            'И мальчики присоединились. Вас перетрахали буквально во всех позах, планомерно заполняя дырочки спермой.'
            'К третьему оргазму вы уже слабо понимали кто что и зачем в вас пихает. Вы просто получали огромное удовольствие, как будто вас пихали не 2 члена, а десять.'
            'Влагалище постоянно ощущало как его раздвигают то член, то пальцы, смазка перемешалась с чьей то спермой, в конце концов [st2.fname] положил на вас член и спустил на груди, а [st3.fname] выплеснул свою сперму глубоко в вашем заднем проходе.'
            'Вы ненадолго потеряли сознание.'
            show expression 'pic/locations/school/class1/hi7d.jpg' at top as tempPic
            'По немного приходя в себя, вы оценивали окружающую обстановку. Всё вокруг было залито спермой, которая стекала изо всех ваших щелей. [st1.fname] лежала рядом и была не в лучшем состоянии.'
            'Давай, приходи в себя! - растолкали вы девушку, и принялись приводить себя и класс в порядок.'
            $ setLoy(3,5)
            $ hadSex(player,st1,st2,st3)
    $ move(prevloc)
    
label event_loc_class1_80_8:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('female')
        st5 = getChar('male')
        st6 = getChar('male')
        st7 = getChar('male')
        st8 = getChar('male')
        player.incLust(30)
    show expression 'pic/locations/school/class1/hi8.png' at top as tempPic
    'Похоже девчёнки решили сегодня устроить соревнование на самые ласковые ножки в школе!'
    'К сожалению вы успели только к самому окончанию, и не знаете, кто из парней кончил первым, в любом случае кончили все! И это замечательно, раз в очередной раз победила дружба!'
    $ hadSex(st1,st2,st3,st4,st5,st6,st7,st8)
    $ move(curloc)
    
label event_loc_class1_75_9:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.incLust(10)
    show expression 'pic/locations/school/class1/hi9.jpg' at top as tempPic
    st1.say 'Трахай меня, [st2.fname], трахай, вытрахай мою задницу полностью! - вопила связанная ученица на члене парня, буравившего её узенькую попку'
    player.say '"Не припомню я, чтобы БДСМ преподавался в школе. Небось в хентайных журналах начитались..." - подумали вы, с возбуждением разглядывая спаривавшуюся парочку.'
    'На секунду вам даже захотелось, чтобы этот крепкий член начал исследовать глубины вашего анала...'
    $ hadSex(st1,st2)
    $ move(curloc)
    
label event_loc_class1_65_10:
    show class1
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('female')
        player.incLust(10)
    show expression 'pic/locations/school/class1/hi10.jpg' at top as tempPic
    '[st1.fname], [st2.fname], [st3.fname] и [st4.fname] примеряют свои новые игрушки. Все мило приветствуют вас, и продолжают обсуждать достоинства и недостатки своих вибраторов.'
    st1.say 'Мой, ммм, классный'
    st2.say 'А у моего есть функция вращения, сейчас, ахх'
    st3.say ' А я свой и попу могу засунуть!'
    st4.say 'А я кажется сейчас уже кончу... - застонала девушка и тихим всхлипом сползла на пол'
    $ hadSex(st1,st2, st3, st4)
    $ move(curloc)
    
######################################################################################################################################
#
######################################################################################################################################

label event_loc_class2_0_1:
    show class2
    python:
        if is_cherleaderClub != 0:
            skipEvent()
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLoy(10)
        st1.incLoy(10)
    show expression 'pic/locations/school/class2/no1.jpg' at top as tempPic
    st1.say 'Здравствуйте, [player.name]!'
    st2.say 'Да, здравствуйте!'
    player.say 'Здравствуйте...'
    st1.say 'У нас есть просьбочка...'
    st2.say 'Да, вот просьбочка у нас есть одна...'
    player.say 'Ага... Ну если в рамках разумного...'
    'Вы судорожно прикидываете свои финансы и варианты того, что девушки могут у вас попросить.'
    st1.say 'Мы хотим открыть клуб!'
    st2.say 'Да, клуб!'
    st1.say 'Клуб поддержки нашей...'
    st2.say 'Школьной спортивной команды!'
    'Да! И девушки встают в стойку черлидеров, представляя, что в руках у них помпоны.'
    player.say 'А, вы об этом... Я подумаю, девушки!'
    st1.say 'Ура!!! Наша директор не против!'
    st2.say 'Да!!! Мы будем президентами!'
    st1.say 'Нет, это я буду президентом!'
    'Девушки уходят, ругаясь о том, кто станет президентом нового клуба.'
    'В вашем школьном компьютере появилась возможность открыть клуб черлидеров.'
    $ move(curloc)
    
label event_loc_class2_0_10:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
    show expression 'pic/locations/school/class2/no10.jpg' at top as tempPic
    '[st1.fname] заснула. Толи урок был слишком утомительным, толи просто не выспалась. [st2.fname] и [st3.fname] хихикают над соней. А вот вам не до веселья. Она испортила парту!'
    menu:
        'Потребовать деньги с родителей':
            hide tempPic
            show expression getCharImage(player,'dialog') as temp1
            show expression getCharImage(st1,'dialog') as temp2
            'Вы бесцеремонно будите ученицу.'
            player.say 'Чтобы вот за это, - вы тыкаете пальцем в парту, - завтра же пришла с родителями в школу!'
            st1.say 'Но, но я, это я тут, это всё до меня, да!'
            player.say 'И слышать ничего не хочу!'
            st1.say 'Можно я просто деньгами отдам?'
            player.say 'Ладно, я никому не скажу.'
            'Девушка возместила ущерб карманными деньгами.'
        'Просто наказать её':
            $ scoldWho = [st1]
            jump scoldAll
        'Ничего не делать':
            'Вы просто хмыкнули, и погладили спящую девушку по голове, не желая тревожить её сон. К сожалению парту придёться чистить за счёт школы.'
            $ st1.incLoy(10)
            $ setRep(3,5)
            $ setLoy(3,5)
            $ school.budget -= 100
    $ move(curloc)
    
label event_loc_class2_5_2:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st1.incCorr(1)
    show expression 'pic/locations/school/class2/no2.jpg' at top as tempPic
    '[st1.fname] похоже поймана с поличным за написанием любовного письма. [st2.fname] пока ещё не понял, чем она занималась, но уже заметил шокированное выражение лица ученицы.'
    if player.getCorr() > 40:
        player.say '"Хех, интересно было бы посмотреть, чем это всё закончится, но если я продолжу пялиться на них, обо мне могут подумать нехорошо."'
        show expression 'pic/locations/school/class2/no2a.jpg':
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        'Вы прикрываете глаза, представляя один из вариантов, как могла бы закончится эта маленькая сценка в классе.'
        player.say '"Да, если бы [st2.fname] засунул свой член ей в рот и долбил, пока не выбил бы слова любви, это было бы прекрасно!"'
        if st2.getCorr() < 50:
            player.say '"Жаль, что пока неосуществимо!"'
        else:
            player.say '"Хотя парень наверняка вытворяет со своей подружкой вещи и посрамнее!"'
        $ player.incLust(5)
    $ move(curloc)
    
label event_loc_class2_0_3:
    show class2
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class2/no3.jpg' at top as tempPic
    '[st1.fname] сидит на трибуне преподавателя и грустит. Зачем грустить в такой прекрасный день? Непонятно.'
    if player.getCorr() > 30:
        show expression 'pic/locations/school/class2/no3a.jpg':
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        player.say '"Хотя может быть маленькая развратница только и ждёт, пока я уйду, чтобы усесться на колени к физруку и начать ласкать своей ручкой его торчащий член???"'
        show expression 'pic/locations/school/class2/no3.jpg' at top as tempPic
        'Поддавшись соблазну вы разворачиваетесь, но нет, просто сидит и чего то ждёт.'
        $ player.incLust(5)
    $ move(curloc)
    
label event_loc_class2_0_4:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incCorr(1)
    show expression 'pic/locations/school/class2/no4.jpg' at top as tempPic
    '[st2.fname] решила сделать массаж плеч подруге. Вы не думаете, что [st2.fname] против данного внимания, так что вам тут делать нечего.'
    if player.getCorr() > 50:
        player.say '"Хотела бы я посмотреть, как [st2.fname] массирует и другие части тела своей подружки!"'
        show expression 'pic/locations/school/class2/no4a.jpg' at top as tempPic
        'Перед вашими глазами проносится картинка того, как [st1.fname] сидит на парте широко расставив ноги, а [st2.fname] язычком и ручками доводит подружку до бурного оргазма!'
        $ player.incLust(5)
    $ move(curloc)
    
label event_loc_class2_5_5:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
    show expression 'pic/locations/school/class2/no5.jpg' at top as tempPic
    '[st1.fname] приглашает своего бойфренда в кино. Хотя немного присмотревшись, вы понимаете, что [st2.fname] скорее всего ещё не её бойфренд, ну чтож, удачи им.'
    if player.getCorr() > 50:
        show movie
        play movie "pic/locations/school/class2/no5a.gif.webm" loop
        player.say '"Будем надеятся, что в кино на последнем ряду, да с членом любимого во рту, [st1.fname] наконец то разберётся, бойфренд ей [st2.fname], или не бойфренд."'
        if st1.getCorr() > 30:
            'И глядя на нездоровый блеск в глазах девушки, вы понимаете, что всё именно так и закончится.'
        else:
            'Жаль, что мечты пока несбыточны, и максимум на что парню можно рассчитывать - это невинный поцелуй.'
        stop movie
        hide movie
    $ move(curloc)
    
label event_loc_class2_0_6:
    show class2
    python:
        if player.getEnergy > 300:
            skipEvent()
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
    show expression 'pic/locations/school/class2/no6.jpg' at top as tempPic
    'Всё в порядке. Перед вами [st1.fname] и [st2.fname]. И 15 сантиметровая [st3.fname] на столе вам просто кажется. Вы ОЧЕНЬ сильно надеетесь, что вам просто кажеться. Надо пойти домой отдохнуть.'
    $ move(curloc)
    
label event_loc_class2_0_7:
    show class2
    python:
        st1 = getChar('female')
        setLoy(5,10)
    show expression 'pic/locations/school/class2/no7.jpg' at top as tempPic
    '[st1.name] вытирает пыль с доски. Очень трудолюбивая девочка. Хотя и немного страшненькая.'
    'Вы заводите с ней разговор о полезности труда в юном возрасте, и заканчиваете его африканскими детьми - рабами находящихся под гнётом проклятых белых эксплуататоров. Ваша речь произвела на всех впечатление.'
    $ move(curloc)
    
label event_loc_class2_10_8:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        hadSex(st1,st2)
    show expression 'pic/locations/school/class2/no8.jpg' at top as tempPic
    player.say '"Кхем. Похоже девочки просто не приняли душ после физкультуры, и отдыхают на прохладном полу. Да, вряд ли тут что то крамольное."'
    if player.getCorr() > 20:
        player.say '"Хотя кого я обманываю? Девочки просто чувствуют просыпающуюся сексуальность, и исследуют свои тела при любом удачном случае!"'
        'Вы проводите небольшую лекцию о сексуальном образовании, и важности его в современном обществе. [st1.fname] и [st2.fname] выглядят смущённо.'
    $ move(curloc)
    
label event_loc_class2_5_9:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/school/class2/no9.png' at top as tempPic
    '[st1.fname] подвернула ногу и [st2.fname] несёт её в медкабинет. Именно поэтому она так вспотела и тяжело дышит.'
    if getPar(studs,'corr') > 20:
        player.say '"Всё бы ничего. Только [st2.fname] несёт подругу не вставая со стула. И потеет. Потом зайду."'
        $ hadSex(st1,st2)
    $ move(curloc)
    
    
label event_loc_class2_10_1:
    show class2
    python:
        if player.getCorr() < 50:
            skipEvent()
        st1 = getChar('male')
        st2 = getChar('male')
        hadSex(st1)
        hadSex(st2)
        player.incLust(40)
        st1.incLoy(10)
        st2.incLoy(10)
    show expression 'pic/locations/school/class2/lo1a.jpg' at top as tempPic
    'Зайдя в класс вы заметили двух учеников, снимающих с себя одежду. [st1.fname] и [st2.fname] уже были полностью обнажены, разве что их боксеры пока оставались на их бедрах. Ваш взгляд мгновенно остановился на выпуклых очертаниях их довольно больших по возрасту членов.'
    player.say '"Кажется в моей школе начались новомодные нетрадиционные отношения," - подумали вы, - "необходимо пресечь их на корню."'
    show expression 'pic/locations/school/class2/lo1b.jpg' at top as tempPic
    player.say 'Так мальчики, чем это мы тут занимаемся? - грозно спросили вы'
    st1.say 'Мммммммыы.. Это...'
    st2.say 'Нуууууу...'
    'Начали что то невнятно мычать парни.'
    player.say 'Ну вы продолжайте, продолжайте, снимайте все, - металл в вашем голосе подсказал ученикам, что лучше подчиниться'
    show expression 'pic/locations/school/class2/lo1c.jpg' at top as tempPic
    'Под вашим взглядом вскоре обнажились два небольших, но молодых и крепких достоинств. Их розовые головки обнажились и смотрели вверх. Прямо на вас. Вы почувствовали как между ножек становится влажно, но не дали желанию прорваться, сейчас несколько иная задача.'
    player.say 'Итак, [st1.fname] и [st2.fname]! В то время как рядом гуляют молоденькие, практические нетронутые девочки, горящие внутри пламенем любви и секса, я застаю вас друг с другом!'
    player.say 'Мне не приносит это радости. И кроме того, что вам обоим придется сегодня отбыть наказания, ВЫ, дорогие мои на моих глазах сейчас спустите свое напряжения, думаю об их прелестях'
    st1.say 'Но...'
    st2.say 'Мы же это...'
    player.say 'Никаких но!! Думаю что я помогу вам. Во избежания дальнейших некорректных действий'
    show expression 'pic/locations/school/class2/lo1d.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Вы облокотились на учительскую парту и ловя на себе взгляды учеников, медленно подтянули юбку вверх, открывая их горящим взорам свое нижнее белье. Сегодня на вас были белые трусики с кружевной оборкой, что очень выгодно смотрелось на вашем безукоризненном теле.'
    player.say '"Надеюсь они не заметят как я возбуждена."'
    'Прием сработал - вы увидели как их руки заработали, сдвигая кожу членов вниз-вверх. Ощущение их горящих взоров между ног наполняло вас невиданным восторгом'
    show expression 'pic/locations/school/class2/lo1e.jpg' at top as tempPic
    'Долго это продолжаться не могло и вскоре из их членов полилось густое семя, оставляя свои следы на полу, партах, и их телах.'
    player.say 'Надеюсь вы все поняли?'
    'Вы поправили юбку и направились к дверям. Оглянувшись, вы поймали их взоры, полные любви не только к вам лично, но и всем женскому полу в целом.'
    player.say '"Кажется затея удалась. Осталось найти укрытие чтобы сбросить СВОЕ напряжение!"'
    $ move(curloc)
    
label event_loc_class2_25_2:
    show class2
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        hadSex(st1)
    'Аккуратно зайдя в класс, вы услышали за занавеской тихое шептание:'
    st1.say 'Пожалуйста, не прячь, ещё чуть чуть и я кончу!'
    show expression 'pic/locations/school/class2/lo2.png' at top as tempPic
    'Решив приоткрыть для себя завесу тайны, вы заглянули за шикарные гардины в классе, и увидели, что [st1.fname] яростно наяривает свой член глядя на грудь одноклассницы.'
    'Прежде чем вы успели открыть рот, он с громким стоном спустил, заляпав школьницу своим семенем. [st2.fname] шокированно смотрит на вас, и по её грудям и животику медленно стекают капли свежей спермы.'
    menu:
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Хмыкнуть и уйти':
            'Вы хмыкнули, и приказав любовникам прибрать за собой, занялись своими делами, раз за разом прокручивая в голове картинку великолепного для такого возраста тела школьницы.'
            $ st1.incLoy(5)
            $ st2.incLoy(5)
    $ move(curloc)
    
label event_loc_class2_15_3:
    show class2
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('female')
        st5 = getChar('female')
        setLust(5,20)
        hadSex(st1,st2)
        player.incLust(5)
    show expression 'pic/locations/school/class2/lo3.jpg' at top as tempPic
    'Зайдя в класс, вы услышали как [st2.fname] рассказывает подружкам про вчерашнюю встречу со своим одноклассником. Якобы [st1.fname] накончал ей полные трусы, стоило только показать ему свою киску. [st3.fname], [st4.fname] и [st5.fname] возбуждённо ахают в ответ.'
    'Вас этот разговор тоже немного возбудил.'
    $ move(curloc)
    
label event_loc_class2_40_4:
    show class2
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        hadSex(st1,st2)
        player.incLust(10)
    'Ещё с коридора услышав странные звуки из кабинета, вы решили зайти и посмотреть, что же их издаёт?'
    show expression 'pic/locations/school/class2/lo4.jpg' at top as tempPic
    'Как вы и догадывались, перед вами открылась знакомая картина... [st2.fname] вовсю ублажала своего парня, невзирая на то, что место, мягко говоря неудачное. Хотя вот способ весьма неплох.'
    'Вы даже засмотрелись, как она ловко двигает в рукой в такт движениям головы. Да, судя по сладострастным причмокиваниям, девушка получает от минета не меньшее удовольствие, чем парень! Редкий случай в наши дни. Что же с ними делать?'
    menu:
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Да пусть себе развлекаются':
            show expression 'pic/locations/school/class2/lo4a.jpg' at top as tempPic
            'Вы решили не отвлекать занятую молодёжь, и бросив на них последний взгляд, увидели, что [st2.fname] быстро вытащила член изо рта, и, умело двигая ручкой, заставила его сочиться семенем.'
            $ st1.incLoy(5)
            $ st2.incLoy(5)
    $ move(curloc)
    
label event_loc_class2_35_5:
    show class2
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        hadSex(st1,st2)
        player.incLust(10)
    show expression 'pic/locations/school/class2/lo5.jpg' at top as tempPic
    'В целях проверки школы, вы заглянули во второй кабинет. Судя по довольному лицу школьницы, она тоже устраивает неплохую проверку однокласснику. Вы не знаете сколько раз он уже кончил, но спермой залито всё. Причём [st2.fname] и не думает останавливаться, продолжая наяривать чувствительный член парня.'
    menu:
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Да пусть себе тестирует ёмкость яиц. От парня не убудет':
            $ st1.incLoy(5)
            $ st2.incLoy(5)
    $ move(curloc)
    
label event_loc_class2_25_6:
    show class2
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        st1.incCorr(5)
        player.incLust(5)
    show expression 'pic/locations/school/class2/lo6.jpg' at top as tempPic
    'Довольно интересный способ признания в любви Вы имели честь наблюдать. По крайней мере бешенный стояк парня напротив определённо намекал на ответные чувства. А [st2.fname] всё стояла перед ним со спущенными трусиками и говорила что то про то, как её киска жить без члена не может. Да, по обилию выделяющейся влаги киска просто плачет по хорошему члену.'
    menu:
        'Что же с ними делать то? С развратниками этими?'
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Признание в любви - дело тонкое. Мои взгляды могли и устареть...':
            $ st1.incLoy(5)
            $ st2.incLoy(5)
    $ move(curloc)
    
label event_loc_class2_25_7:
    show class2
    python:
        st1 = getChar('female')
        hadSex(st1)
        st1.incCorr(2)
        player.incLust(5)
    show expression 'pic/locations/school/class2/lo7.png' at top as tempPic
    'Зайдя в класс, вы заметили вашу ученицу, самоудовлетворяющуся, кхм, столом. То ли все парни испарились, то ли это новое направление в ориентации. Менсафилия какая то. Вы не смогли не заметить как сквозь тонкую ткань трусиков на стол уже просочилось довольно неслабое количество смазки.'
    menu:
        'Наказать':
            $ scoldWho = [st1]
            jump scoldAll
        'Уйти':
            $ st1.incLoy(5)
    $ move(curloc)
    
label event_loc_class2_11_8:
    show class2
    python:
        player.incLust(5)
        setLust(10,20)
    show expression 'pic/locations/school/class2/lo8.jpg' at top as tempPic
    'Хммм. Вы случайно нашли довольно пикантную, но сильно потёртую фотографию обнажённой женщины. Интересная ситуация. Как она здесь оказалась? Вы решили приберечь фотографию до лучших времён.'
    $ move(curloc)
    
label event_loc_class2_20_9:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        player.incLust(5)
        setLust(5,15)
        if st1.body.parts['грудь'].size > st2.body.parts['грудь'].size:
            st3 = st1
        else:
            st3 = st2
    show expression 'pic/locations/school/class2/lo9.jpg' at top as tempPic
    '[st1.name] и [st2.name] меряются сиськами. Какой занимательный конкурс. Хотя на Ваш непредвзятый судейский взгляд, [st3.fname] очевидно впереди.'
    $ move(curloc)
    
label event_loc_class2_35_10:
    show class2
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(25)
        hadSex(st1,st2)
    show expression 'pic/locations/school/class2/lo10.jpg' at top as tempPic
    'Звуки громких хлопков и стоны привлекли ваше внимание. [st1.fname] звонко хлопал девочку по заднице, явно наслаждаясь процессом. Кинув быстрый взгляд ей под юбку, вы осознали, что как ни странно,  [st2.fname] наслаждается поркой тоже.'
    ' Ну раз все наслаждаются, вы тоже решили присесть в сторонке и посмотреть на примерное наказание ученицы. К тому же её киска настолько призывно текла, что вы не смогли отказать себе в этом удовольствии.'
    st2.say 'Да, да, да! Отшлёпай свою сучку, я кончаю, [st1.fname], кончаю!!!'
    'К вашему удивлению, с оргазмом девушки ничего и не думало заканчиваться.'
    st1.say 'Чёт я перевозбудился глядя на тебя... Сделай что нибудь с этим.'
    show expression 'pic/locations/school/class2/lo10a.jpg' at top as tempPic
    'С этими словами парень снял штаны и направил свой член к ногам подружки, которая быстро смекнула, чего от неё хотят. Нежно обняв пальчиками напряжённую головку своего парня, [st2.fname] начала двигать ступнями. Член становился всё больше, вены вздувались всё сильней, пока перевозбуждённый парень не начал выплёскивать из себя сперму, аккуратно заляпывая ласкающие его пальчики ног.'
    player.say '"Мда, ну вот и насмотрелась... Сообщество мазохистов какое то, а не молодая пара."'
    $ move(curloc)
    

label event_loc_class2_20_1danokova:
    show class2
    python:
        if danokova.getCorr() < 30:
            skipEvent()
        st1 = danokova
        st2 = getChar('male','corrmax')
        hadSex(st1,st2)
    show expression 'pic/locations/school/class2/mid1.png':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    st1.say 'Повторяй за мной, я больше не буду так вести себя на уроках!'
    'Вы видите, как [st1.name], зажав крепкий член ученика ступнями, ведёт воспитательную работу.'
    st2.say 'Я, ах, больше не буду, ммм, так себя вести, ммм...'
    '[st2.fname] стонет, но двигает бёдрами в такт движениям ног учительницы.'
    st1.say 'Надеюсь после того, как твоё либидо будет удовлетворено, ты больше не будешь отпускать подобные шуточки в мой адрес'
    '[st1.name] серьёзно отчитывает школьника, не забывая усиленно массировать его пенис, пока тот не разряжается струями спермы.'
    player.say '"Ну чтож, образовательный процесс в действии, делать тут нечего."'
    $ move(curloc)
    
label event_loc_class2_15_2danokova:
    show class2
    python:
        if danokova.getCorr() < 30:
            skipEvent()
        st1 = danokova
        st2 = getChar('male','corrmax')
        hadSex(st1,st2)
    show expression 'pic/locations/school/class2/mid2.jpg' at top as tempPic
    st1.say 'Надеюсь, после того, как мы обманем твой мозг, заставив спустить часть твоей спермы из детородного органа, ты начнёшь внимательнее слушать, что я тебе объясняю на уроках!'
    'Вы наблюдаете за биологичкой, поучающей ученика. Встав немного сзади, она умело массирует его член, провоцируя скорое семяизвержение. Вот если бы не её заковыристый язык, цены бы ей не было!'
    'С чувством глубокого удовлетворения, вы покидаете кабинет'
    $ move(curloc)
    
label event_loc_class2_40_3:
    show class2
    python:
        if 'dildo' not in school.furniture:
            skipEvent()
        st1 = getChar('female','corrmax')
        player.incLust(10)
        hadSex(st1)
    show movie
    play movie "pic/locations/school/class2/mid3.gif.webm" loop
    'Вы обнаружили в классе одну из учениц. [st1.fname] сидела на столе, и меж её ног отчаянно крутился вибратор.'
    player.say '"Однако почему было нельзя воспользоваться вибратором прямо в третьем кабинете? Неужто от смены места удовлетворения что то меняется? Ох, не понять мне этих фантазёров!"'
    'Вы прикрикнули на ученицу, чтобы она вернула вибратор на место, когда закончит, и пошли по своим делам.'
    stop movie
    hide movie
    $ move(curloc)

label event_loc_class2_35_4:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st3 = getChar('male')
    show expression 'pic/locations/school/class2/mid4.jpg' at top as tempPic
    st1.say ' А вон там вон киска, - говорила [st1.fname] показывая одноклассникам своё совсем уже не детское тело.'
    st2.say 'Прям под волосами, да? - спросил [st2.fname] пытаясь разглядеть половые губы.'
    st3.say ' Да вон же, - поправил его [st3.fname], и провёл по киске рукой, - Ой, а чего это там всё влажное?'
    menu:
        'Наказать':
            $ scoldWho = [st1,st2,st3]
            jump scoldAll
        'Анатомия - полезная наука':
            $ setCorr(5,5)
            player.say '"Хоть не оконфузятся в первый раз, как мой парень, который зачем то начал пихать свою письку мне в пупок"'
            'Вы оставили юных экспериментаторов одних.'
    $ move(prevloc)
    
label event_loc_class2_60_5:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st1.incCorr(5)
    show expression 'pic/locations/school/class2/mid5.jpg' at top as tempPic
    player.say '"Да они вообще чтоли с ума посходили?"'
    'Вы наблюдаете, как [st2.fname] пытается впихнуть в анус одноклассницы откровенно невпихуемое. Хотя не похоже, что [st1.fname] хоть как то этому противится. Скорее наоборот, приняла максимально расслабленную позу, и покорно ожидает пока член начнёт теребить стенки её кишки.'
    menu:
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Надо уважать женское право выбора':
            $ hadSex(st1,st2)
            'Вы решаете дать девушке самой решать, что запихивать в себя, а что нет, и удаляетесь из класса.'
    $ move(prevloc)
    
label event_loc_class2_50_6:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1)
    show expression 'pic/locations/school/class2/mid6.jpg' at top as tempPic
    'Брызги из влажной киски. Вот что вы увидели, когда обратили внимание на копошение за партой. [st2.fname] своими умелыми пальчиками только довёл девушку до оргазма.'
    player.say '"Интересно, ему понравилось чувствовать её выделения на своём лице?"'
    'Немного отойдя после оргазма, [st1.fname] с удвоенными силами принялась сосать член парня.'
    menu:
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Дать девушке закончить':
            $ hadSex(st2)
            'Грустно было бы оставить парня без сладенького, поэтому вы решили не мешать маленьким развратникам, и вышли из класса.'
    $ move(prevloc)
    
label event_loc_class2_65_7:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
        player.incLust(15)
    show expression 'pic/locations/school/class2/mid7.jpg' at top as tempPic
    'Вы откровенно не ожидали, что такая штука может поместиться в чью то задницу. Хотя на ваших глазах [st1.fname] с успехом доказывала обратное, причём похоже ещё и получая удовольствие от процесса!'
    'Колечко её сфинктера довольно сильно натянулось, плотно обхватывая член, и наверное, доставляя парню немалое удовольствие от тесноты. [st2.fname], в свою очередь, довольно резко вгонял в её анус член, так, что ваша собственная попка непроизвольно сжималась опасаясь подобного вторжения. Несмотря на всю животную ярость спаривающейся парочки, вам тоже захотелось чего нибудь этаково.'
    menu:
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Дать им закончить':
            $ hadSex(st2)
            player.say '"Ну раз беременность исключена, то и опасаться нечего!"'
    $ move(prevloc)
    
label event_loc_class2_50_8:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
        player.incLust(10)
    show expression 'pic/locations/school/class2/mid8.jpg' at top as tempPic
    st1.say 'Сильнее! Умоляю тебя, сильнее!'
    '[st1.fname] умоляла трахающего её парня. И [st2.fname] двигался сильнее. Настолько, насколько мог. Его член резко входил в мокрое влагалище девочки, заставляя её ноги подрагивать от удовольствия. Смазка заливала ноги школьницы, и капала на пол вперемешку с потом. Два юных тела сладострастно сплетались в танце любви, пытаясь выжать максимально возможное из сложившейся ситуации. Они совершенно не обращают на вас внимания.'
    menu:
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Дать им закончить':
            show expression 'pic/locations/school/class2/mid8a.jpg' at top as tempPic
            'Вы уже собирались уходить, как вдруг [st1.fname] произнесла: "Дай я сама!", и повалив парня на пол уселась сверху.'
            st1.say 'Дааааа, - протяжно выдохнула девушка, снова вгоняя в себя член одноклассника, - Вот так то лучше!'
            'Активно двигаясь на парне, школьница ощущала как толстая головка таранит шейку её матки, неотвратимо приближая к оргазму. Внезапно парень покрепче ухватил подругу, и полностью вогнав свой член начал кончать, выплёскивая своё семя прямо внутрь девушки.'
            st1.say 'Иииии, - тоненько запищала [st1.fname], и, высунув язычок, задрожала, не в силах сдержать оргазма.'
            'Немного посмотрев на вздрагивающие после секса тела, вы вышли, прикрыв за собой дверь.'
            $ player.incLust(10)
    $ move(prevloc)
    
label event_loc_class2_50_9:
    show class2
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.incLust(10)
    show expression 'pic/locations/school/class2/mid9.jpg' at top as tempPic
    st1.say 'А так? - спросила [st1.fname] у своего парня, покачивая перед ним задницей и раскрыв свою киску руками, - А так меня хочешь?'
    st2.say 'Да! - кинулся к ней [st2.fname], скидывая на ходу одежду.'
    menu:
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Посмотреть':
            show movie
            play movie "pic/locations/school/class2/mid9a.gif.webm" loop
            st1.say 'По-до-жди! - выдавала девушка по слегу в перерывах между вторжениями члена в её лоно, - Не так рез-ко!'
            'Но парень обращал на неё мало внимания, ритмично вводя свой член в узенькую киску. Вскоре девушка перестала сопротивляться, и полностью отдалась напору трахающего её парня.'
            'Стоны школьницы становились всё громче, рискуя порвать ваши барабанные перепонки, и пока тут не собралась вся школы, Вы решили покинуть кабинет.'
            stop movie
            hide movie
            $ hadSex(st1,st2)
        'Предложить замену' if player.getLust() > 50:
            show expression 'pic/locations/school/class2/mid9b.jpg' at top as tempPic
            player.say 'Может быть ты хочешь кого нибудь по опытнее? - спросили вы парня, раздвигая свою киску и представая перед ним во всей красе.'
            'Конечно! - закивал головой школьник, пожирая вас глазами, и доставая свой член.'
            player.say 'Возьми меня наконец!'
            show expression 'pic/locations/school/class2/mid9c.jpg' at top as tempPic
            'Вы нетерпеливо заёрзали перед школьником. Подскочив к вам, он положил вас грудью на стол, и без прелюдий ввёл свой кол в вашу текущую киску.'
            player.say 'Даааа, - простонали вы, ощущая как возбуждённое влагалище заполняется крепким членом.'
            '[st2.fname] наяривал Вас с поистине юношеским рвением и умением. То есть энтузиазма было много, а у меня мало. Но несмотря на это, вы получали огромное удовольствия от движения члена в вашей хлюпающей щели. Внезапно горячая струйка семени ударила в вашей киске, и вскоре движения парня стали замедляться, и а вы так и остались без оргазма.'
            player.say 'Ну что же ты, засранец? - кинули вы недовольный взгляд на школьника, - А я?'
            player.say 'Давайте я вами займусь... - подползла к вашей киске [st1.fname] и с готовностью вытащила свой язычок.'
            $ hadSex(st2,player)
            $ st2.incLoy(10)
            menu:
                'Нет, хватит с меня экспериментов!':
                    $ player.coverSperm('вагина','ноги')
                    player.say 'Нет, всё, достаточно! - сказали вставая и ощущая как сперма из вашей киски стекает по ногам.'
                    player.say 'Приберитесь тут, а я займусь собой сама! - с этими словами, вы покинули кабинет.'
                    $ player.incLust(25)
                'Ну попробуй...':
                    show expression 'pic/locations/school/class2/mid9d.jpg' at top as tempPic
                    player.say 'Ну попробуй, - подставили Вы свою попу ученице, и та с готовностью взялась за дело.'
                    'Её язык сразу же погрузился в вашу попку, а пальчики начали вытаскивать из вашего влагалища сперму одноклассника. Вы с радостью отдались этим неумелым, но очень приятным ласкам. Пальцы школьницы как то сразу нашли вашу точку G и плавно надавливая на неё, начали двигаться. Язычок без устали работал над попкой, тщательно вылизывая её. Ваши ноги начали подрагивать от каждого прикосновения, и вскоре с губ сорвался протяжный стон и тело скрутили конвульсии оргазма.'
                    player.say 'Спасибо! - отдышавшись вы поцеловали девушку, перемазанную в сперме одноклассника, и пошли приводить себя в порядок.'
                    $ hadSex(st1,player)
                    $ st1.incLoy(10)
    $ move(prevloc)
    
label event_loc_class2_85_1:
    show class2
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
        hadSex(st1,st2,st3,st4,st5,st6,st7,st8,st9)
        hadSex(st1,st2,st3,st4,st5,st6,st7,st8,st9)
        player.incLust(25)
    show expression 'pic/locations/school/class2/hi1.jpg' at top as tempPic
    player.say '"Ого!"'
    'Это была, пожалуй, самая членораздельная мысль появившаяся в вашей голове, после того, как вы увидели что происходит в классе.'
    '[st6.name]скакала на лежащем на парте однокласснике, [st1.fname] в свою очередь старался проявить как можно больше активности в таком положении и положив руки на бёдра девушки, интенсивно двигал тазом, ритмично вгоняя свой член в хлюпающую пещерку.'
    '[st2.name], ухватив за волосы другу девушку, жадно сношал её в рот. Хотя, судя по её виду, [st7.fname] совсем не против подобного обращения и с радость принимает всё, что может ей дать парень.'
    'А вот [st3.fname] похоже не только страстен, но и довольно силён! Шутка ли, держать килограмм 40 чистого веса на руках, да ещё и с завидным упорством приседать...'
    'Зато сразу видно, что [st4.name] и [st5.name] - лучшие друзья! Делят между собой всё, включая девушку...'
    if player.getLust() > 80:
        player.say '"Ну ка, мальчишки, помогите мне!"'
        'Крикнули вы парням, и, задрав ноги выше головы, попросили, чтобы [st1.fname] подержал их.'
        show expression 'pic/locations/school/class2/hi1a.png' at top as tempPic
        'Помимо ученика, держащего вас за ноги, вашей позой заинтересовался [st2.fname]. Свой интерес он немедленно предъявил, и положил на вашу влажную киску.'
        player.say 'Ты бы хотя бы гондон одел, ловелас!'
        st2.say 'Боитесь залететь? - прищурился парень.'
        player.say 'Лень мыться! - парировали вы.'
        show expression 'pic/locations/school/class2/hi1b.png' at top as tempPic
        st1.say 'Это мы запросто! [st3.fname], угости заначкой! - не прошло и мгновения, как кондом оказался на члене, а член погрузился в вашу киску.'
        player.say 'М-м-матерь ты моя! - от удовольствия вы даже закатили глаза, ощущая каждой клеточкой вашего влагалища, проникающий в него член.'
        '[st2.name] начал неспешные движения, проникая всё глубже, вплоть до матки и даже дальше, растягивая влагалище всё сильнее. Ваши ноги задрожали, а ногти проскребли небольшую борозду на паркете.'
        player.say 'Ты великолепен! Почти как Ахмед!'
        st1.say 'Я лучше! - самодовольно ответил парень, и с удвоенной силой начал таранить вашу хлюпающую киску.'
        show expression 'pic/locations/school/class2/hi1c.png' at top as tempPic
        player.say 'Да! Да! Да! И-и-и! Да! Да! О-о-о!!!'
        'Член ученика доставал вам чуть ли не желудка, по крайней мере у вас складывалось такое впечатление. Но это была приятная заполненность, словно вы всю жизнь искали подобный пенис, которому можно было бы отдаться без остатка. Хлюпания текущей киски, ваши стоны, крики экстаза от сношающихся рядом школьников подвели ваш разум на грань оргазма.'
        'Вы беспорядочно повизгивали и подмахивали совсем не в такт. Пенис входил в щёлку постоянно под разными углами и с разной скоростью. Вы почти начали терять сознание от наслаждения, когда вас настиг спасительный оргазм.'
        'Тело затрясло так, что вы чуть не вырвались из рук парня, держащего вас за ноги. Одновременно вы ощутили, как в вас надувается огромный и горячий пузырь, не сразу поняв, что [st1.fname] тоже начал кончать, и заполняет презерватив своей молодой спермой.'
        player.say '"Ах, Ах, Оооо, Ах! Зря... Ах... Зря я настояла на кондоме.. Ах, ах.. О боже, как же хорошо!!!"'
        show expression 'pic/locations/school/class2/hi1d.png' at top as tempPic
        'Через несколько минут судорожных трепыханий, [st1.fname] наконец то извлёк свой член из вас, предъявив полный спермы презерватив.'
        player.say 'Ну ты и гигант, [st1.fname]!'
        st1.say 'Ну я же говорил!'
        'Вы попросили отпустить вас, после чего привели себя в порядок и обязали учеников прибрать за собой после оргии.'
        $ hadSex(st1,player)
        $ hadSex(st1,player)
        $ st1.incLoy(20)
        $ player.setLust(0)
        $ player.incCorr(5)
    $ move(curloc)
    
######################################################################################################################################
#
######################################################################################################################################

label event_loc_class3_0_no1:
    show class3
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/school/class3/no1.jpg' at top as tempPic
    'Сегодня выдался жаркий денёк. [st1.fname] обмахивает тетрадкой свою подругу.'
    if player.getCorr() > 60:
        player.say '"Да, жарковато сегодня... В такой то жаркий денёк неплохо было бы раздеться и утолить жажду похоти своей подруги..."'
        show expression 'pic/locations/school/class3/no1a.jpg' at top as tempPic
        player.say '"Да-а-а, снять с неё и себя трусики, слиться в долгом поцелуе, потереться влажной киской о нежную кожу бедра..."'
        player.say '"Потом достать огромный дилдо и... Кхм... Что то я отвлеклась..."'
        show expression 'pic/locations/school/class3/no1.jpg' at top as tempPic
        'Несмотря на ваши мечтания, [st2.fname] продолжает наслаждаться ветерком от тетрадки.'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_class3_0_no2:
    show class3
    python:
        st1 = frigidovna
    show expression 'pic/locations/school/class3/no2.jpg' at top as tempPic
    '[st1.name] подготавливает доску для следующего занятия. У неё сконцентрированное и задумчивое лицо.'
    if 'dildo' in school.furniture:
        show expression 'pic/locations/school/class3/no2a.jpg' at top as tempPic
        player.say '"Ага, как будто она представляет, словно докупила ко всем вибраторам и вагинам вибрационное седло, и активно испытывает его лично!"'
        'Вы ещё немного посмаковали в воображении картинку Фригидовны в чудо-седле, как она медленно насаживается на эти резиновые члены, и её внутренности сотрясаются в наслаждении...'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_class3_0_no3:
    show class3
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLoy(10)
        st2.incLoy(10)
    show expression 'pic/locations/school/class3/no3.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] развлекаются игрой на гитаре. Вы немного послушали их лирическую песни о солдате пропадающем в каком-то Афганистане, смахнули слезу, и вышли.'
    'Ученицам польстило, что вам понравилось их пение.'
    $ move(curloc)
    
label event_loc_class3_0_no4:
    show class3
    python:
        setRep(5,5)
    show expression 'pic/locations/school/class3/no4.jpg' at top as tempPic
    'Обычная перемена в обычной школе. Кто то ссориться, кто то разговаривает, кто то смотрит на вас заинтересованно, кто то не очень.'
    'Сделав ссорящейся парочке замечание, вы удаляетесь.'
    $ move(curloc)
    
label event_loc_class3_5_no5:
    show class3
    python:
        st1 = getChar('futa','lustmax')
        st1.setLust(70)
        st2 = getChar('male')
    show expression 'pic/locations/school/class3/no5.jpg' at top as tempPic
    'Вы появляетесь в середине разговора.'
    st1.say 'А ещё у меня член под юбкой!'
    'Вместо ответа, [st2.fname] шокированно смотрит на одноклассницу.'
    if st1.getCorr() > 20:
        st1.say 'Хочешь посмотреть?'
        show expression 'pic/locations/school/class3/no5a.png' at top as tempPic
        'Не дождавшись ответа одноклассника, [st1.fname] встаёт из за парты и всем становится отчётливо виден торчащий под юбкой член.'
        player.say '[st1.name]! А ну немедленно прекрати!'
        '[st2.name] смотрит на вас с благодарностью.'
        $ st2.incLoy(10)
    $ move(curloc)
    
label event_loc_class3_0_no6:
    show class3
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incLust(30)
        st1.incCorr(5)
    show expression 'pic/locations/school/class3/no6.jpg' at top as tempPic
    '[st1.fname] внимательно читает какой-то любовный роман, машинально накручивая на палец локон спящей рядом подружки. Не желая нарушать идиллию, вы тихо выходите, пока вас не заметили.'
    $ move(curloc)
    
label event_loc_class3_5_no7:
    show class3
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class3/no7.jpg' at top as tempPic
    'Грустная картина. Похоже на то, что [st1.fname] порвала со своим парнем, и теперь жалеет об этом.'
    'Вы подходите, и жалеете бедную девочку, успокаивая её тем, что это наверняка не последняя любовь в ее жизни.'
    $ st1.incLoy(5)
    if player.getCorr() > 60:
        show expression 'pic/locations/school/class3/no7a.jpg' at top as tempPic
        'Увлёкшись утешением, вы рассказываете девушке про то, что она ещё найдёт парня, который после школы будет нежно тыкаться горячей писькой в её молодую киску. Про то, как они сладко сольются в жарких обьятьях и будут любить друг друга с утра до самого вечера.'
        player.say 'А может быть вы потом и поженитесь!'
        if st1.getCorr() < 20:
            'Вы наконец обращаете внимание на шокированное лицо девушки. Похоже, что вы слегка перегнули палку.'
            $ st1.incLoy(-15)
        else:
            'Девушка благодарно улыбается вам. Похоже, что от вашего рассказа, она не только успокоилась, но и слегка развратилась!'
            $ st1.incLoy(5)
            $ st1.incCorr(5)
    $ move(curloc)
    
label event_loc_class3_0_no8:
    show class3
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('male','lustmax')
    show expression 'pic/locations/school/class3/no8.jpg' at top as tempPic
    player.say '"Да что же такое! Как не зайду в этот кабинет, так кто либо плачет, либо грустит. Карма тут нехорошая."'
    player.say 'У тебя что то случилось, [st1.fname]? - аккуратно интересуетесь вы.'
    'Её подруга [st2.fname] рассказывает ей, что сегодня на уроке Секспросвета [st1.fname] не смогла найти пенис на анатомическом атласе человека. Вы несколькими словами утешаете ученицу.'
    if player.getCorr() > 70:
        'А потом вам в голову приходит замечательная мысль, показать всё более наглядно.'
        show expression getCharImage(player, 'dialog') as temp1
        player.say 'Эй, [st3.name]! Подойди ка сюда!'
        show expression getCharImage(st3, 'dialog') as temp2
        st3.say 'А?'
        player.say 'Садись рядом, нам нужно кое что показать девчёнкам!'
        'Ничего не подозревающий парень, садится к вам за парту, и вы умелым движением расстёгиваете его ширинку, и достаёте наружу член.'
        hide temp1
        hide temp2
        show expression 'pic/locations/school/class3/no8a.png' at top as tempPic
        player.say 'Вот!'
        'Вы радостно потряхиваете достоинством парня, с улыбкой наблюдая за реакцией учеников. На задворках сознания вы понимаете, что вот так сразу член встать не мог, и вы достали его уже довольно возбуждённым, даже с небольшой влагой на кончике. Но всё таки продолжаете потряхивать им.'
        st3.say '[player.name], простите, я больше не могу!'
        player.say 'Что?'
        show expression 'pic/locations/school/class3/no8b.png' at top as tempPic
        'В ответ на невинное "что", член задрожал сам по себе и вам в ладонь выплеснулась накопленная за день сперма.'
        player.say 'А, ну счас мы можем наблюдать типичную эякуляцию, да... - мгновенно сориентировались вы.'
        'Девушки шокированно взирают на устроенный вашей шаловливой ручкой беспорядок.'
        player.say '"Ну по крайней мере теперь они знают не только где этот мужской половой пенис находится..."'
        'Вы быстренько собираетесь и, пряча заляпанную спермой руку за спиной, покидаете перешёптывающихся учеников.'
        python:
            st3.setLust(0)
            st1.incLust(20)
            st2.incLust(20)
            st1.incCorr(5)
            st2.incCorr(5)
            st3.incCorr(5)
            player.coverSperm('руки')
            player.incLust(15)
    $ move(curloc)
        
label event_loc_class3_10_no9:
    show class3
    python:
        st1 = getChar('female','corrmax')
        st1.incCorr(5)
    show expression 'pic/locations/school/class3/no9.jpg' at top as tempPic
    '[st1.fname] вытирает тряпочкой случайно пролившийся крем для рук.'
    player.say '"Ок. Расставим все палки над Й:\n1. Это не крем для рук.\n2. И не тряпочка."'
    player.say '"Это развратная [st1.fname] вытирает лубрикант своими трусиками."'
    $ move(curloc)
        
label event_loc_class3_0_no10:
    show class3
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class3/no10.jpg' at top as tempPic
    '[st1.fname] грустно стоит около открытого окна, и занавески нежно обмахивают её. Весьма поэтичная картина. Чего только не увидишь!'
    if player.getCorr() > 40:
        show expression 'pic/locations/school/class3/no10a.jpg' at top as tempPic
        player.say '"Хотя с моей точки зрения, она лучше бы смотрелась у доски с чьим то членом в заднице. Тоже было бы весьма поэтично!"'
        player.say '"Ну как минимум достойно бессмертных произведений Луки Мудищева!"'
        $ player.incLust(5)
    $ move(curloc)


    
label event_loc_class3_30_lo1:
    show class3
    python:
        st1 = getChar('futa','corrmax')
    show expression 'pic/locations/school/class3/lo1.jpg' at top as tempPic
    player.say 'Святая Дева Мария! - воскликнули вы, когда на вас приземлились потоки спермы, исторгнутые членом ученицы.'
    '[st1.fname], всё ещё постанывая, стискивает свой член, виновато разглядывая капли спермы.'
    menu:
        'Заставить убрать':
            player.say 'И кто это теперь будет убирать? - сурово сдвинув брови, спросили вы.'
            st1.say 'Ддавайте я...'
            show expression 'pic/locations/school/class3/lo1a.png' at left as tempPic
            'Ученица с готовностью подошла, тут же начав слизывать капли с вашего забрызганного лица.'
            player.say 'Подожди, что ты делаешь? - попытались вы отодвинуть виноватую школьницу.'
            st1.say 'Ничего, всё в порядке, пальцами только размажете, - c этими словами она всосала ещё одну капельку.'
            if player.getCorr() > 50:
                show movie
                play movie "pic/locations/school/class3/lo1b.gif.webm" loop
                player.say '[st1.fname], [st1.fname]... Куда ты? - испуганно спросили вы ученицу, когда та вдруг подняла вашу юбочку, и залезла языком прямо в киску'
                st1.say 'По моему туда тоже попало, [player.name], - ученица всерьёз занялась клитором, заставив вас испустить стон удовольствия.'
                player.say 'Да, пожалуй ты права, там ещё глубже чуть чуть, - закрыв глаза от наслаждения вы полностью отдались ласкам ученицы.'
                stop movie
                hide movie
                show expression 'pic/locations/school/class3/lo1c.jpg' at top as tempPic
                player.say 'Да, да, ДА! - закричали вы в оргазме , плотнее прижимаясь к лицу маленькой футанари своей киской'
                'Её язычок активней заработал над трепещущимся бугорком, и вы вдруг ощутили как пульсирующая киска начала исторгать большой объём жидкости прямо на личико девочки.'
                player.say 'А ты хороша! - улыбнулись вы ученице, - только вот не до конца всё слизала, ну да ладно, иди.'
                st1.say 'Спасибо за всё, [player.name], - поклонилась девушка и вышла из класса. Интересно, что же на неё нашло?'
                $ st1.incLoy(10)
                $ st1.incCorr(10)
                $ player.setLust(0)
            else:
                player.say 'Всё, достаточно, дальше я сама, - вы выгнали расстроенную ученицу из класса.'
                $ st1.incLoy(-10)
                $ player.coverSperm('ноги','грудь')
        'Выгнать и заняться чисткой одежды':
            'Вы негодующе посмотрели на ученицу, жалея что не наказали её, и, выгнав из класса, стали рассматривать размеры катастрофы с одеждой. А они велики, потому что посмотревшись в зеркальце,  вы обнаружили пару капель даже на своём лице.'
            player.say '"Мда уж, полна [st1.fname] неожиданностей!"'
            $ player.coverSperm('лицо','ноги','грудь')
            $ st1.incLoy(5)
        'Наказать':
            $ player.coverSperm('лицо','ноги','грудь')
            $ scoldWho = [st1]
            jump scoldAll
    $ move(curloc)
    
label event_loc_class3_40_mid1:
    show class3
    python:
        st1 = getChar('male')
        st2 = getChar('male')
        st3 = getChar('female')
        player.incLust(5)
    st1.say 'Мне так неприятно!'
    show expression 'pic/locations/school/class3/mid1.jpg' at top as tempPic
    'И действительно, [st3.name] делала ему весьма непрофессиональную работу ножками, от чего приятного было мало.'
    st3.say 'Не ври мне! Всё должно быть хорошо!'
    '[st3.fname] с силой водила по оголённой головке ногами. Вас аж передёрнуло от этого зрелища.'
    menu:
        'Наказать их':
            $ scoldWho = [st1,st3]
            jump scoldAll
        'Пусть сами учатся':
            $ hadSex(st1,st3)
        'Вмешаться в процесс' if player.getCorr() > 70:
            $ player.incCorr(5)
            $ player.coverSperm('ноги')
            $ player.incLust(20)
            player.say 'Нет, ну кто так делает! Иди сюда! - [st2.fname] проходивший по коридору был затянут вами в класс.'
            show expression 'pic/locations/school/class3/mid1a.jpg' at top as tempPic
            player.say 'Смотри и учись! - вы умело обхватили пальчиками ног орган ученика и начали его аккуратно массировать, - Чего замерла? Повторяй!'
            '[st3.fname] неуверенно начала повторять ваши движения и [st1.fname] застонал от её движений, благодарно посмотрев на вас.'
            player.say 'Давай же, родной, давай!'
            'Вы поглядывали на ученика, активно массируя его головку ступнями, кинув взгляд на ученицу, вы замечаете, что она тоже ускорилась вслед за вами.'
            show expression 'pic/locations/school/class3/mid1b.jpg' at top as tempPic
            st1.say 'Д-а-а-а!'
            st2.say 'О-о-о!'
            'Хрип кончающих парней cлился воедино, и ваши с ученицей ножки оказались забрызганы их семенем.'
            player.say 'Чудненько же! [st3.fname], надеюсь в следующий раз ты будешь более аккуратна!'
            'Покрасневшая школьница кивнула вам в ответ'
    $ move(curloc)
    
label event_loc_class3_50_mid2:
    show class3
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        hadSex(st1,st2)
        player.incLust(10)
    show movie
    play movie "pic/locations/school/class3/mid2.gif.webm" loop
    '[st1.fname] и [st2.fname] яростно заканчивают спаривание прямо у Вас на глазах. Вы не можете назвать это действие ничем иным, потому что ученик двигается буквально как зверь внутри одноклассницы.'
    menu:
        'Наказать их':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Подождать, пока они закончат':
            play movie "pic/locations/school/class3/mid2b.gif.webm" loop
            'Наконец [st2.fname] кричит: "Сновааа!", и вы видите как её сокращающееся в оргазме влагалище выплёскивает из себя потоки спермы прямо на яйца ученика.'
    stop movie
    hide movie
    $ move(curloc)

label event_loc_class3_50_mid3:
    show class3
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        hadSex(st1,st2)
        player.incLust(10)
    show expression 'pic/locations/school/class3/mid3.jpg' at top as tempPic
    st2.say 'Да, да, да, да!'
    'Вы с любопытством наблюдаете как [st1.fname], положив одноклассницу на стол, с силой хлопает своим животом по её бёдрам.'
    st2.say 'Сильнее, даааа!'
    'C каждым движением парня [st2.fname] выделяет больше смазки, которая стекает по её бёдрам прямо на стол и и капает на пол.'
    st2.say 'Кончаю!'
    'Девушка затряслась, и выгнувшись дугой, вырвалась из рук одноклассника, конвульсируя в оргазме.'
    st2.say 'Извини, в следующий раз займёмся тобой!'
    '[st2.fname] чмокнула одноклассника в щёчку и стала поправлять одежду.'
    if player.getLust() > 80:
        player.say 'Позволь мне им занятся, коль ты уже устала!'
        hide tempPic
        'Вы отодвигаете девушку в сторонку, скидываете с себя одежду, и занимаете место "уставшей" ученицы.'
        show expression 'pic/locations/school/class3/mid3a.png' at top as tempPic
        'Не долго взвешивая все за и против того, стоит ли трахать своего директора. Даже не задумываясь об этом! Парень резко вставил измазанный соками одноклассницы член в ваше хлюпающее влагалище.'
        player.say 'О-о-ох!'
        'Вы резко выдохнули, наслаждаясь сильным проникновением. Вы так долго ждали, пока вас кто то заполнит, что нетерпеливо принялись елозить попой по столу, ритмично вгоняя в себя скользкий член.'
        st1.say 'Ка-а-айф! - протянул парень, - [player.name], только я так долго не протяну!'
        player.say 'Кончай! Давай! Я разрешаю! Я и так этого долго ждала!'
        show expression 'pic/locations/school/class3/mid3b.png' at top as tempPic
        'Парень ускорился ещё сильнее, и вскоре два голоса закричали в экстазе. Лишь [st2.fname] сидела одиноко в сторонке, с ревностью взирая на ваше неистовое соитие.'
        player.say 'Вообще то, когда я кричала "кончай", я не имела в виду "кончай прямо в меня!" - вы с неудовольствием рассматриваете капли спермы, капающие из вашей киски на пол.'
        player.say 'А, ладно, один раз живём!'
        hide tempPic
        'На этой житейской мудрости вы расстались с юной парой, слыша, как за вашей спиной разгорается скандал.'
        $ player.coverSperm('вагина')
        $ player.setLust(0)
        $ hadSex(st1,player)
        $ st1.incLoy(10)
        $ st2.incLoy(-10)
    $ move(curloc)

label event_loc_class3_55_mid5:
    show class3
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        st3 = getChar('male')
        hadSex(st1,st2,st3)
    show expression 'pic/locations/school/class3/mid5.jpg' at top as tempPic
    player.say '"Кого то только что страстно отжарили..."'
    'Вы разглядываете до сих пор вздрагивающую в оргазме девушку. Парень ушёл, а посторгазменные конвульсии отстались. Хотя кого жарили и так понятно, имя этой преносчицы чужой спермы - [st2.fname], а вот кто её заполнял - это вопрос.'
    'Вы насилу привели в себя девушку, и выяснили, что развлекалась она сразу с двумя парнями. Теперь вы знаете кого наказать и за что.'
    menu:
        'Наказать их':
            $ scoldWho = [st1,st2,st3]
            jump scoldAll
        'Дело молодое, женщин на всех не хватает..':
            $ setLoy(3,10)
    $ move(curloc)

######################################################################################################################################
#
######################################################################################################################################

label event_loc_class4_0_no1:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('female')
        st5 = getChar('futa')
        setFun(10,10)
    show expression 'pic/locations/school/class4/no1.jpg' at top as tempPic
    'Школьная рок группа репетирует песню "Это математично" из своего нового альбома "Время приключений". Казалось бы причём тут собака? Вы не стали мешать репетиции, и ушли.'
    $ move(curloc)
    
label event_loc_class4_0_no10:
    show class4
    python:
        st1 = bissektrisovna
        st2 = getChar('female')
        st3 = getChar('male')
        st4 = getChar('male')
        setFun(5,10)
    show expression 'pic/locations/school/class4/no10.jpg' at top as tempPic
    'Похоже [st3.fname] всё таки смог доказать теорему Пифагора. Правда [st1.name] немного шокирована формулировкой "Пифагоровы трусы".'
    $ move(curloc)
    
label event_loc_class4_0_no2:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('male','lustmax')
        st4 = getChar('male','corrmax')
    show expression 'pic/locations/school/class4/no2.jpg' at top as tempPic
    'Похоже назревает конфликт. [st1.fname] поставила ноги на стол однокласснице, и снисходительно смотрит на неё сидя на соседней парте. Если так пойдёт дальше, [st2.fname] тоже в долгу не останется.'
    menu:
        'Наказать их':
            $ scoldWho = [st1,st2]
            jump scoldAll
        'Разнять их':
            'Вы отчитали обеих учениц, за недостойное поведение, и пригрозили сообщить обо всём их родителям.'
            $ st1.incLoy(10)
            $ st2.incLoy(10)
        'Не обращать внимания':
            $ st1.incLoy(10)
            $ st2.incLoy(-10)
    $ move(curloc)
    
    
label event_loc_class4_0_no3:
    show class4
    python:
        st1 = getChar('female')
        st1.incFun(10)
    show expression 'pic/locations/school/class4/no3.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.name] проветривает ножки на перемене. Вы и сами не понимаете, почему обратили на это внимание.'
    if player.getCorr() > 40:
        show expression 'pic/locations/school/class4/no3a.jpg' at top as tempPic
        player.say '"Наверное потому, что эта ножка гораздо лучше смотрелась бы на члене одноклассника..."'
        $ player.incLust(5)
    $ move(curloc)
 
label event_loc_class4_0_no5:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('male')
        setFun(4,15)
    show expression 'pic/locations/school/class4/no5.jpg' at top as tempPic
    '[st1.fname], [st2.fname], [st3.fname] и [st4.fname] решили устроить соревнование по новой игре для дандендо - "Шмота 2". Ну чтож, время не учебное, пусть отдыхают.'
    if st4.getCorr() > 40:
        show expression 'pic/locations/school/class4/no5a.png' at top as tempPic
        'Вы отвлеклись на свои дела на несколько минут, но когда обернулись, обнаружили, что [st4.fname] уболтал одноклассницу на лёгкий интим.'
        'Как ни странно, соревнований по игре это не прекратило, хотя победитель определённо наметился.'
        menu:
            'Наказать их':
                $ scoldWho = [st1,st4]
                jump scoldAll
            'Не обращать внимания':
                $ hadSex(st1,st4)
                $ setLust(4,20)
                $ st1.incLoy(10)
                $ st4.incLoy(10)
    $ move(curloc)

label event_loc_class4_0_no6:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/school/class4/no6.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] решили обсудить достижения Перельмана в математике.'
    if player.getIntel() > 50:
        'Вы довольно обоснованно вспомнили про доказательство гипотезы Пуанкаре, а так же про дальнейший отказ от "Премии тысячелетия".'
        'Ученики обязательно расскажут родителям, какой у них эрегированный директор.'
        $ setRep(2,10)
    else:
        'Откровенно говоря, слово "соснула" довольно чётко описывает вашу дальнейшую дискуссию. Это довольно плохо сказалось на вашей репутации.'
        $ setRep(2,-10)
    $ move(curloc)
    
label event_loc_class4_0_no7:
    show class4
    python:
        st1 = getChar('female','corrmax')
    show expression 'pic/locations/school/class4/no7.jpg' at top as tempPic
    '[st1.fname] уселась на парты, и с интересом наблюдает за вами.'
    if st1.getCorr() > 50:
        'Потом встаёт, и направляется к выходу.'
        show expression 'pic/locations/school/class4/no7a.png':
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        'Вы не удерживаетесь от любопытства, заглядываете ей под юбочку, чтобы узнать причину столь внимательного взгляда. И вашему взгляду предстают пара проводочков выходящих из под трусиков девочки.'
        player.say '"Ну тут два варианта. Либо это бабаробот, либо [st1.name] - очень развратная девушка!"'
        $ st1.incLust(25)
    $ move(curloc)
    
    
label event_loc_class4_0_no8:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incFun(10)
        st2.incFun(10)
    show expression 'pic/locations/school/class4/no8.jpg' at top as tempPic
    '[st1.fname] уснула на коленях у своей подруги. Такое чувство, что у меня в школе ученики вообще не занимаются, а только дрыхнут! Стоило конечно разбудить девочку, но человек способный разбудить спящего, способен вообще на любую подлость!'
    $ move(curloc)
    
label event_loc_class4_0_no9:
    show class4
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st1.incFun(10)
        st2.incFun(10)
        setRep(2,10)
    show expression 'pic/locations/school/class4/no9.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] высунулись в окно, и дышат свежим воздухом.'
    'Вы делаете им замечание, чтобы они слишком далеко не высовывались.'
    $ move(curloc)
    
######################################################################################################################################
#
######################################################################################################################################

label event_loc_class5_0_no1:
    show class5
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/class5/no1.jpg' at top as tempPic
    'Зайдя в кабинет, Вы видите что [st1.fname] решила сесть на диету, или просто тренирует свою силу воли. Хотя её лицо говорит о том, что от силы воли остались лишь мелкие крохи.'
    if player.getEnergy() < 500:
        'Не желая больше мучить ученицу, вы накинулись на сладости, и к вашему удивлению всё умяли. Ученица смотрит на Вас с благодарностью.'
        $ player.incEnergy(200)
    $ move(curloc)

label event_loc_class5_0_no2:
    show class5
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        st3 = getChar('female')
        setFun(10,5)
    show expression 'pic/locations/school/class5/no2.jpg' at top as tempPic
    'Кто то бегает, вот [st1.fname] спит,  [st2.fname] и [st3.fname] общаются о чём то в сторонке. Обычный день в школе.'
    $ move(curloc)
    
label event_loc_class5_0_no3:
    show class5
    python:
        st1 = getChar('female')
        setFun(10,10)
    show expression 'pic/locations/school/class5/no3.jpg' at top as tempPic
    'Это вы удачно зашли! Похоже, что [st1.fname] справляет свой день рождения! Вы говорите ей свои дежурные поздравления, и оставляете учеников праздновать дальше.'
    $ move(curloc)
    
label event_loc_class5_5_no4:
    show class5
    python:
        st1 = getChar('futa')
        st2 = getChar('female')
    show expression 'pic/locations/school/class5/no4.jpg' at top as tempPic
    'Войдя в класс, вы заметили, что [st1.fname] одёргивает юбку так, словно секунду назад она была поднята.'
    st1.say 'Это не то, о чём вы подумали, - со страхом говорит [st1.fname].'
    player.say 'А о чём я подумала?'
    st1.say 'Ну как будто я всем показывала свой, своего... - ученица замолкает.'
    player.say 'Они тебе не верили, да? Не переживай, я знаю что такие иногда рождаются, - быстро всё поняв, утешаете вы ученицу.'
    if player.getCorr() > 50:
        player.say 'А вы не смейтесь! - окрикиваете вы расшалившихся учеников.'
        show expression 'pic/locations/school/class5/no4a.jpg' at top as tempPic
        player.say 'Настанет время, и может быть даже ты, [st2.fname], будешь с трепетом касаться её члена, направляя его в свою узенькую дырочку!'
        player.say '"Да... Огромный член в её маленькой дырочке..."'
        'Вы оставляете немного шокированных вашими словами учеников.'
    $ move(curloc)
    
label event_loc_class5_0_no5:
    show class5
    python:
        st1 = getChar('futa','lustmax')
        st2 = getChar('female')
    show expression 'pic/locations/school/class5/no5.jpg' at top as tempPic
    '[st1.name] вцепилась в волосы своей одноклассницы, и куда то ведёт её.'
    menu:
        'Сделать замечание':
            'Вы сделали замечание ученице, и [st1.fname] отпустила волосы. [st2.fname] смотрит на вас с благодарностью.'
            $ st1.incLoy(-10)
            $ st2.incLoy(15)
        'Не обращать внимания':
            $ st1.incLoy(10)
            $ st2.incLoy(5)
            'Вы решили не обращать внимания на эту странную парочку. Остаётся надеятся, что ничего страшного не случится.'
        'Проследить за ними' if getPar(studs,'corr') > 25 or development == 1:
            $ hadSex(st1,st2)
            show expression 'pic/locations/school/class5/no5a.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            'Девушки уединяются в свободном кабинете, и вы замечаете, что [st1.name] не совсем девушка. Усевшись на парту, она приспускает трусики и из под юбки выпрыгивает крепкий член.'
            st1.say 'Подрочи мне, как всегда, - требовательно произносит молодая фута.'
            '[st2.fname] кладёт свои ручки на подрагивающий пенис и начинает медленно ласкать уздечку.'
            show expression 'pic/locations/school/class5/no5b.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            st1.say 'Да... Вот так вот хорошо! Продолжай!'
            'С кончика члена девушки начинает стекать небольшая струйка преэякулята, смазывая шаловливые пальчики подружки. Она берёт член покрепче, и продолжает ласкать уздечку своей влажной ладошкой.'
            show expression 'pic/locations/school/class5/no5c.jpg':
                xalign 1.0 yalign 0.0
                ease  10.0 yalign 1.0
                ease  10.0 yalign 0.0
                repeat
            'Наконец [st1.fname] издаёт громкий стон и в потолок бьёт маленький фонтанчик спермы.'
            st2.say 'Мне уже можно идти?'
            '[st2.fname] с беспокойством разглядывает перемазанные в семени руки.'
            st1.say 'Ага! Завтра я тебя снова найду!'
            player.say '"Однако интересные отношения завязываются в моей школе..."'
            $ player.incLust(10)
    $ move(curloc)
    
label event_loc_class5_0_no6:
    show class5
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        st1.incFun(10)
        st2.incFun(15)
    show expression 'pic/locations/school/class5/no6.png' at top as tempPic
    st1.say 'Ну, короче, выхожу я вчера на мид, а керри в лесу. Ну я ему кричу, мол какого хера, кто мид пушить будет, я саппорт!'
    '[st1.fname] рассказывает подружке, как он вчера до 2 часов ночи рубал с друзьями в Шмоту. Вы бы не сказали, что [st2.name] в восторге от этих разговоров, но что в этом мальчике ей определённо нравится.'
    if player.getCorr() > 60:
        show expression 'pic/locations/school/class5/no6a.jpg' at top as tempPic
        player.say '"А может быть ей нравится его упругий член, который каждый день, по ночам,терзает её хрупкий анус?"'
        'Вы отчётливо представили, как [st1.fname], закончив свои ночные бои в Шмоте, заходит в спальню к подружке и, перевернув её попкой к верху, медленно вводит член в неподатливое колечко сфинктера. У вас аж всё сжалось от реалистичности картинки предоставленной воображением.'
        $ player.incLust(10)
    $ move(curloc)
    

label event_loc_class5_10_no7:
    show class5
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/school/class5/no7.jpg' at top as tempPic
    player.say '"Ого, сколько учебников приходится таскать в школу нашим ученикам!"'
    'Хотя не видно, чтобы [st1.fname] сильно напрягалась от переноски такой стопки. Вот он, скрытый спортивный потенциал! В любом случае неплохо было бы помочь донести их.'
    menu:
        'Помочь':
            'Вы помогли донести учебники до парты. [st1.fname] благодарит вас.'
            $ st1.incLoy(10)
        'Подрядить ученика на это дело':
            $ hadSex(st1,st2)
            player.say 'Эй, [st2.fname]! Подойди пожалуйста, помоги девочке с тяжёлыми книжками!'
            'Парень, постоянно подтягивая спадающие треники, кивает вам, и бросается на помощь однокласснице. Вы, с удовлетворённым видом отворачиваетесь, как внезапно слышите глухой удар и крик девушки за спиной.'
            show expression 'pic/locations/school/class5/no7a.jpg' at top as tempPic
            'Нет, вы конечно читали в объяснительные, мол шёл, упал на девушку, случайно изнасиловал, но вживую подобную ситуацию видите впервые. Стремительно бегущий парень в конце концов запутался в своих трениках, и врезался в школьницу. Со спущенными штанами. Со стоящим членом. Врезался так, что вдавил членом трусики глубоко ей во влагалище.'
            show expression 'pic/locations/school/class5/no7b.jpg' at top as tempPic
            st1.say 'В-в-выйди из меня, пожалуйста! - шепчет девушка, стоя на подрагивающих ногах и поддерживаемая в вертикальном положении глубоко сидящим в ней членом.'
            st2.say 'Я ненаро... О боже, подожди, НЕ ДВИГАЙСЯ!!!'
            'Девушка активно заёрзала, пытаясь выбраться из щекотливой ситуации. Парень же, в свою очередь, вовсю пытался минимизировать эти движения. В итоге все эти действия со стороны смотрелись как банальные фрикции.'
            st2.say 'Ч-ч-чёрт! Прости!'
            show expression 'pic/locations/school/class5/no7c.jpg' at top as tempPic
            'Когда парень наконец то достал свой член из влажных трусиков, за ним протянулась густая белая капля спермы. [st1.fname] слегка застонала, видимо не совсем понимая, что сейчас произошло.'
            player.say 'Эмм, давайте я лучше закрою глаза на то, что сейчас произошло. Боюсь, что даже если я расскажу, мне всё равно никто не поверит.'
            'Школьники согласно закивали головами. Хотя [st1.name] ещё не в себе. Будем надеятся, что на тоже никому не расскажет.'
            $ player.incLust(5)
    $ move(curloc)

label event_loc_class5_0_no8:
    show class5
    python:
        st1 = getChar('female')
        st1.incFun(-10)
    show expression 'pic/locations/school/class5/no8.png':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Похоже, что [st1.fname] потеряла свою школьную обувь, и ищет её. Выражение её лица говорит вам о том, что ищет [st1.fname] уже давно.'
    if player.getCorr() > 60:
        show expression 'pic/locations/school/class5/no8a.jpg' at top as tempPic
        player.say '"Такая задница! Да, эта попа прекрасно бы смотрелась залитой спермой из парочки членов!"'
    $ move(curloc)
    
label event_loc_class5_0_no9:
    show class5
    python:
        setFun(5,20)
    show expression 'pic/locations/school/class5/no9.jpg' at top as tempPic
    'Школьная рок группа репетирует песню "Стрела в колене" из своего нового альбома "Молодые сливки 5". Казалось бы причём тут драконы? Вы не стали мешать репетиции, и ушли.'
    $ move(curloc)
    
    
    
######################################################################################################################################
#
###################################################################################################################################### 



label event_loc_entrance_20_StartClubPanties:
    show entrance
    python:
        global is_pantiesClub
        if is_pantiesClub != 0:
            skipEvent()
        st1 = getChar('female','corrmax')
    player.say 'Хммм...'
    'Вы слышите странное кряхтение неподалёку.'
    st1.say 'Ну снимайся же, давай! Эх, надо было на размер больше брать!'
    show expression 'pic/locations/school/entrance/pantiesClub.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Вы заходите за школу и видите, как [st1.name] пытается снять свои трусики!'
    if player.getCorr() < 40:
        player.say 'Это что ещё за разврат на голом месте! А ну немедленно прекрати, пока никто не видит!'
        st1.say 'Да уже поздно, вы всё равно увидели... - вздыхает ученица, но всё таки натягивает трусики назад.'
        player.say 'В наказание останешься после уроков!'
        st1.say 'Ясно... - вздыхает ученица и направляется к школе.'
        $ addDetention(st1)
    else:
        player.say 'Это чем это ты занимаешься, позволь спросить?'
        st1.say 'Я ну просто... Это... - неудачно пытается выкрутиться ученица.'
        player.say 'Только не говори, что тебе доставляет эстетическое удовольствие сидеть голой задницей на стуле.'
        st1.say 'Нет, конечно нет... Мы их продаём.'
        player.say 'Продаёте? ВЫ? То есть ты не единственная, кто сегодня носится по школе без нижнего белья?'
        st1.say 'Упс... - прикрывая свой рот шепчет девочка.'
        player.say 'И кому же вы их, простите, продаёте?'
        'Спустя мгновение на вас обрушивается сбивчивый рассказ о том, что девчёнки выискали в интернете сайт с извращенцами, которые покупают поношенные трусики. Ну разумеется им не пришло в голову ничего лучше, как начать встречаться с ними и продавать своё нижнее бельё. Вы решаете взять дело в свои руки.'
        player.say 'Так, хватит шляться по подворотням и продавать свои трусы!'
        '[st1.fname] понуро опускает голову.'
        player.say 'Теперь вы будете делать это организованно! Мы создадим клуб, и вы, каждый день будете отдавать мне свои трусики, продажу я беру на себя, а барыши делим пополам, согласна?'
        st1.say 'Конечно! - радостно улыбается ученица.'
        player.say 'Отлично! Тогда снимай и кидай своё добро мне в сумку.'
        '[st1.fname] снимает свои трусики под вашим пристальным взором и отдаёт их вам.'
        python:
            global is_pantiesClub
            player.addItem(clubPanties)
            st1.removeItems(studpantiesF.name)
            st1.club = 'pants'
            is_pantiesClub = 1
    $ move(curloc)
    
label event_loc_entrance_0_1:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st3 = getChar('female')
        st4 = getChar('female')
    show expression 'pic/locations/school/entrance/no1.jpg' at top as tempPic
    '[st2.name] подаёт подруге зонтик с отстранённым видом. Всем понятно, что делает он это не просто так, но вот 2 девчёнки, которые подглядывают за этим, явно завидуют.'
    if player.getCorr() > 50:
        show expression 'pic/locations/school/entrance/no1a.jpg' at top as tempPic
        player.say '"Надёюсь ему перепадёт сегодня не только улыбка!"'
        'У вас аж голова закружилась, от мыслей, чего [st1.fname] и [st2.fname] могут вытворять вместе!"'
        $ player.incLust(5)
    $ st1.incCorr(1)
    $ st2.incCorr(1)
    $ move(curloc)
    
label event_loc_entrance_0_2:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/school/entrance/no2.jpg' at top as tempPic
    'Упс. Мимоветерок случайно поднял юбочку девчёнки! Как мило!'
    if player.getCorr() > 50:
        player.say '"И как развратно!"'
        $ player.incLust(5)
    $ setFun(10,5)
    $ setLust(10,10)
    $ move(curloc)
    
label event_loc_entrance_0_3:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/school/entrance/no3.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] похоже опаздывают в школу! Заметив вас, [st2.fname] делает испуганное лицо.'
    if player.getCorr() > 50:
        player.say 'Ну, ну, милая, я не кусаюсь!'
        $ st2.incLoy(5)
    $ st1.incFun(-5)
    $ st2.incFun(-5)
    $ move(curloc)
    
label event_loc_entrance_0_4:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('female')
    show expression 'pic/locations/school/entrance/no4.png' at top as tempPic
    '[st1.fname] и [st2.fname] радостно приветствуют вас! Хотя вот [st2.fname] приветствует как то менее радостно...'
    if player.getCorr() > 50:
        player.say 'Солнышко, ну чего ты надулась? Иди сюда, я тебя обниму! - и вы нежно обнимаете ученицу.'
        $ st2.incLoy(5)
    $ st1.incFun(5)
    $ st2.incFun(5)
    $ move(curloc)
    
label event_loc_entrance_0_5:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
    show expression 'pic/locations/school/entrance/no5.jpg' at top as tempPic
    '[st1.fname] ещё смотрит на Вас с улыбкой, [st3.fname] уже спешит Вам на помощь, [st2.fname] сейчас случайно зарядит вам портфелем по лиц... БУМ... '
    player.say '"Мда, жаль, это была многообещающий день, если бы не портфель." - подумали вы лёжа на земле'
    $ player.incEnergy(-100)
    $ move(curloc)
    $ setFun(3,5)
    $ move(curloc)
    
label event_loc_entrance_5_6:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/school/entrance/no6.png' at top as tempPic
    '[st1.fname] и [st2.fname] похоже нашли друг друга. Какая милая картина, видеть их держащимися за руку!'
    if player.getCorr() > 50:
        player.say '"Хотя я бы лучше посмотрела на них вдвоём в постели..."'
        show expression 'pic/locations/school/entrance/no6a.jpg' at top as tempPic
        player.say '"Или вдвоём на парте... Да, вдвоём, да на школьной парте они смотрелись бы великолепно!"'
        player.say '"Особенно его толстенный член в её узенькой киске!"'
        $ player.incLust(10)
    $ st1.incCorr(1)
    $ st2.incCorr(1)
    $ move(curloc)
    
label event_loc_entrance_0_7:
    show entrance
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/entrance/no7.png' at top as tempPic
    'Вы с удовольствием отметили короткость юбки и белизну трусиков школьницы. Будем надеяться, что не только у вас глаз намётан!'
    $ player.incLust(5)
    $ setFun(10,5)
    $ move(curloc)
    
label event_loc_entrance_0_8:
    show entrance
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/entrance/no8.png' at top as tempPic
    'Поднимаясь по лестнице к школе, и бросив случайный взгляд наверх, у вас резко потеплело в трусиках. Да, такой симпатичный видок не каждый день открывается!'
    $ player.incLust(5)
    $ setFun(10,5)
    $ move(curloc)
    
label event_loc_entrance_0_9:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
    show expression 'pic/locations/school/entrance/no9.png' at top as tempPic
    'Вы видите, как [st1.fname] и [st2.fname] мило беседуют, кушая принесённую из дома еду.'
    if player.getCorr() > 50:
        show expression 'pic/locations/school/entrance/no9a.jpg' at top as tempPic
        player.say '"Интересно, успел ли сегодня [st1.fname] накормить киску подружки своим молочком?"'
        player.say '"Я бы посмотрела на такую кормёжку!"'
        $ player.incLust(10)
    $ st1.incFun(10)
    $ st2.incFun(10)
    $ move(curloc)
    
label event_loc_entrance_30_1:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.incLust(10)
    'Проходя мимо входа, вы услышали часть разговора за углом школы.'
    st2.say 'Конечно!, - всегда хотел это попробовать!'
    show expression 'pic/locations/school/entrance/lo1.png' at top as tempPic
    'Вам стало интересно кто и что хотел попробовать. Вы вышли из за угла и увидели что это [st1.fname] и [st2.fname].'
    'Улыбнувшись, [st1.fname] положила член между грудей и сжала его ими. Его член попал в мягкий нежный плен из которого ему совсем не хотелось выбираться. Начав двигаться, она принялась трахать его своими сиськами.'
    player.say '"Чёрт, и правда как в  порнофильмах, что я смотрела!"'
    '[st1.fname] убыстряла свои движения, лаская головку языком когда она показывалась между сисек. [st2.fname] напрягся и мне показалось что он щас кончит.'
    st2.say '[st1.fname]! Я сейчас кончу! Я хочу кончить тебе в сиськи!'
    '[st1.fname] лишь сжала их сильней и, улыбаясь, смотрела на него.'
    st1.say 'Давай, [st2.fname], кончи в мои большие сиськи!'
    'И вот он разрядился несколькими мощными выбросами и его сперма показался между ложбинок ее грудей,когда ее стало много она потекла вниз. Некоторые особо густые капли ненадолго задерживались на ее соске.'
    'Парень стоял над ней и смотрел на её сиськи покрытые его спермой. Ученица же принялась размазывать сперму по всей груди, как бы втирая её в кожу. Судя по его лицу он даже в самых своих смелых мечтах не мог представить подобного!'
    menu:
        'Оставить их':
            'Аккуратно развернувшись, вы ушли, оставив молодых развлекаться.'
            $ hadSex(st1,st2)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_15_2:
    show entrance
    python:
        st1 = getChar('male')
        player.incLust(5)
    'Проходя мимо входа, Вы услышали часть разговора за углом школы.'
    show expression 'pic/locations/school/entrance/lo2.png' at top as tempPic
    '[st1.fname] рассказывал своим друзьям, как он вчера "классно трахнул" свою младшую сестрёнку.'
    player.say '"Врёт наверняка, но зараза, как реалистично рассказывает!"'
    '"Текущая пиздёнка", "хлюпание", "стоны". У вас перед глазами промелькнула картина того, как это могло выглядеть. Весьма так возбуждающе!'
    'Вы решили не наказывать ученика, так как всё равно не поверили ему.'
    $ setLust(5,15)
    $ move(curloc)
    
label event_loc_entrance_30_3:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(10)
    'Услышав странные звуки за углом школы, вы выглянули посмотреть, что же там происходит?'
    show expression 'pic/locations/school/entrance/lo3a.png' at top as tempPic
    'К вашему удивлению, вы увидели как [st2.fname] стоит на коленях, засунув себе в рот член своего одноклассника!'
    st2.say 'Мффф, чафффф, мфффф, мы так не договаривались!'
    st1.say 'Ты же сама сказала, что сделаешь всё что угодно, если я дам тебе списать? Вот и отрабатывай!'
    'Парень вновь засунул свой член меж полных губ одноклассницы.'
    menu:
        'Смотреть дальше':
            show expression 'pic/locations/school/entrance/lo3b.png' at top as tempPic
            'Вы решили не вмешиваться. Дело то житейское, и с удовольствием продолжили наблюдать за любительским исполнением минета. Чавканье ненадолго прерывалось судорожным вздохом, и продолжалось снова.'
            'Наконец парень подался вперёд, выдохнул, и в уголках рта девушки показались белые капли. [st1.fname] не отпускал её, пока не закончил кончать.'
            st2.say 'Кхе, кхе!'
            'Девушка закашлялась, пытаясь продышаться.'
            st2.say 'Чтобы я ещё раз! Тьфу!'
            'Отплёвываясь и глубоко дыша, [st2.fname] вытерлась и стала подниматься. Вы решили исчезнуть, пока ученики случайно не застукали своего директора.'
            $ hadSex(st1,st2)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_30_4:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(10)
    st2.say 'Не останавливайся, только не останавливайся!'
    'Вы услышали тихий девичий голос неподалёку. Недоумённо оглянувшись, вы заметили какие то тени возле подсобки.'
    show expression 'pic/locations/school/entrance/lo4.png' at top as tempPic
    'Аккуратно приблизившись, вы увидели, как [st2.fname] буквально самоудовлетворяется рукой своего парня.'
    st1.say 'Тихо, нас могут услышать!'
    'Зашептал [st1.fname] на ушко девушке, поглядывая по сторонам. Благо вы неплохо замаскировались в кустах.'
    st2.say 'Ах, ах, даааа!!!'
    '[st2.fname] задрожала и обмякла в руках одноклассника.'
    st1.say 'Пошли, я не хочу чтобы [player.name] нас застукала!'
    '[st1.fname] одёрнул однокласснице юбку, и потащил девочку в школу.'
    $ move(curloc)
    
label event_loc_entrance_20_6:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(5)
    show expression 'pic/locations/school/entrance/lo6a.png' at top as tempPic
    'Вы видите, что двух учеников вдруг обуяла страсть на глазах у всех. [st1.fname] жадно целуется со своей подругой, и проходящие мимо ученики любопытно посматривают на них.'
    menu:
        'Смотреть дальше':
            show expression 'pic/locations/school/entrance/lo6b.png' at top as tempPic
            player.say 'Как мило наблюдать первые любовные порывы!'
            'Начинаете вы было свою речь, как вдруг замечаете, что рука парня вдруг оказывается между ног школьницы, и начинает там незамысловатые движения. Бёдра девушки начинают подаваться навстречу, и до вас долетает тихий стон, сорвавшийся с её губ. Похоже простыми поцелуями они не ограничатся.'
            menu:
                'Всё таки наказать их':
                    $ scoldWho = [st1,st2]
                    jump scoldAll
                'Заткнуться и смотреть' if getPar(studs, 'corr') > 40:
                    show expression 'pic/locations/school/entrance/lo6c.png' at top as tempPic
                    'Движения парня под юбкой всё ускорялись. Девушка уже не стесняясь во всю стонала. Ученики вокруг остановились как вкопанные и наблюдали за разворачивающимся перед ними действом.'
                    st2.say 'Мммм, Аааах, ААААаааААААааа!!!'
                    'Школьница задрожала, и в руку парня выплеснулась горячая влага женского оргазма.'
                    'Не обращая ни на кого внимания, [st1.fname] и [st2.fname] поцеловались ещё раз, и взявшись за руки отправились в школу.'
                    $ hadSex(st1,st2)
                    $ setLust(10, 20)
        'Всех наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_15_7:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(5)
    show expression 'pic/locations/school/entrance/lo7.png' at top as tempPic
    player.say '"Оппа. Какая попа! То есть, кхм, какого чёрта [st2.fname] показывает свои текущие прелести этому парню в окне?"'
    menu:
        'Не вмешиваться':
            player.say '"Хотя показывает и показывает. Чем бы дитя не тешилось!"'
            'Вот и [st1.fname] имеет весьма довольный, хотя и удивлённый вид. Хотя родителям это решение явно не будет по душе.'
            python:
                st2.incRep(-5)
                st2.incCorr(5)
                setLust(5,10)
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_13_8:
    show entrance
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        player.incLust(5)
    show expression 'pic/locations/school/entrance/lo8.png' at top as tempPic
    'Лёгкий ветерок приоткрыл прелести ученицы. Интересно, это повальная мода, или [st2.fname] одна такая? И стоит ли прилюдно наказать её, или фиг бы с ней?'
    menu:
        'Не вмешиваться':
            player.say '"В конце концов погода тёплая, ничего себе не простудит. Может стоит вообще задуматься об обязательности ношении трусов?"'
            python:
                st2.incCorr(2)
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_25_9:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        setLust(20,15)
        setCorr(20,1)
        player.incLust(5)
    show expression 'pic/locations/school/entrance/lo9.png' at top as tempPic
    'Хмм. Какая любопытная униформа! Настолько оригинальная, что кажется как будто [st1.fname], [st2.fname] и [st3.fname] попросту забыли до конца одеться.. Да и остальные в вашем поле зрения одеты точно так же. Новый флэшмоб? Какой то протест? Сейчас я Вам устрою протест!'
    menu:
        'Не обращать внимания':
            player.say '"А хотя если это такой способ самовыражения, то пусть."'
            'В конце концов именно за это Вы и ратуете на школьном совете. Надо только ещё раз проверить, не пишут ли родители гневных писем на Ваш адрес.'
            python:
                st1.incRep(-5)
                st2.incRep(-5)
                st3.incRep(-5)
        'Наказать':
            $ scoldWho = [st1,st2]
            jump scoldAll

    
label event_loc_entrance_15_11:
    show entrance
    python:
        st1 = getChar('female')
    menu:
        'Вы слышите шевеление в кустах.'
        'Проверить':
            show expression 'pic/locations/school/entrance/lo11.png' at top as tempPic
            'Увидев шевеление в кустах, вы застали там ученицу со спущенными трусиками. Похоже  [st1.fname] собиралась пописать, но Вы прервали её уединение. Мда, неудобно получилось.'
            $ st1.incLoy(-10)
        'Не проверять':
            player.say '"Я слишком тороплюсь, чтобы проверять каждый куст с кошкой по пути!"'
    $ move(curloc)
    
label event_loc_entrance_25_12:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
        st1.incLoy(-5)
        st1.incRep(5)
        addDetention(st1)
    show expression 'pic/locations/school/entrance/lo12.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    player.say '[st1.fname]! - окликнули вы девушку и дождались, пока она подойдёт своей странной походкой, - Я даже не спрашиваю, [st1.fname], куда подевались твои трусики, но что, прости меня пожалуйста, стекает по твоей ляжке, можешь объяснить?'
    'Ученица смотрит на вас, потом ниже на свои ноги, тихо ойкает, и краснеет.'
    player.say 'В общем иди подмойся, и ты сегодня наказана!'
    'Вы отсылаете ученицу и продолжаете наблюдать за учениками.'
    $ move(curloc)
    
label event_loc_entrance_10_13:
    show entrance
    python:
        st1 = getChar('female')
        if school.uniform != 'usual':
            skipEvent()
    show expression 'pic/locations/school/entrance/lo13.png' at top as tempPic
    'У школьного входа стоит [st1.fname]. Похоже, что ваш указ о свободной одежде она поняла немного по своему...'
    'В принципе, если подумать, то длину ее рубашки можно принять за мини юбку , вернее за микро юбку...'
    $ move(curloc)

label event_loc_entrance_10_14:
    show entrance
    python:
        st1 = getChar('male')
    show expression 'pic/locations/school/entrance/lo14.png' at top as tempPic
    '[st1.fname], буквально у вас на глазах, заглядывает под юбку задремавшей учительнице!'
    menu:
        'Не вмешиваться':
            player.say '"Младший школьничек, мальчик молодой, все хотят потанце..."'
            player.say '"Кхм, нет, в любом случае неважно, образование штука многогранная, никогда не знаешь, где убудет, а где прибудет."'
            python:
                st1.incCorr(2)
        'Наказать':
            $ scoldWho = [st1]
            jump scoldAll
    $ move(curloc)
    
label event_loc_entrance_40_1:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
        player.incLust(10)
    st1.say '[st2.fname], он не войдёт!'
    'Услышали вы из ближайших кустов, и сразу же решили полюбопытствовать, что же там не входит.'
    show expression 'pic/locations/school/entrance/mid1.png' at top as tempPic
    ' Аккуратно раздвинув ветви, Вы увидели, что [st1.fname] готовится принять член парня в место не совсем для этого подходящее.'
    st2.say 'Сейчас, чёрт, больно! - ругнулся парень, а девушка тихо ойкнула.'
    show expression getCharImage(player,'dialog') as temp1
    player.say 'А ты плюнь и смажь, - вышли вы из кустов перед обалдевшей парочкой.'
    st2.say 'Ой, мы тут это, - начал запинаться ученик.'
    player.say 'От запора лечитесь, я вижу, а ну марш на занятия! - крикнули вы на них, и с чистой совестью отправились дальше.'
    $ move(curloc)
    
label event_loc_entrance_55_1:
    show entrance
    python:
        st1 = getChar('female')
        st2 = mustangovich
        hadSex(st1,st2)
        player.incLust(10)
    show expression 'pic/locations/school/entrance/hi1.png' at top as tempPic
    'Заметив шебуршение у забора, Вы заглянули в кусты. Мда, а Ахмед то времени не теряет в школе... Вон и спортивную форму себе прикупил, и девочку соблазнил. Какой прекрасный вид на киску, как будто физрук специально для вас приоткрыл створки этой раковинки.'
    'Ну да ладно, все уже не маленькие, сами знают что и как делать. Вы выползаете их кустов, пока никто вас не заметил.'
    $ move(curloc)

label event_loc_entrance_50_2:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        player.coverSperm('лицо')
        hadSex(st1,st2)
    menu:
        'Вы слышите шевеление в кустах.'
        'Проверить':
            show expression 'pic/locations/school/entrance/hi2.png' at top as tempPic
            'Ваше любопытство вас погубит. Или нанесёт непоправимый вред репутации. Услышав стоны из кустов возле забора, вы знали что там увидите. Но не догадывались, что ваша голова высунется прямо под парочкой во время оргазма.'
            'В итоге на вашем лице оказалась большая часть эякулята вытекающего из киски. Хорошо что хоть [st1.fname] и [st2.fname] вас не засмеяли, а лишь улыбнулись, и пообещали найти место поукромней, чтобы больше вас не пачкать.'
        'Не проверять':
            player.say '"Я слишком тороплюсь, чтобы проверять каждый куст с кошкой по пути!"'
    $ move(curloc)
    
label event_loc_entrance_65_3:
    show entrance
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st3 = getChar('female')
        st4 = getChar('male')
        player.incLust(10)
        hadSex(st1,st2)
        hadSex(st3)
    show expression 'pic/locations/school/entrance/hi3.png' at top as tempPic
    '[st1.fname] и [st2.fname] без всякого стеснения занимаются сексом прямо на школьном крыльце. Ученица громко стонет в то время, как её одноклассник вгоняет в её узенькое влагалище свой крепкий член.'
    'Мимо проходящие [st3.fname] и [st4.fname] тоже не отличаются обилием целомудрия. Интересно, это вообще удобно ходить, когда пальцы парня в твоём влагалище? Вы чувствуете возбуждение от созерцания происходящего.'
    $ move(curloc)
    
label event_loc_entrance_70_4:
    show entrance
    python:
        st1 = getChar('female')
        setLust(10,-20)
        setFun(10,10)
    show expression 'pic/locations/school/entrance/hi4.png' at top as tempPic
    'Ученица сидит на лавочке у школьного входа, предлагая каждому обладателю мужского достоинства минет.'
    player.say '[st1.fname], с тобой всё в порядке? - участливо спрашиваете вы девушку.'
    st1.say 'Конечно, просто биологичка дала мне задание собрать побольше семенного образца, вот я и собираю, - сплюнув сперму изо рта в руки ответила девочка, - всё в порядке, идите.'
    player.say 'Понятненько... - задумчиво говорите вы и отправляетесь дальше по своим делам.'
    $ move(curloc)
    
label event_loc_entrance_70_5:
    show entrance
    python:
        st1 = getChar('futa')
        st2 = getChar('female')
        st3 = getChar('female')
        hadSex(st1,st2)
        setFun(5,10)
        setLust(10,10)
    show expression 'pic/locations/school/entrance/hi5.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    st2.say 'Ну же, давай же, дай мне своего молочка!'
    '[st2.fname] активно скакала на члене своей одноклассницы - футы, неподалёку от школьного входа.'
    st1.say 'М-м-м, я сейчас, м-м-м.'
    '[st1.fname] напрягала бёдра, двигаясь в такт движениям своей любовницы.'
    st2.say 'Ну же, ну! Докажи что ты не хуже моего парня! Я так люблю писькино молочко!'
    '[st2.fname] опустилась, полностью поглотив член своей щёлкой и начала круговые движения попкой.'
    'Вас немного удивило обилие зрителей, как будто не все верят, что мужской причиндал девушки способен выдать сперму.'
    show expression 'pic/locations/school/entrance/hi5a.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    st1.say 'Ммммм-олочко! - вдруг застонала [st1.fname] и резко задвигала попой в оргазме.'
    st2.say 'Да, да! Я чувствую!'
    '[st2.fname] вытащила член из себя, и успела заметить последний фонтанчик вырвавшийся из головки.'
    'Класс! Я всё засняла! - похвасталась [st3.fname], - Теперь твоему парню нечего будет противопоставить футе! Она такая же как и он, только лучше!'
    player.say '"Мда, они уже выбирают что лучше, девочка с мужским органом или парень..."'
    $ move(curloc)
    
label event_loc_entrance_60_6:
    show entrance
    python:
        st1 = getChar('female')
        st2 = mustangovich
        hadSex(st1,st2)
        setFun(5,10)
        setLust(5,10)
    show expression 'pic/locations/school/entrance/hi6.png' at top as tempPic
    st1.say 'Да, [st2.name], в меня!!!'
    '[st1.fname] визжит в крепких руках физрука, пока тот изливает свою сперму глубоко в её матку.'
    player.say '"Вот ведь кобель!", - с негодованием смотрите вы, как очередная девушка пала жертвой его мускулистого торса и красных трусов.'
    $ move(curloc)
    
######################################################################################################################################
#
######################################################################################################################################
label event_loc_street_0_no1:
    show street
    python:
        st1 = getChar('female')
        st1.incLoy(10)
        st1.incFun(-10)
    show expression 'pic/locations/street/no1.jpg' at top as tempPic
    '[st1.fname] поскользнулась на мокрой дорожке и упала. Бедная девочка. Вы помогаете ей подняться.'
    if player.getCorr() > 30:
        'Вам на секунду стало жаль, что трусики у девушки совсем не промокли.'
        show expression 'pic/locations/street/no1a.jpg' at top as tempPic
        player.say '"Ведь мокрые трусики, это так эротично! Особенно когда они мокрые не от дождя, а, скажем, от первых забав с продолговатыми предметами..."'
        $ player.incLust(5)
    $ move(curloc)
    
label event_loc_street_0_no2:
    show street
    python:
        st1 = getChar('female')
        st1.incFun(-5)
    show expression 'pic/locations/street/no2.jpg' at top as tempPic
    'Дождь уже вроде бы закончился, но [st1.fname] не справилась с зонтом, и его вырвало поднявшимся ветром.'
    if player.getCorr() > 50:
        show expression 'pic/locations/street/no2a.jpg' at top as tempPic
        player.say '"Жаль, что ветер не умеет вырывать всю скромность из девушек! Как бы было хорошо, если бы они приветствовали меня, раскрыв лепестки своего влажного бутончика!"'
        'Вы закатили глаза, смакуя подобную перспективу.'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_street_0_no3:
    show street
    python:
        setFun(4,10)
    show expression 'pic/locations/street/no3.jpg' at top as tempPic
    'Кого же они пародируют? Вы никак не можете припомнить из за жёлтой подлодки, зачем то всплывшей из глубин вашей памяти.'
    if player.getCorr() > 40:
        show expression 'pic/locations/street/no3a.jpg' at top as tempPic
        player.say '"А, ну конечно! - вы хлопнули себя по лбу, - "Анальная сага 8"! Помню в том фильме так же всё начиналось, 4 девчёнки, одни на улице, ну и потом поехало!"'
        'Вы с удовольствием смакуете один из моментов фильма в памяти.'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_street_0_no4:
    show street
    python:
        st1 = getChar('female')
    show expression 'pic/locations/street/no4.jpg' at top as tempPic
    '[st1.fname] продаёт печеньки на улице возле ресторана. Вы не думаете, что это особо прибыльный бизнес...'
    if st1.getCorr() > 20 or development == 1:
        show expression 'pic/locations/street/no4a.jpg' at top as tempPic
        $ st1.incCorr(5)
        'Неожиданно девушка замечает потенциального покупателя, и бесстыдно приподнимает перед ним юбку! Мгновенно заинтересовавшийся парень подходит, и тут же оказывается одарён замечательной улыбкой и пачкой не самых дешёвых печенек.'
        player.say '"Интересный маркетинговый ход конечно. Думаю, таким образом она сможет продать и запечёные какашки в шоколаде..."'
        $ player.incLust(5)
    $ move(curloc)
    
label event_loc_street_0_no5:
    show street
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st3 = getChar('male')
        setFun(3,10)
    show expression 'pic/locations/street/no5.jpg' at top as tempPic
    'Все куда то спешат, торопятся. Хотя вон [st1.fname] и [st3.fname] сидят у уличной кафешки и болтают о чём то, [st2.fname] катается на роликах.'
    if st1.getCorr() > 40 or development == 1:
        $ hadSex(st1,st3)
        'Вы замечаете странное поведение парня, и присматриваетесь к парочке за столиком в летнем кафе.'
        show expression 'pic/locations/street/no5a.png' at top as tempPic 
        player.say '"Нет, ну ты только посмотри на эту маленькую проказницу! И ведь фиг заметишь!"'
        'Однако, в отличие от окружающих, глаз у вас намётан. И вы с наслаждением наблюдаете, как [st1.fname] ласкает парня прямо сквозь штаны.'
        player.say '"Нет, ему оно приятно конечно, но вряд ли [st3.fname] сможет добиться полного удовлетворения, находясь в штанах."'
        show expression 'pic/locations/street/no5b.png' at top as tempPic 
        'Словно услышав ваши мысли, [st1.fname] аккуратно хватает резинку треников своими пальчиками и достаёт наружу пунцовый от прилившей крови член, и продолжает массировать узедчку своей ножкой.'
        'Парень вцепляется в стол обеими руками и до вас долетают слова, как он просит её прекратить над ним издеваться. Но слова какие то неуверенные. Вы бы его не послушались. Не послушалась и [st1.fname], продолжив ласкать истекающую влагой головку.'
        show expression 'pic/locations/street/no5c.png' at top as tempPic
        'Вы уже почти отчаялись дождаться кульминации разворачивающегося перед вами действа, как [st3.fname] всхлипнул, пытаясь сдержать стон, и в нижняя часть стола оказалась заляпанной спермой.'
        player.say '"Умеют они развлекаться! Мне надо идти, а то стою уже 10 минут как тополь на плющихе."'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_street_0_no6:
    show street
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        st3 = getChar('female')
        st4 = getChar('female')
        setFun(4,10)
        setLoy(4,5)
    show expression 'pic/locations/street/no6.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Ух ты! [st1.fname], [st2.fname], [st3.fname] и [st4.fname]! Девчёнки радостной гурьбой приветствуют вас.'
    $ move(curloc)
    
label event_loc_street_0_no7:
    show street
    python:
        st1 = getChar('female')
        st1.incLoy(10)
    show expression 'pic/locations/street/no7.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] гуляет со своей собачкой. Вы немного поболтали о домашних животных, и посетовали, что хозява квартиры вам не разрешают заводить своего любимца.' 
    menu:
        'Вы собираетесь прощаться'
        'Проследить за девушкой':
            if st1.getCorr() < 75:
                show street
                'Вы скрываетесь по кустам битый час, но так ничего крамольного и не замечаете. Просто девушка, просто выгуливает собачку.'
                $ changetime(60)
            else:
                show street
                'Вы некоторое время следуете за девушкой, пока наконец не оказываетесь на каком то пустыре неподалёку.'
                show expression 'pic/locations/street/no7a.jpg' at top as tempPic
                player.say '"Ох ничего себе!"'
                'Девушка медленно раздевается перед своей собачкой, которая уже не кажется вам такой маленькой, и становится в позу, понятную только ей и её лохматому другу. Не долго размышляя, пёс сразу принимается вылизывать бритую киску девчёнки, попутно скользя шершавым языком по её попке.'
                st1.say 'Да, Пушистик, вот тут! Сделай свою сучку влажной!'
                'И Пушистик сделал. То ли от обильных слюней, то ли по естественным причинам, но киска девушки обильно истекала жидкостью и поблёскивала на солнце.'
                st1.say 'А теперь войди в меня!'
                show expression 'pic/locations/street/no7b.jpg' at top as tempPic
                player.say '"Воу!"'
                'Девушка перевернулась на спину и приподняла попку настолько высоко, насколько могла. Хорошо выдрессированный пёс не стал дожидаться повторного приказа, и почти сразу ввёл свой собачий член в узкую киску школьницы.'
                st1.say 'О ДА!!!!'
                'Глаза девушки округлились от смеси боли и наслаждения, а киска немедленно исторгнула тонкую струйку мочи, смазывая и без того текущее влагалище.'
                st1.say 'ЕБИ МЕНЯ МОЙ ПЁС! ЕБИ!!!'
                player.say '"Нет, ну всё, я так больше не могу! На эти крики сейчас пол города сбежится!"'
                player.say '"Пёс изнасиловал ученицу, пока директорша смотрела и мастурбировала! Именно такие заголовки и будут в завтрашних газетах!"'
                player.say '"Стоп, я что?"'
                show expression 'pic/locations/street/no7c.jpg' at top as tempPic
                'Вы с удивлением опускаете голову вниз и понимаете, что некоторое время активно ласкаете свою текущую щёлку. Не сдержавшись, вы засовываете в неё два пальца и начинаете трахать себя ими, повторяя ритм пса рядом.'
                player.say 'Да, Пушистик, еби меня!'
                'Движения ваших пальцев всё ускоряются, и вот уже два крика тревожат окрестности. Ваш, и оргазмирующей под псом ученицы.'
                'Не желая, чтобы кто то связал вас с вакханалией происходящей рядом, вы быстро вытираете пальцы и покидаете пустырь.'
                $ changetime(30)
                $ hadSex(player)
                python:
                    for x in 10:
                        hadSex(st1)
        'Попрощаться':
            pass
    $ move(curloc)
    
label event_loc_street_5_no8:
    show street
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
    show expression 'pic/locations/street/no8.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] сидят рядом на одной лавочке и слушают один плеер. Но вы почему-то не совсем уверены, что они сидят именно вместе.'
    if player.getCorr() > 70:
        player.say '"Мде, не тот нынче ученик пошёл. Не тот. Вот помню в моё время, встал спозаранку, взял дочку фермера с подружкой, и хлоп на сеновал!"'
        show movie
        play movie 'pic/locations/street/no8a.gif.webm' loop
        'Вы с ностальгией вспоминаете то время, когда развлекались с подружкой на сеновале...'
        'Очень отчётливо вспоминаете и страстные стоны Алёнки, сидящей на лице Макса, и суровый взгляд отца из за двери амбара...'
        stop movie
        hide movie
    $ move(curloc)
    
label event_loc_street_0_no9:
    show street
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        setFun(2,10)
    show expression 'pic/locations/street/no9.jpg' at top as tempPic
    '[st1.fname] и [st2.fname] идут куда то вместе, обсуждая свои, девчачьи дела.' 
    if player.getCorr() > 50:
        menu:
            'Интересно, а трусики они сегодня одели?'
            'Потребовать поднять юбки':
                $ player.incCorr(2)
                if st1.getCorr() + st2.getCorr() < 70:
                    player.say 'Полиция нравов! Быстро поднять юбки и не двигаться!'
                    'Девчёнки делают круглые глаза и с визгом убегают от вас.'
                    show street as tempPic
                    player.say '"Это я, конечно, погорячилась!"'
                    'Вы с сожалением смотрите вслед убегающим девушкам и вашей репутации.'
                    $ st1.incLoy(-10)
                    $ st2.incLoy(-10)
                    $ st1.incRep(-10)
                    $ st2.incRep(-10)
                else:
                    player.say 'Полиция нравов! Быстро поднять юбки и не двигаться!'
                    show expression 'pic/locations/street/no9a.png' at top as tempPic
                    '"Могли бы и просто попросить киски показать!" - смеясь ответили девчёнки, приспуская трусы и задирая юбки.'
                    player.say 'Это не педагогично!'
                    'Вы как могли попытались сохранить суровый тон, но всё таки рассмеялись вместе с девушками.'
                    python:
                        player.incFun(10)
                        st1.incFun(10)
                        st2.incFun(10)
                        st1.incCorr(5)
                        st2.incCorr(5)
            'Не делать глупостей':
                pass
    $ move(curloc)
    
label event_loc_street_0_no10:
    show street
    python:
        st1 = getChar('female','brustmax')
    show expression 'pic/locations/street/no10.jpg' at top as tempPic
    '[st1.fname]! - окликнули вы ученицу, и та с готовностью повернулась. Вы немного поболтали о различных пустяках.'
    if player.getCorr() > 20:
        show expression 'pic/locations/street/no10a.png' at top as tempPic
        'Хотя пока вы общались с девушкой, вы всё представляли, почему её "пустяки" такие большие, и какой лифчик она носит, чтобы они так подчёркивались. На ум вам пришёл только один вариант.'
    $ move(curloc)

label event_loc_street_0_no11:
    show street
    python:
        st1 = getChar('female')
    show expression 'pic/locations/street/no11.jpg' at top as tempPic
    'Навстречу Вам попалась [st1.fname]. Милая девочка, как и вы, прогуливалась в этот чудный денек. Вы с улыбкой вежливо кивнули друг другу.'
    if st1.getCorr() > 40:
        $ hadSex(st1)
        $ incLoy(10)
        'Девушка внезапно опустила руки к паху, сжала коленки и с тихом стоном опустилась на лавочку.'
        show expression 'pic/locations/street/no11a.png' at top as tempPic
        'Вы, было, кинулись на помощь, но меж её раздвинутых в экстазе ног, увидели крохотный вибратор и насквозь промокшие от выделений трусики.'
        player.say 'Этим лучше заниматься дома, понятно?'
        st1.say 'Но когда все смотрят, это та-а-ак возбуждает!'
        '[st1.fname] c виноватым видом смотрит на вас.'
        player.say 'Это да, возбуждает... - вы мечтательно закатываете глаза, - Но мастурбировать всё таки лучше дома!'
        'Вы помогаете выключить жужжалку между ног, и прощаетесь.'
        $ player.incLust(5)
    $ move(curloc)
    
label event_loc_street_0_no12:
    show street
    python:
        st1 = bissektrisovna
    show expression 'pic/locations/street/no12.jpg' at top as tempPic
    'Вы увидели проходящую невдалеке свою подчиненную. [st1.name] не торопясь прогуливается по улице, слегка задумавшись.'
    menu:
        'Окликнуть ее':
            show expression 'pic/locations/street/no12a.jpg' at top as tempPic
            'Вы окликаете учительницу, она оборачивается и ее лицо расцветает легкой улыбкой. Она явно рада Вас видеть и Вы с полчаса болтаете о всяких пустяках.'
            $ changetime(30)
            $ st1.incLoy(10)
        'Понаблюдать за ней':
            show expression 'pic/locations/street/no12b.jpg' at top as tempPic
            'Решив понаблюдать за учительницей, вы устроились в ее кильваторе и прошли за ней до тех пор, пока [st1.fname] не свернула в магазин. '
            if player.getCorr() > 25:
                'Пока шли за ней, вы не смогли отвести взгляда от ее строгой обтягивающей юбки. Наблюдать за движениями упругих ягодиц учительницы было в высшей степени возбуждающим действием. Вы только надеятесь что и ваша попка также выглядит со стороны.'
                $ player.incLust(10)
    $ move(curloc)
    
label event_loc_street_0_no13:
    show street
    show expression 'pic/locations/street/no13.jpg' at top as tempPic
    'Навстречу Вам попалась женщина одетая в бикини. То ли эксбиционистка, толи просто забыла переодеться, в любом случае свист стоял на всю улицу... Не хотелось бы вам оказаться на её месте.'
    $ move(curloc)
    
    
label event_loc_street_15_lo1:
    show street
    python:
        st1 = getChar('female','brustmax')
        st1.incCorr(2)
        player.incLust(5)
    show expression 'pic/locations/street/lo1.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Мимо проехала поливальная машина, а кто то забыл отскочить, а так же надеть лифчик! Хотя с другой стороны [st1.fname] не особо рада видеть ваше улыбающееся лицо.'
    $ move(curloc)
    
label event_loc_street_5_lo2:
    show street
    python:
        st1 = getChar('female')
    show expression 'pic/locations/street/lo2.png':
        xalign 0.5 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    if st1.getCorr() < 20:
        'Лёгкий ветерок слегка поднял юбочку у девочки. [st1.fname] испуганно оглядывается, не заметил ли кто небольшого конфуза.'
        $ st1.incFun(-5)
    else:
        'Лёгкий ветерок слегка поднял юбочку у девочки. [st1.fname] ещё и повиляла попой случайным очевидцам и пошла дальше по своим делам.'
        $ st1.incCorr(2)
    $ move(curloc)
    
label event_loc_street_10_lo3:
    show street
    python:
        st1 = getChar('female')
        player.incLust(5)
        st1.incFun(10)
        st1.incCorr(2)
    show expression 'pic/locations/street/lo3.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] радостно спешит куда то! А юбочка радостно развивается на ветру, открывая всем прохожим вид на тоненькие, полосатые трусики и попку! Как хорошо, когда люди ведут себя естественно!'
    $ move(curloc)
    
label event_loc_street_10_lo4:
    show street
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        st1.incFun(10)
        st2.incLust(20)
    show expression 'pic/locations/street/lo4.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Проказник [st1.fname] решил напугать одноклассницу неожиданными щекотунчиками! Хотя [st2.fname] не выглядит особо испуганной.'
    'Скорее заинтригованной от того, чьи же пальцы сегодня трогают её грудь.'
    $ move(curloc)
    
label event_loc_street_5_lo5:
    show street
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        st1.incCorr(2)
        setFun(2,10)
    show expression 'pic/locations/street/lo5.jpg' at top as tempPic
    'Ой-ой! Похоже чья то попка попала в кадр! Вы не уверены, что [st2.name] особо рада этому событию, но [st1.fname] выглядит вполне довольным...'
    $ move(curloc)
    
label event_loc_street_0_lo6:
    show street
    python:
        st1 = getChar('female')
        st1.incFun(-10)
        st1.incLoy(10)
    show expression 'pic/locations/street/lo6.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Бедная [st1.fname] подскользнулась и упала в лужу. Вы, разумеется, кинулись ей помогать подняться. Успев краем глаза заметить пухлые губки киски, просвечивающие через насквозь промокшие трусики. Ученица благодарно улыбается вам, явно не заметив похотливого взгляда.'
    $ move(curloc)
    
label event_loc_street_0_lo7:
    show street
    python:
        if player.getCorr() < 40:
            skipEvent()
        player.incCorr(2)
        player.incLust(5)
        st1 = getChar('female')
        st1.incFun(-5)
    show expression 'pic/locations/street/lo7.jpg' at top as tempPic
    'Прогуливаясь по улице, вы заметили неподалёку свою ученицу. Аккуратно пристроившись сзади, как бы невзначай вы приподняли её юбочку своей сумочкой. Хех, фиолетовые! [st1.fname] было развернулась к нахалу покусившемуся на святое, но увидев своего директора, скорее всего подумала, что всё произошло случайно.'
    'Вы, мило улыбнувшись, обогнали её и пошли по своим делам, смакуя в голове сладкий вид попки обтянутой трусиками.'
    $ move(curloc)
    
label event_loc_street_0_lo8:
    show street
    python:
        st1 = getChar('female')
        player.incLust(5)
    show expression 'pic/locations/street/lo8.jpg' at top as tempPic
    'Банановая кожура, попытка удержаться на ногах, юбка задранная до спины... Да, [st1.fname] похоже не зря направлялась к окулисту. Диоптрий в очках явно маловато. А вот ягод в ягодицах вполне себе достаточно!'
    $ move(curloc)
    
label event_loc_street_0_lo9:
    show street
    python:
        st1 = getChar('female')
        st1.incCorr(5)
        player.incLust(5)
    show expression 'pic/locations/street/lo9.jpg' at top as tempPic
    'Мимо вас радостно промчалась [st1.fname] на велосипеде. Вы не смогли не обратить внимание на развевающуюся от скорости юбочку. Точнее на место немного пониже.'
    $ move(curloc)
    
label event_loc_street_35_lo10:
    show street
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        hadSex(st1,st2)
    st2.say '[st1.fname], что ты делаешь, нет, не надо!'
    show expression 'pic/locations/street/lo10.jpg' at top as tempPic
    'Вы услышали интересный разговор за углом, и поспешили полюбопытстовать, что же там происходит. На ваших глазах [st1.fname] вылизвала своей подружке прямо под юбкой. [st2.fname] вдруг дернулась и застонала.'
    st1.say 'Не дёргайся и не стони! - прошипела снизу девочка, - А то кто нибудь услышит!'
    player.say '"Ну, тут ты очевидно опоздала с предупреждением!"'
    st2.say 'Х-хорошо, - закусив губу ответила [st2.fname] и замолчала, отдаваясь ласкам одноклассницы.'
    player.say '"Упс, кто то идёт!"'
    'Вы громко закашлялись, спугнув парочку, и поспешили слинять следом.'
    $ move(curloc)

label event_loc_street_20_mid1:
    show street
    python:
        st1 = getChar('female')
        st1.incCorr(5)
        player.incLust(5)
    'Идя по улице, ваш взгляд зацепился за какое то мелькание между заборами. Не справившись с любопытсвом, вы прильнули к ближайшей дырке, чтобы получше рассмотреть то, что происходит во дворе частного дома.'
    show expression 'pic/locations/street/mid1.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Судя по всему, вам посчастливилось проходить мимо дома своей ученицы. [st1.fname] занималась поливкой газона, и случайно обрызгала себя из шланга.'
    'Совершенно не смущаясь, она сняла почти всю мокрую одежду, и только дойдя до трусиков заметила, что за ней кто то подглядывает. Хорошо, что забор почти сплошной, и опознать вас не удастся. Вы поспешно отстранились от дырки и продолжили свой путь.'
    $ move(curloc)
    
label event_loc_street_40_mid2:
    show street
    python:
        st1 = getChar('female')
        hadSex(st1)
        player.incLust(10)
    show expression 'pic/locations/street/mid2.jpg' at top as tempPic
    'Заглянув в ближайшую кафешку, вы обнаружили, что там сидит [st1.fname] и разговаривает с кем то по телефону. Вы уже хотели зказать себе чашечку кофе, как вдруг заметили странные движения рукой не занятой телефоном.'
    player.say '"Хех, похоже что парень девочки заставил её заниматься чем то не совсем приличным в общественном месте!"'
    '[st1.fname] заметила ваше внимание, но продолжает дразнить свою киску пальчиками.'
    show expression 'pic/locations/street/mid2a.jpg' at top as tempPic
    'Вы заказали себе кофейку, и, вливая в себя его обжигающую бодрость, с удовольствием наблюдали за маленькой развратницей. [st1.fname] уже почти потеряла контроль над собой, и интенсивно двигала бёдрами своей ручке. Но стоны пока сдерживала.'
    player.say '"Интересно, надолго ли её хватит, в таком то темпе?"'
    'Вы чуть не поперхнулись, когда увидели как школьница резко застонала, привлекая к себе ненужное внимание, и из её киски полились влажные соки, шумно капая на пол.'
    menu:
        'Смотаться по быстрому':
            'Не желая присутствовать на разборе полётов, вы смотались, кинув деньги на стол.'
            $ st1.incRep(-10)
        'Начать выгораживать девушку (Интеллект)':
            if player.getIntel() < 70:
                player.say 'Да, дрочила! Ну и что же с того?'
                'Вы принялись расталкивать собирающуюся вокруг девушки толпу.'
                player.say 'А кто вот из вас никогда не дрочил? Кто? Пусть этот святоша кинет в меня камень!'
                'Вокруг поднимается гул людей, возмущённых вашим поведением. В конце концов, вас, вместе с девушкой выталкивают из заведения.'
                player.say '"Мда, хотели как лучше, а получилось как всегда!"'
                $ setRep(5,-15)
            else:
                player.say 'Расступитесь! Девушке плохо! У неё воды отходят! Ты, скорее, принеси воды. Вот вы, мужчина, да, вызывайте скорую! Женщина, не стойте столбом, вскипятите полотенца! Я пока выведу роженницу на свежий воздух!'
                'Не давая никому опомниться, вы быстрыми приказами заняли всех очевидцев какими то делами, и незаметно вывели девушку наружу.'
                hide tempPic
                show expression getCharImage(player,'dialog') as temp1
                show expression getCharImage(st1,'dialog') as temp2
                player.say 'Я тебя УХ!'
                'Вы грозите кулаком девушке, но она всё равно смотрит на вас с благодарностью за то, что вы спасли её от возмущённых горожан.'
                $ st1.incLoy(20)
    $ move(curloc)
        
label event_loc_street_25_mid3:
    show street
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        st1.incCorr(5)
        player.incLust(5)
    show expression 'pic/locations/street/mid3.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Решив срезать путь, вы пошли по дворам, где и наткнулись на двух учеников. Интересно, как [st2.fname] умудрился уговорить одноклассницу на столь развратные действия? Судя по тому как он потеет, вид открытых киски и попки вызывает у него весьма однозначную реакцию.'
    'К сожалению вы слишком шумели в кустах, пытаясь устроиться поудобней, и вспугнули парочку.'
    $ move(curloc)
    
label event_loc_street_35_mid4:
    show street
    python:
        st1 = getChar('female')
        hadSex(st1)
        player.incLust(10)
    'Проходя по парку, ваше внимание привлек тихий стон из за дерева.'
    show expression 'pic/locations/street/mid4.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    'Подойдя поближе, вы заметили там одну из своих учениц. [st1.fname] сидела возле дерева в разорванных колготках, и с остервенением теребила свой клитор, засовывая и вытаскивая пальчик из ануса.'
    st1.say 'Давай же, как же это у всех получается, а у меня нет?'
    'Не успели вы задуматься над их смыслом, как девчушку зарясло, и тугая струя ударила в ближайшие кусты. Случайно проходившая мимо девушка тоже заметила необычное поведение, и аж выронила сумки с покупками, когда разглядела, что именно происходит неподалёку. Вы поспешили уйти.'
    $ move(curloc)
    
label event_loc_street_5_mid5:
    show street
    python:
        st1 = getChar()
        st1.incRep(25)
    'Ваше внимание привлёк странный стон и собачье рычание из за ближайшего забора.'
    show expression 'pic/locations/street/mid5.jpg' at top as tempPic
    'Отбросив сомнения, ведь кому то наверное нужна помощь, вы смело заглянули между досок. На лужайке перед домом лежала стонущая женщина. Судя по её лицу, стонала она не от боли, а от удовольствия сцепки со своим кобелём. Вы хотели бы сказать, что кобель - это такое название мужчины, но не в этот раз. Кобель был самого что ни на есть собачьего рода.'
    'Вы смутно припомнили, что видели эту женщину возле школы. Она встречала одного из ваших учащихся. Да, точно! [st1.name]!'
    if st1.getSex() != 'male':
        'Это её мама валяется на лужайке без трусов с застрявшим во влагалище членом пса. Ну чтож, после увиденного, вам будет чем повлиять на неё.'
    else:
        'Это его мама валяется на лужайке без трусов с застрявшим во влагалище членом пса. Ну чтож, после увиденного, вам будет чем повлиять на неё.'
    $ move(curloc)
    
label event_loc_street_55_hi1:
    show street
    python:
        st1 = getChar('female')
        st1.incCorr(10)
        player.incLust(20)
    show expression getCharImage(player,'dialog') as temp1
    show expression getCharImage(st1,'dialog') as temp2
    st1.say '[player.name]! - кричит ученица, видя что вы её заметили.'
    player.say '[st1.fname], с тобой всё в порядке? - спрашиваете вы, видя нетвёрдую походку девочки.'
    hide temp1
    hide temp2
    show expression 'pic/locations/street/hi1.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    st1.say 'Вам нравятся мои новые игрушки?'
    'Девушка задирает юбочку, и вы видите, как тело ученицы сотрясается от удовольствия. В киске и попе торчат нехилых размеров вибраторы, а её клитор массирует маленькое яичко, прилемленное скотчем прямо к лобку. Проходящие мимо люди потеряли дар речи, глядя на это выступление.'
    st1.say 'Мне... Очень... Хорошо... - подрагивает, глотая слова, [st1.fname], - Я хочу... так... ходить в школу!'
    if player.getIntel() < 80:
        player.say 'Не думаю, что это самая лучшая идея, [st1.fname], - пытаетесь вы оправдаться в глазах прохожих, - И приведи своих родителей в школу, да!'
        'С этими словами вы разворачиваетесь, и быстро уходите, чувствуя, что несмотря на неловкую ситуацию, и чудовищную потерю вашей репутации, ваша киска жутко намокла.'
        $ setRep(5,-15)
    else:
        player.say 'Конечно, дорогая! Но мне кажется, что твои кардио стимуляторы не достаточно эффективно работают с сердцем, находясь вот там. Позволь мне, пожалуйста!'
        'Всем своим видом, вы показываете окружающим, что произошла просто ошибка из за неопытности девушки. Умелыми движениями, вы одной рукой вытаскиваете выбраторы из влагалища девушки, и запихиваете их ей под рубашку, якобы это просто медицинские приборы.'
        'Ваш спокойный голос и уверенные слова убеждают горожан, что им наверное всё привиделось, и ничего страшного действительно не произошло. Но внутри вы чувствуете сильное напряжение, то ли от страха, то ли от возбуждения.'
    $ move(curloc)
    
label event_loc_street_75_hi2:
    show street
    python:
        st1 = getChar('female')
        st1.incCorr(10)
        player.incLust(10)
    show expression 'pic/locations/street/hi2.jpg':
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    player.say 'Мать моя женщина, - тихо прошептали вы, видя как [st1.fname] собирается отдаться какому то мужику у всех на глазах.'
    'Где ты говоришь тебя научили так себя вести? - лениво ковыряясь в маленькой киске спросил мужик.'
    st1.say 'Ммм, в школе.. - млея от прикосновений прошептала девушка.'
    'И много у Вас в школе таких развратниц, как ты? - не отставал толстяк.'
    st1.say 'Да почти все... - девушку вдруг затрясло, и из её киски вырвался малекий фонтанчик.'
    'Как мило, мы уже кончили! - улыбнулся извращенец, но не остановил своих домогательств.'
    st1.say 'Я всё, отпустите меня! - девушка похоже начала осозновать, что натворила.'
    player.say 'А ну отстань от неё! - быстро подошли вы к парочке.'
    'Ну член у меня уже стоит, и сам по себе не ляжет, - задумчиво произнёс мужик, - Хочешь занять её место?'
    player.say 'Да я директор её школы! Я счас полицию вызову! - яростно прошипели вы извращенцу.'
    'Ах ты директор? Ну тогда я про её школу молчать не стану на допросе! - нахально ухмыльнулся он, - Ну так что, директор, займёшь место своей ученицы?'
    menu:
        'Угрожать (Интеллект)' if player.getIntel() > 60:
            player.say 'Ну давай прикинем расклад. Ты, совращающий учениц, будешь обвинять меня в том, что она, - вы кивнули на ученицу, - Не смогла устоять перед тобой.'
            player.say 'В свою очередь я обвиню тебя в том, что изнасиловал девушку и домогался до меня. Учитывая, что из нас твоих штаны спущены именно у тебя, как ты думаешь, чьи доводы весомей?'
            'Э-э-э-э, а давайте не будем усугублять! Я счас тихо соберусь, а вы про всё забудете!'
            player.say '10 тысяч.'
            'Извинений? Я приношу десять тысяч извинений! Извиняюсь, извиняюсь, извиняюсь, извиняюсь, извиняюсь, извиняю...'
            player.say '10 тысяч монет, и я забуду про тебя.'
            'У меня только около 6 000...'
            player.say 'Сойдёт!'
            'Вы уже даже собрались пожать мужику руку, но вовремя вспомнили, что ситуация немного не располагает к рукопожатиям, к тому же руки у извращенца всё ещё перемазаны в выделениях девушки. Так или иначе, девушка с благодарностью смотрит на вас.'
            $ player.money += 5847
            $ st1.incLoy(15)
        'Согласиться занять место ученицы' if player.getLust() > 50:
            player.say 'Чёрт с тобой, давай! - сказали вы, быстро скидывая с себя одежду, - только по быстрому!'
            'Ого какие формы! - ухмыльнулся извращенец, - Да я счас без прелюдии кончу от тебя, детка!'
            show expression 'pic/locations/street/hi2a.jpg' at top as tempPic
            'С этими словами, он действительно без прелюдий вошёл в вашу влажную от возбуждения киску. Вы застонали, ощутив заполнивший Вас объём, из вашего влагалища брызнули соки в ответ на мощный толчок внутрь.'
            player.say 'Д-а-а-а, ещё!'
            'Кричали вы и вовсю отдавались случайному мужику прямо на глазах у публики. Вы громко стонали от каждого толчка достигающего вашей матки и на крики из кустов собралось порядочное количество зрителей.'
            'Кончаю! - вдруг простонал мужик, и вашу киску начала наполнять горячая жидкость.'
            player.say 'Нет, Нет! - замолотили Вы ручками по его спине, - Мне ещё чуть чуть, гад!'
            'Да пошла ты в задницу, шлюха, - довольно ответил мужик одеваясь и скрываясь с глаз долой.'
            'Вы стремительно последовали его примеру, ощущая, что до спонтанного оргазма остался один шаг.'
            player.say '"Уж лучше бы я отказалась!" - думали вы, убегая от охеревшей от увиденного толпы.'
            $ st1.incLoy(20)
            $ setFun(25,20)
            $ setRep(25,-10)
        'Оставить их и уйти':
            player.say 'Да пошёл ты нахер! Если с ней что нить случится, я тебя лично прибью!'
            'Вас мутило от мысли о том, что он без смазки будет лезть в ваше влагалище. За спиной у вас снова начали раздаваться стоны и возмущённые крики прохожих.'
            $ st1.incLoy(-20)
            $ setRep(15,-10)
    $ move(curloc)
    
label event_loc_street_75_hi3:
    show street
    python:
        st1 = getChar('female')
        st1.incCorr(10)
        player.incLust(10)
        setFun(25,20)
    show expression 'pic/locations/street/hi3.jpg' at top as tempPic
    st1.say 'Четыыыыыреееее! - протяжный крик привлекает ваше внимание, и вы видите ученицу, которая сидит на огромном члене незнакомца, трахаясь буквально на глазах у всей улицы.'
    'Один, - шумно выдыхает незнакомец, и из сильно растянутой киски девушки начинает вытекать густая сперма.'
    st1.say 'Ах, ах, а в школе только два получается, ах, - вздыхает ученица.'
    menu:
        'Уйти':
            player.say '"М-м-мать! Опять!" - мелькает у вас в голове и вы быстро сматываетесь с места разврата одной из ваших подопечных.'
            $ setRep(15,-10)
        'Спасти положение' if player.getIntel() > 70:
            player.say 'О, Михаил Развратович! Вот вы где! Я надеюсь вы уже закончили своё исследование реакции общественности на аморальные действия?'
            'Э-э-э, - протягивает ничего не понимающий мужик.'
            player.say 'Позвольте забрать нашу анатомическую куклу с динамиком, она нужна Владимиру Потрахунько, который проводит анатомический курс для чайников в Беридеритрахском Институте.'
            'Пока никто не успел опомнится и полностью осознать, что вы наплели, вы стягиваете обессилившую ученицу с увядающего члена, кладёте на плечо и удаляетесь в ближайшую подворотню, где приводите девушку в чувство.'
            hide tempPic
            show expression getCharImage(player,'dialog') as temp1
            show expression getCharImage(st1,'dialog') as temp2
            player.say 'Прошу тебя, ну не на людях! Меня же уволят!'
            st1.say 'Ага!'
            'Ученица довольно кивает вам, но искорки в её глазах намекают, что врёт!'
            $ st1.incLoy(20)
    $ move(curloc)
    
label event_loc_street_55_hi4:
    show street
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        hadSex(st1,st2)
        player.incLust(15)
    show expression 'pic/locations/street/hi4.jpg' at top as tempPic
    player.say '"И ведь не стесняются никого!"'
    'C небольшим негодованием, вы разглядываете как [st1.fname] принимает в себя полный заряд спермы от своего одноклассника. Благо дело происходит в кустах, и похоже кроме вас, никто по колючим кустам шариться не любит.'
    $ move(curloc)
    
######################################################################################################################################
#
######################################################################################################################################

label event_loc_shopStreet_0_RedirectToStreet:
    $ tryEvent('loc_street')
    
######################################################################################################################################
#
######################################################################################################################################

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
    show expression 'pic/locations/beach/hi1.jpg':
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
    
######################################################################################################################################
#
######################################################################################################################################

