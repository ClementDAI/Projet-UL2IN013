from ClassRobot import robot
from ClassObstacle import obstacle
from ClassSalle import salle
import numpy as np

#test temporaire pour tester si import marche bien. enlever les pour faire le main
dexter = robot(10,5,0,0,5,10)
print(dexter.getPosition())
Piece = salle(10,10)
Piece.ajoutObstacle(obstacle(2,2,1,1))
Piece.ajoutObstacle(obstacle(4,5,2,2))
print(Piece.ListeObstacle[0].x)
print("dexter va faire un carré de 5 par 5")
for i in range(5):
    dexter.avancer()
print(dexter.getPosition())
dexter.tourner(90)
for i in range(5):
    dexter.avancer()
print(dexter.getPosition())
dexter.tourner(90)
for i in range(5):
    dexter.avancer()
print(dexter.getPosition())
dexter.tourner(90)
for i in range(5):
    dexter.avancer()
print(dexter.getPosition())
print("dexter va aller a la position (2,2) ou il y a un obstacle") #vous pourrez tester collision ici pour voir si le robot est bloqué ou pas
dexter.aller_a(2,2)
print(dexter.getPosition())

def collision(rob, salle):
    """
    rob : paramètre de classe Robot
    salle : paramètre de classe Salle
    Collision va renvoyer true si la position du robot est bloqué par un obsctacle de la salle sinon false
    """

    coinHG = np.array([(rob.x - (rob.largeur / 2)), (rob.y + (rob.longueur / 2))]) # problème sur le calcul des coordonnées dans le cas où le robot est incliné
    coinHD = np.array([(rob.x + (rob.largeur / 2)), (rob.y + (rob.longueur / 2))]) # Il faut trouver un moyen de calculer les coins peu importe l'inclinaison
    coinBG = np.array([(rob.x - (rob.largeur / 2)), (rob.y - (rob.longueur / 2))])
    coinBD = np.array([(rob.x + (rob.largeur / 2)), (rob.y - (rob.longueur / 2))])
    cote_robot = [(coinHG, coinHD), (coinBG, coinBD), (coinBG, coinHG), (coinBD, coinHD)]
    for i in salle.ListeObstacle:
        xObstacle, yObstacle = i.x, i.y
        largeurObstacle = i.largeur
        longueurObstacle = i.longueur
        coinObsHG = np.array([(xObstacle - (largeurObstacle / 2)), (yObstacle + (longueurObstacle / 2))])
        coinObsHD = np.array([(xObstacle + (largeurObstacle / 2)), (yObstacle + (longueurObstacle / 2))])
        coinObsBG = np.array([(xObstacle - (largeurObstacle/ 2)), (yObstacle - (longueurObstacle / 2))])
        coinObsBD = np.array([(xObstacle + (largeurObstacle / 2)), (yObstacle - (longueurObstacle / 2))])
        cote_obs = [(coinObsHG, coinObsHD), (coinObsBG, coinObsBD), (coinObsBG, coinObsHG), (coinObsBD, coinObsHD)]
        for point1_rob, point2_rob in cote_robot:
            for point1_obs, point2_obs in cote_obs: 
                vect_rob = point2_rob - point1_rob
                vect_obs = point2_obs - point1_obs

                prod_vec1 = np.cross(vect_rob, point1_obs - point1_rob)
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

print(collision(dexter, Piece))