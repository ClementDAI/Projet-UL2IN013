from R2D2.controller.avancer import Avancer
from R2D2.controller.tourner import Tourner
from R2D2.controller.carre import Carre
from R2D2.controller.approcher_mur import Approcher_mur
from R2D2.controller.sequencielle import Sequencielle
from R2D2.simulation.robot import Robot
import math
import numpy as np
import unittest

class TestAvancer(unittest.TestCase):
    def setUp(self):
        self.rob = Robot(0, 0, 5, 5, 90, 5, 2)
        self.test_Avancer = Avancer(1, self.rob)

    def test_avancer(self):
        self.test_Avancer.start()
        while not self.test_Avancer.stop():
            self.test_Avancer.step()
            self.rob.x += self.rob.vitesseLineaire * 0.1 * np.sin(np.radians(self.rob.angle))
            self.rob.y -= self.rob.vitesseLineaire * 0.1 * np.cos(np.radians(self.rob.angle))
        self.assertTrue(math.isclose(self.rob.x, 1, abs_tol=1e-6)) #is close : == mais pour les float
        self.assertTrue(math.isclose(self.rob.y, 0, abs_tol=1e-6)) #abs_tol : tolérance pour le is close : 0.000001

class TestTourner(unittest.TestCase):
    def setUp(self):
        self.rob = Robot(0,-1,1,0,90,6,3)
        self.test = Tourner(90 ,self.rob)

    def test_tourner(self):
        self.test.start()
        while not self.test.stop():
            self.test.step()
            self.rob.angle = (self.rob.angle + self.rob.vitesseAngulaire * 0.2) % 360 # angle compris entre [0, 360]
        self.assertTrue(math.isclose(self.rob.angle, 180, abs_tol=0.1))

class TestCarre(unittest.TestCase):
    def setUp(self):
        self.rob = Robot(0, 0, 1, 1, 0, 5, 2)
        self.test_Carre = Carre(1, self.rob)

    def test_carre(self):
        self.test_Carre.start()
        while not self.test_Carre.stop():
            self.test_Carre.step()
            self.rob.x += self.rob.vitesseLineaire * 0.1 * np.sin(np.radians(self.rob.angle))
            self.rob.y -= self.rob.vitesseLineaire * 0.1 * np.cos(np.radians(self.rob.angle))
            self.rob.angle = (self.rob.angle + self.rob.vitesseAngulaire) % 360
        self.assertTrue(math.isclose(self.rob.x, 0, abs_tol=1e-6))
        self.assertTrue(math.isclose(self.rob.y, 0, abs_tol=1e-6))
        self.assertTrue(math.isclose(self.rob.angle, 0, abs_tol=1e-6))


class TestApprocherMur(unittest.TestCase):
    def setUp(self):
        self.rob = Robot(0, 0, 1, 1, 0, 5, 2)
        self.test_approcher_mur = Approcher_mur(self.rob)

    def test_approcher_mur(self):
        self.test_approcher_mur.start()
        while not self.test_approcher_mur.stop():
            self.test_approcher_mur.step()
            self.rob.x += self.rob.vitesseLineaire * 0.1 * np.sin(np.radians(self.rob.angle))
            self.rob.y -= self.rob.vitesseLineaire * 0.1 * np.cos(np.radians(self.rob.angle))
            self.rob.capteur = max(0, self.rob.capteur - self.rob.vitesseLineaire * 0.1)
        self.assertTrue(math.isclose(self.rob.capteur, 0, abs_tol=1e-6))

class TestSequencielle(unittest.TestCase):
    def setUp(self):
        self.rob = Robot(0, 0, 1, 1, 0, 5, 2)
        self.test_Sequencielle = Sequencielle(self.rob, [Avancer(1, self.rob), Tourner(90, self.rob)])

    def test_sequencielle(self):
        self.test_Sequencielle.start()
        while not self.test_Sequencielle.stop():
            self.test_Sequencielle.step()
            self.rob.x += self.rob.vitesseLineaire * 0.1 * np.sin(np.radians(self.rob.angle))
            self.rob.y -= self.rob.vitesseLineaire * 0.1 * np.cos(np.radians(self.rob.angle))
            self.rob.angle = (self.rob.angle + self.rob.vitesseAngulaire * 0.2) % 360
        self.assertTrue(math.isclose(self.rob.y, -1, abs_tol=1e-6))
        self.assertTrue(math.isclose(self.rob.x, 0, abs_tol=1e-6))
        self.assertTrue(math.isclose(self.rob.angle, 90, abs_tol=0.1))


if __name__ == '__main__':
    unittest.main()