from robot import Robot
from tourner import Tourner
import math

def test_tourner():
    rob = Robot(0,-1,1,0,90,6,3)
    test = Tourner(90 ,rob)
    test.start()
    while not test.stop():
        test.step()
        rob.angle = (rob.angle + rob.vitesseAngulaire * 0.2) % 360 # angle compris entre [0, 360]
    assert math.isclose(rob.angle, 180, abs_tol=0.1)
    
test_tourner()