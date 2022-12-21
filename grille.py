import pygame
# Librairie pour l'aléatoire :
import random

class GrilleJeu():
    def load_reward_image(self):
        # On charge l'image de la récompense et on modifie sa taille
        reward_img_full = pygame.image.load('./img/reward.png')
        resized_reward = pygame.transform.scale(reward_img_full, (self.snake.head_size/2, self.snake.head_size/2))
        self.reward = resized_reward

    # On initialise en donnant l'instance du snake,
    # C'est dans cette classe qu'on gère tous les autres éléments
    def __init__(self, snake_instance):
        self.snake = snake_instance
        self.load_reward_image()
        self.max_x, self.max_y = self.snake.max_x, self.snake.max_y
        # On fait apparaitre une récompense aléatoirement 
        self.spawn_random_reward()
        self.screen = self.snake.screen
    
    def spawn_random_reward(self):
        # On choisit les coordonnées x et y de la récompense au hasard
        # Entre les bordures de la fenêtre (je prends 20 de sécurité pour pas qu'elle sorte de l'écran et qu'on la voie pas)
        self.reward_x = random.randint(0, self.max_x - 20)
        self.reward_y = random.randint(20, self.max_y)
    
    def draw(self):
        self.screen.blit(self.reward, [self.reward_x, self.reward_y])
    
