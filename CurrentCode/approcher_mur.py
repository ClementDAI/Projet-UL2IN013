from robot import Robot
from avancer import Avancer

class Approcher_mur:
    def __init__(self, rob):
        self.rob = rob
        self.distance = rob.capteur
    
    def start(self):
        self.distance_parcouru = 0

    def step(self):
        strat = Avancer(self.distance, self.rob)
        strat.start()
        if not strat.stop():
            strat.step()
            self.distance_parcouru += strat.parcouru

    def stop(self):
        return self.distance_parcouru >= self.distance
