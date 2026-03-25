from ..simulation.robot import Robot
import math

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
