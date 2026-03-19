from R2D2.simulation.salle import Salle
import unittest
    
class TestSalle(unittest.TestCase):
    def test_salle(self):
        salle = Salle(10, 5)
        coins = salle.coins()
        self.assertEqual(coins[0][0][0], 0)
        self.assertEqual(coins[0][0][1], 0)
        self.assertEqual(coins[0][1][0], 10)
        self.assertEqual(coins[0][1][1], 0)
        self.assertEqual(coins[1][0][0], 0)
        self.assertEqual(coins[1][0][1], 5)
        self.assertEqual(coins[1][1][0], 10)
        self.assertEqual(coins[1][1][1], 5)
    
if __name__ == '__main__':
    unittest.main()