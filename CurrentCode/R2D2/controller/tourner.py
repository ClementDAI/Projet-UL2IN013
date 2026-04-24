from ..simulation.robot import Robot

class Tourner:
    def __init__(self,angle,trad):
        self.angle_cible = angle
        self.trad = trad
    
    def start(self):
        self.angle_parcouru = 0
        self.trad.set_angle_roue_zero()
        self.trad.set_vitesse(-10, 10)

    def step(self):
        self.angle_parcouru += abs(self.trad.get_angle_parcouru())
        self.trad.set_angle_roue_zero()
        self.trad.set_vitesse(-10, 10)

    def stop(self):
        return self.angle_parcouru >= self.angle_cible 