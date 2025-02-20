import pygame

class SpaceShip:
    def __init__(self, configuraciones,window):
        self.window = window
        self.configuraciones = configuraciones
        self.image = pygame.image.load("Space-invaders/resources/nave.bmp") 
        self.rect = self.image.get_rect()
        self.window_rect = window.get_rect()
        
        #Posicion de la nave 
        self.rect.centerx = self.window_rect.centerx
        self.rect.bottom = self.window_rect.bottom
        
        #Posicion en numero decimal
        self.center = float(self.rect.centerx)
        
        self.moving_right = False
        self.moving_left = False
        
    #Actualizar posicion de la nave    
    def update_pos(self):
        if self.moving_right:
            self.center += self.configuraciones.factor_velocidad
            
        if self.moving_left:
            self.center -= self.configuraciones.factor_velocidad
        
        self.rect.centerx = self.center
        
    #Dibuja la nave    
    def blitme(self):
        self.window.blit(self.image, self.rect)
        
    