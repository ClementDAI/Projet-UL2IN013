from .carre import Carre
from .avancer import Avancer
from .tourner import Tourner
from .approcher_mur import Approcher_mur

#a modifier apres avoir testé que tout marche avec le traducteur simu et réel

class Controller:
    def __init__(self, trad):
        self.trad = trad
        self.strat = ""
        self.action = None #[ Avancer(10,self.trad),Tourner(90, self.trad),Carre(10,self.trad)]
        #self.current = -1
    
    def update(self): 
        """met à jour le controller """
        if self.action == None:
            self.strat = input("Entrez une action : 0 pour Avancer, 1 pour tourner, 2 pour carré, 3 pour s'approcher d'un mur, Dessine(True) et Dessine(False) qui set le crayon, change_couleur: ")
            if self.strat == "0":
                valeur = float(input("Distance (positif) que le robot avance : "))
                self.action = Avancer(valeur, self.trad)
                self.action.start()
            
            elif self.strat == "1":
                valeur = float(input("Angle (positif) que le robot doit tourner : "))
                self.action = Tourner(valeur, self.trad)
                self.action.start()
            
            elif self.strat == "2":
                valeur = float(input("Valeur (positif) du coté du carré à tracer par le robot : "))
                self.action = Carre(valeur, self.trad)
                self.action.start()
            
            elif self.strat == "3":
                self.action = Approcher_mur(self.trad)
                self.action.start()

            elif self.strat == "Dessine(True)":
                self.trad.robot.crayon = True
            
            elif self.strat == "Dessine(False)":
                self.trad.robot.crayon = False

            elif self.strat == "change_couleur":
                couleur = input("couleur en anglais (blue initialement) : ")
                self.trad.robot.couleur = couleur
            
            else:
                print("Choix invalide, aucune action, veuillez entrez une action valide : 0, 1, 2, 3")
        else:
            if not self.action.stop():
                self.action.step() 
            else:
                self.action = None

