import pygame
import random


class Bola (pygame.Rect):

    def __init__(self,  velocidad_x, *args, **kwargs):
        super(Bola, self).__init__(*args, **kwargs)
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_x-random.randint(2, 5)

    def muevete(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y

    def rebote_por_paleta(self):
        pass

    def iniciar(self):
        pantalla = pygame.display.get_surface()
        dimensiones = pantalla.get_size()
