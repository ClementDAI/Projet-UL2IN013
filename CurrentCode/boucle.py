from avancer import Avancer
from tourner import Tourner
from carre import Carre
from robot import Robot

#Boucle pour faire n fois une stratégie
#on arrive pas a faire en sorte que la stratégie lance une instance entiere et pas juste un step et donc on peut pas gérer
#les conditions d'arrêt de la stratégie et du coup on peut pas faire n fois la stratégie

class Boucle():
    def __init__(self, strat, n, rob):
        self.cur = -1
        self.nbIt = n
        self.rob = rob
        self.strategie = strat
    
    def start(self):
        self.cur = 0
        self.strategie.start()

    def step(self):
        if self.stop():
            return
        
        while self.cur < self.nbIt:
            while not self.strategie.stop():
                self.strategie.step()
            self.cur += 1
            self.strategie.start()

    def stop(self):
        return self.cur >= self.nbIt


