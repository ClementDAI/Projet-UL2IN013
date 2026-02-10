from ClassRobot import robot
from ClassObstacle import obstacle
from ClassSalle import salle
from AfficherTexte import afficher_le_texte 
import numpy as np
import pygame
import math

#test temporaire pour tester si import marche bien. enlever les pour faire le main

Piece = salle(10,10)
Piece.ajoutObstacle(obstacle(2,2,1,1))
Piece.ajoutObstacle(obstacle(4,5,2,2))
print(Piece.ListeObstacle[0].x)

def collision(rob, salle):
    """
    rob : paramètre de classe Robot
    salle : paramètre de classe Salle
    Collision va renvoyer true si la position du robot est bloqué par un obsctacle de la salle sinon false
    """

    angle = np.deg2rad(rob.angle - 90)
    cos = np.cos(angle)
    sin = np.sin(angle)
    larg = rob.largeur / 2
    long = rob.longueur / 2
    
    coinHG = np.array([(rob.x - (larg * cos) - (long * sin)), (rob.y - (larg * sin) + (long * cos))]) # calcul des coins du robots
    coinHD = np.array([(rob.x + (larg * cos) - (long * sin)), (rob.y + (larg * sin) + (long * cos))]) 
    coinBG = np.array([(rob.x - (larg * cos) + (long * sin)), (rob.y - (larg * sin) - (long * cos))])
    coinBD = np.array([(rob.x + (larg * cos) + (long * sin)), (rob.y + (larg * sin) - (long * cos))])

    cote_robot = [(coinHG, coinHD), (coinBG, coinBD), (coinBG, coinHG), (coinBD, coinHD)]

    for i in salle.ListeObstacle:
        xObstacle, yObstacle = i.x, i.y
        largeurObstacle = i.largeur
        longueurObstacle = i.longueur
        coinObsHG = np.array([(xObstacle - (largeurObstacle / 2)), (yObstacle + (longueurObstacle / 2))]) # calculs des coins de l'obstacle
        coinObsHD = np.array([(xObstacle + (largeurObstacle / 2)), (yObstacle + (longueurObstacle / 2))])
        coinObsBG = np.array([(xObstacle - (largeurObstacle/ 2)), (yObstacle - (longueurObstacle / 2))])
        coinObsBD = np.array([(xObstacle + (largeurObstacle / 2)), (yObstacle - (longueurObstacle / 2))])
        cote_obs = [(coinObsHG, coinObsHD), (coinObsBG, coinObsBD), (coinObsBG, coinObsHG), (coinObsBD, coinObsHD)]
        for point1_rob, point2_rob in cote_robot:
            for point1_obs, point2_obs in cote_obs: 
                vect_rob = point2_rob - point1_rob
                vect_obs = point2_obs - point1_obs

                prod_vec1 = np.cross(vect_rob, point1_obs - point1_rob) # calcul des produits vectoriels entre les cotés du robots et celle de l'obstacle pour détecter la collision
                prod_vec2 = np.cross(vect_rob, point2_obs - point1_rob)
                prod_vec3 = np.cross(vect_obs, point1_rob - point1_obs)
                prod_vec4 = np.cross(vect_obs, point2_rob - point1_obs)

                if (prod_vec1 * prod_vec2) < 0 and (prod_vec3 * prod_vec4) < 0: 
                    return True
                
    cote_salle = [(np.array([0, 0]), np.array([salle.dimensionX, 0])), (np.array([0, salle.dimensionY]), np.array([salle.dimensionX, salle.dimensionY])), (np.array([0, salle.dimensionY]), np.array([0, 0])), (np.array([salle.dimensionX, salle.dimensionY]), np.array([salle.dimensionX, 0]))]
    
    for point1_rob, point2_rob in cote_robot: # collision avec la salle
        for point1_salle, point2_salle in cote_salle: 
            vect_rob = point2_rob - point1_rob
            vect_salle = point2_salle - point1_salle

            prod_vec1 = np.cross(vect_rob, point1_salle - point1_rob)
            prod_vec2 = np.cross(vect_rob, point2_salle - point1_rob)
            prod_vec3 = np.cross(vect_salle, point1_rob - point1_salle)
            prod_vec4 = np.cross(vect_salle, point2_rob - point1_salle)

            if (prod_vec1 * prod_vec2) < 0 and (prod_vec3 * prod_vec4) < 0: 
                return True
    
    return False

def affiche_robot(screen, dexter, OFFSET_X, OFFSET_Y, SCALE):
    """Dessine le robot"""
    robot_x = OFFSET_X + dexter.x * SCALE
    robot_y = OFFSET_Y + dexter.y * SCALE
    robot_w = dexter.largeur * SCALE
    robot_h = dexter.longueur * SCALE
    
    size = int(max(robot_w, robot_h) * 1.5) # Taille du carré englobant le robot pour la rotation
    robot_surf = pygame.Surface((size, size))
    robot_surf.fill((255, 255, 255))
    robot_surf.set_colorkey((255, 255, 255))
    
    rect_x = (size - robot_w) // 2
    rect_y = (size - robot_h) // 2
    pygame.draw.rect(robot_surf, (0, 100, 255), (rect_x, rect_y, robot_w, robot_h))
    
    
    pygame.draw.circle(robot_surf, "purple", (int(size/2), int(rect_y)), 3) #point violet pour mieux voir l'orientation du robot
    
    rotated_surf = pygame.transform.rotate(robot_surf, -dexter.angle)
    rotated_rect = rotated_surf.get_rect(center=(int(robot_x), int(robot_y)))
    screen.blit(rotated_surf, rotated_rect)
    screen.blit(rotated_surf, rotated_rect)

def affiche_salle(screen, dexter, OFFSET_X, OFFSET_Y, SCALE):
    """Dessine les obstacles et le robot"""
    screen.fill((255, 255, 255))
    
    for obs in Piece.ListeObstacle:
        obs_x = OFFSET_X + obs.x * SCALE
        obs_y = OFFSET_Y + obs.y * SCALE
        obs_largeur = obs.largeur * SCALE
        obs_longueur = obs.longueur * SCALE
        pygame.draw.rect(screen, "red", (obs_x - obs_largeur/2, obs_y - obs_longueur/2, obs_largeur, obs_longueur))
        pygame.draw.circle(screen, "darkred", (int(obs_x), int(obs_y)), 3)
    
    affiche_robot(screen, dexter, OFFSET_X, OFFSET_Y, SCALE)

def carre(screen, dexter, clock, OFFSET_X, OFFSET_Y, SCALE, c):
    """le robot fait un carré de taille cote par cote"""
    for cote in range(4):
        for i in range(c):
            dexter.avancer()
            affiche_salle(screen, dexter, OFFSET_X, OFFSET_Y, SCALE)
            afficher_le_texte(screen, 'c')
            pygame.display.flip()
            clock.tick(30)  # Ralenti pour mieux voir
        dexter.tourner(90)
        affiche_salle(screen, dexter, OFFSET_X, OFFSET_Y, SCALE)
        afficher_le_texte(screen, 'c')
        pygame.display.flip()

def menu():
    print("Menu simulation :")
    print("1 : test via terminal")
    print("2 : test via interface graphique")
    choix = input("Entrez votre choix : ")
    if choix == "1":
        print("Test via terminal")
        test_terminal()
    elif choix == "2":
        print("Test via interface graphique")
        test_pygame()
    else:
        print("Choix invalide, choissisez 1 ou 2")
        menu()

def test_terminal():
    c = 10 #taille du carré
    (x,y) = (5,5) #destination du robot
    print("Test de la classe robot :")
    dexter = robot(10,5,0,0,5,10)
    print("position initiale de dexter :" + str(dexter.getPosition()))
    print("dexter va faire un carré de {c} par {c}".format(c=c))
    for i in range(c):
        dexter.avancer()
    print("Dexter est en " + str(dexter.getPosition()))
    dexter.tourner(90)
    for i in range(c):
        dexter.avancer()
    print("Dexter est en " + str(dexter.getPosition()))
    dexter.tourner(90)
    for i in range(c):
        dexter.avancer()
    print("Dexter est en " + str(dexter.getPosition()))
    dexter.tourner(90)
    for i in range(c):
        dexter.avancer()
    print("Dexter est en " + str(dexter.getPosition()))
    print("dexter va aller a la position (2,2) où il y a un obstacle") #vous pourrez tester collision ici pour voir si le robot est bloqué ou pas
    dexter.aller_a(2,2)
    print("dexter va aller vers la position définie par l'utilisateur")
    dexter.aller_a(x,y)
    print("position finale de dexter :"+ str(dexter.getPosition()))

def test_pygame():
    pygame.init()
    longueur_salle = 970
    largeur_salle = 600
    screen = pygame.display.set_mode((longueur_salle, largeur_salle))
    pygame.display.set_caption("Simulation de robot")
    clock = pygame.time.Clock()
    SCALE = 40 # Échelle pour convertir les coordonnées de la salle en pixels
    OFFSET_X = 50
    OFFSET_Y = 50
    xd = 10  # position x du robot
    yd = 10  # position y du robot
    longueur_robot = 2  # longueur du robot
    largeur_robot = 1  # largeur du robot
    dexter = robot(xd, yd, 0, 0, longueur_robot, largeur_robot)
    running = True
    commande_actuelle= "menu"
    mode_deplacement = False
    cible_x = 0
    cible_y = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        affiche_salle(screen, dexter, OFFSET_X, OFFSET_Y, SCALE)
        if commande_actuelle is not None:
            afficher_le_texte(screen, commande_actuelle)
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            print("utilisation de la commande c")
            commande_actuelle='c'
            c = 5 #taille du carré
            carre(screen, dexter, clock, OFFSET_X, OFFSET_Y, SCALE, c)
            commande_actuelle="menu"
        
        if keys[pygame.K_a] and not mode_deplacement:
            print("utilisation de la commande a")
            print("La salle fait du 21.5 x 12.5 unités")
            try:
                cible_x = float(input("Entrez X de la destination : "))
                cible_y = float(input("Entrez Y de la destination : "))
                mode_deplacement = True
                commande_actuelle = "a"
            except:
                print("Veuillez entrer des nombres valides.")
        if mode_deplacement:
            distance = math.sqrt((cible_x - dexter.x)**2 + (cible_y - dexter.y)**2)
            if distance > 1:
                dexter.rotation(cible_x, cible_y)
                dexter.avancer()
            else:
                dexter.x = round(cible_x, 2)
                dexter.y = round(cible_y, 2)
                mode_deplacement = False
                commande_actuelle = "menu"
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

menu()
