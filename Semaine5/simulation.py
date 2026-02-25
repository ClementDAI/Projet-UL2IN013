import numpy as np
from robot import Robot
from salle import Salle
from controller import Controller
import math

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
    
        cote_robot = self.rob.coins()

        for i in self.salle.ListeObstacle:
            xObstacle, yObstacle = i.x, i.y
            largeurObstacle = i.largeur
            longueurObstacle = i.longueur
            if ((self.rob.x > xObstacle - largeurObstacle / 2) and (self.rob.x < xObstacle + largeurObstacle / 2) and (self.rob.y > yObstacle - longueurObstacle / 2) and (self.rob.y < yObstacle + longueurObstacle / 2)):
                return True
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
                
        cote_salle = self.salle.coins()
    
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
    
    def update_capteur(self):
        """rob : objet de classe robot
            salle : salle ou se trouve rob
            la fonction va mettre à jour la valeur de capteur de rob"""
        distance = 0
        angle = self.rob.angle
        sin = math.sin(math.radians(angle))
        cos = -math.cos(math.radians(angle))
        rob_tmp = Robot(self.rob.x, self.rob.y, self.rob.vangGauche, self.rob.vangDroite, self.rob.angle, self.rob.longueur, 0.1)
        salle_tmp = Salle(self.salle.dimensionX, self.salle.dimensionY)
        L = []
        for obs in self.salle.ListeObstacle:
            L.append(obs)
        salle_tmp.ListeObstacle = L
        simu_tmp = Simulation(rob_tmp, salle_tmp)
        old_x, old_y = simu_tmp.rob.x, simu_tmp.rob.y
        while not(simu_tmp.collision()):
            simu_tmp.rob.x += sin * 0.1  # pas de 0.1 pour le vecteur capteur
            simu_tmp.rob.y += cos * 0.1
            distance += 0.1
        
        simu_tmp.rob.x, simu_tmp.rob.y = old_x, old_y
        self.rob.capteur = round(distance, 2)


    def updateSimulation(self):
        """
        updateSimulation va mettre à jour la position du robot en fonction de sa vitesse et de son angle d'orientation
        """
        self.rob.x += self.rob.vitesseLineaire * np.cos(self.rob.angle)
        self.rob.y += self.rob.vitesseLineaire * np.sin(self.rob.angle)
        if self.collision() :
            self.rob.vangGauche = 0
            self.rob.vangDroite = 0
    
    
