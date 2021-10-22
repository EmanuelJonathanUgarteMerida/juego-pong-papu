import pygame as pg
from . import BOLA_DIMEN, PALETA_ANCHO, PALETA_ALTO, PANTALLA_ALTURA,PANTALLA_ANCHO, VELOCIDAD_B, VELOCIDAD_P


class Bola (pg.Rect):
    def __init__(self):
        super(Bola, self).__init__(0, 0, BOLA_DIMEN, BOLA_DIMEN)
        self.velocidad_x = VELOCIDAD_B
        #self.velocidad_y = velocidad-random.randint(2, 5)
        self.velocidad_y = -VELOCIDAD_B
        self.iniciar()

    def iniciar(self):
        self.center=(PANTALLA_ANCHO/2,PANTALLA_ALTURA/2)

        #self.velocidad_x = random.randint(-3, 3)
        self.velocidad_x = -self.velocidad_x
        self.velocidad_y = -self.velocidad_y

    def muevete(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y


class Paleta (pg.Rect):
    def __init__(self, nombre, teclas, pos_x):
        super(Paleta, self).__init__(pos_x, 0, PALETA_ANCHO, PALETA_ALTO)
        self.teclas = teclas
        self.velocidad = VELOCIDAD_P
        self.golpe = 0
        self.puntos = 0
        self.nombre = nombre
        # Init objeto rect()
        self.x = pos_x
        self.y = PANTALLA_ALTURA/2-self.height/2

    def muevete(self):
        pulsando = pg.key.get_pressed()
        if pulsando[self.teclas[0]]:
            self.y -= self.velocidad
            if self.y < 0:
                self.y = 0
        elif pulsando[self.teclas[1]]:
            self.y += self.velocidad
            if self.y > PANTALLA_ALTURA-self.height:
                self.y = PANTALLA_ALTURA-self.height
