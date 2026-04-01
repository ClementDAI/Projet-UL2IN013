import robot2i013
import math
class TraducteurReel:
    def __init__(self, robot):
        self.robot = robot #robot irl 
    
    def set_vitesse(self, vangGauche, vangDroite):
        self.robot.set_motor_dps(robot.MOTOR_LEFT, vangGauche)
        self.robot.set_motor_dps(robot.MOTOR_RIGHT, vangDroite)
    
    def get_capteur(self):
        return get_distance

    def set_angle_zero(self):
        pos_g, pos_d = self.robot.get_motor_position()
        self.robot.offset_motor_dps(self.robot.MOTOR_LEFT,pos_g)
        self.robot.offset_motor_dps(self.robot.MOTOR_RIGHT,pos_d)

    def get_distance_parcourue(self):
        new_pos_g, new_pos_d = self.robot.get_motor_position()
        distance_roue_gauche = new_pos_g/360*(2*math.pi*self.robot.WHEEL_DIAMETER/2)
        distance_roue_droite = new_pos_d/360*(2*math.pi*self.robot.WHEEL_DIAMETER/2) #on fait set_angle_zero puis on fait avancer() sa change l angle avec ce nouvelle angle ou fait get_distance_parcourue on a angle/360= le nb de tour multiplier par le perimetre
        return distance_roue_gauche, distance_roue_droite