from R2D2.simulation.salle import Salle
def test_salle():
    salle = Salle(10, 5)
    coins = salle.coins()
    assert coins[0][0][0] == 0 and coins[0][0][1] == 0 #coin bas-gauche
    assert coins[0][1][0] == 10 and coins[0][1][1] == 0 #coin bas-droit
    assert coins[1][0][0] == 0 and coins[1][0][1] == 5 #coin haut-gauche
    assert coins[1][1][0] == 10 and coins[1][1][1] == 5 #coin haut-droit