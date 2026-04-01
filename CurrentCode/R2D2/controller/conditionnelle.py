from .avancer import Avancer
from .tourner import Tourner
from .boucle import Boucle
from .approcher_mur import Approcher_mur

class Conditionnelle:
    def __init__(self, trad, condition, strat1, strat2):
        self.trad = trad
        self.condition = condition
        self.strat1 = strat1
        self.strat2 = strat2

    def start(self):
        if self.condition:
            self.strat1.start()
        else:
            self.strat2.start()

    def step(self):
        if not self.strat1.stop():
            self.strat1.step()
        elif not self.strat2.stop():
            self.strat2.step()

    def stop(self):
        return self.strat1.stop() and self.strat2.stop()
