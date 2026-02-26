from affichage import Affichage #changer les noms qd le module sera codé
from controller import Controller
from simulation import Simulation
from robot import Robot
from salle import Salle
from obstacle import Obstacle
import pygame

pygame.init()
xd = 10
yd = 10
longueur_robot = 10
largeur_robot = 5
dexter = Robot(xd, yd, -20, -20, 110, longueur_robot, largeur_robot)
salle = Salle(100, 100)
ob1 = Obstacle(30, 10, 5, 5, 45)
ob2 = Obstacle(50, 50, 10, 10, 192)
ob3 = Obstacle(70, 30, 15, 15, 62)
salle.ListeObstacle.append(ob1)
salle.ListeObstacle.append(ob2)
salle.ListeObstacle.append(ob3)
simulation = Simulation(dexter,salle)
affichage = Affichage(simulation)
controller = Controller(dexter)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    controller.updateController(5, 5)
    simulation.updateSimulation()
    affichage.updateAffichage() 

