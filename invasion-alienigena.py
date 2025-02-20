import funciones_juego as fj
import pygame
from config import Config
from spaceship import SpaceShip

def run():
    pygame.init() #Inicializacion de pygame
    configuraciones = Config() #Estancia de las configuraciones del juego
    window = pygame.display.set_mode((configuraciones.screenWidth, configuraciones.screenHeight)) #Definicion del tamaño de la pantalla
    pygame.display.set_caption("Space invaders") #Definicion de titulo de ventana  
    
    #Instancia de la nave
    nave = SpaceShip(window)
 
    #Bucle principal del juego/eventos
    while True:
        # Reaccion a eventos
        fj.verificar_eventos()
        
        #Rellenado de la pantalla con el color de fondo
        window.fill(configuraciones.bgColor) 
        nave.blitme()
        
        pygame.display.flip() #Redibujar el frame (¿Dependiente de la taza de refrezco de la pantalla?)

run()
        