import math
import numpy as np

class Robot():

    def __init__(self,x,y,vitesse,angle,longueur,largeur):
        """Attention : si x augmente alors déplacement vers la droite, vers la gauche sinon
                        si y augmente alors déplacement vers le BAS, vers le HAUT sinon"""
        self.x = x #coordonné x du centre du robot
        self.y = y #coordonné y du centre du robot
        self.vitesse = vitesse #vitesse en pixel par seconde
        self.angle = angle #angle positif ou négatif en degré dont son orientation initial est 0 (vers le haut)
        self.longueur = longueur #valeur de sa longueur sur y
        self.largeur = largeur #valeur de sa largeur sur x
        self.capteur = 0 # initiliase la valeur du capteur d'obstacle à 0
        self.vitesse_angD = 0 #vitesse angulaire de la roue droite 
        self.vitesse_angG = 0 #vitesse angulaire de la roue gauche
    

    
    def getPosition(self):
        """Accesseur de la position du robot"""
        return self.x,self.y #renvoie le x et y du robot
    
    def set_vitesse(self, vitesseD, vitesseG): 
        """Setter de la vitesse des roues"""
        self.vitesse_angD = vitesseD
        self.vitesse_angG = vitesseG
    
    def tourner(self,angle):
        """Fait tourner le robot de {angle}° """
        self.angle += angle
    
    def rotation (self, x_cible, y_cible):
        """Met à jour l'angle du robot vers une direction cible (x_cible,y_cible)"""
        xVecteur1 = x_cible - self.x # Vecteur vers la cible
        yVecteur1 = self.y - y_cible
        xVecteur2 = math.sin(math.radians(self.angle)) # Vecteur direction du robot
        yVecteur2 = math.cos(math.radians(self.angle))
        norme1 = math.sqrt(xVecteur1**2 + yVecteur1**2)
        norme2 = 1
        PrScalaire = xVecteur1 * xVecteur2 + yVecteur1 * yVecteur2 # Produit Scalaire entre les 2 vecteurs
        valeur = PrScalaire / (norme1 * norme2)
        valeur = max(-1, min(1, valeur)) #sécurité sur les flottants
        theta = math.degrees(math.acos(valeur)) # theta(u,v) = arccos(PrScalaire(u,v) / norme(u) * norme(v))
        PrVectoriel = xVecteur1 * yVecteur2 - xVecteur2 * yVecteur1
        if PrVectoriel < 0:
            theta = -theta
        self.angle+= theta

    def avancer(self):
        """
        fonction avancer
        fait avancer le robot de 1 pixel dans la direction de son angle
        aucun paramètre
        """
        self.x += 0.1 * math.sin(math.radians(self.angle))
        self.y -= 0.1 * math.cos(math.radians(self.angle))
        self.x = round(self.x, 2) #arrondi pour eviter les problemes de précision avec les floats
        self.y = round(self.y, 2)

    def aller_a(self, x, y):
        """
        fonction aller_a
        Si il n'y a pas d'obstacles : fait avancer le robot jusqu'à la position (x,y) passée en paramètre 
        Sinon : arrête le robot
        """
        distance = math.sqrt((x - self.x)**2 + (y - self.y)**2) #pythagore
        while distance > 0.1: #pas egalité a cause des floats et arrondis
            self.rotation(x,y)
            self.avancer()
            distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)  # Recalculer la distance
        self.x = round(x, 2) #pour eviter que le robot soit a 0.99/1.01 de la cible a cause des floats
        self.y = round(y, 2)

