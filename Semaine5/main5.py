from affichage import Affichage #changer les noms qd le module sera codé
from controller import Controller
from simulation import Simulation
from robot import Robot
from salle import Salle
from obstacle import Obstacle
import pygame

pygame.init()
simulation = Simulation(10, 10, 10, 5, 100, 100)
affichage = Affichage(simulation)
controller = Controller(simulation.rob)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    controller.updateController(5, 5)
    simulation.updateSimulation()
    affichage.updateAffichage() 

