from .avancer import Avancer
from .tourner import Tourner

class Carre:
    def __init__(self, cote, rob):
        self.rob = rob
        self.cote = cote
        self.strats = [Avancer(self.cote, self.rob), Tourner(90, self.rob), Avancer(self.cote, self.rob), Tourner(90, self.rob), Avancer(self.cote, self.rob), Tourner(90, self.rob), Avancer(self.cote, self.rob)]
        self.cur = -1

    def start(self):
        self.cur = -1

    def step(self):
        if self.stop():
            return
        
        if self.cur < 0 or self.strats[self.cur].stop():
            self.cur += 1
            self.strats[self.cur].start()
        self.strats[self.cur].step()

    def stop(self):
        return self.cur == len(self.strats) - 1 and self.strats[self.cur].stop()