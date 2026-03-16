

class Boucle():
    def __init__(self,n,strat):
        self.cur = -1
        self.nbIt = n
        self.strat = strat
    
    def start(self):
        self.cur = 0

    def step(self):
        if self.stop():
            return
        while not strat.stop():
            strat.step()
        self.cur+=1

    def stop(self):
        return self.cur >= self.nbIt


