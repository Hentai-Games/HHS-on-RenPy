init python:
    class Olympiad():
        def __init__(self, active = False, month = 0, weekday = 0, score = 0, cheat = False, qwest = 0, confirm = False):
            self.active = active
            self.month = month
            self.weekday = weekday
            self.score = score
            self.cheat = cheat
            self.qwest = qwest
            self.confirm = confirm
            
    olympiad = Olympiad()