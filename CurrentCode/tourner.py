from robot import Robot

class Tourner:
    def __init__(self,angle,robot):
        self.angle_cible = angle
        self.angle_depart = None
        self.robot = robot
    
    def start(self):
        self.angle_depart = self.robot.angle
        self.angle_parcouru = 0

    def step(self):
        self.robot.angle = (self.robot.angle + 1) % 360 # angle compris entre [0, 360]
        self.angle_parcouru += 1

    def stop(self):
        return self.angle_parcouru >= self.angle_cible or (self.rob.vangGauche == 0 and self.rob.vangDroite == 0)