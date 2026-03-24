from .avancer import Avancer
from .tourner import Tourner
from .sequencielle import Sequencielle
from .boucle import Boucle


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