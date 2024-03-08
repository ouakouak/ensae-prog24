from grid import Grid
from solver import Solver
from graph import Graph

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Définition de la taille de la fenêtre
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

# Création de la fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Simple Game")

# Position initiale du carré
x = WINDOW_WIDTH // 2
y = WINDOW_HEIGHT // 2

# Taille du carré
square_size = 50

# Vitesse de déplacement du carré
speed = 5

# Boucle principale du jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des touches pour déplacer le carré
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Limiter les coordonnées du carré à l'intérieur de la fenêtre
    x = max(0, min(x, WINDOW_WIDTH - square_size))
    y = max(0, min(y, WINDOW_HEIGHT - square_size))

    # Effacer l'écran
    window.fill(WHITE)

    # Dessiner le carré
    pygame.draw.rect(window, BLACK, (x, y, square_size, square_size))

    # Mettre à jour l'affichage
    pygame.display.update()

    # Limiter le taux de rafraîchissement de l'écran
    pygame.time.Clock().tick(30)

# Quitter Pygame
pygame.quit()
sys.exit()







'''
data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)
'''


