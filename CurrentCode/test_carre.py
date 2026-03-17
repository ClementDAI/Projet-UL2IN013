from carre import Carre
from robot import Robot
import numpy as np

def test_carre():
    rob = Robot(0, 0, 1, 1, 0, 5, 2)
    test_Carre = Carre(1, rob)
    test_Carre.start()
    while not test_Carre.stop():
        test_Carre.step()
        rob.x += rob.vitesseLineaire * 0.1 * np.sin(np.radians(rob.angle))
        rob.y -= rob.vitesseLineaire * 0.1 * np.cos(np.radians(rob.angle))
        rob.angle = (rob.angle + rob.vitesseAngulaire) % 360
    print("Position fin :", rob.x, rob.y, rob.angle)
    
test_carre()