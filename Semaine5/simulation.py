import numpy as np
from class_robot import Robot
from class_salle import Salle
from controller import Controller

class Simulation:
    def __init__(self,Robot,Salle):
        self.rob = Robot
        self.salle = Salle
        self.controller = Controller(self.rob)

    def cross2D(self,a, b):
        return a[0]*b[1] - a[1]*b[0]

    def collision(self):
        """
        rob : paramètre de classe Robot
        salle : paramètre de classe Salle
        Collision va renvoyer true si la position du robot est bloqué par un obsctacle de la salle sinon false
        """

        angle = np.deg2rad(self.rob.angle)
        cos = np.cos(angle)
        sin = np.sin(angle)
        larg = self.rob.largeur / 2
        long = self.rob.longueur / 2
    
        coinHG = np.array([(self.rob.x - (larg * cos) - (long * sin)), (self.rob.y - (larg * sin) + (long * cos))]) # calcul des coins du robots
        coinHD = np.array([(self.rob.x + (larg * cos) - (long * sin)), (self.rob.y + (larg * sin) + (long * cos))]) 
        coinBG = np.array([(self.rob.x - (larg * cos) + (long * sin)), (self.rob.y - (larg * sin) - (long * cos))])
        coinBD = np.array([(self.rob.x + (larg * cos) + (long * sin)), (self.rob.y + (larg * sin) - (long * cos))])

        cote_robot = self.rob.coins()

        for i in self.salle.ListeObstacle:
            xObstacle, yObstacle = i.x, i.y
            largeurObstacle = i.largeur
            longueurObstacle = i.longueur
            inclinaison = i.inclinaison
            larg2 = i.largeur / 2
            long2 = i.longueur / 2 
            cos2 = np.cos(inclinaison)
            sin2 = np.sin(inclinaison)
            if ((self.rob.x > xObstacle - largeurObstacle / 2) and (self.rob.x < xObstacle + largeurObstacle / 2) and (self.rob.y > yObstacle - longueurObstacle / 2) and (self.rob.y < yObstacle + longueurObstacle / 2)):
                return True
            coinObsHG = np.array([(xObstacle - (larg2 * cos2) - (long2 * sin2)), (yObstacle - (larg2 * sin2) + (long2 * cos2))]) # calculs des coins de l'obstacle
            coinObsHD = np.array([(xObstacle + (larg2 * cos2) - (long2 * sin2)), (yObstacle + (larg2 * sin2) + (long2 * cos2))])
            coinObsBG = np.array([(xObstacle - (larg2 * cos2) + (long2 * sin2)), (yObstacle - (larg2 * sin2) - (long2 * cos2))])
            coinObsBD = np.array([(xObstacle + (larg2 * cos2) + (long2 * sin2)), (yObstacle + (larg2 * sin2) - (long2 * cos2))])
            cote_obs = i.coins()
            for point1_rob, point2_rob in cote_robot:
                for point1_obs, point2_obs in cote_obs: 
                    vect_rob = point2_rob - point1_rob
                    vect_obs = point2_obs - point1_obs

                    prod_vec1 = self.cross2D(vect_rob, point1_obs - point1_rob) # calcul des produits vectoriels entre les cotés du robots et celle de l'obstacle pour détecter la collision
                    prod_vec2 = self.cross2D(vect_rob, point2_obs - point1_rob)
                    prod_vec3 = self.cross2D(vect_obs, point1_rob - point1_obs)
                    prod_vec4 = self.cross2D(vect_obs, point2_rob - point1_obs)

                    if (prod_vec1 * prod_vec2) < 0 and (prod_vec3 * prod_vec4) < 0: 
                        return True
                
        cote_salle = [(np.array([0, 0]), np.array([self.salle.dimensionX, 0])), (np.array([0, self.salle.dimensionY]), np.array([self.salle.dimensionX, self.salle.dimensionY])), (np.array([0, self.salle.dimensionY]), np.array([0, 0])), (np.array([self.salle.dimensionX, self.salle.dimensionY]), np.array([self.salle.dimensionX, 0]))]
    
        for point1_rob, point2_rob in cote_robot: # collision avec la salle
            for point1_salle, point2_salle in cote_salle: 
                vect_rob = point2_rob - point1_rob
                vect_salle = point2_salle - point1_salle

                prod_vec1 = self.cross2D(vect_rob, point1_salle - point1_rob)
                prod_vec2 = self.cross2D(vect_rob, point2_salle - point1_rob)
                prod_vec3 = self.cross2D(vect_salle, point1_rob - point1_salle)
                prod_vec4 = self.cross2D(vect_salle, point2_rob - point1_salle)

                if (prod_vec1 * prod_vec2) < 0 and (prod_vec3 * prod_vec4) < 0: 
                    return True
    
        return False
