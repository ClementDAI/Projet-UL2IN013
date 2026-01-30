import pygame
#Vector2 : pour les poisitons : ajouter 50 a x d'une position : pos + pygame.Vector2(50, 0)

while True:
    vitesse = input("Choisissez la vitesse (nombre entier) du robot en pixel/s : ")
    if float(vitesse) % 1 != 0:
        print("Veuillez entrer un nombre entier")
    else :
        vitesse = int(vitesse)
        break


pygame.init()
screen = pygame.display.set_mode((1440, 810))  # Taille de la fenetre largeur x hauteur
pygame.display.set_caption("Simulation Dexter") #Titre de la fenetre
clock = pygame.time.Clock() #Clock pour les fps
running = True #pour la boucle infinie

class Robot(object):
    def __init__(self,nom,speed,x,y):
        self.nom = nom
        self.pos = pygame.Vector2(x,y) #position du robot , avec pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) le robot commence au toujour au centre de la fenetre
        self.angle = 0 # l'angle 0 va correspondre a vers le haut et pour rappel dans pygame x est vers la droite et y vers le bas comme pour la matrice qu on a fait
        self.speed = speed
        self.largeur = 40
        self.longueur = 70

    def avancer_reculer(self,dt):
        if (self.angle == 0):
            self.pos.y -= self.speed * dt
        if (self.angle == 90):
            self.pos.x += self.speed * dt
        if (self.angle == 180):
            self.pos.y += self.speed * dt
        if (self.angle == 270):
            self.pos.x -= self.speed * dt

r = Robot("r2d2",vitesse,screen.get_width() / 2,screen.get_height() / 2) #speed temporairement a 50, il faudra qu il soit ajustable sans toucher le code avec x y correspond au centre de la fenetre comme dit avant

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #fermer la fenetre si on appuie sur la croix
            running = False

    screen.fill("white") #couleur de la fenetre

    pygame.draw.rect(screen, "black", pygame.Rect(r.pos.x - r.largeur/2, r.pos.y - r.longueur/2, r.largeur, r.longueur)) #70 pixels de haut 40 pixel de large et centré sur la position de base

    pygame.draw.line(screen, "red", r.pos + pygame.Vector2(0, -35), r.pos + pygame.Vector2(0, -50), 2) #ligne pour la direction
    pygame.draw.line(screen, "red", r.pos + pygame.Vector2(0, -50), r.pos + pygame.Vector2(-5, -45), 2) #coté gauche de la fleche
    pygame.draw.line(screen, "red", r.pos + pygame.Vector2(0, -50), r.pos + pygame.Vector2(5, -45), 2) #coté droit de la fleche
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        r.angle = 0
        r.avancer_reculer(dt)
    if keys[pygame.K_s]:
        r.angle = 180
        r.avancer_reculer(dt)
    if keys[pygame.K_q]:
        r.angle = 270
        r.avancer_reculer(dt)
    if keys[pygame.K_d]:
        r.angle = 90
        r.avancer_reculer(dt)

    pygame.display.flip() #met a jour l'ecran

    dt = clock.tick(60)/1000 #max fps convertit pour que se soit par seconde avec la division

pygame.quit()
