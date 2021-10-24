import os
import pygame as pg
from pygame import Rect, font
from pygame.draw import circle
from pygame.mixer import pause
from pong.entidades import Paleta, Bola
import pygame
from . import BOLA_DIMEN, CONTACTO, CUENTA_ATRAS, FIN_PARTIDA, GRIS, INICIAR_PARTIDA, MARCA_PUNTO, REBOTE, SELECCION_JUGADOR, TAMANIO_KEY, FUENTE, NEGRO, PARA_EMPEZAR, PANTALLA_ANCHO, PANTALLA_ALTURA, PANTALLA_MARGEN_LATERAL, BLANCO, ANCHO_LINEA, VELOCIDAD_B, VOLVER_EMPEZAR, pantalla_centro_h, JUEGO_FPS, LIMITE_MARCADOR, PALETA_ANCHO, PALETA_ALTO
import pong.utilidades as util


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.jugadores = 0
        fuente = pg.font.Font(os.path.join(
            'resources', 'fonts', FUENTE), 50)
        self.uno = util.texto_pantalla(fuente, '1', BLANCO)
        self.uno[1].midright = (PANTALLA_ANCHO/2-50, PANTALLA_ALTURA/2)
        self.dos = util.texto_pantalla(fuente, '2', BLANCO)
        self.dos[1].midleft = (PANTALLA_ANCHO/2+50, PANTALLA_ALTURA/2)
        fuente = pg.font.Font(os.path.join('resources', 'fonts', FUENTE), 10)
        self.texto_inicio = util.texto_pantalla(fuente, PARA_EMPEZAR, BLANCO)
        self.texto_inicio[1].midbottom = (PANTALLA_ANCHO/2, PANTALLA_ALTURA-20)

    def bucle_principal(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        if self.jugadores != 0:
                            util.cargar_sonido(INICIAR_PARTIDA)
                            return
                    elif event.key in (pg.K_1, pg.K_KP1):
                        self.jugadores = 1
                        util.cargar_sonido(SELECCION_JUGADOR)
                    elif event.key in (pg.K_KP2, pg.K_KP2):
                        self.jugadores = 2
                        util.cargar_sonido(SELECCION_JUGADOR)

            # pintamos el fondo
            self.pantalla.fill(GRIS)

            # pintamos los textos (como empezar y selección de jugadores)
            self.pantalla.blit(self.texto_inicio[0], self.texto_inicio[1])

            self.pantalla.blit(self.uno[0], self.uno[1])
            self.pantalla.blit(self.dos[0], self.dos[1])

            # marcamos la selección de jugadores
            if self.jugadores == 1:
                margen_recuadro = 20
                pygame.draw.rect(self.pantalla, BLANCO, pygame.Rect(self.uno[1].x-margen_recuadro/2,
                                 self.uno[1].y-margen_recuadro/2, self.uno[1].width+margen_recuadro, self.uno[1].height+margen_recuadro),  2, 3)
            elif self.jugadores == 2:
                pygame.draw.rect(self.pantalla, BLANCO, pygame.Rect(self.dos[1].x-margen_recuadro/2,
                                 self.dos[1].y-margen_recuadro/2, self.dos[1].width+margen_recuadro, self.dos[1].height+margen_recuadro),  2, 5)

            pg.display.flip()


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.fuente = pg.font.Font(os.path.join(
            'resources', 'fonts', FUENTE), 20)
        self. cuenta_atras = CUENTA_ATRAS
        self.inicializar()

    def inicializar(self):
        self.jugador1 = Paleta(
            'Jugador1', (pygame.K_a, pygame.K_z), PANTALLA_MARGEN_LATERAL)
        self.jugador2 = Paleta(
            'Jugador2', (pygame.K_UP, pygame.K_DOWN), PANTALLA_ANCHO-PALETA_ANCHO-PANTALLA_MARGEN_LATERAL)

        self.bola = Bola()
        self.marcador = Marcador()
        self.pausar = False

    def colision_paleta(self):
        if self.bola.colliderect(self.jugador1) or self.bola.colliderect(self.jugador2):
            self.bola.velocidad_x = -self.bola.velocidad_x
            util.cargar_sonido(CONTACTO)

    def colision_bordes(self):
        if self.bola.y >= PANTALLA_ALTURA-self.bola.height or self.bola.y <= 0:
            self.bola.velocidad_y = -self.bola.velocidad_y
            util.cargar_sonido(REBOTE)
        elif self.bola.x <= 0:
            self.bola.velocidad_x = -self.bola.velocidad_x
            self.comprobar_colision(self.jugador2)
        elif self.bola.x >= PANTALLA_ANCHO-self.bola.width:
            self.bola.velocidad_x = -self.bola.velocidad_x
            self.comprobar_colision(self.jugador1)

    def comprobar_colision(self, jugador):
        jugador.puntos += 1
        if jugador.puntos == LIMITE_MARCADOR:
            texto = util.texto_pantalla(self.fuente, jugador.nombre, BLANCO)
            self.pantalla.blit(texto[0], texto[1])
            util.cargar_sonido(FIN_PARTIDA)
        else:
            util.cargar_sonido(MARCA_PUNTO)
        self.bola.iniciar()
        self.jugador2.midright = (self.jugador2.right, PANTALLA_ALTURA/2)
        self.jugador1.midleft = (self.jugador1.x, PANTALLA_ALTURA/2)
        self.pausar = True

    def bucle_principal(self):
        alguiengana = False
        contar = 3
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pg.quit()
                elif event.type == pg.KEYDOWN:
                    if alguiengana and event.key == pg.K_SPACE:
                        self.inicializar()
                        alguiengana = False

            # pintamos el fondo
            self.pantalla.fill(GRIS)

            if alguiengana:
                txt = self.marcador.volver_jugar()
                self.pantalla.blit(txt[0], txt[1])
                #ganador = self.marcador.ganador()
                #ganador_rect = ganador.get_rect()

            else:
                # hacemos que se muevan las entidades
                self.jugador1.muevete()
                self.jugador2.muevete()
                self.bola.muevete()

                if LIMITE_MARCADOR in (self.jugador1.puntos, self.jugador2.puntos):
                    self.bola.center = (PANTALLA_ANCHO/2, PANTALLA_ALTURA/2)
                    alguiengana = True

                # comprobamos las coliciones
                self.colision_paleta()
                self.colision_bordes()
            # pintamos marcador
            puntos = self.marcador.pintar((1, self.jugador1.puntos))
            self.pantalla.blit(puntos[0], puntos[1])

            puntos = self.marcador.pintar((2, self.jugador2.puntos))
            self.pantalla.blit(puntos[0], puntos[1])

            # pintamos la red
            self.dibujar_red()
            # pintamos las entidades que iteractuan
            pygame.draw.circle(self.pantalla, (BLANCO),
                               (self.bola.x+BOLA_DIMEN/2, self.bola.y+BOLA_DIMEN/2), BOLA_DIMEN/2)
            pygame.draw.rect(self.pantalla, (BLANCO), self.jugador1)
            pygame.draw.rect(self.pantalla, (BLANCO), self.jugador2)
            #pygame.draw.rect(self.pantalla, (BLANCO), self.bola)

            if self.pausar:
                c = util.texto_pantalla(self.fuente, f'{contar}', BLANCO)
                c[1].center = (PANTALLA_ANCHO/2, PANTALLA_ALTURA/2)
                self.pantalla.blit(c[0], c[1])
                contar -= 1
                if contar == 0:
                    self.pausar = False
                    contar = 3
                else:
                    pg.time.delay(1000)
            else:
                pass
            pg.display.flip()
            self.reloj.tick(JUEGO_FPS)

    def dibujar_red(self):
        y_start = 20
        y_end = y_start+10
        puntos = PANTALLA_ALTURA-20
        while y_end < puntos:
            pygame.draw.line(self.pantalla, BLANCO, (pantalla_centro_h,
                             y_start), (pantalla_centro_h, y_end), ANCHO_LINEA)
            y_start = y_end+10
            y_end = y_start+10


class Marcador:
    posicion_rect = (0, 0)
    margen_sup = 10
    margen_hor = 20

    def __init__(self):
        self.fuente = pg.font.Font(os.path.join(
            'resources', 'fonts', FUENTE), 30)
        self.centro = PANTALLA_ANCHO/2

    def pintar(self, jugador):
        texto = util.texto_pantalla(self.fuente, str(jugador[1]), BLANCO)
        if jugador[0] == 1:
            texto[1].topright = (self.centro-self.margen_hor, self.margen_sup)
        elif jugador[0] == 2:
            texto[1].topleft = (self.centro+self.margen_hor, self.margen_sup)
        return texto

    def volver_jugar(self):
        f = pg.font.Font(os.path.join('resources', 'fonts', FUENTE), 16)
        texto = util.texto_pantalla(f, VOLVER_EMPEZAR, BLANCO)
        texto[1].midbottom = (self.centro, PANTALLA_ALTURA-self.margen_sup)
        return texto

    def ganador(self):
        f = pg.font.Font(os.path.join('resources', 'fonts', FUENTE), 16)
        gana = f.render('Jugador Ganador', True, BLANCO)
        return gana
