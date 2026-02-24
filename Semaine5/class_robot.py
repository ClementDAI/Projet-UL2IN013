import math
import numpy as np

class Robot(object):

    def __init__(self,x,y,vangGauche,vangDroite,angle,longueur,largeur):
        self.x = x #coordonné x(abscisse) du centre du robot
        self.y = y #coordonné y (ordonnée) du centre du robot
        self.angle = angle #angle positif ou négatif en degré dont son orientation initial est 0 (vers le haut)
        self.longueur = longueur #valeur de la longueur sur y du robot
        self.largeur = largeur #valeur de la  largeur sur x du robot
        self.vangGauche = vangGauche #vitesse angulaire de la roue gauche en rad/seconde
        self.vangDroite = vangDroite #vitesse angulaire de la roue droite en rad/seconde
        self.rayonRoues = 0.05 #rayon des roues en mètre
        self.ecartRoues = 0.2 #écart entre les roues en mètre
        self.capteur = 0 #distance entre le robot et l'obstacle en face de lui (ou la bordure de la salle)
        self.vitesseLineaire = 0 #initialisation de la vitesse linéaire 
        self.vitesseAngulaire = 0 #initialisation de la vitesse angulaire 

    def coins(self):
        angle = np.deg2rad(self.angle)
        cos = np.cos(angle)
        sin = np.sin(angle)
        larg = self.largeur / 2
        long = self.longueur / 2
        
        coinHG = np.array([(self.x - (larg * cos) - (long * sin)), (self.y - (larg * sin) + (long * cos))]) # calcul des coins du robots #haut-gauche
        coinHD = np.array([(self.x + (larg * cos) - (long * sin)), (self.y + (larg * sin) + (long * cos))]) #haut-droit
        coinBG = np.array([(self.x - (larg * cos) + (long * sin)), (self.y - (larg * sin) - (long * cos))]) #bas-gauche
        coinBD = np.array([(self.x + (larg * cos) + (long * sin)), (self.y + (larg * sin) - (long * cos))]) #bas-droit

        return [(coinHG, coinHD), (coinBG, coinBD), (coinBG, coinHG), (coinBD, coinHD)] 
    
    def calculerVitesses(self):
        """
        Calcule la vitesse linéaire et la vitesse angulaire du robot à partir des vitesses angulaires des roues
        Rappel : la vitesse angulaire du robot est la vitesse à laquelle il tourne sur lui même,
        la vitesse linéaire est la vitesse à laquelle il avance dans la direction de son angle
        """
        # Vitesses linéaires des roues
        v_gauche = self.rayonRoues * self.vangGauche #produit du rayon des roues et vitesse angulaire 
        v_droite = self.rayonRoues * self.vangDroite
        
        # Vitesse linéaire du robot (moyenne des deux roues)
        self.vitesseLineaire = (v_gauche + v_droite) / 2
        
        # Vitesse angulaire du robot (rotation)
        self.vitesseAngulaire = (v_droite - v_gauche) / self.ecartRoues
    
    def getPosition(self):
        return self.x,self.y #renvoie le x et y du robot
    
    def setVitessesAngulaires(self, vangGauche, vangDroite):
        """
        Setter pour les vitesses angulaires des roues
        vangGauche = vitesse angulaire de la roue gauche en rad/s
        vangDroite = vitesse angulaire de la roue droite en rad/s
        """
        self.vangGauche = vangGauche
        self.vangDroite = vangDroite
        self.calculerVitesses()
    
    def getVitessesAngulaires(self):
        """
        Getter pour les vitesses angulaires des roues
        Retourne: (vangGauche, vangDroite)
        """
        return self.vangGauche, self.vangDroite 
#Question1: a t-on réleement besoin de faire une fonction get vitesse angulaire ? Pourquoi ne pas directement faire une focntion get générale qui reprend get vitesse angulaire,
    get vitesse, et get position au meme endroit ? 

    
    def getVitesses(self):
        """
        Getter pour les vitesses linéaire et angulaire du robot
        Retourne: (vitesseLineaire, vitesseAngulaire)
        """
        return self.vitesseLineaire, self.vitesseAngulaire
    
    def update_angle(self,angle):
        """Fait tourner le robot de {angle}° """
        self.angle = angle

    def normaliser_angle(self):
        """Normalise self.angle dans l'intervalle [-180, 180]."""
        self.angle = (self.angle + 180) % 360 - 180

    def assurer_direction_avant(self):
        """
        Si le robot a une vitesse linéaire négative (ou les deux roues avec vitesses négatives),
        on pivote le robot de 180° et on inverse les vitesses angulaires des roues pour
        conserver le même mouvement mais avec des vitesses positives dans la direction "avant".
        """
        self.calculerVitesses()
        if self.vitesseLineaire < 0 or (self.vangGauche < 0 and self.vangDroite < 0):
            self.angle += 180
            self.vangGauche = -self.vangGauche
            self.vangDroite = -self.vangDroite
            self.calculerVitesses()
            self.normaliser_angle()
    
