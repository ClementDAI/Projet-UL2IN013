from .avancer import Avancer
from .tourner import Tourner
from .sequencielle import Sequencielle
from .boucle import Boucle

class Carre:
    def __init__(self, cote, trad):
        self.trad = trad
        self.cote = cote
        self.strats = Boucle(Sequencielle([Avancer(cote, trad), Tourner(90, trad)]), 4, trad)
        self.cur = -1

    def start(self):
        self.strats.start()

    def step(self):
        self.strats.step()

    def stop(self):
        return self.strats.stop()