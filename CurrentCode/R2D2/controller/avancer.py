from ..simulation.robot import Robot
import math

class Avancer:
    def __init__(self, distance, trad):
        self.distance = distance
        self.trad = trad
        
    def start(self):
        self.parcouru = 0
        self.trad.set_vitesse(50,50)

    def step(self):
        self.trad.set_vitesse(50,50)
        self.trad.robot.calculerVitesses() #ligne inutile dcp
        distance = self.trad.robot.vitesseLineaire * 0.1
        self.parcouru += distance
        #les 2 lignes d'au dessus deviennent self.parcouru = self.trad.get_distance_parcourue() 
        # si on utilise la fonction get_distance_parcourue() du traducteur mais je suis pas bien sur 

    def stop(self):
        return self.parcouru >= self.distance or self.trad.rob_vit_nulle()
