from ..simulation.robot import Robot
import math

class Avancer:
    def __init__(self, distance, vitesse, trad):
        self.distance = distance
        self.trad = trad
        self.vitesse = vitesse
        
    def start(self):
        self.parcouru = 0
        self.trad.set_vitesse(self.vitesse,self.vitesse)

    def step(self):
        self.trad.set_angle_roue_zero()
        self.trad.set_vitesse(self.vitesse,self.vitesse)
        self.parcouru += self.trad.get_distance_parcourue()

    def stop(self):
        return self.parcouru >= self.distance
