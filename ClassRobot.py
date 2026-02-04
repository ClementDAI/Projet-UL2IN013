class robot(object):

    def __init__(self,x,y,vitesse,angle,longueur,largeur):
        self.x = x #coordoné x du centre du robot
        self.y = y #coordoné y du centre du robot
        self.vitesse = vitesse #vitesse en pixel par seconde
        self.angle = angle #angle en degrés de son orientation avec l'angle a 0
        self.longueur = longueur #valeur de sa longueur sur y
        self.largeur = largeur #valeur de sa largeur sur x
    

    
    def getPosition(self):
        return self.x,self.y #renvoie le x et y du robot
    
    def tourner(self, angle): #Angle négatif ou positif
        self.angle += angle % 360 
    