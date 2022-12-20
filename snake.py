import pygame

UNITE_DE_MOUVEMENT = 0.8

class Snake():
    def __init__(self, paramScreen):
        self.screen = paramScreen
        self.x = 250
        self.y = 250
        self.size = 20
    
    def mise_a_jour_position(self, keys):
        # On met à jour la position du snake en fonction de la touche pressée !
        if keys[pygame.K_DOWN]:
            self.y += UNITE_DE_MOUVEMENT
        if keys[pygame.K_UP]:
            self.y -= UNITE_DE_MOUVEMENT
        if keys[pygame.K_LEFT]:
            self.x -= UNITE_DE_MOUVEMENT
        if keys[pygame.K_RIGHT]:
            self.x += UNITE_DE_MOUVEMENT

    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), [self.x, self.y, self.size, self.size])