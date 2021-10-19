import pygame
import random


class Bola (pygame.Rect):

    def __init__(self,  velocidad, dimensiones):
        super(Bola, self).__init__(0, 0, dimensiones, dimensiones)
        self.velocidad_x = velocidad
        self.velocidad_y = velocidad-random.randint(2, 5)
        self.iniciar()

    def iniciar(self):
        pantalla = pygame.display.get_surface()
        (ancho, alto) = pantalla.get_size()

        self.x = ancho//2-self.width
        self.y = alto//2-self.height

        self.velocidad_x = random.randint(-3, 3)
        self.velocidad_y = -self.velocidad_y

    def muevete(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y
