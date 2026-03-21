from R2D2.simulation.robot import Robot

class Tourner:
    def __init__(self,angle,robot):
        self.angle_cible = angle
        self.angle_depart = None
        self.robot = robot
    
    def start(self):
        self.angle_depart = self.robot.angle
        self.angle_parcouru = 0
        self.robot.vangGauche = -10
        self.robot.vangDroite = 10

    def step(self):
        self.robot.vangGauche = -10
        self.robot.vangDroite = 10
        self.robot.calculerVitesses()
        self.angle_parcouru += abs(self.robot.vitesseAngulaire * 0.2)

    def stop(self):
        return self.angle_parcouru >= self.angle_cible or (self.robot.vangGauche == 0 and self.robot.vangDroite == 0)