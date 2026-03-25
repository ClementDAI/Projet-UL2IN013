<<<<<<< HEAD
from .avancer import Avancer
from .tourner import Tourner
from .approcher_mur import Approcher_mur
from .sequencielle import Sequencielle
from ..simulation.robot import Robot
import numpy as np
=======
from R2D2.controller.sequencielle import Sequencielle
>>>>>>> fb13e81096299a7abca6dbd4e3a5cc1d1fe96a3f

class Boucle:
    def __init__(self, strats, n, trad):
        self.cur = -1
        self.nbIt = n
        self.trad = trad
        self.strats = strats #tab des strats
        self.strategie = None #strat actuelle

    def start(self):
        self.cur = 0
        self.strategie = Sequencielle(self.strats)
        self.strategie.start()

    def step(self):
        if self.stop():
            return
        
        if self.strategie.stop():
            self.cur += 1
            if not self.stop():
                self.strategie = Sequencielle(self.strats)
                self.strategie.start()
        else:
            self.strategie.step()


    def stop(self):
        return self.cur >= self.nbIt


