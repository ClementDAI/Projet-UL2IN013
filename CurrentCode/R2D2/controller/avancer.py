from R2D2.simulation.robot import Robot
import math

class Avancer:
    def __init__(self, distance, rob):
        self.distance = distance
        self.rob = rob
        
    def start(self):
        self.parcouru = 0
        self.rob.vangGauche = 50
        self.rob.vangDroite = 50

    def step(self):
        self.rob.calculerVitesses()
        distance = self.rob.vitesseLineaire * 0.1
        self.parcouru += distance

    def stop(self):
        return self.parcouru >= self.distance or (self.rob.vangGauche == 0 and self.rob.vangDroite == 0)
