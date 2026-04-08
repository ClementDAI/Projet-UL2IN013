from .avancer import Avancer
from .tourner import Tourner
from .sequencielle import Sequencielle
from .boucle import Boucle


class Hexagone:
    def __init__(self, cote, trad):
        self.cote = cote
        self.trad = trad 
        self.strats = Boucle(Sequencielle([Avancer(cote, trad), Tourner(72, trad)]), 5, trad)
        self.cur = -1
    def start(self):
        self.strats.start()

    def step(self):
        self.strats.step()

    def stop(self):
        return self.strats.stop()