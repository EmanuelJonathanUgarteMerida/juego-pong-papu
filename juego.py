import pygame as pg
from configuracion import _PANTALLA_ANCHO, _PANTALLA_ALTURA
from escenas import Portada, Partida, Resumen


class Juego():
    def __init__(self):
        self.pantalla = pg.display.set_mode(
            (_PANTALLA_ANCHO, _PANTALLA_ALTURA))
        self.escenas = [
            Portada(self.pantalla),
            Partida(self.pantalla),
            Resumen(self.pantalla)
        ]

    def jugar(self):

        for escena in self.escenas:
            escena.bucle_principal()

        pg.quit()