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

r = Robot("r2d2",vitesse,screen.get_width() / 2,screen.get_height() / 2) # x et y correspond a sa position de départ, ici c est le centre de la fenetre
l1 = r.largeur
l2 = r.longueur

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #fermer la fenetre si on appuie sur la croix
            running = False

    screen.fill("white") #couleur de la fenetre

    pygame.draw.rect(screen, "black", pygame.Rect(r.pos.x - l1/2, r.pos.y - l2/2, l1, l2)) #70 pixels de haut 40 pixel de large et centré sur la position de base

    if (r.angle == 0):
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(0, -r.longueur/2), r.pos + pygame.Vector2(0, -r.longueur/2-15), 2) #ligne pour la direction, 15 la longueur de la fleche
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(0, -r.longueur/2-15), r.pos + pygame.Vector2(-5, -r.longueur/2-10), 2) #coté gauche de la fleche, -5 et +5 pour faire un ligne diagonale entre le bout de la ligne et le bout du coté
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(0, -r.longueur/2-15), r.pos + pygame.Vector2(5, -r.longueur/2-10), 2) #coté droit de la fleche
    
    if (r.angle == 90):
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(r.longueur/2, 0), r.pos + pygame.Vector2(r.longueur/2+15, 0), 2) 
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(r.longueur/2+15, 0), r.pos + pygame.Vector2(r.longueur/2+10, 5), 2)
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(r.longueur/2+15, 0), r.pos + pygame.Vector2(r.longueur/2+10, -5), 2)

    if (r.angle == 180):
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(0, r.longueur/2), r.pos + pygame.Vector2(0, r.longueur/2+15), 2) 
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(0, r.longueur/2+15), r.pos + pygame.Vector2(5, r.longueur/2+10), 2)
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(0, r.longueur/2+15), r.pos + pygame.Vector2(-5, r.longueur/2+10), 2)

    if (r.angle == 270):
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(-r.longueur/2, 0), r.pos + pygame.Vector2(-r.longueur/2-15, 0), 2) 
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(-r.longueur/2-15, 0), r.pos + pygame.Vector2(-r.longueur/2-10, -5), 2) 
        pygame.draw.line(screen, "red", r.pos + pygame.Vector2(-r.longueur/2-15, 0), r.pos + pygame.Vector2(-r.longueur/2-10, 5), 2) 
    
    keys = pygame.key.get_pressed()
    dimension = pygame.display.get_window_size() #Tuple : (longueur,largeur)
    longueur,largeur = dimension 
    if keys[pygame.K_z] and r.pos.y > r.longueur/2 :
        r.angle = 0
        r.avancer_reculer(dt)
        l1 = r.largeur
        l2 = r.longueur
    if keys[pygame.K_s] and r.pos.y < largeur - r.longueur/2:
        r.angle = 180
        r.avancer_reculer(dt)
        l1 = r.largeur
        l2 = r.longueur
    if keys[pygame.K_q] and r.pos.x > r.longueur/2:
        r.angle = 270
        r.avancer_reculer(dt)
        l1 = r.longueur
        l2 = r.largeur
    if keys[pygame.K_d] and r.pos.x < longueur - r.longueur/2:
        r.angle = 90
        r.avancer_reculer(dt)
        l1 = r.longueur
        l2 = r.largeur

    pygame.display.flip() #met a jour l'ecran

    dt = clock.tick(60)/1000 #max fps convertit pour que se soit par seconde avec la division

pygame.quit()
