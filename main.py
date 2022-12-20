import pygame
from win32api import GetSystemMetrics
from PIL import Image
from snake import Snake

################# INITIALISATION #################
# Définir les dimensions de la fenêtre
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
new_width = int(0.9*height)
new_height = int(0.9*height)
screen = pygame.display.set_mode((new_width,new_height))
# Lire image
image = Image.open("./img/background.png")
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
# Initialisation du snake
snake = Snake(screen)
snake.draw()

# Boucle d'affichage
running = True
pygame.key.set_repeat(True)
while running:
    for event in pygame.event.get():
        # On check si on a un évènement de sortie
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys:
            snake.mise_a_jour_position(keys)
    screen.blit(background, (0, 0))
    snake.draw()
    pygame.display.update()