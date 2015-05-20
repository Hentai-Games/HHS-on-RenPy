init python:
    def textgen(char):
        description = ''

        name = char.fullName()
        age = str(char.age)
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
                if edu < 20: description += 'имеет слабое образование. Настолько слабое, что Вы удивлены, что этот человек работает учителем'
                elif edu < 50: description += 'имеет неплохое образование, но всё же её знания оставляют желать лучшего'
                elif edu < 80: description += 'имеет хорошее представление о своём предмете преподавания'
                else : description += 'имеет прекрасные знания не только о своём предмете, но и в смежных науках'

            description += '\n'
            description += char.fname + ' '
            if loyalty < 20: description += 'совсем не знает Вас.'
            elif loyalty < 50: description += 'не против иногда перекинуться с Вами парой словечек.'
            elif loyalty < 80: description += 'весьма хорошего о Вас мнения.'
            else : description += 'просто обожает вас.'

            if loyalty >= 50 and sex == 'futa': description += ' Девочка недавно призналась, что она не совсем девочка и прячет член под юбкой.'

            description += '\n'

            if sex == 'female':
                if lust < 20: description += ''
                elif lust < 50: description += 'Вы замечаете у неё немного покрасневшие щёчки. '
                elif lust < 80: description += 'Вы замечаете, что она сильно краснеет, когда встречается с Вами взглядом. '
                else : description += 'Вы замечаете, что она сильно краснеет, когда встречается с Вами взглядом. '
            else :
                if lust < 20: description += ''
                elif lust < 50: description += 'Вы замечаете у него немного покрасневшие щёки. '
                elif lust < 80: description += 'Вы замечаете, что он сильно краснеет, когда встречается с Вами взглядом. '
                else : description += 'Вы замечаете, что ученик переминается с ноги на ногу, и Вы замечаете видимый бугорок на его штанах. '

            if corr < 20: description += 'По слухам, ' + char.fname + ' не знает о сексе ничего.'
            elif corr < 50: description += 'По слухам, ' + char.fname + ' мастурбирет и подглядывает за парочками.'
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
                elif rep < 50: description += 'родители не очень высокого о Вас мнения.'
                elif rep < 80: description += 'родители ставят Вас в пример своим детям.'
                else : description += 'родители в восторге от вас.'

            if sex != 'female' and corr > 50:
                description += '\n[name] прозрачно намекает вам, что под одеждой от вас скрывается '+ psize +' сантиметровый змий!'
            
            description += '\n'
            if sex == 'female':
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
            description += '\n'
            
            if name in complains:
                description += 'Родители этого ученика жаловались на вас.'

#########################################
# Игрок
#########################################

        else:
            description += 'Меня зовут ' + name + ', мне '+ age +' лет.\n'
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
            description += '\n'
            temp = school.myIncome()
            description += 'Я отработала '+ getDays(school.daysWorked) +' на этой неделе. На данный момент мой заработок составит '+ str(temp) +' монет.'
            if complains != '':
                description += '\n'
                description += '\n'
                description += 'Родители следующих учеников жаловались на меня: ' + complains
        return description


# self.inventory = inventory
# self.will = will
# self.club = club
# self.energy = energy
# self.health = health
# self.intel = intel
# self.body = body
# self.beauty = beauty
# self.dirty = dirty