from R2D2.simulation.robot import Robot
import unittest

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(0, 0, 0, 0, 0, 0.2, 0.1)

    def test_coins(self):
        coins = self.robot.coins()
        self.assertEqual(coins[0][0][0], -0.05)
        self.assertEqual(coins[0][0][1], 0.1)
        self.assertEqual(coins[0][1][0], 0.05)
        self.assertEqual(coins[0][1][1], 0.1)
        self.assertEqual(coins[1][0][0], -0.05)
        self.assertEqual(coins[1][0][1], -0.1)
        self.assertEqual(coins[1][1][0], 0.05)
        self.assertEqual(coins[1][1][1], -0.1)

    def test_calculerVitesses(self):
        robot = Robot(0, 0, 1, 1, 0, 0.3, 0.2) #ligne droite
        vlin, vang = robot.calculerVitesses()
        self.assertEqual(vlin, 0.05)
        self.assertEqual(vang, 0)

    def test_calculerVitesses_roues_opposees(self):
        robot2 = Robot(0, 0, -1, 1, 0, 0.3, 0.2) #roues opposées
        robot2.calculerVitesses()
        self.assertEqual(robot2.vitesseLineaire, 0)
        self.assertGreater(robot2.vitesseAngulaire, 0)
