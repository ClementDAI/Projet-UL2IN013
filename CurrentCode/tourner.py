from robot import Robot

class Tourner:
    def __init__(self,angle,robot):
        self.angle_cible = angle
        self.angle_depart = None
        self.robot = robot
    
    def start(self):
        self.angle_depart = self.robot.angle

    def step(self):
        self.robot.angle += 1

    def stop(self):
        return self.robot.angle >= self.angle_depart + self.angle_cible