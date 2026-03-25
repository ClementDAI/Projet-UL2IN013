<<<<<<< HEAD
from ..simulation.robot import Robot
import math
=======
>>>>>>> fb13e81096299a7abca6dbd4e3a5cc1d1fe96a3f

class Avancer:
    def __init__(self, distance, trad):
        self.distance = distance
        self.trad = trad
        
    def start(self):
        self.parcouru = 0
        self.trad.set_vitesse(50,50)

    def step(self):
        self.trad.set_vitesse(50,50)
        self.trad.robot.calculerVitesses()
        distance = self.trad.robot.vitesseLineaire * 0.1
        self.parcouru += distance

    def stop(self):
        return self.parcouru >= self.distance or self.trad.rob_vit_nulle()
