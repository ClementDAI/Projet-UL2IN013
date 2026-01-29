import pygame
#Vector2 : pour les poisitons : ajouter 50 a x d'une position : pos + pygame.Vector2(50, 0)
pygame.init()
screen = pygame.display.set_mode((1440, 810))  # Taille de la fenetre largeur x hauteur
pygame.display.set_caption("Simulation Dexter") #Titre de la fenetre
clock = pygame.time.Clock() #Clock pour les fps
running = True #pour la boucle infinie

robot_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) #robot commence au centre de la fenetre

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #fermer la fenetre si on appuie sur la croix
            running = False
    
    screen.fill("white") #couleur de la fenetre

    pygame.draw.rect(screen, "black", pygame.Rect(robot_pos.x - 20, robot_pos.y - 35, 40, 70)) #70 pixels de haut 40 pixel de large et centré sur la position de base

    pygame.draw.line(screen, "red", robot_pos + pygame.Vector2(0, -35), robot_pos + pygame.Vector2(0, -50), 2) #ligne pour la direction
    pygame.draw.line(screen, "red", robot_pos + pygame.Vector2(0, -50), robot_pos + pygame.Vector2(-5, -45), 2) #coté gauche de la fleche
    pygame.draw.line(screen, "red", robot_pos + pygame.Vector2(0, -50), robot_pos + pygame.Vector2(5, -45), 2) #coté droit de la fleche
    
    pygame.display.flip() #met a jour l'ecran

    clock.tick(60) #max fps

pygame.quit()
