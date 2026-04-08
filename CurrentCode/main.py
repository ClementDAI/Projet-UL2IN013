from R2D2 import *
import pygame
import time 
pygame.init()
running = True
Simu = True
temps = 0

if Simu:
    simulation = Simulation(47,26,0,13,5,51,51, 4,26,0,13,5)
    affichage = Affichage(simulation)
    traducteur = TraducteurSimu(simulation.rob)
    traducteur2 = TraducteurSimu(simulation.rob2)
# else:
#     creer robot pour robot irl
#     traducteur = TraducteurReel()
controller = Controller(traducteur)
controller2 = Controller(traducteur2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    deb = time.time() #secondes passés
    simulation.updateSimulation(temps)
    affichage.updateAffichage()
    controller.update()
    fin = time.time()
    temps = fin - deb



    