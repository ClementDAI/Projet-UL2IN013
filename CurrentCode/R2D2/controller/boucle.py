from .sequencielle import Sequencielle

class Boucle:
    def __init__(self, strategie, n, trad):
        self.cur = -1
        self.nbIt = n
        self.trad = trad
        self.strategie = strategie

    def start(self):
        self.cur = 0
        self.strategie.start()

    def step(self):
        if self.stop():
            return
        
        if self.strategie.stop():
            self.cur += 1
            if not self.stop():
                self.strategie.start()
        else:
            self.strategie.step()


    def stop(self):
        return self.cur >= self.nbIt


