# Import the pygame module
import pygame
from win32api import GetSystemMetrics

# Définir la couleur du background
background_color = (0,0,0)
# Définir les dimensions de la fenêtre
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
screen = pygame.display.set_mode((0.9*height,0.9*height))
# Définir le titre de la fenêtre
pygame.display.set_caption("PySnake des bg")
# Remplir la fenêtre avec la couleur choisie
screen.fill(background_color)
# Afficher la fenêtre avec flip
pygame.display.flip()

# Boucle d'affichage
running = True
while running:
    # Boucle des évènements
    for event in pygame.event.get():
        # On check si on a un évènement de sortie
        if event.type == pygame.QUIT:
            running = False
    