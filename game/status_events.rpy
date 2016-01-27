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
    
    # go_status = LocationStatus('Идёт', None, 'any', stats_actions = {'fun':(0.1,10)})
    go_status = LocationStatus('Идёт', None, 'any')
    stop_status = LocationStatus('Стоит', None, 'any')
    pee_status = LocationStatus('Писает', None, 'any', 
        events = ['status_wc'])
    play_status = LocationStatus('Играет', None, 'any', char_type = 'student', 
        stats_actions = {'fun':(0.1,20)})
    shopping_status = LocationStatus('Делает покупки', None, ['female','futa'], 
        stats_actions = {'fun':(0.3,30)})
    football_status = LocationStatus('Играет в футбол', None, 'any', char_type = 'student',
        events = ['status_football'], 
        stats_actions = {'fun':(0.3,30)})
    undress_status = LocationStatus('Переодевается', None, 'any', 
        events = ['status_undress'])
        
    peep_status_male = LocationStatus('Подглядывает за девочками', None, ['male'], char_type = 'student', 
        stats_actions = {'fun':(0.1,40), 'lust':(1,70)})
    peep_status_female = LocationStatus('Подглядывает за мальчиками', None, ['female','futa'], char_type = 'student', 
        stats_actions = {'fun':(0.1,40), 'lust':(1,70)})
    
    # Мастурбация
    hidden_mastur = LocationStatus('Копошится', None, 'any', char_type = 'student', 
        events = ['status_hidden_mastur'], 
        requirements = {'lust':60}, 
        stats_actions = {'lust':(-100,0),'corr':(0.5,10),'fun':(1,30)})
    mastur = LocationStatus('Мастурбирует', None, 'any', char_type = 'student', 
        events = ['status_mastur'], 
        requirements = {'lust':80, 'corr':30}, 
        stats_actions = {'lust':(-100,0),'corr':(0.5,40),'fun':(1,30)})
    public_mastur = LocationStatus('Мастурбирует', None, 'any', char_type = 'student', 
        events = ['status_public_mastur'], 
        requirements = {'lust':80, 'corr':60}, 
        stats_actions = {'lust':(-100,0),'corr':(0.5,80),'reputation':(-1,0),'fun':(1,50)})
    
    # Секс add name to char_classes from 715 string (function moveToLocation)
    hidden_sex = LocationStatus('Скрытничает', None, 'any', char_type = 'student', 
        events = ['status_hidden_sex'], 
        requirements = {'corr':30, 'lust':60}, 
        stats_actions = {'lust':(-100,0),'corr':(1,50),'fun':(2,60)})
    school_sex = LocationStatus('Занимается сексом', None, 'any', char_type = 'student', 
        events = ['status_sex'], 
        requirements = {'corr':50, 'lust':60}, 
        stats_actions = {'lust':(-100,0),'corr':(1,80),'fun':(3,80)})
    public_sex = LocationStatus('Публично трахается', None, 'any', char_type = 'student', 
        events = ['status_public_sex'], 
        requirements = {'corr':80, 'lust':80}, 
        stats_actions = {'lust':(-100,0),'corr':(1,100),'fun':(5,100), 'reputation':(-1,10)})
    
    # Зависит от формы
    look_strict_status = LocationStatus('Осматривается', None, 'any', stats_actions = {'lust':(-1,0),'corr':(-1,10)})
    look_uniform_status = LocationStatus('Осматривается', None, 'any')
    look_usual_status = LocationStatus('Осматривается', None, 'any', stats_actions = {'lust':(0.5,50)})
    look_sexy_status = LocationStatus('Осматривается', None, 'any', stats_actions = {'lust':(1,50)})
    look_skimpy_status = LocationStatus('Осматривается', None, 'any', stats_actions = {'lust':(2,70)})
    look_naked_status = LocationStatus('Осматривается', None, 'any', stats_actions = {'lust':(4,100),'corr':(0.1,40)})
    look_bdsm_status = LocationStatus('Осматривается', None, 'any', stats_actions = {'lust':(4,100),'corr':(0.1,80)})
    
    # Фурнитура
    manec1_status = LocationStatus('Осматривает манекен', None, 'any', stats_actions = {'lust':(1,50)})
    manec2_status = LocationStatus('Трогает манекен', None, 'any', 
        requirements = {'corr': 10}, 
        stats_actions = {'lust':(3,70), 'corr':(0.1,20)})
    manec3_status = LocationStatus('Использует манекен', None, 'any', 
        events = ['status_useManec'],
        requirements = {'corr': 40, 'lust': 60}, 
        stats_actions = {'lust':(-100,0), 'corr':(1,60),'fun':(1,50)})
    
    video_status = LocationStatus('Смотрит порно', None, 'any',  
        events = ['status_watchVideo'], 
        requirements = {'corr': 10}, 
        stats_actions = {'lust':(5,80)})
    
    dildo1_status = LocationStatus('Осматривает игрушки', None, 'any',  stats_actions = {'lust':(1,50)})
    dildo2_status = LocationStatus('Трогает игрушки', None, 'any',  
        requirements = {'corr': 15}, 
        stats_actions = {'lust':(1,50),'corr':(0.01,25)})
    dildo3_status = LocationStatus('Использует игрушки', None, 'any', 
        events = ['status_useDildo'],
        requirements = {'corr': 30, 'lust': 60}, 
        stats_actions = {'lust':(-100,0), 'corr':(1,40), 'fun':(1,50)})
    
    # Фотки
    inhibLow_status1 = LocationStatus('Рассматривает фотографии', None, 'any', 
        stats_actions = {'lust':(inhibLow/2,60),'fun':(0.2,50)})
    inhibLow_status2 = LocationStatus('Принюхивается', None, ['male','futa'], 
        stats_actions = {'lust':(5,70)})
    
    flirt_status = LocationStatus('Флиртует', None, 'any', char_type = 'student', 
        requirements = {'lust':30}, 
        stats_actions = {'lust':(3,65)})
    kiss_status = LocationStatus('Целуется', None, 'any', char_type = 'student', 
        events = ['status_kiss'], 
        requirements = {'lust':60}, 
        stats_actions = {'lust':(5,90)})
    kiss_public_status = LocationStatus('Целуется', None, 'any', char_type = 'student', 
        events = ['status_kiss'], 
        requirements = {'lust':60,'corr':25}, 
        stats_actions = {'lust':(5,90)})
    
    # Наказания (распределяются в on_move)
    clean_status = LocationStatus('Убирается', None, 'any', stats_actions = {'fun':(-0.5,0)})
    learn_status = LocationStatus('Учится', None, 'any', stats_actions = {'fun':(-0.5,0)})
    shame_status = LocationStatus('Стыдится', None, 'any', stats_actions = {'fun':(-0.2,0),'lust':(1,100)})
    lock_status = LocationStatus('Взаперти', None, 'any', stats_actions = {'fun':(-0.5,0)})
    torture_status = LocationStatus('Висит в цепях', None, 'any', stats_actions = {'fun':(-1,0)})
    
    # Пляжные действия
    swim_status = LocationStatus('Плавает', None, 'any', 
        events = ['status_swim'], 
        stats_actions = {'fun':(0.3,50),'lust':(0.5,30)})
    tan_status = LocationStatus('Загорает', None, 'any', 
        stats_actions = {'beauty':(0.1,60),'fun':(0.2,50),'lust':(0.5,40)})
    voleyball_status = LocationStatus('Играет в волейбол', None, 'any', char_type = 'student', 
        events = ['status_voleyball'], 
        stats_actions = {'fun':(0.3,40),'lust':(1,40)})
    
    
    # Во время уроков
    learn_low_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'fun':(-0.4,0),'education': (0.1, 25)})
    learn_mid_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'fun':(-0.2,5),'education': (0.1, 50)})
    learn_high_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'education': (0.1, 75)})
    learn_lust_status = LocationStatus('Занимается', None, 'any', char_type = 'student', stats_actions = {'fun':(0.1,50),'education': (0.1, 50), 'lust':(0.1,70)})
    
    # Прочие локации и действия
    medexam_status = LocationStatus('Проходит медосмотр', None, 'any', char_type = 'student', stats_actions = {'fun':(1,50),'lust':(1,70)})
    
    # Клубы
    sport_status = LocationStatus('Занимается спортом', None, 'any', char_type = 'student', stats_actions = {'fun':(1,50)})
    cheerleader_status = LocationStatus('Разучивает танцы', None, 'any', char_type = 'student', stats_actions = {'fun':(1,50),'lust':(1,40)})
    paint_status = LocationStatus('Рисует', None, 'any', char_type = 'student', stats_actions = {'fun':(1,50),'education':(0.1,40)})
    cosplay_status = LocationStatus('Косплеит кого-то', None, 'any', char_type = 'student', stats_actions = {'fun':(2,50),'lust':(1,70)})
    medic_status1 = LocationStatus('Проводит осмотр', None, 'any', char_type = 'student', stats_actions = {'fun':(2,50),'lust':(4,70)})
    medic_status2 = LocationStatus('Проходит осмотр', None, 'any', char_type = 'student', stats_actions = {'fun':(2,50),'lust':(10,70)})
    
    # Учителя
    teach_status = LocationStatus('Преподаёт', None, 'any', char_type = 'teacher', stats_actions = {'fun':(0.1,30),'education':(0.01, 80)})
    pre_teach_status = LocationStatus('Готовится к уроку', None, 'any', char_type = 'teacher', stats_actions = {'fun':(0.1,30),'education':(0.1, 80)}) # статус для свободного учителя
    teacher_hidden_mastur = LocationStatus('Мастурбирует', None, 'any', char_type = 'teacher', events = ['status_teacherHidden_mastur'], requirements = {'lust':60}, stats_actions = {'lust':(-100,0),'corr':(1,20),'fun':(1,30)})
    
init 11 python:
    def lookSelector():
        if 'strict' == school.uniform:
            return look_strict_status
        elif 'unifrom' == school.uniform:
            return look_uniform_status
        elif 'usual' == school.uniform:
            return look_usual_status
        elif 'sexy' == school.uniform:
            return look_sexy_status
        elif 'skimpy' == school.uniform:
            return look_skimpy_status
        elif 'naked' == school.uniform:
            return look_naked_status
        elif 'bdsm' == school.uniform:
            return look_bdsm_status
        else:
            return look_uniform_status
            
    def learnSelector():
        if 'poor' == school.eduMats:
            return learn_low_status
        elif 'standart' == school.eduMats:
            return learn_mid_status
        elif 'good' == school.eduMats:
            return learn_high_status
        elif 'eduSexy' == school.eduMats:
            return learn_lust_status
        else:
            return learn_mid_status
            
    def statusDistribution():
        for loc in locations:
            loc.eraseStatuses()
            loc.addStatus(go_status) # Всюду ходят
            loc.addStatus(flirt_status) # Всюду флиртуют
            loc.addStatus(stop_status, 1) # Стоят
            loc.addStatus(play_status) # Играют
            loc.addStatus(kiss_public_status) # Публично целуются
            
            if 'school' not in loc.position:
                loc.addStatus(public_mastur) # Публичная мастурбация всюду, где не школа
                
            if 'school' in loc.position:
                loc.addStatus(mastur) # Мастурбация в школе
                loc.addStatus(lookSelector(),20) # Реакция на одежду
                if inhibLow in [1,2,3]:
                    loc.addStatus(inhibLow_status1) # Реакция на разврат школы
                if inhibLow in [4]:
                    loc.addStatus(inhibLow_status2) # Реакция на разврат школы
                
            if loc.id in ['loc_wcf','loc_wcm']:
                loc.removeStatus(play_status)
                loc.addStatus(kiss_status) # Поцелуи в сортире
                loc.addStatus(pee_status) # Писают
                loc.addStatus(hidden_mastur,40) # Дрочат скрытно
                loc.addStatus(teacher_hidden_mastur) # Учителя дрочат скрытно
                
            if loc.id == 'loc_wcf':
                loc.addStatus(peep_status_male) # Подглядывает за девочками
            
            if loc.id == 'loc_wcm':
                loc.addStatus(peep_status_female) # Подглядывает за мальчиками
                
            if loc.id in ['loc_shoppingStreet']:
                loc.addStatus(shopping_status) # Занимаются шоппингом
                
            if 'swim' in loc.position:
                loc.addStatus(kiss_status) # Целуются на пляжу и в бассейне
                loc.addStatus(swim_status) # Плавают
                
            if loc.id in ['loc_beach']:
                loc.addStatus(tan_status) # Загорают на пляже
                loc.addStatus(voleyball_status) # Играют в волейбол на пляже
            
            if loc.id in ['loc_gym']:
                loc.addStatus(football_status) # Играют в футбол в спортзале
                
            if loc.id in ['loc_changeRoom']:
                loc.addStatus(undress_status) # Переодеваются в раздевалке
                
            if loc.id in ['loc_doctor']:
                loc.addStatus(medexam_status) # Проходит медосмотр
                
            if 'classroom' in loc.position:
                if lt() > 0:
                    loc.eraseStatuses() # Сносим статусы
                    loc.addStatus(hidden_mastur)        # Скрытно дрочить
                    loc.addStatus(learnSelector(),50)   # Выбор уроков
                    loc.addStatus(teach_status)         # Учитель учит
                else:
                    loc.removeStatus(learnSelector())   # Сносим учёбу
                    loc.removeStatus(teach_status)      # Сносим обучение
                if loc.id in ['loc_class2'] and lt() <= 0:
                    if 'manec' in school.furniture:
                        loc.addStatus(manec1_status)    #
                        loc.addStatus(manec2_status)    # Развлекалово с манекеном
                        loc.addStatus(manec3_status)    #
                if loc.id in ['loc_class3'] and lt() <= 0:
                    if 'dildo' in school.furniture:
                        loc.addStatus(dildo1_status)    #
                        loc.addStatus(dildo2_status)    # Развлечения с игрушкой
                        loc.addStatus(dildo3_status)    #
                if loc.id in ['loc_class5'] and lt() <= 0:
                    if 'video' in school.furniture:
                        loc.addStatus(video_status)     # Просмотр порно
            if loc.id == 'loc_teacherRoom':                 # для учительской
                loc.addStatus(pre_teach_status)        # Готовится к занятию
            if loc.id == 'loc_doctor':
                loc.addStatus(medexam_status)
    statusDistribution()

    
label status_wc: # Complete
    if interactionObj.getSex() == 'female':
        show expression 'pic/status/pee_female.png'
    elif interactionObj.getSex() == 'male':
        show expression 'pic/status/pee_male.jpg'
    else:
        show expression 'pic/status/pee_futa.png'
    interactionObj.say 'А можно я пописаю в одиночестве, а?'
    $ interactionObj.incLoy(-1)
    $ move(curloc)
    
label status_swim: # Complete
    if interactionObj.getSex('mf') == 'female':
        show expression 'pic/status/swim_female.jpg'
        '[interactionObj.name] купается. Вам не докричаться до неё.'
    else:
        show expression 'pic/status/swim_male.png'
        '[interactionObj.name] плавает. Вам не докричаться до него.'
    $ move(curloc)
    
label status_hidden_mastur: # Complete
    if curloc in ['loc_wcf','loc_wcm']:
        if interactionObj.getSex() == 'futa':
            show expression 'pic/status/futa_toilet_mastur.jpg'
            interactionObj.say 'Чёрт, простите, я не, О-о-ох.'
            '[interactionObj.name] уже не в силах остановиться, её тело трясёт, а рука быстро двигается вдоль члена.'
            'Вы видите, как футу скручивают спазмы, и из её члена вырываются густые струи спермы, покрывая унитаз белыми каплями.'
            interactionObj.say 'Зачем вы так, ну зачем?'
            'Закрыв лицо, девочка убегает.'
            $ interactionObj.incLoy(-5)
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
                    $ interactionObj.incLoy(-5)
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
                    'Вы прикрываете дверь, и из-за неё слышутся приглушённые стоны и судорожное шуршание ног по полу. Похоже, что у девочки всё получилось!'
                    $ interactionObj.moveToLocation(choice(locations).id)
        else:
            show expression 'pic/status/male_toilet_mastur.png' as tempPic
            interactionObj.say 'О, да, [player.fname], пососи его вот так, детка!'
            'С этими словами и вашим именем на устах, парень выпускает из своего члена длинную струйку спермы прямо на пол.'
            'Вы поспешно уходите, прежде чем вас замечают.'
            $ interactionObj.moveToLocation(choice(locations).id)
        $ move('loc_secondFloor')
    else:
        if interactionObj.getSex() == 'male':
            show expression 'pic/status/male_class_mastur.jpeg' as tempPic
            'Не обращая ни на кого внимания (кроме, разве что, своей симпатичной соседки), [interactionObj.name] ласкает своего дружка прямо во время занятий!'
            'Вы уже хотели сделать ему замечание, но лёгкий стук капель по полу известил вас, что всё уже кончено. Удовлетворённый мальчишка, сбросивший мучавшее его напряжение вновь вернулся к занятиям.'
        elif interactionObj.getSex() == 'female':
            show expression 'pic/status/female_class_mastur.jpg' as tempPic
            '[interactionObj.fname] мелко взрагивает, кончая прямо на уроке, с её губ срывается лёгкий стон, который остаётся незамечанным всеми, кроме вас.'
        else:
            show expression 'pic/status/futa_class_mastur.jpg' as tempPic
            'Вы только и успеваете заметить, как [interactionObj.fname] вздрагиает и убирает руку от юбки, по которой расплывается влажное пятно спермы.'
    $ changetime(10)
    $ player.incLust(15)
    $ move(curloc)
    
label status_mastur: # Complete
    if interactionObj.getSex() == 'female':
        'Со всех сторон слышны крики: "Давай, ты сможешь ещё один, давай же!"'
        show expression 'pic/status/female_mastur.png' as tempPic
        interactionObj.say 'Ах, нет, я больше не могу, о-о-о!!!'
        'С громким стоном девушка начинает кончать, и из её вагины один за другим выталкиваются фломастеры и карандаши, которые она в пылу страсти запихала в себя.'
        'По полу растекается пахучая жидкость женских выделений.'
        $ interactionObj.moveToLocation(choice(locations))
    elif interactionObj.getSex() == 'male':
        show expression 'pic/status/male_mastur.png' as tempPic
        '[interactionObj.name], мало кого стесняясь, начинает прибирать за собой после обильного семяизвержения.'
        $ interactionObj.moveToLocation(curloc)
    else:
        show expression 'pic/status/futa_mastur.jpg' as tempPic
        interactionObj.say 'Всё, я больше не могу этого терпеть!'
        'С этими словами, девушка достаёт из сумки розовый и продолговатый предмет и спешно снимает с себя трусики, под которыми оказывается торчащий колом член.'
        '[interactionObj.name], дрожа от нетерпения, засовывает свой член в узенькую дырочку искусственной вагины. Её лицо искажает сладострастие, и, активно двигая бёдрами и руками, девочка начинает трахать свою игрушку.'
        'Движения ученицы становятся всё дёрганнее и нетерпеливей, и вот уже первая струйка спермы вырывается с кончика пениса, звонко плюхаясь на пол.'
        '[interactionObj.fname] ещё вздрагивает пару раз и неспеша упаковывает свою игрушку в портфель.'
        $ changetime(10)
    $ player.incLust(15)
    $ move(curloc)
    
label status_public_mastur: # Incomplete. Futa, male.
    if interactionObj.getSex() == 'female':
        show expression 'pic/status/female_public_mastur.jpg' as tempPic
        '[interactionObj.fname] мастурбирует, сидя на лавочке. Она совершенно никого не стесняется, и из её молодой киски капают соки, заливая злополучное место для для отдыха и асфальт.'
        menu:
            'Поставить её на место':
                player.say '[interactionObj.name]! Чем это ты тут занимаешься?!'
                interactionObj.say 'Да так, то тем, то этим, - не отвлекаясь от своего занятия, сообщает вам ученица.'
                player.say 'А ну, немедленно прекрати! Люди же смотрят!'
                interactionObj.say 'Да я уже сейчас, ммм...'
                'Ученица громко стонет, её тело напрягается, и из влагалища вырываются последние струйки влаги, возвещающие о только что пережитом оргазме. Немного посидев с закрытыми от удовольствия глазами, [interactionObj.fname] одевается и уходит, заканчивая представление.'
                'Некоторые люди по достоинству оценили то, что вы хотя бы попытались остановить девушку. А вот она - нет.'
                $ interactionObj.incLoy(-5)
                $ interactionObj.incRep(5)
            'Ничего не делать':
                'Немного поглазев на развратную девушку, вы пожимаете плечами, как будто ничего не происходит, и идёте дальше по своим делам.'
                'За вашей спиной раздаётся громкий стон и ругань мимо проходящих мамаш, которым это зрелище не очень-то и нравится.'
                $ interactionObj.moveToLocation(choice(locations))
    else:
        '[interactionObj.name] публично дрочит.' # У меня нет пика на этот случай.
    $ changetime(10)
    $ player.incLust(15)
    $ move(curloc)
    
label status_voleyball: # Complete
    show expression 'pic/status/volleyball.jpg' as tempPic
    '[interactionObj.name] играет с другими ребятами в пляжный волейбол. Вы не хотите мешать.'
    $ move(curloc)
    
label status_football: # Complete
    show expression 'pic/status/football.jpg' as tempPic
    '[interactionObj.name] играет с другими ребятами в футбол. Вы не хотите мешать.'
    $ move(curloc)
    
label status_kiss: # Complete
    if interactionObj.getSex('mf') != interactionObj.partner.getSex('mf'):
        show expression 'pic/status/kiss_getero.jpg' as tempPic
    else:
        if curloc in ['loc_pool','loc_beach']:
            show expression 'pic/status/kiss_yuri_pool.png' as tempPic
        else:
            show expression 'pic/status/kiss_yuri.png' as tempPic
    '[interactionObj.name] и [interactionObj.partner.name] целуются. Вы недолго постояли, надеясь что они перейдут к более активным действиям, но нет. Не перешли.'
    $ changetime(10)
    $ player.incLust(5)
    $ move(curloc)

label status_undress: # Complete
    if interactionObj.getSex() == 'male':
        show expression 'pic/status/boy_undress.png' as tempPic
        '[interactionObj.name] просит вас не мешать переодеваться.'
    elif interactionObj.getSex() == 'female':
        show expression 'pic/status/girl_undress.png' as tempPic
        '[interactionObj.name] просит вас не мешать переодеваться.'
    else:
        show expression 'pic/status/futa_undress.png' as tempPic
        '[interactionObj.name] просит вас не мешать переодеваться.'
        'Вы почему-то никак не можете выбросить её эрегированный член из головы. Это ведь так естествнно. Или нет?'
        $ player.incLust(5)
    $ move(curloc)
    
label status_useManec: # Complete
    if interactionObj.getSex() == 'male':
        show expression 'pic/status/male_manec.png' as tempPic
        '[interactionObj.name] активнейшим образом изучает внутреннее устройство женского организма, путём введения своего щупа непосредственно в искусственное влагалище купленного вами манекена.'
    elif interactionObj.getSex() == 'female':
        show expression 'pic/status/female_manec.png' as tempPic
        'Не сдержавшись, [interactionObj.name] всё таки решила испробовать столь подробно описанный на уроках биологии мужской орган. И сейчас, слегка напрягаясь от вхождения точной копии члена в свою киску, она осторожно неумело двигает бёдрами, пытаясь доставить себе удовольствие.'
        'Через минутку движения становятся более естественными. Похоже, что смазанный членозаменитель перестал доставлять ученице дискомфорт.'
        'По классу разносятся влажные хлюпания истекающей смазкой киски. [interactionObj.fname] прикрывает глаза, полностью отдаваясь наслаждению.'
        show expression 'pic/status/female_manec_cum.png' as tempPic
        'Ого! Похоже, анатомичность манекена просто зашкаливает!'
        'Просто в момент, когда стенки влагалища девчушки начали сокращаться в оргазме, копия детородного органа незамедлительно выпустила из себя заменитель спермы, чем удивила и вас, и учениицу.'
        $ interactionObj.moveToLocation(choice(locations).id)
    else:
        show expression 'pic/status/futa_maneca.jpg':
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        'Вы видите, как [interactionObj.fname], отделив голову манекена, плюёт ему в рот и тут же вводит в открытый рот свой торчащий от возбуждения член.'
        'Её рот приоткрывается в экстазе, а движения становятся всё глубже и учащённей. Взирая на это, вы всерьёз начинаете опасаться, не будет ли после этого у манекена вечно удивлённое выражение с незакрывающимся ртом в виде буквы О. Но вспомнив для каких целей вы их приобрели, вы успокаиваетесь.'
        'Чего нельзя сказать о девушке. Она, наоборот, возбуждается всё сильнее, двигая бёдрами с такой силой и скоростью, словно пытается пронзить манекен насквозь. Вы видите, что теперь он увлажнён не только первоначальным плевком, но и выделенной подрагивающим членом смазкой.'
        'Между ног ученицы ритмично покачивается капелька с её женского начала. Немного сменив ракурс, вы замечаете блестящие половые губки и слегка сокращающуюся вагину. Вы готовы поставить 100 монет на то, что в ближайшие пару секунд она кончит.'
        show expression 'pic/status/futa_maneca.jpg':
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        interactionObj.say 'Да! Да! Да!'
        'Спина девушки изгибается в оргазме, до упора засаживая член в рот несчастному предмету обстановки. Её язычок вываливается от экстаза, и по подбородку начинает стекать струйка слюны. Из губ манекена вырываются белые капли, разбрызгиваясь вокруг. Видимо, он всё таки не совсем предназначен для подобных развлечений.'
        'Вы строго наказываете девушке прибраться за собой, чтобы в очередной раз не шокировать уборщицу. Удовлетворённая ученица кивает.'
    $ player.incLust(5)
    $ changetime(10)
    $ move(curloc)
    
label status_useDildo: # Complete.
    if interactionObj.getSex() == 'female':
        show expression 'pic/status/female_toy.png' as tempPic
        '[interactionObj.name] тестирует вибратор, про который столько долго рассказывали на уроках секспросвета.'
        'Капельки пота, забавное жужжание и открытый в экстазе рот доказывают, что на уроках не врали.'
    elif interactionObj.getSex() == 'futa':
        show expression 'pic/status/futa_toya.jpg':
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        '[interactionObj.name] решила примерить несколько игрушек в обилии разбросанных по классу. Она запихала в кондом три небольших вибратора и натянула получившуюся конструкцию на свой член. С виду получилась довольно неплохо, но [interactionObj.fname] сидит, так и не решаясь её включить.'
        'Наконец, девушка решается, и её пальцы тянутся к заветным регуляторам.'
        show expression 'pic/status/futa_toyb.jpg':
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        'Класс наполняет тихое жужжание, а на лице девушки читается неподдельное удивление от интенсивности стимуляции её полового органа.'
        'Член мгновенно подпрыгивает к парте, упираясь в неё головкой, и вы даже со своего места можете видеть, как он напряжён.'
        interactionObj.say 'М-м-м, - срывается тихий стон с губ футы.'
        'Она неосознанно начинает совершать поступательные движения бёдрами, водя головкой по парте, но так и не касается его руками. Через пару минут стонов и закатывания глаз, девушка начинает регулярно вздрагивать, и с кончика её пениса срывается первая маленькая струйка спермы.'
        show expression 'pic/status/futa_toyc.jpg':
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        'Вскоре к первой струйке присоединяется вторая, и вот уже член бешенно пульсирует, стукаясь головкой об парту и наполняя средство контрацепции бурными потоками спермы. [interactionObj.fname] чудом не вскрикивает на всю школу, закусывая нижнюю губу от сладострастия.'
        'Вы довольно улыбаетесь, наслаждаясь увиденными моментами.'
    else:
        show expression 'pic/status/male_toy.jpg':
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        'Крепко сжав своё мужское достоинство через резиновую вагину, [interactionObj.name] применяет на практике теорию из уроков секспросвета. Вы дожидаетесь брызг спермы с одной из выходной дырочки вагины и удовлетворённо киваете, словно подтверждая, что урок усвоен.'
    $ changetime(10)
    $ player.incLust(5)
    $ move(curloc)
    
label status_teacherHidden_mastur: # Complete
    if interactionObj.getSex() == 'male':
        show expression 'pic/status/ahmed_mastur.png' as tempPic
        'Заглянув в мужскую кабинку, вы увидели, как Ахмед пытается снять накопившееся за день напряжение. Вы засматриваетесь на его мускулистое тело и плавные движения руки, втайне мечтая присоединиться к этому празднику сластолюбия.'
        interactionObj.say 'Ээх, бабубы.... - вздыхает физрук и, слегка вздрагивая, роняет капли спермы на ободок унитаза.'
    elif interactionObj.getSex() == 'futa':
        show expression 'pic/status/futa_teacher_mastur.jpg' as tempPic
        'Услышав стоны из кабинки, вы решили в неё заглянуть. К вашему удивлению, это оказалась не одна из ваших учениц, как обычно, а одна из ваших учительниц.'
        '[interactionObj.name] сидела на унитазе и, широко раздвинув ноги, буквально трахала собственную руку. Пальцы учительницы были все перемазаны в выделившемся с кончика головки эякуляте, но вытирать их она и не думала.'
        'Плотно обхватив свой мужской орган, столь органично смотряшийся на женском теле, [interactionObj.fname] вращательными движениями ласкала красную от возбуждения головку.'
        interactionObj.say 'М-м-м, как хорошо! Как же я долго ждала окончания этого чёртового урока!'
        'Движения руки становились всё беспорядочней и быстрее, и вдруг, выгнувшись дугой и чуть не свалившись с унитаза, учительница исторгла из себя громкий стон и несколько струй спермы. Тяжело дыша, она откинулась на бачок и начала приводить себя в порядок.'
    else:
        'Вы услышали сдавленные стоны из ближайшей кабинки.'
        show expression 'pic/status/female_teacher_mastur.png' as tempPic
        '[interactionObj.name] сидела на унитазе, запустив свою руку в трусики. Вообще, это довольно необычное явление, когда на унитазе сидят не снимая нижнего белья. Но в данном случае унитаз выступал не по прямому назначению, а в качестве подпорки под пятую точку, дабы не свалиться на пол от удовольствия.'
        'Тем временем движения руки и дыхание учительницы всё учащалось, и на трусиках уже появилось влажное пятнышко, сигнализирующее о пике возбуждения и приближении развязки данного развратного акта.'
        interactionObj.say 'О боже, кажется я сейчас кончу!'
        interactionObj.say 'Кончу прямо в школьном туалете, как какая-то развратная шлюшка!'
        interactionObj.say 'Я, я, я к-о-о-ончаю!!!!'
        '[interactionObj.fname] несколько раз дёрнулась, плотно прижимая руку к своей киске, и затихла, восстанавливая дыхание.'
    'Вы поспешно ретируетесь, чтобы вас не заметили.'
    $ player.incLust(5)
    $ changetime(10)
    $ move(prevloc)
        
    
label status_watchVideo: # Incomplete. Add more Video.
    show expression 'pic/status/video_porn1.jpg' as tempPic
    '[interactionObj.name] смотрит порно с обилием больших членов, спермы и миловидных личиков.'
    'Вы ненадолго тоже задерживаете свой взгляд на экране. Действительно, все диалоги происходят на английском. Правда, их немного.'
    $ player.incLust(10)
    $ move(curloc)
    
label status_hidden_sex: # Complete
    if (interactionObj.getSex() == 'male' and interactionObj.partner.getSex() == 'female') or (interactionObj.getSex() == 'female' and interactionObj.partner.getSex() == 'male'):
        python:
            if interactionObj.getSex() == 'male':
                st2 = interactionObj
                st1 = interactionObj.partner
            else:
                st1 = interactionObj
                st2 = interactionObj.partner
        'Вас привлёк странный хлюпающий звук из одной кабинки. Вы решили заглянуть в неё.'
        'Зайдя в соседнюю кабинку, вы опустились на колени, чтобы удовлетворить своё любопытство.'
        show expression 'pic/status/getero_sex.png' as tempPic
        'На ваших глазах, [interactionObj.name] и [interactionObj.partner.name] самозабвенно совокуплялись буквально в полуметре от вас.'
        'Вы даже не удивились, поняв, что причина привлёкших вас звуков - влажная киска ученицы, в которую, словно молотом, забивал свой член парень.'
        st2.say 'О, да! Давай, сжимай его сильнее! Твоя киска такая узенькая, словно свёрнутое в рулон полотенце! - мальчик сделал сомнительный комплимент своей девушке.'
        st1.say 'Заткнись! М-м-м! Дурак!'
        'Движения парня ускорились, и вытекающий из маленькой щёлки сок стал разбрызгиваться вокруг.'
        st2.say 'Д-а-а-а! Словно я трахаю горячий мамин пирог! - ученик явно не испытывал недостатка в фантазиях.'
        st1.say 'О-а-о-а! - в такт его движениям стонала [st1.fname], - З-а-а-т-к-н-и-сь наконец-то!'
        st1.say 'Д-д-д-у-р-а-ш-к-а-а-а-а-а!'
        'Последнее слово ученицы перешло в крик, её тело задрожало в оргазме и безвольно обмякло в руках парня.'
        'Вы тихонько собрались и вышли из туалета.'
    elif (interactionObj.getSex() == 'futa' and interactionObj.partner.getSex() == 'female') or (interactionObj.getSex() == 'female' and interactionObj.partner.getSex() == 'futa') or (interactionObj.getSex() == 'futa' and interactionObj.partner.getSex() == 'futa'):
        python:
            if interactionObj.getSex() == 'futa':
                st2 = interactionObj
                st1 = interactionObj.partner
            else:
                st1 = interactionObj
                st2 = interactionObj.partner
        st1.say 'Ну же, [st2.name], кончай скорее, я не могу провести весь день с тобой в туалете! - услышали вы шёпот из кабинки.'
        player.say '"Я должна это видеть!"'
        show expression 'pic/status/futa_female_sex.png' as tempPic
        'Вы немного приоткрыли дверцу и стали наблюдать за происходящим.'
        '[st1.fname] и [st2.fname] предавались ласкам в туалете. Ну как предавались. Очевидное удовольствие от процесса получала только [st2.fname], [st1.fname] в свою очередь всячески поторапливала подружку.'
        st1.say 'Ну долго ты там ещё? - ручка девушки, обхватывающая пенис подружки, задвигалась чуть быстрее, и, кажется, нажим слегка усилися. По крайней мере, глаза футы начали закатываться от удовольствия.'
        st2.say 'Да, вот так, не останавливайся пожалуйста!!!'
        st1.say 'Да у меня рука счас отнимется уже! - в сердцах воскликнула ученица, но всё таки нашла в себе силы ускорить движения ещё чуть-чуть.'
        st2.say 'Я, я, я о-о-о-о-о!!!'
        '[st2.fname] задрожала, сильно вжимаясь попой в живот своей подружки, и с её члена начали вылетать крупные капли густой спермы, покрывающие ободок и бачок унитаза.'
        st1.say 'О, сегодня вроде как гуще, чем обычно! - хихикнула девушка, облизывая перемазанные в белой жидкости пальцы.'
        st1.say 'Да и на вкус, кажется, неплохо!'
        st2.say 'Ты, ты меня смущаешь, [st1.fname], - тяжело дыша, зарделась фута.'
        'Вы решили не показываться на глаза этой мило щебечущей парочке и осторожно покинули туалет.'
    elif (interactionObj.getSex() == 'futa' and interactionObj.partner.getSex() == 'male') or (interactionObj.getSex() == 'male' and interactionObj.partner.getSex() == 'futa'):
        python:
            if interactionObj.getSex() == 'futa':
                st2 = interactionObj
                st1 = interactionObj.partner
            else:
                st1 = interactionObj
                st2 = interactionObj.partner
        st2.say 'Давай милый, вставь его прям туда!'
        'Вам непременно захотелось посмотреть, что и куда "милый" будет вставлять. Ради этого вы подкрались к одной из кабинок и заглянули в неё.'
        show expression 'pic/status/futa_male_sex.png' as tempPic
        st1.say 'О, Боже! Какая ты там узкая и горячая!'
        'В ответ на его движение девушка вскрикнула от удовольствия и положила обе руки себе на член, начиная его ласкать.'
        'К вашему удивлению, парень решил воспользоваться вовсе не той дырочкой, о которой вы подумали вначале. С другой стороны, если это обоим доставляет удовольствие, то почему бы и нет?'
        st2.say 'О, как же хорошо! Ты так глубоко в меня входишь! - девушка активно помогала своему парню, пытаясь двигать попкой в то время, пока он держал её на руках.'
        'Движения молодых людей вошли в унисон, и, тесно прижавшись друг к другу, они слились в поцелуе.'
        st2.say 'Возьми его в руку! - томно попросила фута.'
        st1.say 'Что?'
        st2.say 'Подрочи мне! Я сейчас кончу!'
        show expression 'pic/status/futa_male_sex_cum.png' as tempPic
        'Положив девушку на пол, [st1.name] схватился за её пенис и, не останавливая свои движения в её узеньком анусе, начал ласкать покрасневшую и сочащуюся преэякулятом головку.'
        st2.say 'КОНЧАЮ!!!! - закричала фута, и её собственное семя начало покрывать живот, грудь и лицо.'
        st1.say 'Я, я тоже! - судорожно выдохнул парень, и вы заметили, как его член запульсировал в тугой дырочке.'
        'Вы осторожно вышли из туалета.'
    elif interactionObj.getSex() == 'female' and interactionObj.getSex() == interactionObj.partner.getSex():
        $ st1 = interactionObj
        $ st2 = interactionObj.partner
        st1.say '[st2.fname], я тебя хочу!'
        'От этого милого голосочка по вашей коже незамедлительно побежали мурашки, и вы прильнули к щели ближайшей кабинки, чтобы рассмотреть происходящее.'
        show expression ('pic/status/yuri_sex.jpg'):
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        st1.say 'Ох, - выдохнула девушка, скользя своей киской по ляжке подруги, - Ты меня так заводишь! Поласкай мои дырочки!'
        st2.say 'Ах ты маленькая проказница!'
        '[st2.fname] опустила свои руки к упругой попке подруги и пальчиками принялась ласкать маленькие дырочки, чем вызвала полный вожделения стон из уст любовницы.'
        st1.say 'Да, вот так!'
        'Ловкие пальчики девушки погружались в текущую от возбуждения щёлку,  вторая рука подбиралась к сморщенному колечку ануса.'
        st1.say 'Что ты со мной делаешь?'
        '[st1.fname] прильнула к своей подружке, еще сильнее прижимаясь клитором к скользкой от её соков ноге, и, вздрагивая, насаживалась на шаловливые пальчики.'
        st1.say 'Я сейчас кончу! - движения девушки стали беспорядочней, она всё активней тёрлась своей киской о нежную кожу подружки.'
        st2.say 'Кончай! - шепнула [st2.fname] ей на ушко, и к двум пальчикам в киске присоединился третий.'
        st1.say 'И-и-и-и-и, - [st1.fname] тихонько запищала, и, сжав покрепче своими бёдрами ножку любовницы, начала кончать.'
        'Не желая быть замеченной этими двумя, вы вышли из туалета.'
    else:
        me 'В теории ты попал на яой, но я как-то не люблю это дело, и, по идее, ты даже увидеть этого сообщения не должен.'
    $ player.incLust(5)
    $ changetime(10)
    $ move(prevloc)
    
label status_sex: # Complete
    if (interactionObj.getSex() == 'male' and interactionObj.partner.getSex() == 'female') or (interactionObj.getSex() == 'female' and interactionObj.partner.getSex() == 'male'):
        python:
            if interactionObj.getSex() == 'male':
                st2 = interactionObj
                st1 = interactionObj.partner
            else:
                st1 = interactionObj
                st2 = interactionObj.partner
        show expression 'pic/status/getero_school_sex.jpg' as tempPic
        'Молодая пара совокуплялась прямо на ваших глазах, слабо обращая внимания на окружающих. Они были полностью погружены в чувства друг друга. И не только.'
        'С влажным хлюпанием [st2.name] доставал свой член из щёлки подруги и вгонял его назад. Ритмичные движения его бёдер и громкие стоны ученицы заставили облизать вас губы от вожделения.'
        st1.say 'Трахай меня, [st2.fname], вытрахай из меня всю похоть! Дааа!'
        'И парень продолжал трахать, невзирая ни на что. Темп его движений всё возрастал, хлюпания и стоны становились всё громче.'
        st2.say 'Внутрь или наружу? - спросил [st2.fname], ни на секунду не останавливая движений.'
        st1.say 'В меня! Я хочу, чтобы ты кончил в меня!'
        show expression 'pic/status/getero_school_sex_cum.jpg' as tempPic
        'Парень перевернул девушку и с рычанием снова вогнал свой пенис в её истекающее влагой лоно.'
        st1.say '[st2.fname]! Я кончаю, [st2.fname]! [st2.fname]! Да-а-а-а-а!'
        '[st1.fname] выгнулась всем телом, крепко обхватив любовника ногами за поясницу. Вы видите, как её киска исторгает из себя просто ненормальные объёмы влаги перемешанные со спермой.'
    elif (interactionObj.getSex() == 'futa' and interactionObj.partner.getSex() == 'female') or (interactionObj.getSex() == 'female' and interactionObj.partner.getSex() == 'futa'):
        python:
            if interactionObj.getSex() == 'futa':
                st2 = interactionObj
                st1 = interactionObj.partner
            else:
                st1 = interactionObj
                st2 = interactionObj.partner
        show expression 'pic/status/school_futa_female_suck.jpg' as tempPic
        st2.say 'Ты что творишь? Не можешь дождаться до дома?'
        st1.say 'Да мне всё равно, я хочу твой член прямо здесь и сейчас!'
        'С этими словами [st1.fname] быстренько достала уже напряжённый член подружки и с причмокиванием поместила его свой рот.'
        st2.say 'Ну может не надо? О-о-о-о, нет, я не могу сопротивляться твоему язычку!'
        '[st1.fname] продолжала мерно качать головой, не выпуская члена изо рта. Из уголка её губ стекала капля слюны по уже блестящему от влаги стволу.'
        st2.say 'Всё! Я больше не могу!'
        show expression 'pic/status/school_futa_female_sex.jpg' as tempPic
        '[st2.fname] схватила подругу и, перевернув её на спину, вошла в узенькую щёлку без прелюдий.'
        st1.say 'Стой! Я ещё не готова!'
        'Не обращая никакого внимания на слова, доносящиеся снизу, [st2.fname] продолжала вбивать свой недетский орган в горячее лоно. С влажного от слюней члена начали капать густые капли смазки.'
        st2.say 'Как же хорошо!'
        st1.say 'Да! Да! Да! Не останавливайся, [st2.fname]! Только не останавливайся!'
        'Фута задрала ножки подруги ещё выше и, уперевшись руками в бёдра, резко увеличила темп и амплитуду движений. Теперь стало сложно уследить за резкими движениями члена, но было видно, как на нём набухла синяя венка, предвещающая скорый оргазм.'
        show expression 'pic/status/school_futa_female_cum.jpg' as tempPic
        st1.say 'Я сейчас кончу, кончу, не останавливайся, кончу! КОНЧАЮ!!!'
        'В ответ на усиленную стимуляцию члена пульсирующей в оргазме киской, [st2.fname] вздрогнула и, засадив пенис поглубже, разрядилась в глубине влагалища. Не поместившееся в нём семя начало стекать с краёв щёлки.'
        'Не решаясь двигаться, подруги слились в долгом поцелуе.'
    elif (interactionObj.getSex() == 'futa' and interactionObj.partner.getSex() == 'futa'):
        python:
            st1 = interactionObj
            st2 = interactionObj.partner
        show expression ('pic/status/school_futa_futa_sex.jpg'):
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        st2.say '[st1.fname], только не в меня, не в этот раз, пожалуйста!'
        '[st1.fname] и [st2.fname] предавались ласкам, если, конечно, так можно назвать полное проникновение члена одной в киску своей подружки.'
        '[st1.fname] дрожала от напряжения, почти не двигаясь, и судорожно раздумывала, куда бы ей спустить. Безусловно, вытаскивать свой напрягшийся пенис из влажной пещерки ей не хотелось в любом случае, но и расстраивать подругу не хотелось тоже.'
        st1.say 'Хорошо, я попробую... - девушка начала медленно вытаскивать поблёскивающий ствол члена до тех пор, пока не показалась головка слегка прикрытая лепестками влажных губ.'
        'Не успев завершить начатое, пенис внезапно запульсировал и вырвался из влагалища, с каждым толчком тыкаясь в губки и орошая их белым семенем.'
        st2.say 'Ну вот, теперь опять кидкиллер покупать... - вздохнула фута и принялась вытирать салфетками свою перемазанную спермой щёлку.'
    elif (interactionObj.getSex() == 'futa' and interactionObj.partner.getSex() == 'male') or (interactionObj.getSex() == 'male' and interactionObj.partner.getSex() == 'futa')  or development == 1:
        python:
            if interactionObj.getSex() == 'futa':
                st2 = interactionObj
                st1 = interactionObj.partner
            else:
                st1 = interactionObj
                st2 = interactionObj.partner
        st2.say 'Я хочу его прямо в себе!'
        st1.say 'А я сегодня и не против! Садись!'
        show movie
        play movie 'pic/status/school_futa_male_sex1.webm' loop
        'Не особо переживая насчёт окружающих, [st2.fname] быстренько приподняла юбку, на секунду засветив свой небольшой член, и с томным вздохом впустила в себя трепещущее достоинство парня.'
        st2.say 'Вот так, милый, не спеши, дай мне насладиться им полностью! О, как же хорошо! Ты такой большой! Мне так нравится, когда твоя головка раздвигает стеночки моей киски!'
        'Пара неспеша двигалась, но постепенно темп увеличивался и увеличивался.'
        play movie 'pic/status/school_futa_male_sex2.webm' loop
        st2.say 'Да! Да! Вот так! Дай мне почувствовать себя настоящей женщиной! Трахай мою киску! ДА!'
        'От удовольствия и тяжёлого дыхания розовый язычок девушки вывалился из рта, покачиваясь в такт толчкам ученика.'
        '[st1.fname] рывками насаживал текущую киску на свой член, не обращая внимания на трущийся о его живот причиндал футы-подружки.'
        st1.say 'Кончу! Сейчас кончу!'
        st2.say 'В меня, милый! Заполни меня своим горячим молочком!'
        play movie 'pic/status/school_futa_male_sex3.webm' loop
        'Спустя секунду до вас донёсся крик экстаза оргазмирующих учеников. Сперма парня толчками выплёскивалась из отверстия в головке, наполняя пульсирующую киску обжигающей влагой.'
        st1.say 'Чёрт! Ты опять обкончала мне весь живот!'
        st2.say 'Ну не сердись, дорогой! Держи салфетку!'
        stop movie
        hide movie
    elif interactionObj.getSex() == 'female' and interactionObj.getSex() == interactionObj.partner.getSex():
        $ st1 = interactionObj
        $ st2 = interactionObj.partner
        show expression 'pic/status/school_yuri_sex.png' as tempPic
        st1.say 'Не смотри, [st2.fname], я стесняюсь!'
        '[st1.fname] лежала на спине раскинув ноги. Её блестящая от возбуждения киска была видна всем окружающим.'
        st2.say 'Я не могу не смотреть на такую красоту! - ответила ей подружка, поглаживая пальчиками трепещущие губки и набухший клитор.'
        st2.say 'М-м-м! А какой запах! Так и не терпится попробовать её на вкус!'
        'Не разделяя слово и дело, [st2.fname] сразу прильнула губками к розовому бутончику, вызвав у подруги страстный стон.'
        st1.say 'Что ты делаешь! Ну не при всех же! - попыталась отодвинуться [st1.fname]'
        st2.say 'Да кому какое дело! - отмахнулась от неё ученица и снова запорхала язычком по сладкой щёлке.'
        'Её рука опустилась вниз, к своей киске, и шаловливые пальчики сразу нырнули в мокрую пещерку.'
        st1.say 'Ах, как хорошо! [st2.fname] иди сюда, я тоже хочу тебя поласкать!'
        'Спустя секунду ученицы приняли позу 69 и с энтузиазмом начали вылизывать и ласкать друг друга пальчиками. Но это не продлилось слишком долго.'
        show expression 'pic/status/school_yuri_cum.png' as tempPic
        st1.say '[st2.fname]! Я кончаю!'
        st2.say 'Я тоже, [st1.fname]!'
        'Бурный оргазм сотряс молодые тела и киски. Из них выплеснулась выталкиваемая пульсациями влагалища влага, заливая всё вокруг проказниц, и, тяжело дыша, девушки повалились друг на друга.'
    else:
        me 'Тут тип яой или ошибка. В любом случае, в нормальной игре попасть сюда нельзя.'
    $ player.incLust(15)
    $ changetime(10)
    $ move(curloc)
    
label status_public_sex: # Incomplete. Male-futa. Female-futa. Futa-futa. Female-Female.
    if (interactionObj.getSex() == 'male' and interactionObj.partner.getSex() == 'female') or (interactionObj.getSex() == 'female' and interactionObj.partner.getSex() == 'male'):
        python:
            if interactionObj.getSex() == 'male':
                st2 = interactionObj
                st1 = interactionObj.partner
            else:
                st1 = interactionObj
                st2 = interactionObj.partner
        show expression 'pic/status/public_getero_sex.png' as tempPic
        st1.say 'Да, [st1.fname], да! Трахни мою развратную попку! Сделай хорошо своей шлюшке!'
        'Вы немного шокированно смотрите на трахающуюся у всех на глазах парочку. Член парня упрямо вгрызался в поддатливое колечко ануса ученицы, издавая срамные звуки.'
        '[st1.fname] призывно оттопыривала попку, немного двигаясь навстречу пенису, а её пальчики теребили истекающую соком киску. Вы не уверены, но вам кажется, что парень уже не первый раз собирается кончить. По крайней мере, у вас нет другого объяснения тому, что ученица движениями своих пальцев выталкивает капли белесой жидкости прямо на асфальт.'
        menu:
            'Охладить их пыл':
                player.say 'Эй, вы! Что это вы там делаете, а? - грозно сдвинув брови, кричите вы совокупляющейся парочке.'
                'Кончаееем!!!! - хором ответили ученики, и из попки девчушки брызнули белые капли, покрывая её ножки и живот парня.'
                player.say 'А ну, быстро прекратите! А не то я полицию вызову!'
                st2.say 'Ладно, ладно, не кричите, - тяжело дыша бросил парень, - Уже уходим.'
                'Некоторые люди по достоинству оценили то, что вы хотя бы попытались остановить парочку. А вот она - нет.'
                $ interactionObj.incLoy(-15)
                $ interactionObj.incRep(5)
                $ interactionObj.partner.incLoy(-15)
                $ interactionObj.partner.incRep(5)
            'Ничего не делать':
                'Хмыкнув, вы пошли дальше, чтобы окружающие не дай бог не связали вас с этими любвеобильными молодыми людьми.'
    else:
        'Вы наблюдаете, как [interactionObj.name] и [interactionObj.partner.name] неистово спариваются у всех на глазах.'
    $ player.incLust(20)
    $ changetime(10)
    $ move(curloc)
