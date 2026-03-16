from robot import Robot
from carre import Carre
from avancer import Avancer
from tourner import Tourner
from boucle import Boucle
#normalement ici tout marche mais cf boucle.py
class Controller:
    def __init__(self, Robot,simulation):
        self.robot = Robot
        self.xprec = Robot.x
        self.yprec = Robot.y
        self.distance_parcourue = 0
        self.simulation = simulation
    
    def step(self): 
        """Correspond à updateController """
        carre = Carre(1,self.robot)
        boucle = Boucle(1,carre)
        boucle.step()




