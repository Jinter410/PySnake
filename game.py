import pygame
from win32api import GetSystemMetrics
from PIL import Image
from snake import Snake
from grille import GrilleJeu

MODES = {
    "solo": Snake
}

class Game():
    def __init__(self, mode):
        pygame.init()
        # Horloge pour limiter les FPS (pas encore utilisé pour l'instant)
        self.clock = pygame.time.Clock()
        # Définir les dimensions de la fenêtre
        self.full_width = GetSystemMetrics(0)
        self.full_height = GetSystemMetrics(1)
        self.window_width = int(0.9*self.full_height)
        self.window_height = int(0.9*self.full_height)
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        # Lire image, la resize pour la taille de notre fenêtre
        image = Image.open("./img/background.png")
        new_image = image.resize((self.window_width, self.window_height))
        new_image.save('./img/background_resize.png')
        # Lire l'image avec la librairie
        self.background = pygame.image.load('./img/background_resize.png')
        # Remplir la fenêtre avec l'image
        self.screen.blit(self.background, (0, 0))
        # Afficher la fenêtre avec flip
        pygame.display.flip()
        # Définir le titre de la fenêtre
        pygame.display.set_caption("PySnake des bg")
        # Initialiser le snake 
        self.snake = MODES[mode](self.screen)
        self.snake.draw()
        # Initialisation de la grille de jeu
        self.grid = GrilleJeu(self.snake)

    def game_loop(self):
        running = True
        pygame.key.set_repeat(True)
        while running:
            for event in pygame.event.get():
                # On check si on a un évènement de sortie
                if event.type == pygame.QUIT:
                    running = False
                # Si on a relâché une touche alors le snake n'a plus de direction
                if event.type == pygame.KEYUP:
                    self.snake.direction = None
            keys = pygame.key.get_pressed()
            if keys:
                self.snake.mise_a_jour_position(keys)
                self.grid.mise_a_jour_grille()
            # On redessne tout à chaque image : le fond, la récompense et la grille
            self.screen.blit(self.background, (0, 0))
            self.grid.draw()
            self.snake.draw()
            pygame.display.update()
    
    def start(self):
        self.game_loop()



