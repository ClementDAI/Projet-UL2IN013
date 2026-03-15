import numpy as np

class Salle(object):

    def __init__(self,longueur,largeur):
        self.dimensionX = longueur #j'ai mit dimensionX en nom d argument pcq robot et obstacle s appelle deja comme sa pour pas trop ce répéter
        self.dimensionY = largeur #j'ai mit dimensionY en nom d argument pcq robot et obstacle s appelle deja comme sa pour pas trop ce répéter
        self.ListeObstacle = [] #initialisé par une liste vide
    
    def coins(self):
        return [(np.array([0, 0]), np.array([self.dimensionX, 0])), (np.array([0, self.dimensionY]), np.array([self.dimensionX, self.dimensionY])), (np.array([0, self.dimensionY]), np.array([0, 0])), (np.array([self.dimensionX, self.dimensionY]), np.array([self.dimensionX, 0]))]