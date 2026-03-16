from obstacle import Obstacle
from salle import Salle
import math

def test_obstacle():
    salle = Salle(10, 10)
    obstacle = Obstacle(5, 5, 2, 2, 0)
    obstacle.ajoutObstacle(salle)
    assert len(salle.ListeObstacle) == 1
    assert salle.ListeObstacle[0] == obstacle
    coins = obstacle.coins()
    assert len(coins) == 4
    assert coins[0][0][0] < coins[0][1][0] # HG x < HD x
    assert coins[0][0][1] > coins[1][0][1] # HG y > BG y
    assert coins[1][0][0] < coins[1][1][0] # BG x < BD x
    assert coins[1][0][1] < coins[0][0][1] # BG y < HG y

    obstacle2 = Obstacle(1,1,1,1, math.pi/2)
    obstacle2.ajoutObstacle(salle)
    assert len(salle.ListeObstacle) == 2
    assert salle.ListeObstacle[1] == obstacle2
    coins2 = obstacle2.coins()
    assert len(coins2) == 4
    assert coins2[0][0][1] < coins2[0][1][1] # HG y < HD y
    assert coins2[1][0][1] < coins2[1][1][1] # BG y < BD y
    assert coins2[0][0][0] < coins2[1][0][0] # HG x < BG x
    assert coins2[0][1][0] < coins2[1][1][0] # HD x < BD x