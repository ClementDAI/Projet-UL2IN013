from .avancer import Avancer
from .tourner import Tourner
from .sequencielle import Sequencielle
from .boucle import boucle

class Hexagone:
    def __init__(self, trad):
        self.trad = trad
        self.strats = Sequencielle([Avancer(5, trad), Tourner(60, trad),Avancer(5, trad), Tourner(60, trad),Avancer(5, trad), Tourner(60, trad),Avancer(5, trad), Tourner(60, trad),Avancer(5, trad), Tourner(60, trad)])
        self.cur = -1

    def start(self):
        self.strats.start()

    def step(self):
        if self.cur == 2:
            self.trad.rob.change_couleur(100,2,30)
        if self.cur == 4:
            self.trad.rob.change_couleur(200,2,30)
        if self.cur == 6:
            self.trad.rob.change_couleur(100,2,255)
        if self.cur == 8:
            self.trad.rob.change_couleur(100,255,30)
        self.strats.step()

    def stop(self):
        return self.strats.stop()