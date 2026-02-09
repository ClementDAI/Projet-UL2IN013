from ClassRobot import robot
from ClassObstacle import obstacle
from ClassSalle import salle
import numpy as np
import pygame

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

    coinHG = np.array([(rob.x - (rob.largeur / 2)), (rob.y + (rob.longueur / 2))]) # problème sur le calcul des coordonnées dans le cas où le robot est incliné
    coinHD = np.array([(rob.x + (rob.largeur / 2)), (rob.y + (rob.longueur / 2))]) # Il faut trouver un moyen de calculer les coins peu importe l'inclinaison
    coinBG = np.array([(rob.x - (rob.largeur / 2)), (rob.y - (rob.longueur / 2))])
    coinBD = np.array([(rob.x + (rob.largeur / 2)), (rob.y - (rob.longueur / 2))])
    cote_robot = [(coinHG, coinHD), (coinBG, coinBD), (coinBG, coinHG), (coinBD, coinHD)]
    for i in salle.ListeObstacle:
        xObstacle, yObstacle = i.x, i.y
        largeurObstacle = i.largeur
        longueurObstacle = i.longueur
        coinObsHG = np.array([(xObstacle - (largeurObstacle / 2)), (yObstacle + (longueurObstacle / 2))])
        coinObsHD = np.array([(xObstacle + (largeurObstacle / 2)), (yObstacle + (longueurObstacle / 2))])
        coinObsBG = np.array([(xObstacle - (largeurObstacle/ 2)), (yObstacle - (longueurObstacle / 2))])
        coinObsBD = np.array([(xObstacle + (largeurObstacle / 2)), (yObstacle - (longueurObstacle / 2))])
        cote_obs = [(coinObsHG, coinObsHD), (coinObsBG, coinObsBD), (coinObsBG, coinObsHG), (coinObsBD, coinObsHD)]
        for point1_rob, point2_rob in cote_robot:
            for point1_obs, point2_obs in cote_obs: 
                vect_rob = point2_rob - point1_rob
                vect_obs = point2_obs - point1_obs

                prod_vec1 = np.cross(vect_rob, point1_obs - point1_rob)
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
    xd = longueur_salle/2
    yd = largeur_salle/2
    longueur_robot = 40
    largeur_robot = 20
    dexter = robot(xd, yd, 0, 0, longueur_robot, largeur_robot)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))#fond

        #obstacles
        for obs in Piece.ListeObstacle:
            obs_x = OFFSET_X + obs.x * SCALE
            obs_y = OFFSET_Y + obs.y * SCALE
            obs_largeur = obs.largeur * SCALE
            obs_longueur = obs.longueur * SCALE
            pygame.draw.rect(screen, "red", (obs_x - obs_largeur/2, obs_y - obs_longueur/2, obs_largeur, obs_longueur))
            #centre utilisé pour début a commenter apres
            pygame.draw.circle(screen, "black", (int(obs_x), int(obs_y)), 3)
        
        #robot
        pygame.draw.rect(screen, "black", (dexter.x - dexter.largeur / 2, dexter.y - dexter.longueur / 2, dexter.largeur, dexter.longueur))

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

menu()