class TraducteurSimu:
    def __init__(self, robot):
        self.robot = robot
    
    def set_vitesse(self, vangGauche, vangDroite):
        self.robot.vangGauche = vangGauche
        self.robot.vangDroite = vangDroite
        self.robot.calculerVitesses()

    def set_vitesse_nulle(self):
        self.robot.vangGauche = 0
        self.robot.vangDroite = 0

    def get_distance_parcourue(self):
        return self.robot.vitesseLineaire * 0.1

    def get_angle_parcouru(self):
        return self.robot.vitesseAngulaire * 0.1

    def get_capteur(self):
        return self.robot.capteur
    
