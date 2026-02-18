from ClassRobot import robot 

class balise(robot):
    #représente une balise qui va repprendre les fonctions avancer, tourner "

    def __init__(self,x,y,vitesse,angle,longueur,largeur):
        #On appelle le constructeur de la classe parente (robot)
        robot.__init__(self,x=x,y=y,vitesse=vitesse,angle=angle,longueur=longueur,largeur=largeur)
