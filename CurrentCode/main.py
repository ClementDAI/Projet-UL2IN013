from R2D2 import *
from R2D2.controller.avancer import Avancer
from R2D2.controller.tourner import Tourner
from R2D2.controller.carre import Carre
import pygame
import time 
pygame.init()
running = True
Simu = True
temps = 0

if Simu:
    simulation = Simulation(41,26,0,13,5,51,51, 4,26,0,13,5)
    affichage = Affichage(simulation)
    traducteur = TraducteurSimu(simulation.rob)
    traducteur2 = TraducteurSimu(simulation.rob2)
# else:
#     creer robot pour robot irl
#     traducteur = TraducteurReel()
controller = Controller(traducteur)
controller2 = Controller(traducteur2)
controller.action = [Avancer(2, traducteur), Tourner(180, traducteur), Avancer(2, traducteur)]
controller2.action = [Carre(2, traducteur2)]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    deb = time.time() #secondes passés
    simulation.updateSimulation(temps)
    affichage.updateAffichage()
    controller.update()
    controller2.update()
    fin = time.time()
    temps = fin - deb



    