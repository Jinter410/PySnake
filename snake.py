import pygame

SPEED = 3
NEW_BODYPART_X = {
    "left":1,
    "right":-1,
    "up":0,
    "down":0
}
NEW_BODYPART_Y = {
    "left":0,
    "right":0,
    "up":1,
    "down":-1
}

class Snake():
    def load_head_and_eyes(self):
        # On charge l'image de la tête et on modifie sa taille
        head_full = pygame.image.load('./img/snake_part.png')
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
        self.body_size = self.head_size * 3/4
        self.load_head_and_eyes()
        self.max_x, self.max_y = self.screen.get_size()
        self.x_eyes = self.x + self.head_size/2 - self.eyes_size/2
        self.y_eyes = self.y + self.head_size/2 - self.eyes_size/2
        # La hitbox du snake
        self.hitbox = pygame.Rect(self.x, self.y, self.head_size, self.head_size)
        # La liste contenant les parties de son corps (qui est vide au début)
        self.bodyparts = []
    
    def mise_a_jour_corps(self):
        # On met à jour les coordonnées du corps du snake s'il y en a et qu'on a hit les arrows
        if len(self.bodyparts) > 0:
            for i in range(len(self.bodyparts)):
                # Si c'est le premier morceau de corps on fait en fonction de la tête
                if i == 0:
                    self.bodyparts[0].x_center += (self.hitbox.centerx - self.bodyparts[0].x_center)*SPEED/50
                    self.bodyparts[0].y_center += (self.hitbox.centery - self.bodyparts[0].y_center)*SPEED/50
                    self.bodyparts[0].update_coords_from_center()
                # Sinon on fait en fonction du morceau d'avant
                else:
                    self.bodyparts[i].x_center += (self.bodyparts[i-1].x_center - self.bodyparts[i].x_center)*SPEED/50
                    self.bodyparts[i].y_center += (self.bodyparts[i-1].y_center - self.bodyparts[i].y_center)*SPEED/50
                    self.bodyparts[i].update_coords_from_center()
    
    def mise_a_jour_position(self, keys):
        # On met à jour la position du snake en fonction de la touche pressée !
        if keys[pygame.K_DOWN]:
            self.down()
            self.mise_a_jour_corps()
        if keys[pygame.K_UP]:
            self.up()
            self.mise_a_jour_corps()
        if keys[pygame.K_LEFT]:
            self.left()
            self.mise_a_jour_corps()
        if keys[pygame.K_RIGHT]:
            self.right()
            self.mise_a_jour_corps()
        self.hitbox.x = self.x
        self.hitbox.y = self.y
    
    def up(self):
        # Si la coordonnée en Y actuelle de la tête du serpent est sous la bordure
        if self.y > 0:
            # Alors on le fait monter d'une unité (pareil pour les yeux du coup hein t'as capté)
            self.y -= SPEED
            self.y_eyes -= SPEED
        else:
            # Sinon on ne le déplace pas
            self.y = 0
            self.y_eyes = 0 + self.head_size/2 - self.eyes_size/2
        # On met à jour la direction du snake pour la position des yeux
        self.direction = "up"

    def down(self):
        # Si la coordonnée en Y actuelle de la tête du serpent est au-dessus de 
        # la bordure (avec prise en compte de la largeur) de la tête
        if self.y < self.max_y - self.head_size:
            # Alors on le fait descendre d'une unité
            self.y += SPEED
            self.y_eyes += SPEED
        else:
            # Sinon on ne le déplace pas
            self.y = self.max_y - self.head_size
            self.y_eyes = self.max_y - self.head_size + self.head_size/2 - self.eyes_size/2
        # On met à jour la direction du snake pour la position des yeux
        self.direction = "down"

    # Même raisonnement pour la droite et la gauche avec les coordonnées en X :
    def left(self):
        if self.x > 0:
            self.x -= SPEED
            self.x_eyes -= SPEED
        else:
            self.x = 0
            self.x_eyes = 0 + self.head_size/2 - self.eyes_size/2
        self.direction = "left"
            
    def right(self):
        if self.x < self.max_x - self.head_size:
            self.x += SPEED
            self.x_eyes += SPEED
        else:
            self.x = self.max_x - self.head_size
            self.x_eyes = self.max_x - self.head_size + self.head_size/2 - self.eyes_size/2
        self.direction = "right"

    def spawn_body(self):
        # Si le serpent a des parties du corps
        if len(self.bodyparts) > 0:
            # Alors on récupère la dernière partie
            last_bodypart = self.bodyparts[-1]
            # Et on définit les coordonnées de la nouvelle partie du corps en fonction de la dernière 
            new_bodypart_x_center = last_bodypart.hitbox.centerx + NEW_BODYPART_X[self.direction] * self.head_size
            new_bodypart_y_center = last_bodypart.hitbox.centery + NEW_BODYPART_Y[self.direction] * self.head_size
        # Sinon on fait la même chose en prenant la tête comme dernière partie
        else:
            new_bodypart_x_center = self.hitbox.centerx + NEW_BODYPART_X[self.direction] * self.head_size
            new_bodypart_y_center = self.hitbox.centery + NEW_BODYPART_Y[self.direction] * self.head_size
        # On crée la dernière partie du corps et on l'ajoute à la liste
        new_part = BodyPart(self.body_size, new_bodypart_x_center, new_bodypart_y_center)
        self.bodyparts.append(new_part)

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
        # Puis on dessine les parties du corps du snake
        for body_part in self.bodyparts:
            self.screen.blit(body_part.body, [body_part.x, body_part.y])

# Objet pour définir les propriétés et fonctions du corps du snake
class BodyPart():
    def load_body(self):
         # On charge l'image du corps et on modifie sa taille
        body_full = pygame.image.load('./img/snake_part.png')
        resized_body = pygame.transform.scale(body_full, (self.size, self.size))
        self.body = resized_body

    def __init__(self, size, x_center, y_center):
        self.x_center = x_center
        self.y_center = y_center
        self.size = size
        self.update_coords_from_center()
        self.load_body()
        # La hitbox d'une partie du corps
        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.size)
    
    def update_coords_from_center(self):
        self.x = self.x_center - self.size/2
        self.y = self.y_center - self.size/2
