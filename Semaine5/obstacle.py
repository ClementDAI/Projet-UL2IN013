import numpy as np
import math

class Obstacle(object):

    def __init__(self,x,y,largeur,longueur, inclinaison): #obstacle de forme rectangulaire centré x,y
        self.x = x #coordoné x du centre du centre de l'obstacle
        self.y = y #coordoné y du centre du centre de l'obstacle
        self.longueur = longueur #valeur de la longueur sur y de l'obstacle
        self.largeur = largeur #valeur de la largeur sur x de l'obstacle
        self.inclinaison = inclinaison

    def ajoutObstacle(self,salle): 
        """
        Cette fonction ajoute un obstacle(x,y,longueur,largeur) dans la liste de la classe salle:
        usage: salle.ajoutObstacle(obstacle) 
        """
        salle.ListeObstacle.append(self) #le paramètre doit être une classe obstacle
    
    def coins(self):
        """
        Cette fonction retourne les coordonnées des 4 coins de l'obstacle
        """
        long2 = self.longueur / 2
        larg2 = self.largeur / 2
        cos2 = math.cos(self.inclinaison)
        sin2 = math.sin(self.inclinaison)
        coinObsHG = np.array([(self.x - (larg2 * cos2) - (long2 * sin2)), (self.y - (larg2 * sin2) + (long2 * cos2))])
        coinObsHD = np.array([(self.x + (larg2 * cos2) - (long2 * sin2)), (self.y + (larg2 * sin2) + (long2 * cos2))])
        coinObsBG = np.array([(self.x - (larg2 * cos2) + (long2 * sin2)), (self.y - (larg2 * sin2) - (long2 * cos2))])
        coinObsBD = np.array([(self.x + (larg2 * cos2) + (long2 * sin2)), (self.y + (larg2 * sin2) - (long2 * cos2))])
        return [(coinObsHG, coinObsHD), (coinObsBG, coinObsBD), (coinObsBG, coinObsHG), (coinObsBD, coinObsHD)]
