class Salle(object):

    def __init__(self,longueur,largeur):
        self.dimensionX = longueur #j'ai mit dimensionX en nom d argument pcq robot et obstacle s appelle deja comme sa pour pas trop ce répéter
        self.dimensionY = largeur #j'ai mit dimensionY en nom d argument pcq robot et obstacle s appelle deja comme sa pour pas trop ce répéter
        self.ListeObstacle = [] #initialisé par une liste vide 

    def ajoutObstacle(self,obstacle): 
        """
        Cette fonction ajoute un obstacle(x,y,longueur,largeur) dans la liste de la classe salle:
        usage: salle.ajoutObstacle(obstacle) 
        """
        self.ListeObstacle.append(obstacle) #le parametre doit etre une classe obstacle