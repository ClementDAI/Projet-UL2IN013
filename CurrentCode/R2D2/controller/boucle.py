from avancer import Avancer
from tourner import Tourner
from carre import Carre
from R2D2.simulation.robot import Robot
import numpy as np

class Boucle():
    def __init__(self, strat, n, rob):
        self.cur = -1
        self.nbIt = n
        self.rob = rob
        self.strategie = strat
    
    def start(self):
        self.cur = 0
        self.strategie.start()

    def step(self):
        if self.stop():
            return
        
        while self.cur < self.nbIt:
            while not self.strategie.stop():

                self.strategie.step()
                self.rob.x += self.rob.vitesseLineaire * 0.1 * np.sin(np.radians(self.rob.angle))
                self.rob.y -= self.rob.vitesseLineaire * 0.1 * np.cos(np.radians(self.rob.angle))
                self.rob.angle = (self.rob.angle + self.rob.vitesseAngulaire) % 360
            self.cur += 1
            self.strategie.start()

    def stop(self):
        return self.cur >= self.nbIt


