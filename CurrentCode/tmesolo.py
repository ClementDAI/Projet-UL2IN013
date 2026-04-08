from R2D2 import *
import pygame
def q1_1():
    pygame.init()
    running = True
    simulation = Simulation(2,6,0,13,5,51,51)
    affichage = Affichage(simulation)
    affichage.updateAffichage()

q1_1()