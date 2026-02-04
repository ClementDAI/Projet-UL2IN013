from ClassRobot import robot
from ClassObstacle import obstacle
from ClassSalle import salle

#test temporaire pour tester si import marche bien. enlever les pour faire le main
dexter = robot(10,5,0,0,0,0)
print(dexter.getPosition())
Piece = salle(10,10)
Piece.ajoutObstacle(obstacle(2,2,1,1))
Piece.ajoutObstacle(obstacle(5,5,1,1))
print(Piece.ListeObstacle[0].x)