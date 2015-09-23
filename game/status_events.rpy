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
    sit_status = LocationStatus('Сидит', None, 'any')
    pee_status = LocationStatus('Писает', None, 'any', events = ['status_wc'])
    play_status = LocationStatus('Играет', None, 'any', char_type = 'student', stats_actions = {'fun':(0.1,20)})
    shopping_status = LocationStatus('Шоппингует', None, ['female','futa'], stats_actions = {'fun':(0.3,20)})
   
    hidden_mastur = LocationStatus('Мастурбирует', None, 'any', char_type = 'student', events = ['status_hidden_mastur'], requirements = {'lust':80}, stats_actions = {'lust':(-100,100),'corr':(1,20)})
    mastur = LocationStatus('Мастурбирует', None, 'any', char_type = 'student', events = ['status_mastur'], requirements = {'lust':80, 'corr':20}, stats_actions = {'lust':(-100,100),'corr':(1,40)})
    public_mastur = LocationStatus('Мастурбирует', None, 'any', char_type = 'student', events = ['status_public_mastur'], requirements = {'lust':80, 'corr':60}, stats_actions = {'lust':(-100,100),'corr':(1,80),'reputation':(-1,100)})
    
    kiss_status = LocationStatus('Целуется', None, 'any', char_type = 'student', events = ['status_kiss'], requirements = {'lust':30}, stats_actions = {'lust':(5,90)})
    
    swim_status = LocationStatus('Плавает', None, 'any', events = ['status_swim'], stats_actions = {'fun':(0.2,50),'lust':(1,30)})
    tan_status = LocationStatus('Загорает', None, 'any', stats_actions = {'beauty':(0.1,60),'fun':(0.1,50),'lust':(1,60)})
    voleyball_status = LocationStatus('Играет в волейбол', None, 'any', char_type = 'student', events = ['status_voleyball'], stats_actions = {'fun':(0.2,40),'lust':(1,40)})
    
    learn_low_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'fun':(-0.2,100),'education': (0.1, 25)})
    learn_mid_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'fun':(-0.1,100),'education': (0.1, 50)})
    learn_high_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'education': (0.1, 75)})
    learn_lust_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'fun':(0.1,30),'education': (0.1, 50), 'lust':(0.1,70)})
    
    teach_status = LocationStatus('Преподаёт', None, 'any', char_type = 'teacher', stats_actions = {'fun':(0.1,30),'education':(0.01, 80)})
    

    def statusDistribution():
        for loc in locations:
            loc.eraseStatuses()
            loc.addStatus(go_status)
            loc.addStatus(stop_status)
            loc.addStatus(play_status)
            loc.addStatus(kiss_status)
            
            if 'school' not in loc.position:
                loc.addStatus(public_mastur)
            if 'school' in loc.position:
                loc.addStatus(mastur,40)
            if loc.id in ['loc_wcf','loc_wcm']:
                loc.addStatus(pee_status)
                loc.addStatus(hidden_mastur,40)
            if loc.id in ['loc_shoppingStreet']:
                loc.addStatus(shopping_status)
            if 'swim' in loc.position:
                loc.addStatus(swim_status)
            if loc.id in ['loc_beach']:
                loc.addStatus(tan_status)
                loc.addStatus(voleyball_status)
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
                    continue
                else:
                    loc.addStatus(sit_status)
                    
    statusDistribution()
            
   
label status_wc:
    '[interactionObj.name] писает.'
    $ move(curloc)
    
label status_swim:
    '[interactionObj.name] плавает.'
    $ move(curloc)
    
label status_hidden_mastur:
    '[interactionObj.name] скрытно дрочит.'
    $ move(curloc)
    
label status_mastur:
    '[interactionObj.name] дрочит.'
    $ move(curloc)
    
label status_public_mastur:
    '[interactionObj.name] публично дрочит.'
    $ move(curloc)
    
label status_voleyball:
    '[interactionObj.name] играет в пляжный волейбол.'
    $ move(curloc)
    
label status_kiss:
    python:
        st = False
        for x in studs:
            if x.getLocationStatus() == kiss_status and x.getSex()!= interactionObj.getSex():
                st = x
                break
                
        if st == False:
            if interactionObj.getSex('mf') == 'female':
                st = getChar('male')
            else:
                st = getChar('female')
                
            st.moveToLocation(curloc)
            st.forceLocationStatus(kiss_status)
            
        interactionObj.moveToLocation(choice(locations).id)
        st.moveToLocation(choice(locations).id)
        
    '[interactionObj.name] и [st.name] целуются. Они замечают, что вы за ними наблюдали и уходят.'
    
    $ move(curloc)