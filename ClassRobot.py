import math

class robot(object):

    def __init__(self,x,y,vitesse,angle,longueur,largeur):
        self.x = x #coordoné x du centre du robot
        self.y = y #coordoné y du centre du robot
        self.vitesse = vitesse #vitesse en pixel par seconde
        self.angle = angle #angle positif en degré dont son orientation initial est 0 (vers le haut)
        self.longueur = longueur #valeur de sa longueur sur y
        self.largeur = largeur #valeur de sa largeur sur x
    

    
    def getPosition(self):
        return self.x,self.y #renvoie le x et y du robot
    
    def tourner(self, x_cible, y_cible):
        """Fait tourner le robot vers une direction cible (x_cible,y_cible)"""
        xVecteur1,yVecteur1 = (x_cible-self.x, y_cible-self.y) #Vecteur vers la direction cible

        #Calcul de x et y du vecteur qui a pour direction self.angle 
        #On considère la norme du vecteur de la direction du robot à 1
        #Attention sur repère orthonormé 
        if self.angle >= 0 and self.angle <=90:
            xVecteur2, yVecteur2 = (math.cos(90-self.angle) * 1, math.cos(self.angle) *1),   #Trigonométrie
        elif self.angle >= 90 and self.angle <=180:
            xVecteur2, yVecteur2 = (math.cos(self.angle-90) * 1, -math.cos(180-self.angle) *1)
        elif self.angle >= 180 and self.angle <=270:
            xVecteur2, yVecteur2 = (-math.cos(270-self.angle) * 1, -math.cos(self.angle-180) *1)
        elif self.angle >= 270 and self.angle <=360:
            xVecteur2, yVecteur2 = (-math.cos(self.angle-270) * 1, cos(360-self.angle) *1)


        prScalaire = xVecteur1*xVecteur2 + yVecteur1*yVecteur2
        theta = math.acos(prScalaire/1*math.sqrt(xVecteur1**2+yVecteur1**2)%360
        self.angle+=theta
    
    def avancer(self):
        """
        fonction avancer
        fait avancer le robot de 1 pixel dans la direction de son angle
        aucun paramètre
        """
        self.x += 1* math.sin(math.radians(self.angle))
        self.y -= 1 * math.cos(math.radians(self.angle))
        self.x = round(self.x, 2) #arrondi pour eviter les problemes de précision avec les floats
        self.y = round(self.y, 2)
    
    def aller_a(self, x, y):
        """
        fonction aller_a
        fait avancer le robot jusqua la position (x,y)passée en paramètre
        """
        distance = math.sqrt((x - self.x)**2 + (y - self.y)**2) #pythagore
        while distance > 1: #pas egalité a cause des floats et arrondis
            anglerad = math.atan2(y - self.y, x - self.x) #angle en radiant entre position actuelle et position cible
            angle2 = math.degrees(anglerad) + 90  # +90 parce que l'angle 0 c'est vers le haut et pas vers la droite
            angle2 = angle2 % 360
            self.angle = angle2 #on utilise pas tourner parce quon tourne qu'une seule fois vers la cible pas progressivement
            self.avancer()
            distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)  # Recalculer la distance
        self.x = round(x, 2) #pour eviter que le robot soit a 0.99/1.01 de la cible a cause des floats
        self.y = round(y, 2)