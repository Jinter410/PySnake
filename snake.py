import pygame

class Snake():
    def __init__(self, paramScreen):
        self.screen = paramScreen
    
    def draw_rectangle(self):
        pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(30, 30, 60, 60))
        pygame.display.flip()