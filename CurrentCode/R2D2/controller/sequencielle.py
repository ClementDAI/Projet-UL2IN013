
class Sequencielle:
    def __init__(self, rob, strats):
        self.rob = rob
        self.strats = strats
        self.cur = -1
    
    def start(self):
        self.cur = -1
    
    def step(self):
        if self.stop():
            return
        
        if self.cur < 0 or self.strats[self.cur].stop():
            self.cur += 1
            self.strats[self.cur].start()
        self.strats[self.cur].step()
    
    def stop(self):
        return self.cur == len(self.strats) - 1 and self.strats[self.cur].stop()