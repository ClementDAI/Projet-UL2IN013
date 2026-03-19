from R2D2.simulation.salle import Salle
import unittest
    
class TestSalle(unittest.TestCase):
    def setUp(self):
        self.salle = Salle(10, 5)
        self.coins = self.salle.coins()
    def test_salle(self):
        self.assertEqual(self.coins[0][0][0], 0)
        self.assertEqual(self.coins[0][0][1], 0)
        self.assertEqual(self.coins[0][1][0], 10)
        self.assertEqual(self.coins[0][1][1], 0)
        self.assertEqual(self.coins[1][0][0], 0)
        self.assertEqual(self.coins[1][0][1], 5)
        self.assertEqual(self.coins[1][1][0], 10)
        self.assertEqual(self.coins[1][1][1], 5)
    
if __name__ == '__main__':
    unittest.main()