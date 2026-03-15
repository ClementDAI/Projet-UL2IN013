#from affichage import Affichage
#from controller import Controller
#from simulation import Simulation
#from robot import Robot
from salle import Salle
from obstacle import Obstacle
import pygame

salle = Salle(100, 100)
ob1 = Obstacle(30, 10, 5, 5, 45)
ob2 = Obstacle(50, 50, 10, 10, 192)
ob3 = Obstacle(70, 30, 15, 15, 62)
ob1.ajoutObstacle(salle)
ob2.ajoutObstacle(salle)
ob3.ajoutObstacle(salle)


#simulation = Simulation(dexter,salle)
#affichage = Affichage(simulation)
#controller = Controller(dexter)

# while True:
#     controller.updateController()
#     simulation.updateSimulation()
#     affichage.updateAffichage() 
