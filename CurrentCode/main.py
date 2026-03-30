from R2D2 import *
from R2D2.simulation import Robot
from R2D2.simulation import Salle
import pygame

rob = Robot(10, 10, -20, -20, 100, 10, 5)
salle = Salle(96, 60)
pygame.init()
running = True
Simu = True

if Simu:
    simulation = Simulation(rob, salle)
    affichage = Affichage(simulation)
    traducteur = TraducteurSimu(rob)
#else
controller = Controller(traducteur)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    simulation.updateSimulation()
    affichage.updateAffichage()
    controller.update()
    