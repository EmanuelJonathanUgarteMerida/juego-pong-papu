import pygame
import configuracion as cf

class Paleta (pygame.Rect):
	#teclas(subir,bajar)
    def __init__(self, nombre, teclas, velocidad, posicion_x):
        super(Paleta, self).__init__(posicion_x, 0, cf._ANCHO, cf._ALTO)
        self.teclas = teclas
        self.velocidad = velocidad
        self.altura_pantalla = pygame.display.get_surface().get_height()
        self.golpe = 0
        self.puntos = 0
        self.nombre = nombre
        self.nombre_render = self.nombre_jugador_render()
        # Init objeto rect()
        self.x = posicion_x
        self.y = self.altura_pantalla/2-self.height/2

    def muevete(self):
		pulsando=pygame.key.get_pressed()
        if pulsando[self.teclas[0]]:
            self.y -= self.velocidad
            if self.y < 0:
                self.y = 0
        elif pulsando[self.teclas[1]]:
            self.y += self.velocidad
            if self.y > self.altura_pantalla-self.height:
                self.y = self.altura_pantalla-self.height