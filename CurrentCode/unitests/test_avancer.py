from controller.avancer import Avancer
from simulation.robot import Robot
import math
import numpy as np

def test_avancer():
    rob = Robot(0, 0, 5, 5, 90, 5, 2)
    test_Avancer = Avancer(1, rob)
    test_Avancer.start()
    while not test_Avancer.stop():
        test_Avancer.step()
        rob.x += rob.vitesseLineaire * 0.1 * np.sin(np.radians(rob.angle))
        rob.y -= rob.vitesseLineaire * 0.1 * np.cos(np.radians(rob.angle))
    assert math.isclose(rob.x, 1, abs_tol=1e-6) #is close : == mais pour les float
    assert math.isclose(rob.y, 0, abs_tol=1e-6) #abs_tol : tolérance pour le is close : 0.000001

test_avancer()