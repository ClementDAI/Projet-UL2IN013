from affichage import Affichage #changer les noms qd le module sera codé
from controller import Controller
from simulation import Simulation
from class_robot import Robot
from class_salle import Sall
from class_obstacle import Obstacle
import pygame

pygame.init()
xd = 10
yd = 10
longueur_robot = 2
largeur_robot = 1
dexter = Robot(xd, yd, 20, 20, 0, longueur_robot, largeur_robot)
salle = Salle(100, 100)
ob1 = Obstacle(20, 20, 5, 5)
ob2 = Obstacle(50, 50, 10, 10)
ob3 = Obstacle(70, 70, 15, 15)
salle.ListeObstacle.append(ob1)
salle.ListeObstacle.append(ob2)
salle.ListeObstacle.append(ob3)
simulation = Simulation(dexter,salle)
affichage = Affichage(simulation)
controller = Controller(dexter)

running=True
while True:
    for event in pyagme.event.get():
        if event.type==game.QUIT:
            running=False
    controller.updateController(dexter, 0, 0)
    simulation.updateSimulation(dexter) #a changer surement qd vous aurez fait la fonction
    affichage.updateAffichage() 
