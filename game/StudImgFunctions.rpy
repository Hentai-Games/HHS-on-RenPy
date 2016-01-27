init python:
    def getStudImg(char,*args):
        if char == player:
            anotherImage = player.picto

        if char in studs :
            if len(char.wear) == 0:
                anotherImage = 'pic/showStud/' + char.getSex('mf') + '/naked/00.png'
            else :
                top_covered = 0
                for x in char.wear:
                    if 'верх' in x.cover:
                        anotherImage = 'pic/showStud/' + char.getSex('mf') + '/'+ x.purpose + '/00.png'
                        top_covered = 1
                if  top_covered == 0 :
                    anotherImage = 'pic/showStud/' + char.getSex('mf') + '/underwear/00.png'

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

                    
        if args[0] == 'dialog':
            if char.name == player.name:
                return Image(anotherImage, xalign=0.2, yalign= 1.0, yanchor = 'center')
            else:
                return Image(anotherImage, xalign=0.8, yalign= 1.0, yanchor = 'center')
        
    def ImgList():
        lf = ''
        lm = ''
        lf += 'pic/showStud/female/naked/00.png\n'
        lm += 'pic/showStud/male/naked/00.png\n'
        lf += 'pic/showStud/female/underwear/00.png   \n'
        lm += 'pic/showStud/male/underwear/00.png\n'
        for x in clothing:
            if x.char == 'stud' and x.sex == 'female' and 'верх' in x.cover:
                lf += 'pic/showStud/female/'+ x.purpose + '/00.png\n'
            if x.char == 'stud' and x.sex == 'male' and 'верх' in x.cover:
                lm += 'pic/showStud/male/'+ x.purpose + '/00.png\n'
        return [lf, lm]