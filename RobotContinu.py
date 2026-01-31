import pygame
#Vector2 : pour les poisitons : ajouter 50 a x d'une position : pos + pygame.Vector2(50, 0)
pygame.init()
screen = pygame.display.set_mode((1440, 810))  # Taille de la fenetre largeur x hauteur
pygame.display.set_caption("Simulation Dexter") #Titre de la fenetre
clock = pygame.time.Clock() #Clock pour les fps
vitesse = 100 #vitesse de base

def menu():
    pygame.display.set_caption("Menu")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    simulation()
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    option()
                if event.key == pygame.K_3 or event.key == pygame.K_KP3 or event.key == pygame.K_ESCAPE:
                    quitter()
        screen.fill("white")
        font = pygame.font.Font(None, 74)
        title_text = font.render("Menu", True, "black")
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))

        font = pygame.font.Font(None, 50)
        option1_text = font.render("1. Lancer la simulation", True, "black")
        option2_text = font.render("2. Option", True, "black")
        option3_text = font.render("3. Quitter", True, "black")

        screen.blit(option1_text, (screen.get_width() // 2 - option1_text.get_width() // 2, 250))
        screen.blit(option2_text, (screen.get_width() // 2 - option2_text.get_width() // 2, 350))
        screen.blit(option3_text, (screen.get_width() // 2 - option3_text.get_width() // 2, 450))

        pygame.display.flip()
        clock.tick(60)

def option():
    screen.fill("white")
    font = pygame.font.Font(None, 74)
    title_text = font.render("Options de Vitesse", True, "black")
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))
    pygame.display.flip()
    global vitesse
    boucle = True
    while boucle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        font = pygame.font.Font(None, 50)
        option1_text = font.render("Appuyez sur Q pour Vitesse Lente (100 pixels/seconde)", True, "black")
        option2_text = font.render("Appuyez sur S pour Vitesse Moyenne (200 pixels/seconde)", True, "black")
        option3_text = font.render("Appuyez sur D pour Vitesse Rapide (400 pixels/seconde)", True, "black")
        screen.blit(option1_text, (screen.get_width() // 2 - option1_text.get_width() // 2, 200))
        screen.blit(option2_text, (screen.get_width() // 2 - option2_text.get_width() // 2, 250))
        screen.blit(option3_text, (screen.get_width() // 2 - option3_text.get_width() // 2, 300))
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            vitesse = 100
        elif keys[pygame.K_s]:
            vitesse = 200
        elif keys[pygame.K_d]:
            vitesse = 400
        if keys [pygame.K_q] or keys[pygame.K_s] or keys[pygame.K_d]:
            screen.fill("white")
            font = pygame.font.Font(None, 50)
            text = font.render(f"Vitesse définie à {vitesse} pixels par frame", True, "black")
            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 300))
            pygame.display.flip()
            pygame.time.delay(2000)  #Pause de 2 secondes pour montrer la sélection
            boucle = False

def simulation():
    font = pygame.font.Font(None, 74)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("white")
        font = pygame.font.Font(None, 50)
        text2 = font.render("Lancement de la simulation...", True, "black")
        text3 = font.render("Contrôles : flèches directionnelles", True, "black")
        screen.blit(text2, (screen.get_width() // 2 - text2.get_width() // 2, 350))
        screen.blit(text3, (screen.get_width() // 2 - text3.get_width() // 2, 400))
        pygame.display.flip()
        pygame.time.delay(3000)  # Pause de 3 secondes pour montrer la sélection
        waiting = False

    if not waiting:
        running = True #pour la boucle infinie
        robot_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) #robot commence au centre de la fenetre
        robot_angle = 0  #angle pour faire les rotations

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #fermer la fenetre si on appuie sur la croix
                running = False
        
        screen.fill("white") #couleur de la fenetre

        robot_surface = pygame.Surface((80, 100), pygame.SRCALPHA)  #Surface où on va dessiner le robot, et qui permet les déplacements et rotations
        pygame.draw.rect(robot_surface, "black", pygame.Rect(20, 15, 40, 70)) #70 pixels de haut 40 pixel de large et centré sur la surface
        pygame.draw.line(robot_surface, "red", (40, 0), (40, 15), 2) #ligne pour la direction
        pygame.draw.line(robot_surface, "red", (40, 0), (35, 5), 2) #coté gauche de la fleche
        pygame.draw.line(robot_surface, "red", (40, 0), (45, 5), 2) #coté droit de la fleche
        font = pygame.font.Font(None, 30)
        menu_text = font.render("Menu : Echap", True, "black")
        screen.blit(menu_text, (10, 0))

        rotated_robot = pygame.transform.rotate(robot_surface, robot_angle)  #robot tourné avec variable angle
        robot_rect = rotated_robot.get_rect(center=(robot_pos.x, robot_pos.y))
        screen.blit(rotated_robot, robot_rect.topleft)
            
        keys = pygame.key.get_pressed() #inputs
        dimension = pygame.display.get_window_size() 
        longueur,largeur = dimension

        if (keys[pygame.K_UP] or keys[pygame.K_z]) and robot_pos.y > 40:
            if robot_angle != 0:
                robot_angle = 0 
            robot_pos.y -= vitesse * dt
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and robot_pos.y < largeur - 40:
            if robot_angle != 180:
                robot_angle = 180
            robot_pos.y += vitesse * dt
        if (keys[pygame.K_LEFT] or keys[pygame.K_q]) and robot_pos.x > 40:
            if robot_angle != 90:
                robot_angle = 90
            robot_pos.x -= vitesse * dt
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and robot_pos.x < longueur - 40:
            if robot_angle != 270:
                robot_angle = 270
            robot_pos.x += vitesse * dt
        
        if keys[pygame.K_ESCAPE]:  #Retour au menu principal
            running = False
            menu()


        pygame.display.flip() #met a jour l'ecran

        dt = clock.tick(60)/1000 #max fps diviser pour passer de miliseconde en seconde
    pygame.quit()

def quitter():
    pygame.quit()
    exit()

menu()
