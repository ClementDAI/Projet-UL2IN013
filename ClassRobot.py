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
    
    def rotation(self, x_cible, y_cible, dt=0.1):
        """
        Ajuste l'angle du robot progressivement en direction de (x_cible, y_cible)
        en tenant compte de la vitesse angulaire disponible fournie par les roues.
        - calcule l'angle cible dans le même repère que `self.angle`
        - applique un pas de rotation limité par `self.vitesseAngulaire * dt`

        Paramètres:
            x_cible, y_cible: coordonnées cible
            dt: pas de temps en secondes
        """
        # vecteur vers la cible (même convention que dans le reste du code)
        xVecteur1 = x_cible - self.x
        yVecteur1 = self.y - y_cible

        # angle cible (en degrés) : atan2(x, y) correspond à la convention utilisée
        angle_cible = math.degrees(math.atan2(xVecteur1, yVecteur1))

        # erreur angulaire (normalisée entre -180 et 180)
        erreur = angle_cible - self.angle
        while erreur > 180:
            erreur -= 360
        while erreur < -180:
            erreur += 360

        # quantité maximale de rotation disponible pendant dt (en degrés)
        # self.vitesseAngulaire est en rad/s, on multiplie par dt puis convertit en degrés
        self.calculerVitesses()
        delta_max_deg = abs(math.degrees(self.vitesseAngulaire * dt))

        # si on peut atteindre la cible dans ce pas, on y va directement
        if abs(erreur) <= delta_max_deg:
            self.angle = angle_cible
        else:
            # sinon on tourne dans le sens de l'erreur, d'une magnitude limitée
            sens = 1 if erreur > 0 else -1
            self.angle += sens * delta_max_deg

    def avancer(self, dt=0.1):
        """
        Fait avancer le robot selon ses vitesses angulaires des roues
        Paramètre: dt = intervalle de temps en secondes (par défaut 0.1s)
        Utilise le modèle cinématique du robot différentiel
        """
        self.calculerVitesses()  # met à jour les vitesses

        # rotation pendant dt (en radians)
        dtheta = self.vitesseAngulaire * dt
        # mise à jour de l'angle (on convertit en degrés)
        self.angle += math.degrees(dtheta)

        # déplacement linéaire pendant dt
        distance = self.vitesseLineaire * dt

        # utilisation de l'angle courant pour le déplacement
        dx = distance * math.sin(math.radians(self.angle))
        dy = -distance * math.cos(math.radians(self.angle))

        self.x += dx
        self.y += dy
        self.x = round(self.x, 2)
        self.y = round(self.y, 2)

    def aller_a(self, x, y, dt=0.1):
        """
        Fait avancer le robot jusqu'à la position (x,y) passée en paramètre
        Utilise les vitesses angulaires des roues et la rotation progressive
        Paramètres: x, y = position cible
                    dt = intervalle de temps pour chaque étape (par défaut 0.1s)
        """
        distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        while distance > 0.1:  # pas egalité a cause des floats et arrondis
            # on oriente progressivement en fonction de la vitesse angulaire
            self.rotation(x, y, dt)
            # puis on avance pendant dt
            self.avancer(dt)
            distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)  # Recalculer la distance
        self.x = round(x, 2)  # pour eviter que le robot soit a 0.99/1.01 de la cible a cause des floats
        self.y = round(y, 2)

