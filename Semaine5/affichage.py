import pygame
import math
from class_robot import Robot
from class_salle import Salle
from simulation import Simulation
from controller import Controller

class Affichage:
    def __init__(self, simulation):
        self.longueur_salle = 970
        self.largeur_salle = 600
        self.screen = pygame.display.set_mode((self.longueur_salle, self.largeur_salle))
        self.SCALE = 40 # Échelle pour convertir les coordonnées de la salle en pixels
        self.OFFSET_X = 50
        self.OFFSET_Y = 50
        self.simulation = simulation

    def affiche_robot(self):
        """Dessine le robot et sa ligne de capteur"""
        dexter = self.simulation.rob #recup du robot de simulation
        robot_x = self.OFFSET_X + dexter.x * self.SCALE
        robot_y = self.OFFSET_Y + dexter.y * self.SCALE
        robot_w = dexter.largeur * self.SCALE
        robot_h = dexter.longueur * self.SCALE
    
        size = int(max(robot_w, robot_h) * 1.5) # Taille du carré englobant le robot pour la rotation
        robot_surf = pygame.Surface((size, size))
        robot_surf.fill((255, 255, 255))
        robot_surf.set_colorkey((255, 255, 255))
    
        rect_x = (size - robot_w) // 2
        rect_y = (size - robot_h) // 2
        pygame.draw.rect(robot_surf, (0, 100, 255), (rect_x, rect_y, robot_w, robot_h))
    
    
        pygame.draw.circle(robot_surf, "purple", (int(size/2), int(rect_y)), 3) #point violet pour mieux voir l'orientation du robot

        angle_rad = math.radians(dexter.angle)
        distance_totale = (dexter.longueur / 2 + dexter.capteur) * self.SCALE #pour l'instant je ne sais pas ou et comment va etre calculer la distance du capteur donc je par du pricncipe que c dans les variable de robot
        fin_x = robot_x + distance_totale * math.sin(angle_rad)
        fin_y = robot_y - distance_totale * math.cos(angle_rad)

        pygame.draw.line(self.screen, (255, 0, 0), (robot_x, robot_y), (fin_x, fin_y), 2) # Dessin de la ligne directement sur l'écran
    
        rotated_surf = pygame.transform.rotate(robot_surf, -dexter.angle)
        rotated_rect = rotated_surf.get_rect(center=(int(robot_x), int(robot_y)))
        self.screen.blit(rotated_surf, rotated_rect)

    
    def affiche_salle(self):
        """Dessine les obstacle et la salle"""
        self.screen.fill((255, 255, 255))
        Piece = self.simulation.salle # recup de la classe salle de simulation
        for obs in Piece.ListeObstacle:
            obs_x = self.OFFSET_X + obs.x * self.SCALE
            obs_y = self.OFFSET_Y + obs.y * self.SCALE
            obs_largeur = obs.largeur * self.SCALE
            obs_longueur = obs.longueur * self.SCALE
            taille = math.sqrt(obs_largeur**2 + obs_longueur**2)
            centre = taille // 2
            obs_surface = pygame.Surface((taille,taille))
            obs_surface.fill((255, 255, 255))
            obs_surface.set_colorkey((255, 255, 255))
            pygame.draw.rect(obs_surface,"red", (centre - obs_largeur/2, centre - obs_longueur/2, obs_largeur, obs_longueur))
            pygame.draw.circle(obs_surface, "darkred", (int(centre), int(centre)), 3)
            rotate = pygame.transform.rotate(obs_surface, -obs.inclinaison)
            rotate_obs = rotate.get_rect(center=(int(obs_x),int(obs_y)))
            
            self.screen.blit(rotate, rotate_obs)

    def affiche_capteur_compteur(self):
        font = pygame.font.Font(None, 24)
        capteur = font.render(f"capteur de distance : {self.simulation.rob.capteur}" , True, "black")
        self.screen.blit(capteur, (10, 550))

    def updateAffichage(self):
        """
        Met a jour l'ensemble de affichage necessaire
        """
        self.affiche_salle()
        self.affiche_robot()
        self.affiche_capteur_compteur()
        pygame.display.flip()