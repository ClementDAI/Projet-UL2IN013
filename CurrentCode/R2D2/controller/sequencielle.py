<<<<<<< HEAD
from .avancer import Avancer
from .tourner import Tourner
=======
>>>>>>> fb13e81096299a7abca6dbd4e3a5cc1d1fe96a3f

class Sequencielle:
    def __init__(self, strats):
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