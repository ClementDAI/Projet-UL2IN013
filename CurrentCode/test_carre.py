from carre import Carre
from robot import Robot
import math

def test_carre():
    rob = Robot(0, 0, 1, 1, 0, 5, 2)
    test_Carre = Carre(1, rob)
    test_Carre.start()
    while not test_Carre.stop():
        print(rob.x, rob.y, rob.angle)
        test_Carre.step()
    print("Position fin :", rob.x, rob.y)
    
test_carre()