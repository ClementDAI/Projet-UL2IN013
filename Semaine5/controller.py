from ClassRobot import robot
import math

class Controller:
    def __init__(self, robot):
        self.robot = robot
        xprec, yprec = self.robot.getPosition()
        self.xprec = xprec
        self.yprec = yprec

    def rotation(self, x_cible, y_cible): 
        """
        se tourner vers la cible en utilisant la v ang des roues
        """
        self.robot.assurer_direction_avant() #si nécessaire, remettre les vitesses en direction "avant"

        xVecteur1 = x_cible - self.robot.x
        yVecteur1 = self.robot.y - y_cible
        angle_cible = math.degrees(math.atan2(xVecteur1, yVecteur1))

        erreur = angle_cible - self.robot.angle #erreur angulaire : différence entre l'angle cible et l'angle actuel du robot
        while erreur > 180:
            erreur -= 360
        while erreur < -180:
            erreur += 360

        if abs(erreur) < 1:
            self.robot.angle = angle_cible
            self.robot.normaliser_angle()
            return
        
        self.robot.normaliser_angle()
    
    def avancer(self):
        """
        Avance en utilisant la vitesse linéaire et angulaire actuelle du robot.
        """
        self.robot.calculerVitesses()

        distance = self.robot.vitesseLineaire * 0.1

        self.robot.x += distance * math.sin(math.radians(self.robot.angle))
        self.robot.y -= distance * math.cos(math.radians(self.robot.angle))
        self.robot.x = round(self.robot.x, 2)
        self.robot.y = round(self.robot.y, 2)
    
    def allerA(self, x, y):
        """
        Boucle jusqu'à la cible en orientant progressivement selon la vitesse angulaire disponible.
        """
        distance = math.sqrt((x - self.robot.x)**2 + (y - self.robot.y)**2)
        max_iters = 10000 #pr le debug de boucle infinie
        it = 0
        while distance > 0.1 and it < max_iters:
            self.rotation(x, y)
            self.avancer()
            distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)
            it += 1
        self.robot.x = round(x, 2)
        self.robot.y = round(y, 2)

    def boucle(self, x, action): #je vois pas trop l'utilité encore mais le prof avait dit que c'était nécessaire
        """
        Répète x fois une instruction.
        """
        for _ in range(x):
            action()
    
    def sarreter(self, distance_voulue, distance_parcourue):
        """
        Arrête le robot si il a parcouru la distance voulue.
        """
        if distance_parcourue >= distance_voulue:
            self.robot.vitesseGauche = 0
            self.robot.vitesseDroite = 0

    def updateController(self, robot, x_cible, y_cible):
        """
        Met a jour les info du controller et lance la boucle pour aller a la cible.
        """
        self.robot = robot
        distance_parcourue = math.sqrt((self.robot.x - self.xprec)**2 + (self.robot.y - self.yprec)**2) 
        distance_voulue = math.sqrt((x_cible - self.xprec)**2 + (y_cible - self.yprec)**2)
        self.sarreter(distance_voulue, distance_parcourue)
        self.allerA(x_cible, y_cible)
        self.xprec = self.robot.x
        self.yprec = self.robot.y