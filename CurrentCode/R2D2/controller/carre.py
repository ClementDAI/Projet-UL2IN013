from R2D2.controller.avancer import Avancer
from R2D2.controller.tourner import Tourner
from R2D2.controller.sequencielle import Sequencielle
from R2D2.controller.boucle import Boucle


class Carre:
    def __init__(self, cote, rob):
        self.rob = rob
        self.cote = cote
        self.strats = Sequencielle(rob, [Boucle([Avancer(cote, rob), Tourner(90, rob)], 4, rob)])
        self.cur = -1

    def start(self):
        self.strats.start()

    def step(self):
        self.strats.step()

    def stop(self):
        return self.strats.stop()