import sys
import pygame

def run():
    pygame.init() #Inicializacion de pygame
    window = pygame.display.set_mode((800, 600)) #Definicion del tamaño de la pantalla
    pygame.display.set_caption("Space invaders") #Definicion de titulo de ventana  
    
    #Bucle principal del juego/eventos
    while True:
        # Reaccion a eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip() #Redibujar el frame (¿Dependiente de la taza de refrezco de la pantalla?)

run()
        