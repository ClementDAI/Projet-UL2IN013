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
        if vitesse == 0:
            print("Vitesse à 0")
            return
        
        t=distance//vitesse
        i=0
        while (i<t):
            if (self.direction == 1):
                self.bouger(0,-vitesse)
            if (self.direction == 2):
                self.bouger(vitesse,0)
            if (self.direction == 3):
                self.bouger(0,vitesse)
            if (self.direction == 4):
                self.bouger(-vitesse,0)
            i=i+1
            time.sleep(1)

        r=distance%vitesse
        if (self.direction == 1):
            self.bouger(0,-r)
        if (self.direction == 2):
            self.bouger(r,0)
        if (self.direction == 3):
            self.bouger(0,r)
        if (self.direction == 4):
            self.bouger(-r,0)
        time.sleep(r/vitesse)
        self.vitesse = 0
    
    def tourner(self,GD): #GD = 0 -> Gauche, GD = 1 -> Droite        
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
        self.rob = robot #on stocke le robot pour pouvoir le voir bouger 

    def obstacle(self,x,y):
        self.posx = x
        self.posy = y

    def cree_matrice(self):
        VIDE = 0
        ROBOT = 1
        matrice = [[VIDE for _ in range(self.xmax)] for _ in range(self.ymax)]
        x, y = self.rob.position()
        matrice[y][x] = ROBOT
        return matrice

    def affiche_matrice(self):
        for ligne in self.cree_matrice():
            for case in ligne:
                if case == 0:
                    print('_', end=' ') #si on met un espace on va pas voir les "case" de la matrice juste un R au mileu de rien et je met un espace entre chaque _ pour aérer sinon tout est collé
                else:
                    print('R', end=' ')
            print()     #retour a la ligne dans l affichage


if __name__ == "__main__":
    r = Robot('R1', 3)
    s = Salle(r, 5, 5)
    print("Matrice initiale :")
    s.affiche_matrice()
    r.avancer(1,2)
    print("Matrice Apres avoir avancé de 2 cases vers le bas :")
    s.affiche_matrice()
    r.tourner(0)
    r.avancer(1,2)
    print("Matrice Apres avoir avancé de 2 cases vers la droite :")
    s.affiche_matrice()
    r.tourner(0)
    r.avancer(1,2)
    print("Matrice Apres avoir avancé de 2 cases vers le haut :")
    s.affiche_matrice()
    r.tourner(0)
    r.avancer(1,2)
    print("Matrice Apres avoir avancé de 2 cases vers la gauche :")
    s.affiche_matrice()

