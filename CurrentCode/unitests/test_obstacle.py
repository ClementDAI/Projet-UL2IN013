from R2D2.simulation.obstacle import Obstacle
from R2D2.simulation.salle import Salle
import math
import unittest

class TestObstacle(unittest.TestCase):
    def setUp(self):
        self.salle = Salle(10, 10)
        self.obstacle = Obstacle(5, 5, 2, 2, 0)
        self.obstacle2 = Obstacle(1, 1, 1, 1, math.pi/2)

    def test_obstacle(self):
        self.obstacle.ajoutObstacle(self.salle)
        self.assertEqual(len(self.salle.ListeObstacle), 1)
        self.assertEqual(self.salle.ListeObstacle[0], self.obstacle)
        coins = self.obstacle.coins()
        self.assertEqual(len(coins), 4)
        self.assertLess(coins[0][0][0], coins[0][1][0]) # HG x < HD x
        self.assertGreater(coins[0][0][1], coins[1][0][1]) # HG y > BG y
        self.assertLess(coins[1][0][0], coins[1][1][0]) # BG x < BD x
        self.assertLess(coins[1][0][1], coins[0][0][1]) # BG y < HG y

    def test_obstacle2(self):
        self.obstacle2.ajoutObstacle(self.salle)
        self.assertEqual(len(self.salle.ListeObstacle), 1)
        self.assertEqual(self.salle.ListeObstacle[0], self.obstacle2)
        coins2 = self.obstacle2.coins()
        self.assertEqual(len(coins2), 4)
        self.assertLess(coins2[0][0][1], coins2[0][1][1]) # HG y < HD y
        self.assertLess(coins2[1][0][1], coins2[1][1][1]) # BG y < BD y
        self.assertLess(coins2[0][0][0], coins2[1][0][0]) # HG x < BG x
        self.assertLess(coins2[0][1][0], coins2[1][1][0]) # HD x < BD x