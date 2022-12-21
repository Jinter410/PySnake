import pygame
# Librairie pour l'aléatoire :
import random

class GrilleJeu():
    def load_reward_image(self):
        # On charge l'image de la récompense et on modifie sa taille
        reward_img_full = pygame.image.load('./img/reward.png')
        resized_reward = pygame.transform.scale(reward_img_full, (self.size, self.size))
        self.reward = resized_reward

    # On initialise en donnant l'instance du snake,
    # C'est dans cette classe qu'on gère tous les autres éléments
    def __init__(self, snake_instance):
        self.snake = snake_instance
        self.size = self.snake.head_size/2
        # On charge l'image de la reward
        self.load_reward_image()
        self.max_x, self.max_y = self.snake.max_x, self.snake.max_y
        # On fait apparaitre une récompense aléatoirement 
        self.reward_x = random.randint(0, self.max_x - self.size)
        self.reward_y = random.randint(0, self.max_y - self.size)
        # On met une hitbox sur la reward
        self.reward_hitbox = pygame.Rect(self.reward_x, self.reward_y, self.size, self.size)
        # Et on récupère l'écran du jeu
        self.screen = self.snake.screen
    
    def spawn_random_reward(self):
        # On choisit les coordonnées x et y de la récompense au hasard
        # Entre les bordures de la fenêtre (je prends 20 de sécurité pour pas qu'elle sorte de l'écran et qu'on la voie pas)
        self.reward_x = random.randint(0, self.max_x - self.size)
        self.reward_y = random.randint(0, self.max_y - self.size)
        self.reward_hitbox.x = self.reward_x
        self.reward_hitbox.y = self.reward_y

    def mise_a_jour_grille(self):
        # Si le serpent est sur la récompense alors elle change de coordonnées
        if self.reward_hitbox.colliderect(self.snake.hitbox):
            self.spawn_random_reward()
            self.snake.spawn_body()
    
    def draw(self):
        self.screen.blit(self.reward, [self.reward_x, self.reward_y])
    
