from ClassRobot import robot
from ClassObstacle import obstacle
from ClassSalle import salle
from ClassBalise import balise #ici
import numpy as np
import pygame
import math

#test temporaire pour tester si import marche bien. enlever les pour faire le main

Piece = salle(10,10)
Piece.ajoutObstacle(obstacle(2,2,1,1))
Piece.ajoutObstacle(obstacle(4,5,2,2))
print(Piece.ListeObstacle[0].x)
#ma_balise=balise(15,5,0.5,0,0.5,0.5)
#print("Position de la balise:", ma_balise.getPosition())

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

def affiche_balise(screen,balise_test, OFFSET_X, OFFSET_Y, SCALE): #ici
    """dessine la balise """
    balise_x=OFFSET_X+balise_test.x *SCALE
    balise_y=OFFSET_Y+balise_test.y*SCALE

    pygame.draw.circle(screen, (255, 215, 0), (int(balise_x), int(balise_y)), 7) #a la 


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
            pygame.display.flip()
            clock.tick(30)  # Ralenti pour mieux voir
        dexter.tourner(90)
        affiche_salle(screen, dexter, OFFSET_X, OFFSET_Y, SCALE)
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
    print("dexter va aller vers vers la position définie par l'utilisateur")
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

    print("configuration de la balise ") #ici
    x_balise= float(input("Entrez la position X initiale de la Balise:"))#position x de la balise 
    y_balise= float(input("Entrez la position Y initiale de la Balise:")) #position y de la balise 
    longueur_balise=0.5
    largeur_balise=0.5
    balise_test=balise(x_balise, y_balise,0,0,longueur_balise, largeur_balise ) # a la 
    suivi_actif=False  # a la 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN: #ici 
                if event.key == pygame.K_b:
                    suivi_actif = not suivi_actif # Alterne entre True et False
                    print(f"Mode suivi : {suivi_actif}") # a la 

        affiche_salle(screen, dexter, OFFSET_X, OFFSET_Y, SCALE)
        affiche_balise(screen,balise_test, OFFSET_X, OFFSET_Y,SCALE) #ici

        keys = pygame.key.get_pressed()

        if suivi_actif:
            distance=math.sqrt((balise_test.x - dexter.x)**2 + (balise_test.y - dexter.y)**2)
            if distance >2.5:
                dexter.rotation(balise_test.x, balise_test.y)
                dexter.avancer() # a la


        
        if keys[pygame.K_c]:
            c = 5 #taille du carré
            carre(screen, dexter, clock, OFFSET_X, OFFSET_Y, SCALE, c)
        
        if keys[pygame.K_a]:
            try:
                x = float(input("Entrez la coordonnée x de destination (unités) : "))
                y = float(input("Entrez la coordonnée y de destination (unités) : "))
            except ValueError:
                print("Veuillez entrer des nombres valides.")
            else:
                # Animer le mouvement pas à pas
                distance = math.sqrt((x - dexter.x)**2 + (y - dexter.y)**2)
                while distance > 1:
                    dexter.rotation(x, y)
                    dexter.avancer()
                    affiche_salle(screen, dexter, OFFSET_X, OFFSET_Y, SCALE)
                    pygame.display.flip()
                    clock.tick(30)  # Ralenti pour mieux voir
                    distance = math.sqrt((x - dexter.x)**2 + (y - dexter.y)**2)
                dexter.x = round(x, 2)
                dexter.y = round(y, 2)
                affiche_salle(screen, dexter, OFFSET_X, OFFSET_Y, SCALE)
                pygame.display.flip()

                # Déplacement manuel de la balise avec les flèches du clavier

           
        
        if keys[pygame.K_q]:
            balise_test.x -= 0.1
        if keys[pygame.K_d]:
            balise_test.x += 0.1
        if keys[pygame.K_z]:
            balise_test.y -= 0.1
        if keys[pygame.K_s]:
            balise_test.y += 0.1
            
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

menu()
