import numpy as np
#PAS BESOIN DE GETTER ET DE SETTER, UTILISEZ DIRECTEMENT LES ATTRIBUTS DE LA CLASSE ROBOT POUR LES MODIFIER OU LES LIRE

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
        self.temps = 0
        self.dessine = True

    def coins(self):
        """
        Retourne les coordonnées des 4 coins du robot
        """
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

        return self.vitesseLineaire, self.vitesseAngulaire

    def dessine(b):
        if b == True:
            self.dessine = True
        else:
            self.dessine = False
