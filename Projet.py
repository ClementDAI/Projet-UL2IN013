import time

class Robot(object):

    def __init__(self,nom,direction):
        self.nom = nom
        self.x = 0
        self.y = 0
        self.vitesse = 0
        self.direction = direction #1=Nord 2=Est 3=Sud 4=Ouest

    def bouger(self,x1,y1):
        self.x = self.x + x1
        self.y = self.y + y1

    def position(self):
        return self.x,self.y

    def avancer(self,vitesse,distance):
        self.vitesse = vitesse
        t=distance//vitesse
        i=0
        while (i<t):
            if (self.direction == 1):
                bouger(self,vitesse,0)
            if (self.direction == 2):
                bouger(self,0,vitesse)
            if (self.direction == 3):
                bouger(self,-vitesse,0)
            if (self.direction == 4):
                bouger(self,0,-vitesse)
            i=i+1
            time.sleep(1)

        t=distance%vitesse
        if (self.direction == 1):
            bouger(self,t,0)
        if (self.direction == 2):
            bouger(self,0,t)
        if (self.direction == 3):
            bouger(self,-t,0)
        if (self.direction == 4):
            bouger(self,0,-t)
        time.sleep(t/vitesse)
        self.vitesse = 0
    
    def Tourner(self,GD): #GD = 0 -> Gauche, GD = 1 -> Droite        
        if (GD == 0):
            if self.direction == 1:
                self.direction = 4
            else:
                self.direction = self.direction - 1
        else :
            if self.direction == 4:
                self.direction = 1
            else :
                self.direction += 1

    
class Salle(object):
    def __init__(self,robot,xmax,ymax):
        self.xmax = xmax
        self.ymax = ymax
        self.rob = position(robot) #Tuple(x,y)

    def obstacle(self,x,y):
        self.posx = x
        self.posy = y

