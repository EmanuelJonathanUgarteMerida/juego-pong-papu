import pygame as pg
from . import LIMITE_MARCADOR, PANTALLA_ANCHO, PANTALLA_ALTURA
from pong.escenas import Portada, Partida


class Juego():
    def __init__(self):
        pg.init()
        pg.font.init()
        pg.mixer.init()

        self.dificultad = {'faFcil': 3, 'normal': 5, 'dificil': 20}
        self.jugadores = 0
        self.sonido = True
        self.gana_marcador = LIMITE_MARCADOR
        self.bola_lenta_sevicio = True

        self.pantalla = pg.display.set_mode(
            (PANTALLA_ANCHO, PANTALLA_ALTURA))
        self.escenas = [
            Portada(self.pantalla),
            Partida(self.pantalla)
        ]

    def jugar(self):

        for escena in self.escenas:
            escena.bucle_principal()

        pg.quit()
