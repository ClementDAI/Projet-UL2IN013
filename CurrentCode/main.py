from affichage import Affichage
from controller import Controller
from simulation import Simulation
from robot import Robot
from salle import Salle
from obstacle import Obstacle
import pygame

simulation = Simulation(10,10,10,5,100,100)
affichage = Affichage(simulation)
controller = Controller(simulation.rob)

while True:
#     controller.updateController()
#     simulation.updateSimulation()
    affichage.updateAffichage() 
