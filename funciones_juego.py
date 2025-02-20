import sys
import pygame

def verificar_eventos():
    """Responde a la entrada de teclado y raton"""    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()