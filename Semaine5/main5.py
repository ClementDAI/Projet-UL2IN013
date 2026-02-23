from Affichage import Affichage #changer les noms qd le module sera codé
from Controller import Controller
from Simulation import Simulation
from ClassRobot import robot
from ClassSalle import Salle
from ClassObstacle import Obstacle

xd = 10
yd = 10
longueur_robot = 2
largeur_robot = 1
dexter = robot(xd, yd, 20, 20, 0, longueur_robot, largeur_robot)
salle = Salle(100, 100)
ob1 = Obstacle(20, 20, 5, 5)
ob2 = Obstacle(50, 50, 10, 10)
ob3 = Obstacle(70, 70, 15, 15)
salle.ListeObstacle.append(ob1)
salle.ListeObstacle.append(ob2)
salle.ListeObstacle.append(ob3)
simulation = Simulation(salle, dexter)
affichage = Affichage(salle, dexter)
controller = Controller(dexter)

while True:
    controller.updateController(dexter, 0, 0)
    simulation.updateSimulation(dexter) #a changer surement qd vous aurez fait la fonction
    affichage.updateAffichage(dexter) #idem