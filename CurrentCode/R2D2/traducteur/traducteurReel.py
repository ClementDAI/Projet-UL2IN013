import robot2i013
class TraducteurReel:
    def __init__(self, robot):
        self.robot = robot #robot irl 
    
    def set_vitesse(self, vangGauche, vangDroite):
        self.robot.set_motor_dps(robot.MOTOR_LEFT, vangGauche)
        self.robot.set_motor_dps(robot.MOTOR_RIGHT, vangDroite)