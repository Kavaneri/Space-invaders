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
    nave = SpaceShip(configuraciones, window)
 
    #Bucle principal del juego/eventos
    while True:
        # Reaccion a eventos
        fj.verificar_eventos(nave)
        nave.update_pos()
        fj.actualizar_pantalla(configuraciones, window, nave)

run()
        