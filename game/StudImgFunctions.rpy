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
        

        
    def getWearList(char):
        tmp_vis = ['none', 'none', 'none', 'none', 'none'] 
        if char.sex == 'male':
            tmp_vis[3] = NoVisstudpantiesM
        else:
            tmp_vis[2] = NoVisstudSlip
            tmp_vis[3] = NoVisstudpantiesF
        tt = []
        
        tt = [e for e in char.wear if 'верх' in e.cover]
        if len(tt) == 1 :
            tmp_vis[0] = tt[0]
            if 'грудь' in tmp_vis[0].cover:
                tmp_vis[2] = 'none'
            if 'попа' in tmp_vis[0].cover:
                tmp_vis[3] = 'none'
        tt = [e for e in char.wear if ('низ' in e.cover) and (not e in tmp_vis)]
        if len(tt) == 1 :
            tmp_vis[1] = tt[0]
            if 'попа' in tmp_vis[1].cover:
                tmp_vis[3] = 'none'

        if tmp_vis[2] != 'none' and (tmp_vis[0] == 'none' or tmp_vis[0].purpose in ['bdsm', 'sexy', 'skimpy']):
            tt = [e for e in char.wear if 'грудь' in e.cover]
            if len(tt) == 1 :
                tmp_vis[2] = tt[0]
            else: 
                tmp_vis[2] = NostudSlip

        v_tmp = (tmp_vis[1] != 'none' and not tmp_vis[1].purpose in ['bdsm', 'sexy', 'skimpy']) or (tmp_vis[0] != 'none' and 'низ' in tmp_vis[0].cover and not tmp_vis[0].purpose in ['bdsm', 'sexy', 'skimpy'])
        if tmp_vis[3] != 'none' and not v_tmp:
            tt = [e for e in char.wear if 'попа' in e.cover]
            if len(tt) == 1 :
                tmp_vis[3] = tt[0]
            else: 
                if char.sex == 'male':
                    tmp_vis[3] = NostudpantiesM
                else:
                    tmp_vis[3] = NostudpantiesF

        tt = [e for e in char.wear if ('ноги' in e.cover) and (not e in tmp_vis)]
        if len(tt) == 1 :
            tmp_vis[4] = tt[0]
                
        return tmp_vis
        
