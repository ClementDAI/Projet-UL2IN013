from .carre import Carre
from .avancer import Avancer
from .tourner import Tourner
from .approcher_mur import Approcher_mur

class Controller:
    def __init__(self, trad):
        self.trad = trad
        self.current = -1

        #avancer de 0.5m
        self.action = [Avancer(20, 10, self.trad)]

        #tourner de 90°
        # self.action = [Tourner(90, self.trad)]

        # carré de 0.5m
        # self.action = [Carre(0.5, 10, self.trad)]

        #avancer jusqu'au mur
        # self.action = [Approcher_mur(self.trad)]

    def update(self):
        """Met à jour le controller : démarre, avance, et arrête la stratégie courante."""
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