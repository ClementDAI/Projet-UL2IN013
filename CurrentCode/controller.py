from robot import Robot
from carre import Carre
from avancer import Avancer
from tourner import Tourner
from boucle import Boucle
#normalement ici tout marche mais cf boucle.py
class Controller:
    def __init__(self, Robot):
        self.robot = Robot
        self.xprec = Robot.x
        self.yprec = Robot.y
        self.distance_parcourue = 0
        self.action = None
    
    def step(self): 
        """Correspond à updateController """
        self.action = input("Entrez une action : 0 pour Avancer, 1 pour tourner, 2 pour carré, 3 pour s'approcher d'un mur")
    





