import math
import numpy as np

class robot(object):

    def __init__(self,x,y,vitesse,angle,longueur,largeur):
        """Attention : si x augmente alors déplacement vers la droite, vers la gauche sinon
                        si y augmente alors déplacement vers le BAS, vers le HAUT sinon"""
        self.x = x #coordonné x du centre du robot
        self.y = y #coordonné y du centre du robot
        self.vitesse = vitesse #vitesse en pixel par seconde
        self.angle = angle #angle positif ou négatif en degré dont son orientation initial est 0 (vers le haut)
        self.longueur = longueur #valeur de sa longueur sur y
        self.largeur = largeur #valeur de sa largeur sur x
    

    
    def getPosition(self):
        return self.x,self.y #renvoie le x et y du robot
    
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
        cos_theta = PrScalaire / (norme1 * norme2)
        if cos_theta > 1:
            round(cos_theta)
        if cos_theta < -1:
            round(cos_theta)
        theta = math.degrees(math.acos(PrScalaire / (norme1 * norme2))) # theta(u,v) = arccos(PrScalaire(u,v) / norme(u) * norme(v))
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
        self.x += 1* math.sin(math.radians(self.angle))
        self.y -= 1 * math.cos(math.radians(self.angle))
        self.x = round(self.x, 2) #arrondi pour eviter les problemes de précision avec les floats
        self.y = round(self.y, 2)

    def collision(self, salle):
        """
        salle : paramètre de classe Salle
        Collision va renvoyer true si la position du robot est bloqué par un obsctacle de la salle sinon false
        """

        angle = np.deg2rad(self.angle - 90)
        cos = np.cos(angle)
        sin = np.sin(angle)
        larg = self.largeur / 2
        long = self.longueur / 2
        
        coinHG = np.array([(self.x - (larg * cos) - (long * sin)), (self.y - (larg * sin) + (long * cos))]) # calcul des coins du robots
        coinHD = np.array([(self.x + (larg * cos) - (long * sin)), (self.y + (larg * sin) + (long * cos))]) 
        coinBG = np.array([(self.x - (larg * cos) + (long * sin)), (self.y - (larg * sin) - (long * cos))])
        coinBD = np.array([(self.x + (larg * cos) + (long * sin)), (self.y + (larg * sin) - (long * cos))])

        cote_robot = [(coinHG, coinHD), (coinBG, coinBD), (coinBG, coinHG), (coinBD, coinHD)]

        for i in salle.ListeObstacle:
            xObstacle, yObstacle = i.x, i.y
            largeurObstacle = i.largeur
            longueurObstacle = i.longueur
            coinObsHG = np.array([(xObstacle - (largeurObstacle / 2)), (yObstacle + (longueurObstacle / 2))]) # calculs des coins de l'obstacle
            coinObsHD = np.array([(xObstacle + (largeurObstacle / 2)), (yObstacle + (longueurObstacle / 2))])
            coinObsBG = np.array([(xObstacle - (largeurObstacle/ 2)), (yObstacle - (longueurObstacle / 2))])
            coinObsBD = np.array([(xObstacle + (largeurObstacle / 2)), (yObstacle - (longueurObstacle / 2))])
            cote_obs = [(coinObsHG, coinObsHD), (coinObsBG, coinObsBD), (coinObsBG, coinObsHG), (coinObsBD, coinObsHD)]
            for point1_rob, point2_rob in cote_robot:
                for point1_obs, point2_obs in cote_obs: 
                    vect_rob = point2_rob - point1_rob
                    vect_obs = point2_obs - point1_obs

                    prod_vec1 = np.cross(vect_rob, point1_obs - point1_rob) # calcul des produits vectoriels entre les cotés du robots et celle de l'obstacle pour détecter la collision
                    prod_vec2 = np.cross(vect_rob, point2_obs - point1_rob)
                    prod_vec3 = np.cross(vect_obs, point1_rob - point1_obs)
                    prod_vec4 = np.cross(vect_obs, point2_rob - point1_obs)

                    if (prod_vec1 * prod_vec2) < 0 and (prod_vec3 * prod_vec4) < 0: 
                        return True
                    
        cote_salle = [(np.array([0, 0]), np.array([salle.dimensionX, 0])), (np.array([0, salle.dimensionY]), np.array([salle.dimensionX, salle.dimensionY])), (np.array([0, salle.dimensionY]), np.array([0, 0])), (np.array([salle.dimensionX, salle.dimensionY]), np.array([salle.dimensionX, 0]))]
        
        for point1_rob, point2_rob in cote_robot: # collision avec la salle
            for point1_salle, point2_salle in cote_salle: 
                vect_rob = point2_rob - point1_rob
                vect_salle = point2_salle - point1_salle

                prod_vec1 = np.cross(vect_rob, point1_salle - point1_rob)
                prod_vec2 = np.cross(vect_rob, point2_salle - point1_rob)
                prod_vec3 = np.cross(vect_salle, point1_rob - point1_salle)
                prod_vec4 = np.cross(vect_salle, point2_rob - point1_salle)

                if (prod_vec1 * prod_vec2) < 0 and (prod_vec3 * prod_vec4) < 0: 
                    return True
        
        return False

    
    def aller_a(self, salle, x, y):
        """
        fonction aller_a
        Si il n'y a pas d'obstacles : fait avancer le robot jusqu'à la position (x,y) passée en paramètre 
        Sinon : arrête le robot
        """
        distance = math.sqrt((x - self.x)**2 + (y - self.y)**2) #pythagore
        xtmp = self.x
        ytmp = self.y
        while distance > 1: #pas egalité a cause des floats et arrondis
            self.rotation(x,y)
            xtmp += 1 * math.sin(math.radians(self.angle))
            ytmp -= 1 * math.cos(math.radians(self.angle))
            xtmp = round(xtmp, 2)
            ytmp = round(ytmp, 2)
            tmp = robot(xtmp, ytmp, self.vitesse, self.angle, self.longueur, self.largeur) #Création d'un robot temporaire qui effectue un pas en 'avance'
            if tmp.collision(salle) == True:
                print("Il y a un obstacle sur le chemin")
                break
            else:
                self.avancer()
            distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)  # Recalculer la distance
        self.x = round(x, 2) #pour eviter que le robot soit a 0.99/1.01 de la cible a cause des floats
        self.y = round(y, 2)

