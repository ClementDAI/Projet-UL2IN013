from R2D2 import *
import pygame
#Q1.1
def q11():
    pygame.init()
    running = True
    simulation = Simulation(5,55,90,10,5,100,60)
    affichage = Affichage(simulation)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        simulation.updateSimulation()
        affichage.updateAffichage()
#Q1.5
def q15():
    pygame.init()
    running = True
    simulation = Simulation(10,10,90,10,5,100,60)
    affichage = Affichage(simulation)
    traducteur = TraducteurSimu(simulation.rob)
    controller = Controller(traducteur)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        simulation.updateSimulation()
        affichage.updateAffichage()
        controller.update()

#Q2.1

def q21():
    pygame.init()
    running = True
    simulation = Simulation(10,30,180,10,5,90,30,180,10,5,100,60)

    affichage = Affichage(simulation)
    traducteur = TraducteurSimu(simulation.rob)
    controller = Controller(traducteur)
    traducteur2 = TraducteurSimu(simulation.rob2)
    controller2 = Controller(traducteur2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        simulation.updateSimulation()
        affichage.updateAffichage()

#Q2.2
def q22():
    pygame.init()
    running = True
    simulation = Simulation(10,30,180,10,5,90,30,180,10,5,100,60)

    affichage = Affichage(simulation)
    traducteur = TraducteurSimu(simulation.rob)
    controller = Controller(traducteur)
    traducteur2 = TraducteurSimu(simulation.rob2)
    controller2 = Controller(traducteur2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        simulation.updateSimulation()
        affichage.updateAffichage()
        controller.update()
        controller2.update()