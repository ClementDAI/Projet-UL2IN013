from affichage.affichage import Affichage
from simulation.simulation import Simulation
import pygame

pygame.init()
simulation = Simulation(10,10,100,10,5,100,50)
affichage = Affichage(simulation)
controller = simulation.controller
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    simulation.updateSimulation()
    affichage.updateAffichage() 
    controller.update()