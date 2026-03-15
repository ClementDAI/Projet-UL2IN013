from robot import Robot
def test_coins():
    robot = Robot(0, 0, 0, 0, 0, 0.2, 0.1) #robot orienté vers le haut
    coins = robot.coins()
    assert coins[0][0][0] == -0.05 and coins[0][0][1] == 0.1 #coin haut-gauche
    assert coins[0][1][0] == 0.05 and coins[0][1][1] == 0.1 #coin haut-droit
    assert coins[1][0][0] == -0.05 and coins[1][0][1] == -0.1 #coin bas-gauche
    assert coins[1][1][0] == 0.05 and coins[1][1][1] == -0.1 #coin bas-droit
    
def test_calculerVitesses():
    robot = Robot(0, 0, 1, 1, 0, 0.3, 0.2) #ligne droite
    vlin, vang = robot.calculerVitesses()
    assert vlin == 0.05
    assert vang == 0

    robot2 = Robot(0, 0, -1, 1, 0, 0.3, 0.2) #roues opposées
    robot2.calculerVitesses()
    assert robot2.vitesseLineaire == 0
    assert robot2.vitesseAngulaire > 0

