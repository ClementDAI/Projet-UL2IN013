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
print("dexter avance de 5 pixels vers le haut")
for i in range(5):
    dexter.avancer()
    print(dexter.getPosition())
print("dexter tourne de 90° vers la droite et avance de 5 pixels")
dexter.tourner(90)
for i in range(5):
    dexter.avancer()
    print(dexter.getPosition())

def collision(rob, salle):
    """
    rob : paramètre de classe Robot
    salle : paramètre de classe Salle
    Collision va renvoyer true si la position du robot est bloqué par un obsctacle de la salle sinon false
    """

    Robx_min = (rob.x - rob.largeur / 2)
    Robx_max = (rob.x + rob.largeur / 2)
    Roby_min = (rob.y - rob.longueur / 2)
    Roby_max = (rob.y + rob.longueur / 2)
    for obs in salle.ListeObstacle:
        Obsx_min = (obs.x - obs.largeur / 2)
        Obsx_max = (obs.x + obs.largeur / 2)
        Obsy_min = (obs.y - obs.longueur / 2)
        Obsy_max = (obs.y + obs.longueur / 2)
        if not(Robx_max <= Obsx_min or Robx_min >= Obsx_max or Roby_max <= Obsy_min or Roby_min >= Obsy_max): # la fonction collision fonctionne uniquement si le robot a une direction vers le haut ou le bas
            return True
    return False
    

collision(dexter, Piece)