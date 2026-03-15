from avancer import Avancer
from robot import Robot
import math

def test_avancer():
    rob = Robot(0, 0, 1, 1, 0, 5, 2)
    test_Avancer = Avancer(1, rob)
    test_Avancer.start()
    while not test_Avancer.stop():
        test_Avancer.step()
    assert math.isclose(rob.x, 0, abs_tol=1e-6)
    assert math.isclose(rob.y, -1, abs_tol=1e-6)
    
test_avancer()