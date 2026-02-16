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
        self.calculerVitesses() #calcule les vitesses linéaire et angulaire du robot
    
    def calculerVitesses(self):
        """
        Calcule la vitesse linéaire et la vitesse angulaire du robot à partir des vitesses angulaires des roues
        Rappel : la vitesse angulaire du robot est la vitesse à laquelle il tourne sur lui même, la vitesse linéaire est la vitesse à laquelle il avance dans la direction de son angle
        """
        # Vitesses linéaires des roues
        v_gauche = self.rayonRoues * self.vangGauche
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
    
    def getVitesses(self):
        """
        Getter pour les vitesses linéaire et angulaire du robot
        Retourne: (vitesseLineaire, vitesseAngulaire)
        """
        return self.vitesseLineaire, self.vitesseAngulaire
    
    def tourner(self,angle):
        """Fait tourner le robot de {angle}° """
        self.angle += angle

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
    
    def rotation(self, x_cible, y_cible):
        """
        Ajuste l'angle du robot progressivement vers (x_cible,y_cible) en utilisant
        la vitesse angulaire disponible fournie par la différence de vitesses des roues.
        3 cas
          - vitesses opposées de même norme : rotation sur place
          - l'une des roues à 0 : pivot autour de l'autre roue (modélisé par le même kinematic)
          - vitesses négatives : on effectue une inversion 180° pour obtenir des vitesses positives
        """
        self.assurer_direction_avant() #si nécessaire, remettre les vitesses en direction "avant"

        xVecteur1 = x_cible - self.x
        yVecteur1 = self.y - y_cible
        angle_cible = math.degrees(math.atan2(xVecteur1, yVecteur1))

        erreur = angle_cible - self.angle #erreur angulaire : différence entre l'angle cible et l'angle actuel du robot
        while erreur >= 180:
            erreur -= 360
        while erreur < -180:
            erreur += 360

        self.calculerVitesses()
        delta_max_deg = abs(math.degrees(self.vitesseAngulaire * 0.1)) #angle maximum que le robot peut tourner en 0.1s à la vitesse angulaire actuelle

        if delta_max_deg == 0: # si la vitesse angulaire est nulle (roues à la même vitesse), on tourne pas
            return

        if abs(erreur) <= delta_max_deg:
            self.angle = angle_cible
        else:
            sens = 1 if erreur > 0 else -1
            self.angle += sens * delta_max_deg

        self.normaliser_angle()

    def avancer(self):
        """
        Avance pendant 0.1s en utilisant la vitesse linéaire et angulaire actuelle du robot.
        """
        self.calculerVitesses()

        dtheta = self.vitesseAngulaire * 0.1 #angle de rotation pendant 0.1s
        distance = self.vitesseLineaire * 0.1 #distance parcourue pendant 0.1s

        self.angle += math.degrees(dtheta)
        self.normaliser_angle() #Assure que l'angle reste dans [-180, 180]

        dx = distance * math.sin(math.radians(self.angle))
        dy = -distance * math.cos(math.radians(self.angle))

        self.x += dx
        self.y += dy
        self.x = round(self.x, 2)
        self.y = round(self.y, 2)

    def aller_a(self, x, y):
        """
        Boucle jusqu'à la cible en orientant progressivement selon la vitesse angulaire disponible.
        """
        distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        max_iters = 10000 #pr le debug de boucle infinie
        it = 0
        while distance > 0.1 and it < max_iters:
            self.rotation(x, y)
            self.avancer()
            distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)
            it += 1
        self.x = round(x, 2)
        self.y = round(y, 2)

