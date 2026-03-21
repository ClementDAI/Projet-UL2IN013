from R2D2.controller.avancer import Avancer
from R2D2.controller.tourner import Tourner
from R2D2.controller.carre import Carre
from R2D2.controller.approcher_mur import Approcher_mur
from R2D2.controller.sequencielle import Sequencielle
from R2D2.simulation.robot import Robot
import numpy as np

class Boucle:
    def __init__(self, strats, n, rob):
        self.cur = -1
        self.nbIt = n
        self.rob = rob
        self.strats = strats #tab des strats
        self.strategie = None #strat actuelle

    def start(self):
        self.cur = 0
        self.strategie = Sequencielle(self.rob, self.strats)
        self.strategie.start()

    def step(self):
        if self.stop():
            return
        
        if self.strategie.stop():
            self.cur += 1
            if not self.stop():
                self.strategie = Sequencielle(self.rob, self.strats)
                self.strategie.start()
        else:
            self.strategie.step()


    def stop(self):
        return self.cur >= self.nbIt


