class TraducteurSimu:
    def __init__(self, robot):
        self.robot = robot
    
    def set_vitesse(self, vangGauche, vangDroite):
        self.robot.vangGauche = vangGauche
        self.robot.vangDroite = vangDroite

    def set_vitesse_nulle(self):
        self.robot.vangGauche = 0
        self.robot.vangDroite = 0

    def distance_parcourue(self):
        