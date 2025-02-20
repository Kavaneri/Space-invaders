import sys
import pygame

def verificar_eventos():
    """Responde a la entrada de teclado y raton"""    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
def actualizar_pantalla(configuraciones, window, nave):
    """Actualiza las imagenes en la pantalla"""
    #Rellenado de la pantalla con el color de fondo
    window.fill(configuraciones.bgColor) 
    nave.blitme()
        
    pygame.display.flip() #Redibujar el frame (¿Dependiente de la taza de refrezco de la pantalla?)    