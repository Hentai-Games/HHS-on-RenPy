init python:
    def textgen(char):
        description = ''

        name = char.fullName()
        age = char.age
        sex = char.body.sex()
        beauty = char.getBeauty()
        loyalty = char.getLoy()
        edu = char.getEdu()
        lust = char.getLust()
        corr = char.getCorr()
        fun = char.getFun()
        health = char.getHealth()
        inClass = char.inClass
        
        asize = char.body.parts['анус'].size
        
        if sex == 'male':
            psize = char.body.parts['пенис'].size
        elif sex == 'female':
            vsize = char.body.parts['вагина'].size
        else:
            psize = char.body.parts['пенис'].size
            vsize = char.body.parts['вагина'].size

# Студенты и учителя
        if char != player:
            description += 'Перед вами ' + char.fullName() + '\n'
            description += 'Это '

            if char.body.height < 150: description += 'маленького роста '
            elif char.body.height < 175: description += 'среднего роста '
            else:
                if sex == 'male':
                    description += 'высокий '
                else :
                    description += 'высокая '

            if age > 20:
                if sex == 'male':
                    description += 'мужчина'
                elif sex == 'female' or (loyalty < 50 and sex == 'futa'):
                    description += 'женщина'
                else:
                    description += 'футанари'
            else:
                if sex == 'male':
                    description += 'мальчик'
                elif sex == 'female' or (loyalty < 50 and sex == 'futa'):
                    description += 'девочка'
                else:
                    description += 'футанари'

            description += ' '+ str(age) + ' лет. '
            
            if inClass > 0:
                if sex == 'male':
                    description += 'Он '
                else:
                    description += 'Она '
            
                description += 'учится в %d классе. ' % inClass
            
            bsize = char.body.parts['грудь'].size
            if bsize > 0:
                if bsize < 1: description += 'У неё почти нет грудей, что не удивительно для такой молодой девочки. '
                elif bsize < 2: description += 'У неё маленькие, симпатичные титечки. '
                elif bsize < 3: description += 'У неё небольшие, аккуратные груди. '
                elif bsize < 4: description += 'У неё неплохие груди третьего размера. '
                elif bsize < 5: description += 'У неё полные, налитые титьки. '
                elif bsize < 6: description += 'У неё большие, сочные сиськи. '
                elif bsize < 7: description += 'У неё действительно большие сиськи, каждая размером с дыню. Их выпирающие округлости слегка торчат даже со спины. '
                elif bsize < 8: description += 'У неё внушительных размеров большие сиськи, мясистые и налитые, словно перезревшие дыни. Их выпирающие округлости видны даже со спины. '
                elif bsize < 9: description += 'У неё огромные буфера, кажется будто каждая размером с голову девушки. Эти шары видны даже со спины. '
                else : description += 'У неё массивные огромные сисяндры, каждая размером с голову девушки, такие бывают только у порнозвёзд. Эти выпирающие шары видны с любого ракурса. '

            description += '\n'
            if age < 20:
                if sex == 'male':
                    description += 'Он '
                    if edu < 20: description += 'необразован донельзя. Как будто живёт на улице...'
                    elif edu < 50: description += 'посредственно учиться, и его знания оставляют желать лучшего.'
                    elif edu < 80: description += 'имеет хорошее представление о всех науках, преподаваемых в школе.'
                    else : description += 'отличник, спортсмен, будь женского пола был бы ещё и комсомолкой!'
                else :
                    description += 'Она '
                    if edu < 20: description += 'необразованна донельзя. Как будто живёт на улице...'
                    elif edu < 50: description += 'посредственно учиться, и её знания оставляют желать лучшего.'
                    elif edu < 80: description += 'имеет хорошее представление о всех науках, преподаваемых в школе.'
                    else : description += 'отличница, спортсменка, лет 40 назад была бы ещё и комсомолкой!'
            else :
                if sex != 'male':
                    description += 'Она '
                else :
                    description += 'Он '
                if edu < 20: description += 'имеет слабое образование. Настолько слабое, что вы удивлены, что этот человек работает учителем'
                elif edu < 50: description += 'имеет неплохое образование, но всё же её знания оставляют желать лучшего'
                elif edu < 80: description += 'имеет хорошее представление о своём предмете преподавания'
                else : description += 'имеет прекрасные знания не только о своём предмете, но и в смежных науках'

            description += '\n'
            description += char.fname + ' '
            if loyalty < 20: description += 'совсем не знает вас.'
            elif loyalty < 50: description += 'не против иногда перекинуться с вами парой словечек.'
            elif loyalty < 80: description += 'весьма хорошего о вас мнения.'
            else : description += 'просто обожает вас.'

            if loyalty >= 50 and sex == 'futa': description += ' Девочка недавно призналась, что она не совсем девочка и прячет член под юбкой.'

            description += '\n'

            if sex == 'female':
                if lust < 20: description += ''
                elif lust < 50: description += 'Вы замечаете у неё немного покрасневшие щёчки. '
                elif lust < 80: description += 'Вы замечаете, что она сильно краснеет, когда встречается с вами взглядом. '
                else : description += 'Вы замечаете, что она сильно краснеет, когда встречается с вами взглядом. '
            else :
                if lust < 20: description += ''
                elif lust < 50: description += 'Вы замечаете у него немного покрасневшие щёки. '
                elif lust < 80: description += 'Вы замечаете, что он сильно краснеет, когда встречается с вами взглядом. '
                else : description += 'Вы замечаете, что ученик переминается с ноги на ногу, и вы замечаете видимый бугорок на его штанах. '

            if corr < 20: description += 'По слухам, ' + char.fname + ' не знает о сексе ничего.'
            elif corr < 50: description += 'По слухам, ' + char.fname + ' мастурбирует и подглядывает за парочками.'
            elif corr < 80: description += 'По слухам, ' + char.fname + ' знает как, и любит заниматься сексом.'
            else : description += 'По слухам, ' + char.fname + ' любит любой секс во всех его проявлениях и извращениях.'

            description += '\n'

            if sex == 'male':
                description += 'Сегодня он '
            else :
                description += 'Сегодня она '

            if fun < 20: description += 'выглядит расстроенно.'
            elif fun < 50: description += 'выглядит довольно весело.'
            elif fun < 80: description += 'радуется погоде и новому дню.'
            else : description += 'веселится, заражая всех своей энергией.'

            description += '\n'

            rep = char.stats.reputation

            if age < 20:
                if sex  == 'male':
                    description += 'Не секрет, что его '
                else :
                    description += 'Не секрет, что её '
                if rep < 20: description += 'родители просто в ярости от вас.'
                elif rep < 50: description += 'родители не очень высокого о вас мнения.'
                elif rep < 80: description += 'родители ставят вас в пример своим детям.'
                else : description += 'родители в восторге от вас.'

            if sex != 'female' and corr > 50:
                description += '\n[name] прозрачно намекает вам, что под одеждой от вас скрывается '+ str(psize) +' сантиметровый змий!'
            
            if sex != 'male':
                description += '\nНа ней сегодня '
            else:
                description += '\nНа нём сегодня '
                
            if len(char.wear) == 0:
                description += 'ничего нет.'
            else:
                counter = 0
                for x in char.wear:
                    counter += 1
                    description += x.name.lower()
                    if counter < len(char.wear):
                        description += ', '
                    else:
                        description += '.'
            description += '\n'
            
            if name in complains:
                description += 'Родители этого ученика жаловались на вас.'
                description += '\n'

#########################################
# Игрок
#########################################

        else:
            description += 'Меня зовут ' + name + ', мне '+ str(age) +' лет.\n'
            if beauty < 20:
                description += 'Я очень плохо выгляжу. Совершенно не по годам. И это было преувеличение. Я отвратительно выгляжу! До сих пор удивляюсь как люди ещё неначали забрасывать камнями это чудовище.\n'
            elif beauty < 50:
                description += 'Я выгляжу обычно. Не хорошо, но и не плохо. Просто серенькая мышка, на которую мало кто обращает внимания.\n'
            elif beauty < 80:
                description += 'Я отлично выгляжу! Прохожие часто оборачиваются на меня. Это весьма приятно, быть настолько красивой и обаятельной.\n'
            else:
                description += 'Я - королева красоты. Женщины люто завидуют, а мужчины начинают кончать радугой, когда я начинаю с ними разговор. \n'
                
            if corr < 20:
                description += 'Так же я весьма скромна. Мне неприятны любые извращения, хотя обычный секс мне не чужд. '
            elif corr < 50:
                description += 'Так же я  обычная женщина. Иногда люблю "пошалить", но в целом всё как у всех. '
            elif corr < 80:
                description += 'Так же я  довольно развратна. Мне нравятся секс игрушки, я люблю анальный секс, у меня постоянно похабные мысли. И это меня возбуждает! '
            else :
                description += 'Кстати разврат - моё второе имя. '+ char.fname +' Развратная! Мне нравятся все виды сексуальных девиаций. Моя киска настолько несносная, что даже вид фонарного столба заставляет её течь! '
                
            if lust < 20:
                description += 'Сейчас я не испытываю никакого возбуждения.'
            elif lust < 50:
                description += 'Я чувствую небольшое томление внизу живота, но оно не причиняет мне неудобств.\n'
            elif lust < 80 :
                description += 'Моя киска немного влажная, и когда я задумываюсь, руки сами начинают поглаживать её.\n'
            elif lust < 90:
                description += 'Моя киска непрерывно течёт. Приятные волны жара распространяются от неё по всему телу.\n'
            else:
                description += 'Мне надо как минимум подрочить. Желательно дилдо. Желательно огромным. Желательно СЕЙЧАС.\n'
                
            if edu < 20:
                description += 'Мне следует всерьёз озаботиться своим образованием. На текущем уровне я смогу помогать с уроками разве что дошкольникам. В интернате для умственно отсталых. \n'
            elif edu < 50:
                description += 'У меня обычное образование. Но всё же, если я хочу чему либо обучить школьников, а тем паче помогать проводить уроки, мне надо его подтянуть. \n'
            elif edu < 80:
                description +=  'Я хорошо образована. По крайней мере могу отличить Перельмана от пилигрима. \n'
            else:
                description += 'Я - Нобелевский лауреат! Эх, мечты, мечты. Но, в любом случае, моего образования достаточно на любую школьную деятельность. \n'
                
            if health < 800:
                description += '"Я сегодня хочу, обратиться к врачу, я несу ему кал и мочу." Серьёзно, пора задуматься о своём здоровье.\n'
            elif health < 1100:
                description +=  'Я нормально себя чувствую. Но хотелось бы и получше.\n'
            elif health < 1500:
                description += 'Я в хорошей форме. Действительно хорошей.\n'
            else:
                description += 'Я в отличной форме! Могу выложиться на все 100 и работать пару дней без отдыха!\n'
                
            if vsize < 7:
                description += 'У меня практически девственная вагина. Это так мило, такая взрослая женщина и обладает такой красотой! '
            elif vsize < 14:
                description += 'У меня маленькая, аккуратная дырочка между ног. Вполне такого нормального вида. '
            elif vsize < 25:
                description += 'У меня нормальное, женственное влагалище. Влагалище нормальной такой женщины, которая родила пару детей. '
            else:
                description +=  'У меня раздолбанная дыра между ног. Я могу спрятать там бейсбольный мяч, биту и всю бейсбольную команду. Но не буду. Хотя идея заманчивая... '
                
            if asize < 7:
                description += 'Ещё у меня практически девственный анус. Работает только на выход!'
            elif asize < 14:
                description += 'Ещё у меня маленькая, аккуратная дырочка сзади. Видно эта дырочка может не только из себя выпускать что то, но и наобарот!'
            elif asize < 25:
                description += 'Ещё у меня довольно растянутый анус. Ну как довольно, так как будто я пыталась промышлять контрабандой водки, пронося её в известном месте.'
            else:
                description +=  'Ещё у меня раздолбанная дыра вместо задницы. Туда можно спрятать бутылку шампанского. Или две... Эй, гарсон, подайте вон тот ящик Кристалла!'
                
            description += '\nНа мне сейчас '
                
            if len(char.wear) == 0:
                description += 'ничего нет.'
            else:
                counter = 0
                for x in char.wear:
                    counter += 1
                    description += x.name.lower()
                    if counter < len(char.wear):
                        description += ', '
                    else:
                        description += '.'
                        
            description += '\n'
            if him_zavivka > 0:
                description += 'Дней до разрушения причёски: '+str(him_zavivka)
                description += '\n'
            if depilation > 0:
                description += 'Дней до того, как станут заметны отросшие волоски: '+str(depilation)
                description += '\n'
            if skin_care > 0:
                description += 'Дней до того, как кожа придёт в прежнее состояние: '+str(skin_care)
                description += '\n'
            if manicure > 0:
                description += 'Дней до того, как отрастут ногти и маникюр испортится: '+str(manicure)
                description += '\n'
            if pedicure > 0:
                description += 'Дней до того, как педикюр испортится: '+str(pedicure)
                description += '\n'
            description += '\n'
            temp = school.myIncome(player)
            description += 'Я отработала '+ getDays(school.daysWorked) +' на этой неделе. На данный момент мой заработок составит '+ str(temp) +' монет.'
            if complains != '':
                description += '\n'
                description += '\n'
                description += 'Родители следующих учеников жаловались на меня: ' + complains
        return description

    def reactionGen(char):
        global hour
        reaction = []
        name = char.name
        fname = char.fname
        lname = char.lname
        temp = 'он'
        if char.getSex() != 'male': temp = 'она'
        
        if char in detentions and hour >= 15: # если наказан
            if school.detention == 'education':
                reaction.append(lname + ' сидит за партой и занимается на дополнительных занятиях. Не сильно похоже, чтобы он был в восторге от этого.')

            elif school.detention == 'upskirt' and char.getSex() != 'male':
                reaction.append(name + ' стоит наклонившись за партой, позволяя любому посмотреть, что у неё под юбкой. ')
                if char.getLust() > 50:
                    reaction.append('Вы видите, что ей это похоже нравится. По крайней мере на трусиках отчётливо проступает влажное пятнышко.')
                    
            elif school.detention == 'cleaning':
                reaction.append(lname + ' стоит и медленно теребит тряпкой пол. Именно теребит, так как мытьём это можно назвать лишь с большой натяжкой. Ну чтож, на то оно и наказание.')
                
            elif school.detention == 'streetCleaning':
                if char.getSex() == 'male':
                    reaction.append(name + ' нехотя подметает улицы. По опущенному взгляду можно точно определить что он думает о вас, о ваших нововведениях и школе, которая заставляет его выполнять столь грязную работу. Но деньги не пахнут, не так ли?')
                else:
                    reaction.append(name + ' нехотя подметает улицы. По опущенному взгляду можно точно определить что она думает о вас, о ваших нововведениях и школе, которая заставляет её выполнять столь грязную работу. Но деньги не пахнут, не так ли?')
            else:
            
                if char.getSex() == 'male':
                    reaction.append('В обычной школе '+name+' уже драил бы полы или зубрил логарифмическую линейку, но вы решили никак не наказывать нерадивых учеников.')
                else:
                    reaction.append('В обычной школе '+name+' уже драила бы полы или зубрила логарифмическую линейку, но вы решили никак не наказывать нерадивых учеников.')
                
        if player.isSperm() == 2: # Если видна сперма
            if char.getCorr() < 25 or char.getWill() > 80:
                reaction.append('Вы замечаете, что '+fname+' как-то странно поглядывает на Вас. Похоже эти эти белые пятна привлекают лишнее внимание. ')
                if char.getLoy() < 50:
                    reaction.append('И так как лояльность ученика не очень высока, он наверняка проговориться своим родителям.')
                    char.setRep(-0.5)
            else:
                reaction.append('Вы замечаете, что '+fname+' c какой-то странной улыбкой поглядывает на вас. Похоже эти белые пятна привлекают лишнее внимание. Хотя не видно, чтобы это хоть как то смущало собеседника.')
        
        if player.getDirty() > 1: # Если грязь
            if player.getDirty() > 4:
                reaction.append(fname + ' ужасно кривится от вашего запаха. Похоже кого то сейчас стошнит.')
            else:
                reaction.append(fname + ' кривится от вашего запаха.')
            char.setLoy(-1*player.getDirty())

        if player.getClothPurpose('usual'): # Если обычная одежда
            if char.getCorr() > 80:
                if char.getWill() < 80:
                    if char.getSex() == 'male':
                        reaction.append('Разглядывая вашу обычную одежду '+name+' явно скучает. Наверняка он надеялся увидеть что то более сексуальное и обтягивающее. ')
                    else:
                        reaction.append(name + ' явно не одобряет ваш слишком строгий наряд. Она то сама уже без стеснения носит миниюбки. ')
                    char.sayCount = char.sayCount/2
                else:
                    if char.getSex() == 'male':
                        reaction.append(name + ' вежливо кивает головой, разглядывая вашу строгую одежду. Он стал лучше к вам относиться из за того, что Вы не идёте на поводу у толпы и не снимаете с себя шмотки, улюлюкая при этом.')
                    else:
                        reaction.append(name + ' мило улыбается и поправляет свою одежду, разглядывая вашу. Она стала лучше к вам относиться из за того, что вы плевать хотели на последние тренды. ')
                    char.setLoy(1)
            else:
                if char.getSex() == 'male':
                    reaction.append(name +' вежливо здоровается с вами и настраивается на серьёзный разговор, к которому располагает ваша, довольно строгая одежда. ')
                else:
                    reaction.append(name +' кивает Вам и и настраивается на серьёзный разговор, к которому располагает ваша, довольно строгая одежда. ')
                if char.getLoy() > 500:
                    reaction.append('При следующем разговоре с родителями, '+temp+' наверняка упомянёт вашу строгость')
        
        if player.getClothPurpose('sexy'): # Если сексуальная одежда
            
        
        return reaction