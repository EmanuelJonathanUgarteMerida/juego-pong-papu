import pygame as pg
from configuracion import PANTALLA_ANCHO, PANTALLA_ALTURA
from escenas import Portada, Partida, Resumen


class Juego():
    def __init__(self):
        pg.init()
        pg.font.init()
        self.pantalla = pg.display.set_mode(
            (PANTALLA_ANCHO, PANTALLA_ALTURA))
        self.escenas = [
            Portada(self.pantalla),
            Partida(self.pantalla),
            Resumen(self.pantalla)
        ]

    def jugar(self):

        for escena in self.escenas:
            escena.bucle_principal()

        pg.quit()
