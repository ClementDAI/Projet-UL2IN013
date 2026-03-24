from R2D2.controller.avancer import Avancer
from R2D2.controller.tourner import Tourner
from R2D2.controller.sequencielle import Sequencielle
from R2D2.controller.boucle import Boucle


class Carre:
    def __init__(self, cote, trad):
        self.trad = trad
        self.cote = cote
        self.strats = Sequencielle([Boucle([Avancer(cote, trad), Tourner(90, trad)], 4, trad)])
        self.cur = -1

    def start(self):
        self.strats.start()

    def step(self):
        self.strats.step()

    def stop(self):
        return self.strats.stop()