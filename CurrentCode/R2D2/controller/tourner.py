from ..simulation.robot import Robot

class Tourner:
    def __init__(self,angle,trad):
        self.angle_cible = angle
        self.angle_depart = None
        self.trad = trad
    
    def start(self):
        self.angle_depart = self.trad.get_angle()
        self.angle_parcouru = 0
        self.trad.set_vitesse(-10, 10)

    def step(self):
        self.trad.set_vitesse(-10, 10)
        self.angle_parcouru += abs(self.trad.get_angle_parcouru())
    def stop(self):
        return self.angle_parcouru >= self.angle_cible 


#a tester pour le reel si ca marche mieux 
# def start(self):
#     self.angle_parcouru = 0
#     self.trad.set_vitesse(-10, 10)

# def step(self):
#     self.trad.set_vitesse(-10, 10)
#     self.angle_parcouru = abs(self.trad.get_angle_parcouru())