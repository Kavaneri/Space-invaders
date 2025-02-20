import sys
import pygame

def verificar_eventos(nave):
    """Responde a la entrada de teclado y raton"""    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                nave.moving_right = True
            elif event.key == pygame.K_LEFT:
                nave.moving_left = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                nave.moving_right = False
            elif event.key == pygame.K_LEFT:
                nave.moving_left = False
            
def actualizar_pantalla(configuraciones, window, nave):
    """Actualiza las imagenes en la pantalla"""
    #Rellenado de la pantalla con el color de fondo
    window.fill(configuraciones.bgColor) 
    nave.blitme()
        
    pygame.display.flip() #Redibujar el frame (¿Dependiente de la taza de refrezco de la pantalla?)    