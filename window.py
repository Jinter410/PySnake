# Import the pygame module
import pygame
from win32api import GetSystemMetrics
from PIL import Image

def afficher_jeu(lien_image):
    # Définir les dimensions de la fenêtre
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    new_width = int(0.9*height)
    new_height = int(0.9*height)
    screen = pygame.display.set_mode((new_width,new_height))
    # Lire image
    image = Image.open(lien_image)
    new_image = image.resize((new_width, new_height))
    new_image.save('./img/background_resize.png')
    # Définir le titre de la fenêtre
    pygame.display.set_caption("PySnake des bg")
    # Lire l'image avec la librairie
    background = pygame.image.load('./img/background_resize.png')
    # Remplir la fenêtre avec l'image'
    screen.blit(background, (0, 0))
    # Afficher la fenêtre avec flip
    pygame.display.flip()
    
    return screen
    