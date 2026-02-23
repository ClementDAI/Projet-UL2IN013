import math
import numpy as np

class robot(object):

    def __init__(self,x,y,vangGauche,vangDroite,angle,longueur,largeur):
        self.x = x #coordonné x du centre du robot
        self.y = y #coordonné y du centre du robot
        self.angle = angle #angle positif ou négatif en degré dont son orientation initial est 0 (vers le haut)
        self.longueur = longueur #valeur de sa longueur sur y
        self.largeur = largeur #valeur de sa largeur sur x
        self.vangGauche = vangGauche #vitesse angulaire de la roue gauche en rad/s
        self.vangDroite = vangDroite #vitesse angulaire de la roue droite en rad/s
        self.rayonRoues = 0.05 #rayon des roues en m
        self.ecartRoues = 0.2 #écart entre les roues en m
        self.capteur = 0 #distance entre le robot et l obstacle en face (ou la bordure de la salle)

    def coins(self):
        angle = np.deg2rad(self.angle)
        cos = np.cos(angle)
        sin = np.sin(angle)
        larg = self.largeur / 2
        long = self.longueur / 2
        
        coinHG = np.array([(self.x - (larg * cos) - (long * sin)), (self.y - (larg * sin) + (long * cos))]) # calcul des coins du robots
        coinHD = np.array([(self.x + (larg * cos) - (long * sin)), (self.y + (larg * sin) + (long * cos))]) 
        coinBG = np.array([(self.x - (larg * cos) + (long * sin)), (self.y - (larg * sin) - (long * cos))])
        coinBD = np.array([(self.x + (larg * cos) + (long * sin)), (self.y + (larg * sin) - (long * cos))])

        return [(coinHG, coinHD), (coinBG, coinBD), (coinBG, coinHG), (coinBD, coinHD)]