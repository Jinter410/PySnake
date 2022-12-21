import pygame

UNITE_DE_MOUVEMENT = 0.5

class Snake():
    def load_head_and_eyes(self):
        # On charge l'image de la tête et on modifie sa taille
        head_full = pygame.image.load('./img/snake_head.png')
        resized_head = pygame.transform.scale(head_full, (self.head_size, self.head_size))
        self.head = resized_head
        # Pareil pour les yeux
        eyes_full = pygame.image.load('./img/snake_eyes.png')
        resized_eyes = pygame.transform.scale(eyes_full, (self.eyes_size, self.eyes_size))
        self.eyes = resized_eyes

        
    def __init__(self, paramScreen):
        self.screen = paramScreen
        self.x = 250
        self.y = 250
        self.direction = None
        self.head_size = 40
        self.eyes_size = self.head_size/2.3
        self.load_head_and_eyes()
        self.max_x, self.max_y = self.screen.get_size()
        self.x_eyes = self.x + self.head_size/2 - self.eyes_size/2
        self.y_eyes = self.y + self.head_size/2 - self.eyes_size/2
        # La hitbox du snake
        self.hitbox = pygame.Rect(self.x, self.y, self.head_size, self.head_size)
    
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
        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def up(self):
        # Si la coordonnée en Y actuelle de la tête du serpent est sous la bordure
        if self.y > 0:
            # Alors on le fait monter d'une unité (pareil pour les yeux du coup hein t'as capté)
            self.y -= UNITE_DE_MOUVEMENT
            self.y_eyes -= UNITE_DE_MOUVEMENT
        else:
            # Sinon on le téléporte en bas de la fenêtre !
            self.y = self.max_y
            self.y_eyes = self.max_y + self.head_size/2 - self.eyes_size/2
        # On met à jour la direction du snake pour la position des yeux
        self.direction = "up"

    def down(self):
        # Si la coordonnée en Y actuelle de la tête du serpent est au-dessus de la bordure
        if self.y < self.max_y:
            # Alors on le fait descendre d'une unité
            self.y += UNITE_DE_MOUVEMENT
            self.y_eyes += UNITE_DE_MOUVEMENT
        else:
            # Sinon on le téléporte en haut de la fenêtre !
            self.y = 0
            self.y_eyes = 0 + self.head_size/2 - self.eyes_size/2
        # On met à jour la direction du snake pour la position des yeux
        self.direction = "down"

    # Même raisonnement pour la droite et la gauche avec les coordonnées en X :
    def left(self):
        if self.x > 0:
            self.x -= UNITE_DE_MOUVEMENT
            self.x_eyes -= UNITE_DE_MOUVEMENT
        else:
            self.x = self.max_x
            self.x_eyes = self.max_x + self.head_size/2 - self.eyes_size/2
        self.direction = "left"
            
    def right(self):
        if self.x < self.max_x:
            self.x += UNITE_DE_MOUVEMENT
            self.x_eyes += UNITE_DE_MOUVEMENT
        else:
            self.x = 0
            self.x_eyes = 0 + self.head_size/2 - self.eyes_size/2
        self.direction = "right"

    # Fonction de dessin qu'on appelle à chaque frame
    def draw(self):
        self.screen.blit(self.head, [self.x, self.y])
        # Affichage des yeux 
        # Si le snake a une direction (en gros si on est en train de le bouger)
        if self.direction in ["left","right","up","down"]:
            # Si c'est à droite, on déplace les yeux un petit peu à droite
            if self.direction == "right":
                self.screen.blit(self.eyes, [self.x_eyes + 10, self.y_eyes ])
            # Sinon si (elif ça veut dire else if) la direction est à gauche on affiche un peu
            # à gauche et ainsi de suite 
            elif self.direction == "left":
                self.screen.blit(self.eyes, [self.x_eyes - 10, self.y_eyes])
            elif self.direction == "up":
                self.screen.blit(self.eyes, [self.x_eyes, self.y_eyes - 10])
            elif self.direction == "down":
                self.screen.blit(self.eyes, [self.x_eyes, self.y_eyes + 10])
        # Si le snake n'a pas de direction on dessine les yeux au centre
        else:
            self.screen.blit(self.eyes, [self.x_eyes, self.y_eyes])