class Traducteur_Simule:
    def __init__(self, robot):
        self.robot = robot
    
    def set_vitesse(self, vangGauche, vangDroite):
        self.robot.vangGauche = vangGauche
        self.robot.vangDroite = vangDroite

    def set_vitesse_nulle(self):
        self.robot.vangGauche = 0
        self.robot.vangDroite = 0

    def get_capteur(self):
        return self.robot.capteur
    
    def rob_vit_nulle(self):
        return self.robot.vangGauche == 0 and self.robot.vangDroite == 0