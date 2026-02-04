class obstacle(objet):

    def __init__(self,longueur,largeur): #obstacle de forme rectangulaire centré x,y
        self.x = x #coordoné x du centre du centre de l obstacle
        self.y = y #coordoné y du centre du centre de l obstacle
        self.longueur = longueur #valeur de sa longueur sur y
        self.largeur = largeur #valeur de sa largeur sur x
    
    def getMoitié(self,cote): #renvoit la distance qu il y a entre son centre et son coté
        if cote == "gauche" or cote == "droite":
            return self.largeur/2
        if cote == "haut" or cote == "bas":
            return self.longueur/2