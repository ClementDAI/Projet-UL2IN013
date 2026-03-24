from .avancer import Avancer

class Approcher_mur:
    def __init__(self, rob):
        self.rob = rob
        self.distance = rob.capteur
    
    def start(self):
        self.strat = Avancer(self.distance, self.rob)
        self.strat.start()

    def step(self):
        if not self.strat.stop():
            self.strat.step()

    def stop(self):
        return self.strat.stop() # on avance jusqu'a que le capteur devienne 0
