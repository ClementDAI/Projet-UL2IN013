from robot import Robot
from salle import Salle
from obstacle import Obstacle
from controller import Controller

class Simulation:
    def __init__(self, xd, yd, longueur_robot, largeur_robot, xsalle, ysalle):
        self.rob = Robot(xd, yd, -20, -20, 110, longueur_robot, largeur_robot)
        self.salle = Salle(xsalle, ysalle)
        ob1 = Obstacle(30, 10, 5, 5, 45)
        ob2 = Obstacle(50, 50, 10, 10, 192)
        ob3 = Obstacle(70, 30, 15, 15, 62)
        self.salle.ListeObstacle.append(ob1)
        self.salle.ListeObstacle.append(ob2)
        self.salle.ListeObstacle.append(ob3)
        self.controller = Controller(self.rob)