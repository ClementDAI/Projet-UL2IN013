from robot import Robot
from tourner import Tourner

def test_tourner():
    rob = Robot(0,0,0,0,271,6,3)
    test = Tourner(90,rob)
    test.start()
    while not test.stop():
        test.update()
    assert rob.angle == 361
    
test_tourner()