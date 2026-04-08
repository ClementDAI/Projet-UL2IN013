from R2D2 import *
import pygame
#Q1.1
pygame.init()
running = True
simulation = Simulation(5,55,90,10,5,100,60)
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

#Q1.5
class Hexagone:
    def __init__(self, cote, trad):
        self.cote = cote
        self.trad = trad 
        self.strats = Boucle(Sequencielle([Avancer(cote, trad), Tourner(72, trad)]), 5, trad)
        self.cur = -1
    def start(self):
        self.strats.start()

    def step(self):
        self.strats.step()

    def stop(self):
        return self.strats.stop()

#Q2.1