import pygame
import math
import numpy as np
from OpenGL.GL import *
import glm

# ─── Shaders GLSL ────────────────────────────────────────────────────────────

# Vertex shader : positionne chaque sommet via les matrices MVP
VERTEX_SHADER = """
#version 330 core
layout(location = 0) in vec3 position;
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;
void main() {
    gl_Position = projection * view * model * vec4(position, 1.0);
}
"""

# Fragment shader : couleur uniforme passée depuis Python
FRAGMENT_SHADER = """
#version 330 core
uniform vec3 couleur;
out vec4 fragColor;
void main() {
    fragColor = vec4(couleur, 1.0);
}
"""

# ─── Géométrie : pavé (boîte aplatie) centré en 0 ────────────────────────────
# Chaque face = 2 triangles = 6 sommets. 6 faces × 6 = 36 sommets.
# Les coordonnées sont en [-0.5, 0.5] sur X et Z, [-0.5, 0.5] sur Y (hauteur).
# On appliquera ensuite une matrice model pour redimensionner et positionner.

VERTICES_BOITE = np.array([
    # Face avant  (z = +0.5)
    -0.5, -0.5,  0.5,   0.5, -0.5,  0.5,   0.5,  0.5,  0.5,
    -0.5, -0.5,  0.5,   0.5,  0.5,  0.5,  -0.5,  0.5,  0.5,
    # Face arrière (z = -0.5)
    -0.5, -0.5, -0.5,   0.5,  0.5, -0.5,   0.5, -0.5, -0.5,
    -0.5, -0.5, -0.5,  -0.5,  0.5, -0.5,   0.5,  0.5, -0.5,
    # Face gauche  (x = -0.5)
    -0.5, -0.5, -0.5,  -0.5, -0.5,  0.5,  -0.5,  0.5,  0.5,
    -0.5, -0.5, -0.5,  -0.5,  0.5,  0.5,  -0.5,  0.5, -0.5,
    # Face droite  (x = +0.5)
     0.5, -0.5, -0.5,   0.5,  0.5,  0.5,   0.5, -0.5,  0.5,
     0.5, -0.5, -0.5,   0.5,  0.5, -0.5,   0.5,  0.5,  0.5,
    # Face dessus  (y = +0.5)
    -0.5,  0.5,  0.5,   0.5,  0.5,  0.5,   0.5,  0.5, -0.5,
    -0.5,  0.5,  0.5,   0.5,  0.5, -0.5,  -0.5,  0.5, -0.5,
    # Face dessous (y = -0.5)
    -0.5, -0.5,  0.5,   0.5, -0.5, -0.5,   0.5, -0.5,  0.5,
    -0.5, -0.5,  0.5,  -0.5, -0.5, -0.5,   0.5, -0.5, -0.5,
], dtype=np.float32)

# Vertices d'une ligne (segment) pour le capteur et les bords de la salle.
# On passera les deux extrémités via la matrice model.
VERTICES_LIGNE = np.array([
    0.0, 0.0, 0.0,
    1.0, 0.0, 0.0,
], dtype=np.float32)


# ─── Utilitaires shaders ─────────────────────────────────────────────────────

def _compiler_shader(source, type_shader):
    """Compile un shader GLSL et retourne son ID GPU."""
    shader = glCreateShader(type_shader)
    glShaderSource(shader, source)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        raise RuntimeError(glGetShaderInfoLog(shader).decode())
    return shader

def _creer_programme():
    """Compile et link le programme shader (vertex + fragment)."""
    vs = _compiler_shader(VERTEX_SHADER, GL_VERTEX_SHADER)
    fs = _compiler_shader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    prog = glCreateProgram()
    glAttachShader(prog, vs)
    glAttachShader(prog, fs)
    glLinkProgram(prog)
    glDeleteShader(vs)
    glDeleteShader(fs)
    return prog

def _creer_vao(vertices):
    """Envoie un tableau numpy de vertices au GPU et retourne le VAO."""
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)
    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    # slot 0 : 3 floats par sommet, pas de stride ni offset
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)
    glBindVertexArray(0)
    return vao


# ─── Classe Affichage3D ───────────────────────────────────────────────────────

class Affichage3D:
    """
    Remplace Affichage en utilisant PyOpenGL pour le rendu 3D.
    L'interface publique est identique : __init__(simulation) + updateAffichage().
    
    Utilisation dans main.py :
        from R2D2.affichage3D.affichage3D import Affichage3D
        affichage = Affichage3D(simulation)
        # puis en boucle :
        affichage.updateAffichage()
    """

    # Couleurs RGB normalisées [0.0, 1.0] pour chaque élément
    COULEUR_SOL        = (0.15, 0.15, 0.15)   # gris très foncé
    COULEUR_BORDURE    = (0.8,  0.8,  0.8)    # blanc cassé
    COULEUR_ROBOT      = (0.1,  0.4,  1.0)    # bleu
    COULEUR_ROBOT_DIR  = (0.6,  0.1,  0.9)    # violet : indicateur d'orientation
    COULEUR_CAPTEUR    = (1.0,  0.2,  0.2)    # rouge : rayon capteur
    COULEUR_OBSTACLE   = (0.85, 0.2,  0.1)    # rouge brique
    COULEUR_OBS_CENTRE = (0.5,  0.05, 0.05)   # rouge foncé : centre obstacle

    # Hauteur 3D des objets (axe Y en OpenGL = axe vertical)
    HAUTEUR_ROBOT    = 2.0
    HAUTEUR_OBSTACLE = 3.0
    HAUTEUR_SOL      = 0.2   # dalle très fine sous la salle

    def __init__(self, simulation):
        self.simulation = simulation

        # Dimensions de la salle en unités monde
        self.larg_monde = simulation.salle.dimensionX
        self.long_monde = simulation.salle.dimensionY

        # Taille de la fenêtre en pixels
        self.WIN_W = 970
        self.WIN_H = 650   # 50 px en plus pour le HUD texte en bas

        # Crée la fenêtre pygame avec contexte OpenGL
        pygame.display.set_mode(
            (self.WIN_W, self.WIN_H),
            pygame.DOUBLEBUF | pygame.OPENGL
        )
        pygame.display.set_caption("R2D2 - Vue 3D")

        # Active le test de profondeur (les faces cachées ne s'affichent pas)
        glEnable(GL_DEPTH_TEST)
        glClearColor(*self.COULEUR_SOL, 1.0)

        # Compile les shaders une seule fois
        self.programme = _creer_programme()

        # Récupère les emplacements des variables uniform dans le shader
        self.loc_model      = glGetUniformLocation(self.programme, "model")
        self.loc_view       = glGetUniformLocation(self.programme, "view")
        self.loc_projection = glGetUniformLocation(self.programme, "projection")
        self.loc_couleur    = glGetUniformLocation(self.programme, "couleur")

        # Envoie les géométries de base au GPU
        self.vao_boite = _creer_vao(VERTICES_BOITE)   # pavé réutilisé pour robot + obstacles
        self.vao_ligne = _creer_vao(VERTICES_LIGNE)   # segment réutilisé pour capteur + bords

        # ── Matrices caméra ──────────────────────────────────────────────────
        # Vue de dessus : caméra positionnée au-dessus du centre de la salle,
        # regardant vers le bas (target = centre au sol, up = axe Z pour orienter)
        cx = self.larg_monde / 2.0   # centre X de la salle
        cz = self.long_monde / 2.0   # centre Z de la salle (Z = profondeur en OpenGL)
        hauteur_cam = max(self.larg_monde, self.long_monde) * 1.1  # recul suffisant

        self.view = glm.lookAt(
            glm.vec3(cx, hauteur_cam, cz),   # position caméra : au-dessus du centre
            glm.vec3(cx, 0.0,         cz),   # cible : le centre de la salle au sol
            glm.vec3(0.0, 0.0,       -1.0)   # vecteur "haut" : axe -Z (vers le haut de l'écran)
        )

        # Zone de rendu 3D : toute la fenêtre sauf les 50 px du bas réservés au HUD
        self.viewport_h = self.WIN_H - 50

        # Projection perspective légèrement réduite pour vue de dessus
        self.projection = glm.perspective(
            glm.radians(50.0),
            self.WIN_W / self.viewport_h,
            0.1,
            500.0
        )

        # Surface pygame 2D pour le texte HUD (superposée sur OpenGL)
        # On la crée avec SRCALPHA pour pouvoir la blitter par-dessus OpenGL
        self.hud_surface = pygame.Surface((self.WIN_W, 50), pygame.SRCALPHA)
        self.font = pygame.font.Font(None, 20)

    # ─── Méthodes privées de dessin ──────────────────────────────────────────

    def _envoyer_matrices(self, model):
        """Envoie les 3 matrices MVP au shader actif."""
        glUniformMatrix4fv(self.loc_model,      1, GL_FALSE, glm.value_ptr(model))
        glUniformMatrix4fv(self.loc_view,       1, GL_FALSE, glm.value_ptr(self.view))
        glUniformMatrix4fv(self.loc_projection, 1, GL_FALSE, glm.value_ptr(self.projection))

    def _set_couleur(self, rgb):
        """Envoie une couleur (r, g, b) au shader fragment."""
        glUniform3f(self.loc_couleur, *rgb)

    def _dessiner_boite(self, x, z, angle_deg, largeur, longueur, hauteur, couleur):
        """
        Dessine un pavé centré en (x, 0, z) dans le monde.
        angle_deg : rotation autour de l'axe Y (= rotation dans le plan du sol).
        largeur   : dimension sur X, longueur : dimension sur Z, hauteur : dimension sur Y.
        """
        model = glm.mat4(1.0)
        model = glm.translate(model, glm.vec3(x, hauteur / 2.0, z))
        model = glm.rotate(model, glm.radians(angle_deg), glm.vec3(0, 1, 0))
        model = glm.scale(model, glm.vec3(largeur, hauteur, longueur))

        self._envoyer_matrices(model)
        self._set_couleur(couleur)
        glBindVertexArray(self.vao_boite)
        glDrawArrays(GL_TRIANGLES, 0, 36)   # 36 sommets = 12 triangles = 6 faces

    def _dessiner_ligne(self, x1, z1, x2, z2, couleur):
        """
        Dessine un segment de (x1, 0, z1) à (x2, 0, z2) au ras du sol.
        On construit une matrice model qui étire le segment unité [0,0,0]->[1,0,0]
        vers le vecteur (dx, 0, dz).
        """
        dx = x2 - x1
        dz = z2 - z1
        longueur = math.sqrt(dx*dx + dz*dz)
        if longueur < 1e-6:
            return

        angle = math.degrees(math.atan2(dz, dx))  # angle dans le plan XZ

        model = glm.mat4(1.0)
        model = glm.translate(model, glm.vec3(x1, 0.05, z1))   # légèrement au-dessus du sol
        model = glm.rotate(model, glm.radians(-angle), glm.vec3(0, 1, 0))
        model = glm.scale(model, glm.vec3(longueur, 1.0, 1.0))

        self._envoyer_matrices(model)
        self._set_couleur(couleur)
        glBindVertexArray(self.vao_ligne)
        glDrawArrays(GL_LINES, 0, 2)   # 2 sommets = 1 segment

    def _dessiner_sol(self):
        """Dalle fine sous toute la salle."""
        cx = self.larg_monde / 2.0
        cz = self.long_monde / 2.0
        self._dessiner_boite(
            cx, cz,
            angle_deg=0,
            largeur=self.larg_monde,
            longueur=self.long_monde,
            hauteur=self.HAUTEUR_SOL,
            couleur=(0.25, 0.25, 0.25)
        )

    def _dessiner_bordures(self):
        """4 lignes blanches matérialisant les murs de la salle."""
        W = self.larg_monde
        H = self.long_monde
        bords = [
            (0, 0, W, 0),   # bord bas
            (W, 0, W, H),   # bord droit
            (W, H, 0, H),   # bord haut
            (0, H, 0, 0),   # bord gauche
        ]
        for x1, z1, x2, z2 in bords:
            self._dessiner_ligne(x1, z1, x2, z2, self.COULEUR_BORDURE)

    def _dessiner_obstacles(self):
        """Un pavé rouge par obstacle, avec un point foncé au centre."""
        for obs in self.simulation.salle.ListeObstacle:
            # Corps de l'obstacle
            self._dessiner_boite(
                obs.x, obs.y,
                angle_deg=math.degrees(obs.inclinaison),
                largeur=obs.largeur,
                longueur=obs.longueur,
                hauteur=self.HAUTEUR_OBSTACLE,
                couleur=self.COULEUR_OBSTACLE
            )
            # Petit cube foncé au centre (équivalent du cercle darkred de l'affichage 2D)
            self._dessiner_boite(
                obs.x, obs.y,
                angle_deg=0,
                largeur=0.8,
                longueur=0.8,
                hauteur=self.HAUTEUR_OBSTACLE + 0.05,  # légèrement au-dessus
                couleur=self.COULEUR_OBS_CENTRE
            )

    def _dessiner_robot(self):
        """Pavé bleu pour le corps + petit cube violet pour l'orientation + ligne rouge capteur."""
        rob = self.simulation.rob

        # Corps du robot
        self._dessiner_boite(
            rob.x, rob.y,
            angle_deg=rob.angle,
            largeur=rob.largeur,
            longueur=rob.longueur,
            hauteur=self.HAUTEUR_ROBOT,
            couleur=self.COULEUR_ROBOT
        )

        # Indicateur d'orientation : petit cube violet à l'avant du robot
        # L'avant est dans la direction de l'angle (sin, -cos en repère simulation)
        angle_rad = math.radians(rob.angle)
        decalage  = rob.longueur / 2.0 * 0.8   # 80 % de la demi-longueur vers l'avant
        avant_x   = rob.x + decalage * math.sin(angle_rad)
        avant_z   = rob.y - decalage * math.cos(angle_rad)

        self._dessiner_boite(
            avant_x, avant_z,
            angle_deg=rob.angle,
            largeur=rob.largeur * 0.3,
            longueur=rob.longueur * 0.3,
            hauteur=self.HAUTEUR_ROBOT + 0.1,
            couleur=self.COULEUR_ROBOT_DIR
        )

        # Rayon capteur : ligne rouge dans la direction du robot
        fin_x = rob.x + (rob.longueur / 2.0 + rob.capteur) * math.sin(angle_rad)
        fin_z = rob.y - (rob.longueur / 2.0 + rob.capteur) * math.cos(angle_rad)
        self._dessiner_ligne(rob.x, rob.y, fin_x, fin_z, self.COULEUR_CAPTEUR)

    # ─── HUD texte (pygame 2D par-dessus OpenGL) ─────────────────────────────

    def _dessiner_hud(self):
        """
        Affiche les infos du robot dans une bande de 50 px en bas de la fenêtre.
        Technique : on dessine dans une Surface pygame, puis on la convertit en
        texture OpenGL et on la blitte via glDrawPixels.
        """
        rob = self.simulation.rob
        self.hud_surface.fill((30, 30, 30, 220))   # fond semi-transparent foncé

        # Vitesse linéaire
        v_lin = self.font.render(
            f"Vlin: {rob.vitesseLineaire:.2f} m/s", True, (200, 200, 200))
        # Vitesse angulaire
        v_ang = self.font.render(
            f"Vang: {rob.vitesseAngulaire:.2f} rad/s", True, (200, 200, 200))
        # Angle
        angle_txt = self.font.render(
            f"Angle: {rob.angle:.1f}°", True, (200, 200, 200))
        # Position
        pos_txt = self.font.render(
            f"Pos: ({rob.x:.1f}, {rob.y:.1f})", True, (200, 200, 200))
        # Capteur avec couleur selon la distance
        if rob.capteur < 0.5:
            coul_cap = (255, 60, 60)
            label_cap = f"Capteur: {rob.capteur:.2f} [COLLISION!]"
        elif rob.capteur < 1.0:
            coul_cap = (255, 165, 0)
            label_cap = f"Capteur: {rob.capteur:.2f} [DANGER]"
        else:
            coul_cap = (60, 220, 60)
            label_cap = f"Capteur: {rob.capteur:.2f} [OK]"
        cap_txt = self.font.render(label_cap, True, coul_cap)

        # Placement dans la bande HUD
        self.hud_surface.blit(v_lin,     (10,  8))
        self.hud_surface.blit(v_ang,     (10,  28))
        self.hud_surface.blit(angle_txt, (200, 8))
        self.hud_surface.blit(pos_txt,   (200, 28))
        self.hud_surface.blit(cap_txt,   (400, 8))

        # Convertit la surface pygame en pixels raw RGBA pour OpenGL
        raw = pygame.image.tostring(self.hud_surface, "RGBA", True)

        # Positionne le raster (coin bas-gauche de la zone de dessin)
        glWindowPos2i(0, 0)

        # Dessine les pixels directement dans le framebuffer
        glDrawPixels(self.WIN_W, 50, GL_RGBA, GL_UNSIGNED_BYTE, raw)

    # ─── Méthode publique ────────────────────────────────────────────────────

    def updateAffichage(self):
        """
        Point d'entrée principal, appelé à chaque itération de la boucle.
        Remplace updateAffichage() de la classe Affichage originale.
        """
        # Met à jour la valeur du capteur dans la simulation
        self.simulation.update_capteur()

        # Efface le colour buffer et le depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Active notre programme shader pour tous les dessins OpenGL
        glUseProgram(self.programme)

        # Zone de rendu 3D : toute la fenêtre sauf les 50 px du bas
        glViewport(0, 50, self.WIN_W, self.viewport_h)

        # Dessine la scène 3D
        self._dessiner_sol()
        self._dessiner_bordures()
        self._dessiner_obstacles()
        self._dessiner_robot()

        # HUD : revient à la résolution complète pour les pixels 2D
        glViewport(0, 0, self.WIN_W, self.WIN_H)
        self._dessiner_hud()

        # Affiche le buffer caché (double buffering)
        pygame.display.flip()