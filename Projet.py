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

    def avancer(self,salle,vitesse,distance):
        self.vitesse = vitesse
        if vitesse == 0:
            print("Vitesse à 0")
            return
        
        t=distance//vitesse
        i=0
        while (i<t):
            if (self.direction == 1):
                self.bouger(0,-vitesse)
                salle.affiche_matrice()
            if (self.direction == 2):
                self.bouger(vitesse,0)
                salle.affiche_matrice()
            if (self.direction == 3):
                self.bouger(0,vitesse)
                salle.affiche_matrice()
            if (self.direction == 4):
                self.bouger(-vitesse,0)
                salle.affiche_matrice()
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
        print()
        
    def aller_a(self,x_cible,y_cible):
        if not (0 <= x_cible < self.xmax and 0 <= y_cible < self.ymax):
            print("Les coordonnées passées en paramètres ne sont pas dans la salle.")
            return
        mx = x_cible-self.rob.x
        if mx != 0:
            if mx > 0:
                dir = 2 #X cible > X actuel donc on doit aller vers l'est donc 2
            else :
                dir = 4 #vers l'ouest donc 4
            while self.rob.direction != dir:
                tourneD = (dir-self.rob.direction)%4 #calcule le nombre de fois quon doit tourner a droite pour optimiser
                if tourneD <= 2:
                    self.rob.tourner(1)
                else:
                    self.rob.tourner(0)
            self.rob.avancer(self,1, abs(mx)) #abs = val absolue
        my = y_cible-self.rob.y
        if my != 0:
            if my > 0:
                dir = 3
            else :
                dir = 1
            while self.rob.direction != dir:
                tourneD = (dir-self.rob.direction)%4
                if tourneD <= 2:
                    self.rob.tourner(1)
                else:
                    self.rob.tourner(0)
            self.rob.avancer(self,1, abs(my))


if __name__ == "__main__":
    r = Robot('R1', 3)
    while True:
        try:
            xmax = int(input("Entrez la longueur de la matrice : "))
            ymax = int(input("Entrez la largeur de la matrice : "))
            break
        except ValueError:
            print("Veuillez entrer des nombres entier.")
    s = Salle(r, xmax, ymax)
    print("Matrice initiale :")
    s.affiche_matrice()
    while True:
        inp = input("Entrez les coordonnées x y cible (séparées par un espace) : ")
        parts = inp.split()
        if len(parts) != 2:
            if "exit" in parts:
                print("Fin de simulation")
                exit()
            print("Veuillez entrer deux nombres séparés par un espace.")
            continue
        if float(parts[0]) % 1 != 0 or float(parts[1]) % 1 != 0:
            print("Au moins un nombre n'est pas un entier.")
            print("Veuillez entrer deux nombres entiers séparés par un espace.")
            continue
        x, y = map(float, parts) #convertir les string de l'input en int
        x, y = int(x), int(y)
        print(f"Déplacement vers ({x},{y}) :")
        s.aller_a(x, y)
