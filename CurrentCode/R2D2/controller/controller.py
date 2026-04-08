from .carre import Carre
from .avancer import Avancer
from .tourner import Tourner
from .approcher_mur import Approcher_mur
from .hexagone import Hexagone
#a modifier apres avoir testé que tout marche avec le traducteur simu et réel

class Controller:
    def __init__(self, trad):
        self.trad = trad
        self.strat = ""
        self.action = [ Carre(5,trad)]
        self.current = -1
    
    def update(self): 
        """met à jour le controller """
        '''if self.action == None:
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
        else:'''
        if self.current < 0 and len(self.action) > 0:
            self.current = 0
            self.action[self.current].start()
        if self.current >= 0:
            if not self.action[self.current].stop():
                self.action[self.current].step()
            elif self.current < len(self.action) - 1:
                self.current += 1
                self.action[self.current].start()
            else:
                self.trad.set_vitesse_nulle()


