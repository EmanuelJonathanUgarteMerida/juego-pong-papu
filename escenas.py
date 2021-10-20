import os
import pygame as pg
from pygame import font
import pygame
from configuracion import _PARA_EMPEZAR, _PANTALLA_ANCHO, _PANTALLA_ALTURA, _PANTALLA_MARGEN_LATERAL, _BLANCO, _ARIAL, _JUEGO_FPS


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

        self.texto_jugador_2 = ''
        self.jugadores = 0
        self.logo = pg.image.load(os.path.join(
            'resources', 'images', 'logo.png'))
        self.logo_pos = (_PANTALLA_ANCHO/2-self.logo.get_width/2,)
        fuente = pg.font.Font(os.path.join(
            'resources', 'fonts', 'Pacifico-Regular.ttf'), 20)
        self.texto_inicio = fuente.render(_PARA_EMPEZAR, True, 'red')
        self.texto_inicio_pos = (
            _PANTALLA_ANCHO/2 - self.texto_inicio.get_width() / 2,
            _PANTALLA_ALTURA - _PANTALLA_MARGEN_LATERAL - self.texto_inicio.get_height()
        )
        self.texto_jugador_1 = fuente.render('1', True, 'pink')
        self.texto_jugador_1_pos = (200, 200)
        self.texto_jugador_2 = fuente.render('2', True, 'pink')
        self.texto_jugador_2_pos = (400, 400)

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
            self.pantalla.fill((99, 99, 150))
            self.pantalla.blit(self.logo, self.logo_pos)
            self.pantalla.blit(self.texto_inicio, self.texto_inicio_pos)
            self.pantalla.blit(self.texto_jugador_1, self.texto_jugador_1_pos)
            self.pantalla.blit(self.texto_jugador_2, self.texto_jugador_2_pos)
            pg.display.flip()


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.fondo = pg.image.load(os.path.join(
            'resources', 'images', 'fondo.jpeg'))
        self.fondo_rect = self.fondo.get_rect()
        self.fondo_rect.center(_PANTALLA_ANCHO/2, _PANTALLA_ALTURA/2)
        self.marcador= Marcador()

    def bucle_principal(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pg.quit()
            self.pantalla.blit(self.fondo, self.fondo_rect)
            pg.display.flip()
            self.reloj.tick(_JUEGO_FPS)


class Resumen(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)


class Marcador:
    posicion = (0, 0)
    margen_sup = 10
    margen_hor = 20

    def __init__(self):
        self.fuente = pg.font.Font(os.path.join(
            'resources', 'fonts', 'Pacifico-Regular.ttf'), 20)
        self.centro = _PANTALLA_ANCHO/2
        self.color = _BLANCO

    def pintar(self, jugador):
        texto = self.fuente.render(str(jugador[1]), True, self.color)
        ancho_texto = texto.get_width()

        if jugador[0] == 1:
            self.posicion = (self.centro-ancho_texto -
                             self.margen_hor, self.margen_sup)
        elif jugador[0] == 2:
            self.posicion = (self.centro + self.margen_hor, self.margen_sup)
        return texto
