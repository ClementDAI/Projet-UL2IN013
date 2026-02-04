class robot(object):

    def __init__(self,x,y,vitesse,angle):
        self.x = x #coordoné x du centre du robot
        self.y = y #coordoné y du centre du robot
        self.vitesse = vitesse #vitesse en pixel par seconde
        self.angle = angle #angle en degrés de son orientation avec l'angle a 0
    
    def getPostion(self):
        return self.x,self.y #renvoie le x et y du robot
    