import window
import pygame
from snake import Snake

screen = window.afficher_jeu("./img/background.png")
snake = Snake(screen)
snake.draw_rectangle()
# Boucle d'affichage
running = True
while running:
    # Boucle des évènements
    for event in pygame.event.get():
        # On check si on a un évènement de sortie
        if event.type == pygame.QUIT:
            running = False
