init -50 python:
    class Item:
        def __init__ (self, name, cost, durability, picto, type):
            self.durability = durability
            self.name = name
            self.cost = cost
            self.picto = picto
            self.type = type
            
    class Tool(Item):
        def __init__ (self, purpose):
            self.purpose = purpose
            
    class Clothing(Item):
        def __init__ (self, lust, corr, reputation, char, sex, purpose):
            self.cover = []
            self.lust = lust
            self.corr = corr
            self.reputation = reputation
            self.char = char
            self.sex = sex
            self.purpose = purpose
    
    class Toy(Item):
        def __init__ (self, cover, size, corr, lust):
            self.cover = cover
            self.size = size
            self.corr = corr
            self.lust = lust          

    class Food(Item):
        def __init__ (self, energy):
            self.energy = energy

    class Present(Item):
        def __init__(self, sex, loy=0, corr=0, reputation=0, *args, **kwargs):
            """Создает новый подарок

            sex - пол для подарка
            loy - как подарок повлияет на лояльность - может быть 
                  положительным или отрицательным
            corr - как подарок повлияет на коррапшн - может быть положительным
                   или отрицательным
            reputation - как подарок повлияет на репутацию - может быть
                         положительным или отрицательным
            """

            self.__check_sex(sex)

            self.sex = sex
            self.loy = loy
            self.corr = corr
            self.reputation = reputation

            if 'type' not in kwargs:
                kwargs['type'] = 'present'
            if 'durability' not in kwargs:
                kwargs['durability'] = 100

            Item.__init__(self, **kwargs)

        def __check_sex(self, sex):
            avaialble = ['male', 'female', 'any']
            if sex.lower() not in avaialble:
                raise Exception('Wrong "sex" parameter: "{}". Available: {}'
                                .format(sex, avaialble))

        def __repr__(self):
            return ('<{}: "{}", sex: {}, loy: {}, corr: {}, rep: {}>'
                    .format(self.__class__.__name__,
                            self.name.encode('ascii','replace'),
                            self.sex, self.loy, self.corr, self.reputation))
