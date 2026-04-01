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
        self.parcouru += self.trad.get_distance_parcourue()

    def stop(self):
        return self.parcouru >= self.distance
