<<<<<<< HEAD
from ..simulation.robot import Robot
=======
>>>>>>> fb13e81096299a7abca6dbd4e3a5cc1d1fe96a3f

class Tourner:
    def __init__(self,angle,trad):
        self.angle_cible = angle
        self.angle_depart = None
        self.trad = trad
    
    def start(self):
        self.angle_depart = self.trad.robot.angle
        self.angle_parcouru = 0
        self.trad.set_vitesse(-10, 10)

    def step(self):
        self.trad.set_vitesse(-10, 10)
        self.trad.robot.calculerVitesses()
        self.angle_parcouru += abs(self.trad.robot.vitesseAngulaire * 0.2)

    def stop(self):
        return self.angle_parcouru >= self.angle_cible or self.trad.rob_vit_nulle()