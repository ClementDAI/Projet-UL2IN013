from boucle import Boucle
from avancer import Avancer
from tourner import Tourner
from carre import Carre
from robot import Robot
import math
#regler les problems dans boucles avant de faire les tests
def test_boucle():
    rob = Robot(0, 0, 1, 1, 0, 5, 2)
    boucle = Boucle(Avancer(1, rob), 3, rob)
    boucle.start()
    while not boucle.stop():
        boucle.step()
    assert math.isclose(rob.x, 0, abs_tol=1e-2)
    assert math.isclose(rob.y, -3, abs_tol=1e-2)
    boucle2 = Boucle(Tourner(90, rob), 3, rob)
    boucle2.start()
    while not boucle2.stop():
        boucle2.step()
    assert math.isclose(rob.angle, 270, abs_tol=1e-2)
    rob2 = Robot(0, 0, 1, 1, 0, 5, 2)
    boucle3 = Boucle(Carre(1, rob2), 3, rob2)
    boucle3.start()
    while not boucle3.stop():
        boucle3.step()
    assert math.isclose(rob2.x, 0, abs_tol=1e-2)
    assert math.isclose(rob2.y, 0, abs_tol=1e-2)

test_boucle()
    