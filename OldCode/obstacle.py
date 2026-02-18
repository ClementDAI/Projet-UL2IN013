class Obstacle():

    def __init__(self,x,y,largeur,longueur,inclinaison): #obstacle de forme rectangulaire centré x,y
        self.x = x #coordonnée x du centre du centre de l obstacle
        self.y = y #coordonnée y du centre du centre de l obstacle
        self.longueur = longueur #valeur de sa longueur sur y
        self.largeur = largeur #valeur de sa largeur sur x
        self.inclinaison = inclinaison #obstacle incliné de l'angle {inclinaison} en degré