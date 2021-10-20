import pygame as pg
from configuracion import _VELOCIDAD, _BOLA_DIMEN, _PALETA_ANCHO, _PALETA_ALTO, _PANTALLA_ALTURA, _VELOCIDAD


class Bola (pg.Rect):
    def __init__(self):
        super(Bola, self).__init__(0, 0, _BOLA_DIMEN, _BOLA_DIMEN)
        self.velocidad_x = _VELOCIDAD
        #self.velocidad_y = velocidad-random.randint(2, 5)
        self.velocidad_y = -_VELOCIDAD
        self.iniciar()

    def iniciar(self):
        pantalla = pg.display.get_surface()
        (ancho, alto) = pantalla.get_size()

        self.x = ancho//2-self.width//2
        self.y = alto//2-self.height//2

        #self.velocidad_x = random.randint(-3, 3)
        self.velocidad_x = -self.velocidad_x
        self.velocidad_y = -self.velocidad_y

    def muevete(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y


class Paleta (pg.Rect):
    def __init__(self, nombre, teclas, pos_x):
        super(Paleta, self).__init__(pos_x, 0, _PALETA_ANCHO, _PALETA_ALTO)
        self.teclas = teclas
        self.velocidad = _VELOCIDAD
        self.golpe = 0
        self.puntos = 0
        self.nombre = nombre
        # Init objeto rect()
        self.x = pos_x
        self.y = _PANTALLA_ALTURA/2-self.height/2

    def muevete(self):
        pulsando = pg.key.get_pressed()
        if pulsando[self.teclas[0]]:
            self.y -= self.velocidad
            if self.y < 0:
                self.y = 0
        elif pulsando[self.teclas[1]]:
            self.y += self.velocidad
            if self.y > _PANTALLA_ALTURA-self.height:
                self.y = _PANTALLA_ALTURA-self.height
