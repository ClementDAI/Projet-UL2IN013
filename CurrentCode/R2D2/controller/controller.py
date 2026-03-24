from R2D2.controller.carre import Carre
from R2D2.controller.avancer import Avancer
from R2D2.controller.tourner import Tourner
from R2D2.controller.approcher_mur import Approcher_mur

class Controller:
    def __init__(self, trad):
        self.trad = trad
        self.strat = ""
        self.action = None
    
    def update(self): 
        """met à jour le controller """
        if self.action == None:
            self.strat = input("Entrez une action : 0 pour Avancer, 1 pour tourner, 2 pour carré, 3 pour s'approcher d'un mur : ")
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
            
            else:
                print("Choix invalide, aucune action, veuillez entrez une action valide : 0, 1, 2, 3")
        else:
            if not self.action.stop():
                self.action.step() 
            else:
                self.action = None

