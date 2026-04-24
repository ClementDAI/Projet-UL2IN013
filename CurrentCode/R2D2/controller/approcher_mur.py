from ..simulation.robot import Robot
from .avancer import Avancer

class Approcher_mur:
    def __init__(self, trad):
        self.trad = trad
    
    def start(self):
        distance = self.trad.get_capteur() #on lit la distance avant de commencer a avancer pour pas que le robot se mette a avancer s'il est deja collé au mur
        self.strat = Avancer(distance, 10, self.trad)
        self.strat.start()

    def step(self):
        if not self.strat.stop():
            self.strat.step()

    def stop(self):
        return self.strat.stop() # on avance jusqu'a que le capteur devienne 0
