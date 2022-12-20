import pygame

UNITE_DE_MOUVEMENT = 0.8

class Snake():
    def __init__(self, paramScreen):
        self.screen = paramScreen
        self.x = 250
        self.y = 250
        self.size = 20
        self.max_x, self.max_y = self.screen.get_size()
    
    def mise_a_jour_position(self, keys):
        # On met à jour la position du snake en fonction de la touche pressée !
        if keys[pygame.K_DOWN]:
            self.down()
        if keys[pygame.K_UP]:
            self.up()
        if keys[pygame.K_LEFT]:
            self.left()
        if keys[pygame.K_RIGHT]:
            self.right()

    def up(self):
        # Si la coordonnée en Y actuelle de la tête du serpent est sous la bordure
        if self.y > 0:
            # Alors on le fait monter d'une unité
            self.y -= UNITE_DE_MOUVEMENT
        else:
            # Sinon on le téléporte en bas de la fenêtre !
            self.y = self.max_y

    def down(self):
        # Si la coordonnée en Y actuelle de la tête du serpent est au-dessus de la bordure
        if self.y < self.max_y:
            # Alors on le fait descendre d'une unité
            self.y += UNITE_DE_MOUVEMENT
        else:
            # Sinon on le téléporte en haut de la fenêtre !
            self.y = 0

    # Même raisonnement pour la droite et la gauche avec les coordonnées en X :
    def left(self):
        if self.x > 0:
            self.x -= UNITE_DE_MOUVEMENT
        else:
            self.x = self.max_x

    def right(self):
        if self.x < self.max_x:
            self.x += UNITE_DE_MOUVEMENT
        else:
            self.x = 0

    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), [self.x, self.y, self.size, self.size])