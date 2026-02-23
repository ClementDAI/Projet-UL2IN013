import numpy as np
from ClassRobot import robot
from ClassSalle import salle

def cross2D(a, b):
    return a[0]*b[1] - a[1]*b[0]

def collision(rob, salle):
    """
    rob : paramètre de classe Robot
    salle : paramètre de classe Salle
    Collision va renvoyer true si la position du robot est bloqué par un obsctacle de la salle sinon false
    """

    cote_robot = rob.coins

    for i in salle.ListeObstacle:
        xObstacle, yObstacle = i.x, i.y
        largeurObstacle = i.largeur
        longueurObstacle = i.longueur
        if ((rob.x > xObstacle - largeurObstacle / 2) and (rob.x < xObstacle + largeurObstacle / 2) and (rob.y > yObstacle - longueurObstacle / 2) and (rob.y < yObstacle + longueurObstacle / 2)):
            return True
        cote_obs = i.coins
        for point1_rob, point2_rob in cote_robot:
            for point1_obs, point2_obs in cote_obs: 
                vect_rob = point2_rob - point1_rob
                vect_obs = point2_obs - point1_obs

                prod_vec1 = cross2D(vect_rob, point1_obs - point1_rob) # calcul des produits vectoriels entre les cotés du robots et celle de l'obstacle pour détecter la collision
                prod_vec2 = cross2D(vect_rob, point2_obs - point1_rob)
                prod_vec3 = cross2D(vect_obs, point1_rob - point1_obs)
                prod_vec4 = cross2D(vect_obs, point2_rob - point1_obs)

                if (prod_vec1 * prod_vec2) < 0 and (prod_vec3 * prod_vec4) < 0: 
                    return True
                
    cote_salle = [(np.array([0, 0]), np.array([salle.dimensionX, 0])), (np.array([0, salle.dimensionY]), np.array([salle.dimensionX, salle.dimensionY])), (np.array([0, salle.dimensionY]), np.array([0, 0])), (np.array([salle.dimensionX, salle.dimensionY]), np.array([salle.dimensionX, 0]))]
    
    for point1_rob, point2_rob in cote_robot: # collision avec la salle
        for point1_salle, point2_salle in cote_salle: 
            vect_rob = point2_rob - point1_rob
            vect_salle = point2_salle - point1_salle

            prod_vec1 = cross2D(vect_rob, point1_salle - point1_rob)
            prod_vec2 = cross2D(vect_rob, point2_salle - point1_rob)
            prod_vec3 = cross2D(vect_salle, point1_rob - point1_salle)
            prod_vec4 = cross2D(vect_salle, point2_rob - point1_salle)

            if (prod_vec1 * prod_vec2) < 0 and (prod_vec3 * prod_vec4) < 0: 
                return True
    
    return False