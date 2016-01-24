init python:
    import os
    def getStudImg(char,*args):
        if char == player:
            anotherImage = player.picto

        elif char.getSex() == 'male':
            anotherImage = 'pic/showStud/m_1.png'
        else:
            anotherImage = 'pic/showStud/fem/'
            wear_img_sel = 0
            if len(char.wear) == 0:
                anotherImage += 'naked/'
                wear_img_sel = 1
            else:
                for x in char.wear:
                    if 'Девчачий строгий пиджак' == x.name : 
                        anotherImage += 'norm/'
                        wear_img_sel = 1
                    if 'Девчачий пиджак' == x.name : 
                        anotherImage += 'norm/'
                        wear_img_sel = 1
                    if 'Простое платье' == x.name : 
                        anotherImage += 'norm/'
                        wear_img_sel = 1
            if wear_img_sel == 1 : 
                bsize = char.body.parts['грудь'].size
                if bsize > 0:
                    if bsize < 1: anotherImage += 'sm_br/'
                    elif bsize < 2: anotherImage += 'med_br/'
                    else : anotherImage += 'big_br/'
                anotherImage += '00.png'
            else :
                anotherImage = 'pic/showStud/f_1.png'

        if char.lname == 'Данокова':
            anotherImage = 'pic/teachers/danokova_1.png'
        elif char.lname == 'Фригидовна':
            anotherImage = 'pic/teachers/frigidovna_1.png'
        elif char.lname == 'Биссектрисовна':
            anotherImage = 'pic/teachers/bissektrisovna_1.png'
        elif char.lname == 'Диковна':
            anotherImage = 'pic/teachers/dikovna_1.png'
        elif char.lname == 'Купрувна':
            anotherImage = 'pic/teachers/kupruvna_1.png'
        elif char.lname == 'Мустангович':
            anotherImage = 'pic/teachers/mustangovich_1.png'
        elif char.lname == 'Данте':
            anotherImage = 'pic/teachers/dante_1.png'
        elif char.lname == 'Гонореевна':
            anotherImage = 'pic/teachers/gonoreevna_1.png'
        if len(args) == 0:
            return anotherImage

        elif args[0] == 'dialog':
            if char.name == player.name:
                return Image(anotherImage, xalign=0.2, yalign= 1.0, yanchor = 'center')
            else:
                return Image(anotherImage, xalign=0.8, yalign= 1.0, yanchor = 'center')
        
        
