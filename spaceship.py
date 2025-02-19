import pygame

class SpaceShip:
    def __init__(self, window):
        self.window = window
        self.image = pygame.image.load("Space-invaders/resources/nave.bmp") 
        self.rect = self.image.get_rect()
        self.window_rect = window.get_rect()
        
        #Posicion de la nave 
        self.rect.centerx = self.window_rect.centerx
        self.rect.bottom = self.window_rect.bottom
        
    #Dibuja la nave    
    def blitme(self):
        self.window.blit(self.image, self.rect)
        
    