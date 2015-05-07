#############################################################
#Создание айтемов
#############################################################
init python:
    clothing = []
    #Cоздание предметов
    
    napkin = Tool(purpose = 'clean')
    napkin.name = _('Салфетка')
    napkin.cost = 100
    napkin.picto = 'pic/items/napkin.jpg'
    napkin.durability = 10
    napkin.type = 'tool'
    
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
    
    allItems = [napkin, sandwich, eDrink, rawFood]

    
# codeBlc Женские вещи

#######################################################################
# codeBlc Верхняя одежда
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
    #picto
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
    #picto
    skimpyjacket.picto = 'pic/items/skimpyjacket.png'
    skimpyjacket.type = 'sexy'
    clothing.append(skimpyjacket)
# endBlc 
    
#######################################################################
# codeBlc Нижняя одежда    
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
    #picto
    shortSkirt.picto = 'pic/items/shortSkirt.png'
    shortSkirt.type = 'clothing'
    clothing.append(shortSkirt)
    
    skimpySkirt = Clothing(
    lust = 30,
    corr = 50,
    reputation = -1,
    char = 'teacher',
    sex = 'female',
    purpose = 'sexy')
    skimpySkirt.cover = ['низ']
    skimpySkirt.durability = 50
    skimpySkirt.name = _('Широкий пояс')
    skimpySkirt.cost = 1000
    #picto
    skimpySkirt.picto = 'pic/items/skimpySkirt.png'
    skimpySkirt.type = 'clothing'
    clothing.append(skimpySkirt)
    
# endBlc 

#######################################################################
# codeBlc Колготки       
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
    #picto
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
    #picto
    nettights.picto = 'pic/items/nettights.png'
    nettights.type = 'clothing'
    clothing.append(nettights)
# endBlc 

#######################################################################   
# codeBlc Нижнее бельё    
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
    #picto
    sexyUnderwear.picto = 'pic/items/sexyUnderwear.png'
    sexyUnderwear.type = 'clothing'
    clothing.append(sexyUnderwear)

    skimpyUnderwear = Clothing(
    lust = 15,
    corr = 30,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    skimpyUnderwear.cover = ['грудь','попа']
    skimpyUnderwear.durability = 20
    skimpyUnderwear.name = _('Сексуальное нижнее бельё')
    skimpyUnderwear.cost = 1500
    #picto
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
    pantalons.cover = ['грудь','верх']
    pantalons.durability = 2000
    pantalons.name = _('Старые шорты')
    pantalons.cost = 10
    #picto
    pantalons.picto = 'pic/items/simpleUnderwear.png'
    pantalons.type = 'clothing'
    clothing.append(pantalons)

    oldShirt = Clothing(
    lust = -20,
    corr = 0,
    reputation = -1,
    char = 'teacher',
    sex = 'female',
    purpose = 'sleep')
    oldShirt.cover = ['попа','низ']
    oldShirt.durability = 2000
    oldShirt.name = _('Старая футболка')
    oldShirt.cost = 10
    #picto
    oldShirt.picto = 'pic/items/simpleUnderwear.png'
    oldShirt.type = 'clothing'
    clothing.append(oldShirt)
    
# endBlc 

#######################################################################
# codeBlc Купальники 
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
    corr = 30,
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
    corr = 30,
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
    minibikini.picto = 'pic/items/swimsuit.png'
    minibikini.type = 'clothing'
    clothing.append(minibikini)
    
# endBlc 
    
#######################################################################
# codeBlc Сеты
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
    sportUniform.picto = 'pic/items/jaket.png'
    sportUniform.type = 'clothing'
    clothing.append(sportUniform)
    
# endBlc   
    
# endBlc

# codeBlc Мужские вещи
    blueForm = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    blueForm.cover = ['верх']
    blueForm.durability = 10000
    blueForm.name = _('верх','низ')
    blueForm.cost = 1500
    blueForm.picto = 'pic/items/jaket.png'
    blueForm.type = 'clothing'
    clothing.append(blueForm)

# endBlc
    
    allItems.extend(clothing)
    