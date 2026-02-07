from ClassRobot import robot
from ClassObstacle import obstacle
from ClassSalle import salle

#test temporaire pour tester si import marche bien. enlever les pour faire le main
dexter = robot(10,5,0,0,5,10)
print(dexter.getPosition())
Piece = salle(10,10)
Piece.ajoutObstacle(obstacle(2,2,1,1))
Piece.ajoutObstacle(obstacle(5,5,1,1))
print(Piece.ListeObstacle[0].x)

def collision(rob, salle):
    """
    rob : paramètre de classe Robot
    salle : paramètre de classe Salle
    Collision va renvoyer true si la position du robot est bloqué par un obsctacle de la salle sinon false
    """

    coinHG_x, coinHG_y = ((rob.x - (rob.largeur / 2)), (rob.y + (rob.longueur / 2)))
    coinHD_x, coinHD_y = ((rob.x + (rob.largeur / 2)), (rob.y + (rob.longueur / 2)))
    coinBG_x, coinBG_y = ((rob.x - (rob.largeur / 2)), (rob.y - (rob.longueur / 2)))
    coinBD_x, coinBD_y = ((rob.x + (rob.largeur / 2)), (rob.y - (rob.longueur / 2)))
    

collision(dexter, Piece)