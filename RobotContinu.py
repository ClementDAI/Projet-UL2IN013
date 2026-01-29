import pygame

pygame.init()
screen = pygame.display.set_mode((600, 450))  # Taille de la fenetre largeur x hauteur
pygame.display.set_caption("Simulation Dexter") #Titre de la fenetre
clock = pygame.time.Clock() #Clock pour les fps
running = True #pour la boucle infinie
dt = 0

robot_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) #robot commence au centre de la fenetre

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #fermer la fenetre si on appuie sur la croix
            running = False
    
    screen.fill("white") #couleur de la fenetre

    pygame.draw.rect(screen, "black", pygame.Rect(robot_pos.x - 20, robot_pos.y - 15, 30, 40)) #40 pixels de haut 30 pixel de large et centré sur la position de base

    pygame.display.flip()

    clock.tick(60) #max fps

pygame.quit()
