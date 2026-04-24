from R2D2.controller import Controller
from R2D2.robot2I013 import Robot2IN013
from R2D2.traducteur import TraducteurReel
import time 

running = True
temps = 0

robot = Robot2IN013()
traducteur = TraducteurReel(robot)
controller = Controller(traducteur)

while running:
    deb = time.time()
    controller.update()
    fin = time.time()
    temps = fin - deb