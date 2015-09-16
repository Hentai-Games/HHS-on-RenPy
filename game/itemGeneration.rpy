#############################################################
#Создание айтемов
#############################################################
init python:

    # Presents
    test_p = Present(
        name='Колготки',
        sex='female',
        cost=100,
        corr=10,
        picto = 'pic/items/nettights.png'
    )

    print test_p

    clothing = []
    #Cоздание предметов
    
    napkin = Tool(purpose = 'clean')
    napkin.name = _('Салфетка')
    napkin.cost = 100
    napkin.picto = 'pic/items/napkin.jpg'
    napkin.durability = 10
    napkin.type = 'tool'
    
    clubPanties = Tool(purpose = 'sell')
    clubPanties.name = _('Поношенные трусики')
    clubPanties.cost = 100
    clubPanties.picto = 'pic/items/clubPanties.jpg'
    clubPanties.durability = 10
    clubPanties.type = 'tool'
    
    sandwich = Food( energy = 250 )
    sandwich.name = _('Сэндвич')
    sandwich.cost = 0
    sandwich.picto = 'pic/items/sandwich.jpg'
    sandwich.durability = 1
    sandwich.type = 'food'

    eDrink = Food(energy = 100)
    eDrink.name = _('Энергетик')
    eDrink.cost = 150
    eDrink.picto = 'pic/items/edrink.jpg'
    eDrink.durability = 1
    eDrink.type = 'food'

    rawFood = Food(energy = 400)
    rawFood.name = _('Сырая еда')
    rawFood.cost = 500
    rawFood.picto = 'pic/items/food.jpg'
    rawFood.durability = 10
    rawFood.type = 'hidden'
    
    allItems = [napkin, sandwich, eDrink, rawFood, clubPanties]

    
#######################################################################
#  Верхняя одежда
#######################################################################   
    jaket = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    jaket.cover = ['верх']
    jaket.durability = 100
    jaket.name = _('Пиджак')
    jaket.cost = 1500
    jaket.picto = 'pic/items/jaket.png'
    jaket.type = 'clothing'
    clothing.append(jaket)
    
    freejaket = Clothing(
    lust = 10,
    corr = 25,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'sexy')
    freejaket.cover = ['верх']
    freejaket.durability = 100
    freejaket.name = _('Пиджак с вырезом')
    freejaket.cost = 2500
    freejaket.picto = 'pic/items/freejaket.png'
    freejaket.type = 'sexy'
    clothing.append(freejaket)
    
    skimpyjacket = Clothing(
    lust = 25,
    corr = 50,
    reputation = -1,
    char = 'teacher',
    sex = 'female',
    purpose = 'skimpy')
    skimpyjacket.cover = ['верх']
    skimpyjacket.durability = 50
    skimpyjacket.name = _('Полоски ткани')
    skimpyjacket.cost = 5500
    skimpyjacket.picto = 'pic/items/skimpyjacket.png'
    skimpyjacket.type = 'sexy'
    clothing.append(skimpyjacket)
    
#############################################################

    studstrictjaket = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'strict')
    studstrictjaket.cover = ['верх']
    studstrictjaket.durability = 10000
    studstrictjaket.name = _('Девчачий строгий пиджак')
    studstrictjaket.cost = 1500
    studstrictjaket.picto = 'pic/noimage.gif'
    studstrictjaket.type = 'clothing'
    clothing.append(studstrictjaket)
 
    studjaket = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'uniform')
    studjaket.cover = ['верх']
    studjaket.durability = 10000
    studjaket.name = _('Девчачий пиджак')
    studjaket.cost = 1500
    studjaket.picto = 'pic/noimage.gif'
    studjaket.type = 'clothing'
    clothing.append(studjaket)
    
    studsexyjaket = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'sexy')
    studsexyjaket.cover = ['верх','грудь']
    studsexyjaket.durability = 10000
    studsexyjaket.name = _('Сексуальный пиджачок')
    studsexyjaket.cost = 1500
    studsexyjaket.picto = 'pic/noimage.gif'
    studsexyjaket.type = 'clothing'
    clothing.append(studsexyjaket)
    
    studskimpyjaket = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'skimpy')
    studskimpyjaket.cover = ['верх','грудь']
    studskimpyjaket.durability = 10000
    studskimpyjaket.name = _('что-то невесомое')
    studskimpyjaket.cost = 1500
    studskimpyjaket.picto = 'pic/noimage.gif'
    studskimpyjaket.type = 'clothing'
    clothing.append(studskimpyjaket)
    
    studDress = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'usual')
    studDress.cover = ['верх','низ']
    studDress.durability = 10000
    studDress.name = _('Простое платье')
    studDress.cost = 1500
    studDress.picto = 'pic/noimage.gif'
    studDress.type = 'clothing'
    clothing.append(studDress)
    
    studHarness = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'bdsm')
    studHarness.cover = ['верх','низ']
    studHarness.durability = 10000
    studHarness.name = _('Кожанная сбруя')
    studHarness.cost = 1500
    studHarness.picto = 'pic/noimage.gif'
    studHarness.type = 'clothing'
    clothing.append(studHarness)
    
    studJaketM = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'male',
    purpose = 'uniform')
    studJaketM.cover = ['верх']
    studJaketM.durability = 10000
    studJaketM.name = _('Мужской пиджак')
    studJaketM.cost = 1500
    studJaketM.picto = 'pic/noimage.gif'
    studJaketM.type = 'clothing'
    clothing.append(studJaketM)
    
    studStrictJaketM = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'male',
    purpose = 'strict')
    studStrictJaketM.cover = ['верх']
    studStrictJaketM.durability = 10000
    studStrictJaketM.name = _('Строгий пиджак')
    studStrictJaketM.cost = 1500
    studStrictJaketM.picto = 'pic/noimage.gif'
    studStrictJaketM.type = 'clothing'
    clothing.append(studStrictJaketM)
    
    studJaketM = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'male',
    purpose = 'uniform')
    studJaketM.cover = ['верх']
    studJaketM.durability = 10000
    studJaketM.name = _('Школьный пиджак')
    studJaketM.cost = 1500
    studJaketM.picto = 'pic/noimage.gif'
    studJaketM.type = 'clothing'
    clothing.append(studJaketM)
    
    tShirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'male',
    purpose = 'usual')
    tShirt.cover = ['верх']
    tShirt.durability = 10000
    tShirt.name = _('Футболка')
    tShirt.cost = 1500
    tShirt.picto = 'pic/noimage.gif'
    tShirt.type = 'clothing'
    clothing.append(tShirt)
    
    studLeather = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'male',
    purpose = 'bdsm')
    studLeather.cover = ['верх','низ']
    studLeather.durability = 10000
    studLeather.name = _('Кожанная сбруя')
    studLeather.cost = 1500
    studLeather.picto = 'pic/noimage.gif'
    studLeather.type = 'clothing'
    clothing.append(studLeather)
    
#############################################################
    
#######################################################################
#  Нижняя одежда  
#######################################################################     
    longSkirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    longSkirt.cover = ['низ']
    longSkirt.durability = 100
    longSkirt.name = _('Длинная юбка')
    longSkirt.cost = 1000
    longSkirt.picto = 'pic/items/longSkirt.png'
    longSkirt.type = 'clothing'
    clothing.append(longSkirt)

    shortSkirt = Clothing(
    lust = 10,
    corr = 15,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'sexy')
    shortSkirt.cover = ['низ']
    shortSkirt.durability = 75
    shortSkirt.name = _('Короткая юбка')
    shortSkirt.cost = 1000
    shortSkirt.picto = 'pic/items/shortSkirt.png'
    shortSkirt.type = 'clothing'
    clothing.append(shortSkirt)
    
    skimpySkirt = Clothing(
    lust = 30,
    corr = 50,
    reputation = -1,
    char = 'teacher',
    sex = 'female',
    purpose = 'skimpy')
    skimpySkirt.cover = ['низ']
    skimpySkirt.durability = 50
    skimpySkirt.name = _('Широкий пояс')
    skimpySkirt.cost = 1000
    skimpySkirt.picto = 'pic/items/skimpySkirt.png'
    skimpySkirt.type = 'clothing'
    clothing.append(skimpySkirt)
    
#############################################################

    studstrictskirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'strict')
    studstrictskirt.cover = ['низ']
    studstrictskirt.durability = 10000
    studstrictskirt.name = _('Длинная строгая юбка')
    studstrictskirt.cost = 1500
    studstrictskirt.picto = 'pic/noimage.gif'
    studstrictskirt.type = 'clothing'
    clothing.append(studstrictskirt)
 
    studskirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'uniform')
    studskirt.cover = ['низ']
    studskirt.durability = 10000
    studskirt.name = _('Школьная юбка до колен')
    studskirt.cost = 1500
    studskirt.picto = 'pic/noimage.gif'
    studskirt.type = 'clothing'
    clothing.append(studskirt)
    
    studsexyskirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'sexy')
    studsexyskirt.cover = ['низ']
    studsexyskirt.durability = 10000
    studsexyskirt.name = _('Короткая школьная юбка')
    studsexyskirt.cost = 1500
    studsexyskirt.picto = 'pic/noimage.gif'
    studsexyskirt.type = 'clothing'
    clothing.append(studsexyskirt)
    
    studskimpyskirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'female',
    purpose = 'skimpy')
    studskimpyskirt.cover = ['низ','попа']
    studskimpyskirt.durability = 10000
    studskimpyskirt.name = _('Она называет этот пояс юбкой')
    studskimpyskirt.cost = 1500
    studskimpyskirt.picto = 'pic/noimage.gif'
    studskimpyskirt.type = 'clothing'
    clothing.append(studskimpyskirt)
    
    studPants = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'male',
    purpose = 'usual')
    studPants.cover = ['низ']
    studPants.durability = 10000
    studPants.name = _('Брюки')
    studPants.cost = 1500
    studPants.picto = 'pic/noimage.gif'
    studPants.type = 'clothing'
    clothing.append(studPants)
    
    studShorts = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'stud',
    sex = 'male',
    purpose = 'sexy')
    studShorts.cover = ['низ']
    studShorts.durability = 10000
    studShorts.name = _('Шорты')
    studShorts.cost = 1500
    studShorts.picto = 'pic/noimage.gif'
    studShorts.type = 'clothing'
    clothing.append(studShorts)

#######################################################################
#  Колготки     
#######################################################################     
    browntights = Clothing(
    lust = 5,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    browntights.cover = ['ноги']
    browntights.durability = 10
    browntights.name = _('Телесные колготки')
    browntights.cost = 150
    browntights.picto = 'pic/items/browntights.png'
    browntights.type = 'clothing'
    clothing.append(browntights)

    blacktights = Clothing(
    lust = 10,
    corr = 10,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'sexy')
    blacktights.cover = ['ноги']
    blacktights.durability = 10
    blacktights.name = _('Чёрные колготки')
    blacktights.cost = 150
    blacktights.picto = 'pic/items/blacktights.png'
    blacktights.type = 'clothing'
    clothing.append(blacktights)
    
    nettights = Clothing(
    lust = 20,
    corr = 30,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'skimpy')
    nettights.cover = ['ноги']
    nettights.durability = 10
    nettights.name = _('Колготки в сетку')
    nettights.cost = 450
    nettights.picto = 'pic/items/nettights.png'
    nettights.type = 'clothing'
    clothing.append(nettights)
    
#######################################################################
    socks = Clothing(
    lust = 5,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'usual')
    socks.cover = ['ноги']
    socks.durability = 10000
    socks.name = _('Тёмные носочки')
    socks.cost = 150
    socks.picto = 'pic/noimage.gif'
    socks.type = 'clothing'
    clothing.append(socks)

    whitesocks = Clothing(
    lust = 10,
    corr = 10,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'sexy')
    whitesocks.cover = ['ноги']
    whitesocks.durability = 10000
    whitesocks.name = _('Белые носочки')
    whitesocks.cost = 150
    whitesocks.picto = 'pic/noimage.gif'
    whitesocks.type = 'clothing'
    clothing.append(whitesocks)
    
    whitetights = Clothing(
    lust = 20,
    corr = 30,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'skimpy')
    whitetights.cover = ['ноги']
    whitetights.durability = 10000
    whitetights.name = _('Белые чулки')
    whitetights.cost = 450
    whitetights.picto = 'pic/noimage.gif'
    whitetights.type = 'clothing'
    clothing.append(whitetights)
    
#######################################################################   
#  Нижнее бельё    
#######################################################################   
    simpleUnderwear = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    simpleUnderwear.cover = ['грудь','попа']
    simpleUnderwear.durability = 20
    simpleUnderwear.name = _('Простое нижнее бельё')
    simpleUnderwear.cost = 300
    simpleUnderwear.picto = 'pic/items/simpleUnderwear.png'
    simpleUnderwear.type = 'clothing'
    clothing.append(simpleUnderwear)
    
    sexyUnderwear = Clothing(
    lust = 5,
    corr = 15,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'sexy')
    sexyUnderwear.cover = ['грудь','попа']
    sexyUnderwear.durability = 20
    sexyUnderwear.name = _('Красивое нижнее бельё')
    sexyUnderwear.cost = 800
    sexyUnderwear.picto = 'pic/items/sexyUnderwear.png'
    sexyUnderwear.type = 'clothing'
    clothing.append(sexyUnderwear)

    skimpyUnderwear = Clothing(
    lust = 15,
    corr = 30,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'skimpy')
    skimpyUnderwear.cover = ['грудь','попа']
    skimpyUnderwear.durability = 20
    skimpyUnderwear.name = _('Сексуальное нижнее бельё')
    skimpyUnderwear.cost = 1500
    skimpyUnderwear.picto = 'pic/items/skimpyUnderwear.png'
    skimpyUnderwear.type = 'clothing'
    clothing.append(skimpyUnderwear)
    
    pantalons = Clothing(
    lust = -20,
    corr = 0,
    reputation = -1,
    char = 'teacher',
    sex = 'female',
    purpose = 'sleep')
    pantalons.cover = ['попа','низ']
    pantalons.durability = 2000
    pantalons.name = _('Старые шорты')
    pantalons.cost = 10
    pantalons.picto = 'pic/items/pantaloons.png'
    pantalons.type = 'clothing'
    clothing.append(pantalons)

    oldShirt = Clothing(
    lust = -20,
    corr = 0,
    reputation = -1,
    char = 'teacher',
    sex = 'female',
    purpose = 'sleep')
    oldShirt.cover = ['грудь','верх']
    oldShirt.durability = 2000
    oldShirt.name = _('Домашняя футболка')
    oldShirt.cost = 10
    oldShirt.picto = 'pic/items/oldShirt.png'
    oldShirt.type = 'clothing'
    clothing.append(oldShirt)
    
#######################################################################  
    studpantiesF = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'usual')
    studpantiesF.cover = ['попа']
    studpantiesF.durability = 10000
    studpantiesF.name = _('Трусики')
    studpantiesF.cost = 150
    studpantiesF.picto = 'pic/noimage.gif'
    studpantiesF.type = 'clothing'
    clothing.append(studpantiesF)
    
    studSlip = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'usual')
    studSlip.cover = ['грудь']
    studSlip.durability = 10000
    studSlip.name = _('Лифчик')
    studSlip.cost = 150
    studSlip.picto = 'pic/noimage.gif'
    studSlip.type = 'clothing'
    clothing.append(studSlip)
 
    studpantiesM = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'male',
    purpose = 'usual')
    studpantiesM.cover = ['попа']
    studpantiesM.durability = 10000
    studpantiesM.name = _('Трусы')
    studpantiesM.cost = 150
    studpantiesM.picto = 'pic/noimage.gif'
    studpantiesM.type = 'clothing'
    clothing.append(studpantiesM)
    
#######################################################################
#  Купальники 
#######################################################################   

    swimsuit = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'swim')
    swimsuit.cover = ['грудь','попа','верх','низ','ноги']
    swimsuit.durability = 40
    swimsuit.name = _('Купальник')
    swimsuit.cost = 500
    swimsuit.picto = 'pic/items/swimsuit.png'
    swimsuit.type = 'clothing'
    clothing.append(swimsuit)
    
    bikini_top = Clothing(
    lust = 5,
    corr = 15,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'swim')
    bikini_top.cover = ['грудь','верх']
    bikini_top.durability = 20
    bikini_top.name = _('Бикини верх')
    bikini_top.cost = 500
    bikini_top.picto = 'pic/items/bikini_top.png'
    bikini_top.type = 'clothing'
    clothing.append(bikini_top)

    bikini_bottom = Clothing(
    lust = 15,
    corr = 15,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'swim')
    bikini_bottom.cover = ['попа','низ','ноги']
    bikini_bottom.durability = 20
    bikini_bottom.name = _('Бикини низ')
    bikini_bottom.cost = 500
    bikini_bottom.picto = 'pic/items/bikini_bottom.png'
    bikini_bottom.type = 'clothing'
    clothing.append(bikini_bottom)
    
    minibikini = Clothing(
    lust = 40,
    corr = 60,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'swim')
    minibikini.cover = ['грудь','попа','верх','низ','ноги']
    minibikini.durability = 40
    minibikini.name = _('Минибикини')
    minibikini.cost = 2500
    minibikini.picto = 'pic/items/minibikini.png'
    minibikini.type = 'clothing'
    clothing.append(minibikini)
    
#######################################################################
    studswimsuit = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'female',
    purpose = 'swim')
    studswimsuit.cover = ['грудь','попа','верх','низ','ноги']
    studswimsuit.durability = 40000
    studswimsuit.name = _('Полный купальник')
    studswimsuit.cost = 500
    studswimsuit.picto = 'pic/noimage.gif'
    studswimsuit.type = 'clothing'
    clothing.append(studswimsuit)

    swimShorts = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'stud',
    sex = 'male',
    purpose = 'swim')
    swimShorts.cover = ['грудь','попа','верх','низ','ноги']
    swimShorts.durability = 40000
    swimShorts.name = _('Шорты для плавания')
    swimShorts.cost = 500
    swimShorts.picto = 'pic/noimage.gif'
    swimShorts.type = 'clothing'
    clothing.append(swimShorts)
    
#######################################################################
#  Сеты
#######################################################################   

# спортивная форма
    sportUniform = Clothing(
    lust = 5,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'sport')
    sportUniform.cover = ['верх','низ']
    sportUniform.durability = 300
    sportUniform.name = _('Спортформа')
    sportUniform.cost = 1500
    # picto
    sportUniform.picto = 'pic/items/sportUniform.png'
    sportUniform.type = 'clothing'
    clothing.append(sportUniform)
    
#  Форма Мустанговича
    blueForm = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'male',
    purpose = 'usual')
    blueForm.cover = ['верх','низ']
    blueForm.durability = 10000
    blueForm.name = _('Спортивный костюм')
    blueForm.cost = 1500
    blueForm.picto = 'pic/noimage.gif'
    blueForm.type = 'clothing'
    clothing.append(blueForm)

    manpants = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'male',
    purpose = 'usual')
    manpants.cover = ['попа']
    manpants.durability = 10000
    manpants.name = _('Трусы семейные')
    manpants.cost = 1500
    manpants.picto = 'pic/items/jaket.png'
    manpants.type = 'clothing'
    clothing.append(manpants)
    
    
    allItems.extend(clothing)
