from ClassRobot import robot
from robot import Robot
from obstacle import Obstacle
from salle import Salle
from AfficherTexte import afficher_le_texte 
from AfficherTexte import affiche_capteur
import numpy as np
import pygame
import math
import time

#test temporaire pour tester si import marche bien. enlever les pour faire le main

Piece = Salle(21.5,12.5)
Piece.ajoutObstacle(Obstacle(2,2,3,1,45))
Piece.ajoutObstacle(Obstacle(15,6,2,2,160))
print(Piece.ListeObstacle[0].x)

def cross2D(a, b):
    return a[0]*b[1] - a[1]*b[0]

def collision(rob, salle):
    """
    rob : paramètre de classe Robot
    salle : paramètre de classe Salle
    Collision va renvoyer true si la position du robot est bloqué par un obsctacle de la salle sinon false
    """

    angle = np.deg2rad(rob.angle)
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
        inclinaison = i.inclinaison
        larg2 = i.largeur / 2
        long2 = i.longueur / 2 
        cos2 = np.cos(inclinaison)
        sin2 = np.sin(inclinaison)
        if ((rob.x > xObstacle - largeurObstacle / 2) and (rob.x < xObstacle + largeurObstacle / 2) and (rob.y > yObstacle - longueurObstacle / 2) and (rob.y < yObstacle + longueurObstacle / 2)):
            return True
        coinObsHG = np.array([(xObstacle - (larg2 * cos2) - (long2 * sin2)), (yObstacle - (larg2 * sin2) + (long2 * cos2))]) # calculs des coins de l'obstacle
        coinObsHD = np.array([(xObstacle + (larg2 * cos2) - (long2 * sin2)), (yObstacle + (larg2 * sin2) + (long2 * cos2))])
        coinObsBG = np.array([(xObstacle - (larg2 * cos2) + (long2 * sin2)), (yObstacle - (larg2 * sin2) - (long2 * cos2))])
        coinObsBD = np.array([(xObstacle + (larg2 * cos2) + (long2 * sin2)), (yObstacle + (larg2 * sin2) - (long2 * cos2))])
        cote_obs = [(coinObsHG, coinObsHD), (coinObsBG, coinObsBD), (coinObsBG, coinObsHG), (coinObsBD, coinObsHD)]
        for point1_rob, point2_rob in cote_robot:
            for point1_obs, point2_obs in cote_obs: 
                vect_rob = point2_rob - point1_rob
                vect_obs = point2_obs - point1_obs

                prod_vec1 = cross2D(vect_rob, point1_obs - point1_rob) # calcul des produits vectoriels entre les cotés du robots et celle de l'obstacle pour détecter la collision
                prod_vec2 = cross2D(vect_rob, point2_obs - point1_rob)
                prod_vec3 = cross2D(vect_obs, point1_rob - point1_obs)
                prod_vec4 = cross2D(vect_obs, point2_rob - point1_obs)

                if (prod_vec1 * prod_vec2) < 0 and (prod_vec3 * prod_vec4) < 0: 
                    return True
                
    cote_salle = [(np.array([0, 0]), np.array([salle.dimensionX, 0])), (np.array([0, salle.dimensionY]), np.array([salle.dimensionX, salle.dimensionY])), (np.array([0, salle.dimensionY]), np.array([0, 0])), (np.array([salle.dimensionX, salle.dimensionY]), np.array([salle.dimensionX, 0]))]
    
    for point1_rob, point2_rob in cote_robot: # collision avec la salle
        for point1_salle, point2_salle in cote_salle: 
            vect_rob = point2_rob - point1_rob
            vect_salle = point2_salle - point1_salle

            prod_vec1 = cross2D(vect_rob, point1_salle - point1_rob)
            prod_vec2 = cross2D(vect_rob, point2_salle - point1_rob)
            prod_vec3 = cross2D(vect_salle, point1_rob - point1_salle)
            prod_vec4 = cross2D(vect_salle, point2_rob - point1_salle)

            if (prod_vec1 * prod_vec2) < 0 and (prod_vec3 * prod_vec4) < 0: 
                return True
    
    return False

def collision_point(x, y, salle):

    if x < 0 or x > salle.dimensionX or y < 0 or y > salle.dimensionY:
        return True

    for obs in salle.ListeObstacle:
        dx = x - obs.x
        dy = y - obs.y

        cos_o = np.cos(-obs.inclinaison)
        sin_o = np.sin(-obs.inclinaison)

        local_x = dx * cos_o - dy * sin_o
        local_y = dx * sin_o + dy * cos_o

        if abs(local_x) <= obs.largeur/2 and abs(local_y) <= obs.longueur/2:
            return True
    return False

def update_capteur(rob, salle):
        """rob : objet de classe robot
            salle : salle ou se trouve rob
            la fonction va mettre à jour la valeur de capteur de rob"""
        distance = 0
        angle = rob.angle
        sin = math.sin(math.radians(angle))
        cos = -math.cos(math.radians(angle))
        rob_tmp = robot(rob.x, rob.y, rob.vangGauche, rob.vangDroite, rob.angle, rob.longueur, 0.1)
        old_x, old_y = rob_tmp.x, rob_tmp.y
        while not(collision(rob_tmp, salle)):
            rob_tmp.x += sin * 0.1  # pas de 0.1 pour le vecteur capteur
            rob_tmp.y += cos * 0.1
            distance += 0.1
        
        rob_tmp.x, rob_tmp.y = old_x, old_y
        rob.capteur = round(distance, 2)


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

    angle_rad = math.radians(dexter.angle)
    distance_totale = (dexter.longueur / 2 + dexter.capteur) * SCALE # longueur de la ligne du capteur
    fin_x = robot_x + distance_totale * math.sin(angle_rad)
    fin_y = robot_y - distance_totale * math.cos(angle_rad)

    pygame.draw.line(screen, (255, 0, 0), (robot_x, robot_y), (fin_x, fin_y), 2) # Dessin de la ligne directement sur l'écran
    
    rotated_surf = pygame.transform.rotate(robot_surf, -dexter.angle)
    rotated_rect = rotated_surf.get_rect(center=(int(robot_x), int(robot_y)))
    screen.blit(rotated_surf, rotated_rect)
    

def affiche_salle(screen, dexter, OFFSET_X, OFFSET_Y, SCALE):
    """Dessine les obstacles et le robot"""
    screen.fill((255, 255, 255))
    
    for obs in Piece.ListeObstacle:
        obs_x = OFFSET_X + obs.x * SCALE
        obs_y = OFFSET_Y + obs.y * SCALE
        obs_largeur = obs.largeur * SCALE
        obs_longueur = obs.longueur * SCALE
        taille = math.sqrt(obs_largeur**2 + obs_longueur**2)
        centre = taille // 2
        obs_surface = pygame.Surface((taille,taille))
        obs_surface.fill((255, 255, 255))
        obs_surface.set_colorkey((255, 255, 255))
        pygame.draw.rect(obs_surface,"red", (centre - obs_largeur/2, centre - obs_longueur/2, obs_largeur, obs_longueur))
        pygame.draw.circle(obs_surface, "darkred", (int(centre), int(centre)), 3)
        rotate = pygame.transform.rotate(obs_surface, -obs.inclinaison)
        rotate_obs = rotate.get_rect(center=(int(obs_x),int(obs_y)))


        screen.blit(rotate, rotate_obs)
    
    affiche_robot(screen, dexter, OFFSET_X, OFFSET_Y, SCALE)

def carre(screen, dexter, clock, OFFSET_X, OFFSET_Y, SCALE, c):
    """le robot fait un carré de taille cote par cote"""
    for cote in range(4):
        dexter.setVitessesAngulaires(20, 20)
        for i in range(c):
            old_x, old_y = dexter.x, dexter.y
            dexter.avancer()
            update_capteur(dexter,Piece)
            if collision(dexter, Piece):
                dexter.x, dexter.y = old_x, old_y
                print("Collision détectée, arrêt du déplacement")
                return 
            affiche_salle(screen, dexter, OFFSET_X, OFFSET_Y, SCALE)
            afficher_le_texte(screen, 'c')
            affiche_capteur(screen,dexter.capteur)
            pygame.display.flip()
            clock.tick(60)  # Ralenti pour mieux voir
        dexter.setVitessesAngulaires(0, 0)
        dexter.assurer_direction_avant() #si nécessaire, remettre les vitesses en direction "avant"
        angle_cible = (dexter.angle + 90) % 360

        tourne_encore = True
        while tourne_encore:
            erreur = angle_cible - dexter.angle
            while erreur > 180: erreur -= 360
            while erreur < -180: erreur += 360

            if abs(erreur) < 0.5:
                dexter.angle = angle_cible
                tourne_encore = False
            else:
                Kp = 0.1
                vitesse_rot = max(min(Kp * erreur, 5), -5)
                dexter.angle += vitesse_rot
                dexter.normaliser_angle()
            update_capteur(dexter,Piece)
            affiche_salle(screen, dexter, OFFSET_X, OFFSET_Y, SCALE)
            afficher_le_texte(screen, 'c')
            affiche_capteur(screen,dexter.capteur)
            pygame.display.flip()
            clock.tick(60)
        print("Changement de direction")
        time.sleep(1)
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
    dexter = Robot(10,5,0,0,5,10)
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
    dexter = robot(xd, yd, 20, 20, 0, longueur_robot, largeur_robot)
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
            update_capteur(dexter,Piece)
            affiche_capteur(screen,dexter.capteur)
            afficher_le_texte(screen, commande_actuelle)
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            print("utilisation de la commande c")
            commande_actuelle='c'
            c = 50 #taille du carré
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
            dx = cible_x - dexter.x
            dy = dexter.y - cible_y  
            angle_cible = math.degrees(math.atan2(dx, dy))
            erreur_angle = angle_cible - dexter.angle
            while erreur_angle > 180: erreur_angle -= 360
            while erreur_angle < -180: erreur_angle += 360
            distance = math.sqrt((cible_x - dexter.x)**2 + (cible_y - dexter.y)**2)

            if distance > 0.1:
                if abs(erreur_angle) > 2:
                    dexter.rotation(cible_x, cible_y)
                else:
                    old_x, old_y = dexter.x, dexter.y
                    dexter.avancer() 
                    update_capteur(dexter, Piece)
                    affiche_capteur(screen,dexter.capteur)

                    if collision(dexter, Piece):
                        dexter.x, dexter.y = old_x, old_y
                        mode_deplacement = False
                        commande_actuelle = "menu"
                        print("Collision détectée, arrêt du déplacement")
            else:
                dexter.x = round(cible_x, 2)
                dexter.y = round(cible_y, 2)
                mode_deplacement = False
                commande_actuelle = "menu"
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

menu()
