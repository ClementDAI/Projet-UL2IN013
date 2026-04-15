from R2D2.controller import Controller
from R2D2.robot2I013 import Robot2IN013
from R2D2.traducteur.traducteurReel import TraducteurReel
import time 

running = True
Simu = False
temps = 0

if Simu:
    simulation = Simulation(10,10,100,10,5,96,60)
    affichage = Affichage(simulation)
    traducteur = TraducteurSimu(simulation.rob)
else:
    robot = Robot2IN013()
    traducteur = TraducteurReel(robot)
controller = Controller(traducteur)
while running:
    deb = time.time()
    controller.update()
    fin = time.time()
    temps = fin - deb



    