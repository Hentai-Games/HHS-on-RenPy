init 11 python:
    """Создает новый статус для локации.

    name - имя для статуса
    pic - изображение для отображения статуса
    sex - пол для статуса, либо строка: male, female, futa, any,
          либо список с комбинацией этих значений
    char_type - тип персонажа: any, student, teacher
    events - список меток ивентов, либо None - если статус не
             порождает ивентов
    requirements - dict необходимых параметров
                   (key - corr, fun, ...;
                    value - минимально-необходимое значение параметра),
                   либо None если статус не имеет никаких требований
    stats_actions - как статус повлияет на взявшего его персонажа.
                    Задается как dict, где key - corr, fun, ...;
                    value - задает на сколько изменится параметр,
                    но финально параметр не вырастит больше
                    N(заиграться до 100 fun не получится).
                    Пример: stats_actions={'fun': (1, 20)} - fun
                    увеличится на 1, но в итоге будет не больше 20
                    ['loyalty', 'fun', 'corr', 'lust', 'will',
                     'education', 'health', 'intelligence', 'beauty',
                     'reputation', 'energy', 'dirty']
    """
    
    go_status = LocationStatus('Гуляет', None, 'any', stats_actions = {'fun':(0.1,15)})
    stop_status = LocationStatus('Стоит', None, 'any')
    pee_status = LocationStatus('Писает', None, 'any', events = ['status_wc'])
    play_status = LocationStatus('Играет', None, 'any', char_type = 'student', stats_actions = {'fun':(0.1,20)})
    shopping_status = LocationStatus('Шоппингует', None, ['female','futa'], stats_actions = {'fun':(0.3,30)})
    football_status = LocationStatus('Играет в футбол', None, 'any', stats_actions = {'fun':(0.3,30)})
    undress_status = LocationStatus('Переодевается', None, 'any', events = ['status_undress'])
    
    hidden_mastur = LocationStatus('Мастурбирует', None, 'any', char_type = 'student', events = ['status_hidden_mastur'], requirements = {'lust':80}, stats_actions = {'lust':(-100,100),'corr':(1,20)})
    mastur = LocationStatus('Мастурбирует', None, 'any', char_type = 'student', events = ['status_mastur'], requirements = {'lust':80, 'corr':50}, stats_actions = {'lust':(-100,100),'corr':(1,40)})
    public_mastur = LocationStatus('Мастурбирует', None, 'any', char_type = 'student', events = ['status_public_mastur'], requirements = {'lust':80, 'corr':80}, stats_actions = {'lust':(-100,100),'corr':(1,80),'reputation':(-1,100)})
    
    
    
    kiss_status = LocationStatus('Целуется', None, 'any', char_type = 'student', events = ['status_kiss'], requirements = {'lust':30}, stats_actions = {'lust':(5,90)})
    kiss_public_status = LocationStatus('Целуется', None, 'any', char_type = 'student', events = ['status_kiss'], requirements = {'lust':30,'corr':25}, stats_actions = {'lust':(5,90)})
    
    swim_status = LocationStatus('Плавает', None, 'any', events = ['status_swim'], stats_actions = {'fun':(0.2,50),'lust':(1,30)})
    tan_status = LocationStatus('Загорает', None, 'any', stats_actions = {'beauty':(0.1,60),'fun':(0.1,50),'lust':(1,60)})
    voleyball_status = LocationStatus('Играет в волейбол', None, 'any', char_type = 'student', events = ['status_voleyball'], stats_actions = {'fun':(0.2,40),'lust':(1,40)})
    
    learn_low_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'fun':(-0.2,100),'education': (0.1, 25)})
    learn_mid_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'fun':(-0.1,100),'education': (0.1, 50)})
    learn_high_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'education': (0.1, 75)})
    learn_lust_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'fun':(0.1,30),'education': (0.1, 50), 'lust':(0.1,70)})
    
    teach_status = LocationStatus('Преподаёт', None, 'any', char_type = 'teacher', stats_actions = {'fun':(0.1,30),'education':(0.01, 80)})
    
init 11 python:
    def statusDistribution():
        for loc in locations:
            loc.eraseStatuses()
            loc.addStatus(go_status)
            loc.addStatus(stop_status)
            loc.addStatus(play_status)
            loc.addStatus(kiss_public_status)
            
            if 'school' not in loc.position:
                loc.addStatus(public_mastur)
            if 'school' in loc.position:
                loc.addStatus(mastur)
            if loc.id in ['loc_wcf','loc_wcm']:
                loc.removeStatus(play_status)
                loc.addStatus(kiss_status)
                loc.addStatus(pee_status)
                loc.addStatus(hidden_mastur,40)
            if loc.id in ['loc_shoppingStreet']:
                loc.addStatus(shopping_status)
            if 'swim' in loc.position:
                loc.addStatus(kiss_status)
                loc.addStatus(swim_status)
            if loc.id in ['loc_beach']:
                loc.addStatus(tan_status)
                loc.addStatus(voleyball_status)
            if loc.id in ['loc_gym']:
                loc.addStatus(football_status)
                
            if 'classroom' in loc.position:
                if lt() > 0:
                    loc.eraseStatuses()
                    loc.addStatus(hidden_mastur)
                    if 'poor' == school.eduMats:
                        loc.addStatus(learn_low_status)
                    elif 'standart' == school.eduMats:
                        loc.addStatus(learn_mid_status)
                    elif 'good' == school.eduMats:
                        loc.addStatus(learn_high_status)
                    elif 'eduSexy' == school.eduMats:
                        loc.addStatus(learn_lust_status)
                    loc.addStatus(teach_status)
                else:
                    loc.removeStatus(learn_low_status)
                    loc.removeStatus(learn_mid_status)
                    loc.removeStatus(learn_high_status)
                    loc.removeStatus(learn_lust_status)
                    loc.removeStatus(teach_status)
    statusDistribution()
            
   
label status_wc:
    if interactionObj.getSex() == 'female':
        show expression 'pic/status/pee_female.png'
    elif interactionObj.getSex() == 'male':
        show expression 'pic/status/pee_male.jpg'
    else:
        show expression 'pic/status/pee_futa.png'
    interactionObj.say 'А можно я пописаю в одиночестве, а?'
    $ interactionObj.incLoy(-1)
    $ move(curloc)
    
label status_swim:
    if interactionObj.getSex('mf') == 'female':
        show expression 'pic/status/swim_female.jpg'
        '[interactionObj.name] купается. Вам не докричаться до неё.'
    else:
        show expression 'pic/status/swim_male.png'
        '[interactionObj.name] плавает. Вам не докричаться до него.'
    $ move(curloc)
    
label status_hidden_mastur:
    if curloc in ['loc_wcf','loc_wcm']:
        if interactionObj.getSex() == 'futa':
            show expression 'pic/status/futa_toilet_mastur.jpg'
            interactionObj.say 'Чёрт, простите, я не, О-о-ох.'
            '[interactionObj.name] уже не в силах остановиться, её тело трясёт, а рука быстро двигается вдоль члена.'
            'Вы видите, как футу скручивают спазмы, и из её члена вырываются густые струи спермы, покрывая унитаз белыми каплями.'
            interactionObj.say 'Зачем вы так, ну зачем?'
            'Закрыв лицо, девочка убегает.'
            $ interactionObj.setLoy(-5)
            $ interactionObj.moveToLocation(choice(locations).id)
        elif interactionObj.getSex() == 'female':
            show expression 'pic/status/female_toilet_mastur.jpg' as tempPic
            '[interactionObj.name] сидит на унитазе и натирает свою киску прямо сквозь промокшие трусики. Похоже, что её возбуждение достигло предела и ей требуется разрядка.'
            menu:
                'Наказать её':
                    player.say '[interactionObj.fname], чем ты здесь занимаешься, а?'
                    interactionObj.say 'Я? Я, я просто, ой....'
                    'Вы видите, как на трусиках расплывается крупное жёлтое пятно. Похоже, что вы зря напугали девочку в самый ответственный момент. По лицу ученицы начинают бежать слёзы.'
                    show expression 'pic/status/female_toilet_mastur_pull.jpg' as tempPic
                    'Она резко сдёргивает с себя грязные трусики, оставляя их на полу, и убегает.'
                    $ interactionObj.setLoy(-5)
                    $ interactionObj.removeItems(studpantiesF.name)
                    $ interactionObj.moveToLocation(choice(locations).id)
                    menu:
                        'Что делать с трусами?'
                        'Взять':
                            'Вы, немного брезгуя, берёте трусики и кладёте себе в сумочку.'
                            $ player.addItem(clubPanties)
                            $ player.setDirty(1)
                        'Выбросить':
                            'Вы выбрасываете трусики в ближайшую мусорку.'
                'Дать ей кончить':
                    hide tempPic
                    'Вы прикрываете дверь, и из за неё слышутся приглушённые стоны, и судорожное шуршание ног по полу. Похоже, что у девочки всё получилось!'
                    $ interactionObj.moveToLocation(choice(locations).id)
        else:
            show expression 'pic/status/male_toilet_mastur.jpg' as tempPic
            interactionObj.say 'О, да, [player.fname], пососи его вот так, детка!'
            'С этими словами и вашим именем на устах, парень выпускает из своего члена длинную струйку спермы прямо на пол.'
            'Вы поспешно уходите, прежде чем вас замечают.'
            $ interactionObj.moveToLocation(choice(locations).id)
    else:
        pass
    $ move('loc_secondFloor')
    
label status_mastur:
    '[interactionObj.name] дрочит.'
    $ move(curloc)
    
label status_public_mastur:
    '[interactionObj.name] публично дрочит.'
    $ move(curloc)
    
label status_voleyball:
    '[interactionObj.name] играет с дургими ребятами в пляжный волейбол.'
    $ move(curloc)
    
label status_kiss:
    '[interactionObj.name] и [interactionObj.partner.name] целуются. Они замечают, что вы за ними наблюдали и уходят.'
    $ interactionObj.moveToLocation(choice(locations).id)
    $ interactionObj.partner.moveToLocation(choice(locations).id)
    $ move(curloc)
    
label status_undress:
    '[interactionObj.name] просит не мешать переодеваться.'