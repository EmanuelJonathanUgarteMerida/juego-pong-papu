
import pygame as pg
import os
from configuracion import _JUEGO_NOMBRE, _PARA_EMPEZAR, _PANTALLA_ANCHO, _PANTALLA_ALTURA, _PANTALLA_MARGEN_LATERAL


class Portada:
    def __init__(self):
        self.texto_nombre = ''
        self.texto_empezar = ''
        self.texto_jugador_1 = ''
        self.texto_jugador_2 = ''
        self.jugadores = 0
        self.logo = pg.image.load(os.path.join(
            'resources', 'images', 'logo.png'))
        self.logo_pos = (_PANTALLA_ANCHO/2-self.logo.get_width/2,)
        fuente = pg.font.Font(os.path.join(
            'resources', 'fonts', 'Pacifico-Regular.ttf'), 20)
        self.texto_inicio = fuente.render(_PARA_EMPEZAR, True, 'red')
        self.texto_pos = (
            _PANTALLA_ANCHO/2 - self.texto_inicio.get_width() / 2,
            _PANTALLA_ALTURA - _PANTALLA_MARGEN_LATERAL - self.texto_inicio.get_height()
        )

    def bucle_principal(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.K_SPACE:
                    if self.jugadores != 0:
                        return
                elif event.type in (pg.K_1, pg.K_KP1):
                    self.jugadores = 1
                elif event.type in (pg.K_KP2, pg.K_KP2):
                    self.jugadores = 2
        # pintamos la pantalla inicio
