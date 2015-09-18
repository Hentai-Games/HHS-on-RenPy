label event_loc_class1_10_StartKupruvnaQuest:
    show class1
    python:
        global teacher_son, mile_qwest_2_stage
        if mile_qwest_2_stage > 0:
            skipEvent()
        mile_qwest_2_stage = 1
        teacher_son = getChar('male')
        
    show expression 'pic/locations/school/class1/no11.jpg' at top as tempPic
    kupruvna.say '[teacher_son.fname], это ты? -  расположившись на столе в очень интересной позе спросила вас учительница.'
    'Ваш взгляд мгновенно переместился под юбку учительницы. Белье было очень влажное, вы буквально чувствовали это.'
    kupruvna.say 'Ой, простите, - видя ваш ОЧЕНЬ удивлённый взгляд, смущенно сказала Валентина Купрувна, - просто я тут стол протирала, и [teacher_son.fname] должен был мне тряпку принести.'
    player.say 'Эмм, ладно, хорошо... - сказали вы, пятясь к двери.'
    'Интересно, что она и [teacher_son.fname] собиралась делать вместе? Надо бы исследовать этот вопрос поподробней. Только как нибудь незаметней.'
    $ move(curloc)
    
