from ..simulation.robot import Robot
import math

class Avancer:
    def __init__(self, distance, vitesse, trad):
        self.distance = distance
        self.trad = trad
        self.vitesse = vitesse
        
    def start(self):
        self.parcouru = 0
        self.trad.set_angle_roue_zero()
        self.trad.set_vitesse(self.vitesse,self.vitesse)

    def step(self):
        self.parcouru += self.trad.get_distance_parcourue() #on lit dabord avant d'avancer pour si jamais pas une ligne droite ou roue qui bloque : on prend la distance parcourue de la roue qui bloque pas
        self.trad.set_angle_roue_zero()
        self.trad.set_vitesse(self.vitesse,self.vitesse)

    def stop(self):
        return self.parcouru >= self.distance
