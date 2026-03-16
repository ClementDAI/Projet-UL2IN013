from avancer import Avancer
from tourner import Tourner
from carre import Carre
from robot import Robot

#Boucle pour faire n fois une stratégie
#on arrive pas a faire en sorte que la stratégie lance une instance entiere et pas juste un step et donc on peut pas gérer
#les conditions d'arrêt de la stratégie et du coup on peut pas faire n fois la stratégie

class Boucle():
    def __init__(self,n,indice, rob):
        self.cur = -1
        self.nbIt = n
        self.indice = indice
        self.rob = rob
        self.strategie = None
        self.strat = [Avancer(1, self.rob), Tourner(90, self.rob), Carre(1, self.rob)]
    
    def start(self):
        self.cur = 0
        self.strategie = self.strat[self.indice]
        self.strategie.start()

    def step(self):
        while not self.strategie.stop():
            self.strategie
            print(self.rob.x, self.rob.y, self.rob.angle)
            self.cur+=1

    def stop(self):
        return self.cur >= self.nbIt


