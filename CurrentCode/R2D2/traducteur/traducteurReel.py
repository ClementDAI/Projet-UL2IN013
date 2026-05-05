#from ..robot2I013 import Robot2IN013
import math
class TraducteurReel:
    def __init__(self, robot):
        self.robot = robot #robot irl 
        self.distance_g = 0
        self.distance_d = 0
    
    def set_vitesse(self, vangGauche, vangDroite):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, vangGauche)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, vangDroite)
    
    def set_vitesse_nulle(self):
        self.set_vitesse(0,0)
    
    def set_angle_roue_zero(self):
        pos_g, pos_d = self.robot.get_motor_position()
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT,pos_g)
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT,pos_d)
    
    def lire_encodeur(self):
        pos_g, pos_d = self.robot.get_motor_position()
        self.distance_g = pos_g/360*(math.pi*self.robot.WHEEL_DIAMETER)
        self.distance_d = pos_d/360*(math.pi*self.robot.WHEEL_DIAMETER)

    def get_distance_parcourue_roue(self):
        self.lire_encodeur()
        return (self.distance_g + self.distance_d)/2 #moyenne pas une seule roue au cas ou une roue bloque
        
    
    def get_angle_parcouru(self):
        self.lire_encodeur()
        return math.degrees((self.distance_d - self.distance_g) / self.robot.WHEEL_BASE_WIDTH)

    
    def get_capteur(self):
        return self.robot.get_distance()

