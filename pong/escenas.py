import os
import pygame as pg
from pygame import font
from pong.entidades import Paleta, Bola
import pygame
from . import TAMANIO_KEY, FUENTE, NEGRO, PARA_EMPEZAR, PANTALLA_ANCHO, PANTALLA_ALTURA, PANTALLA_MARGEN_LATERAL, BLANCO, ANCHO_LINEA, pantalla_centro_h, JUEGO_FPS, LIMITE_MARCADOR, PALETA_ANCHO, PALETA_ALTO


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
        self.logo = pg.transform.scale(
            self.logo, (PANTALLA_ANCHO, PANTALLA_ALTURA))
        self.logo.get_rect().center = (PANTALLA_ANCHO/2, PANTALLA_ALTURA/2)

        fuente = pg.font.Font(os.path.join(
            'resources', 'fonts', FUENTE), 50)
        self.texto_jugador_1 = fuente.render('1', True, 'white')
        self.texto_jugador_1_rect = self.texto_jugador_1.get_rect()
        self.texto_jugador_1_rect.midright = (
            PANTALLA_ANCHO/2-50, PANTALLA_ALTURA/2)

        self.texto_jugador_2 = fuente.render('2', True, 'white')
        self.texto_jugador_2_rect = self.texto_jugador_2.get_rect()
        self.texto_jugador_2_rect.midleft = (
            PANTALLA_ANCHO/2+50, PANTALLA_ALTURA/2)

        fuente = pg.font.Font(os.path.join(
            'resources', 'fonts', FUENTE), 10)
        self.texto_inicio = fuente.render(PARA_EMPEZAR, True, 'green')
        self.texto_inicio_rect = self.texto_inicio.get_rect()
        self.texto_inicio_rect.midbottom = (
            PANTALLA_ANCHO/2, PANTALLA_ALTURA-20)

    def bucle_principal(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        if self.jugadores != 0:
                            return
                    elif event.key in (pg.K_1, pg.K_KP1):
                        self.jugadores = 1
                    elif event.key in (pg.K_KP2, pg.K_KP2):
                        self.jugadores = 2

            # pintamos el fondo
            self.pantalla.fill(NEGRO)

            # pintamos el logo
            #self.pantalla.blit(self.logo, self.logo.get_rect())

            # pintamos los textos (como empezar y selección de jugadores)
            self.pantalla.blit(self.texto_inicio, self.texto_inicio_rect)

            self.pantalla.blit(self.texto_jugador_1, self.texto_jugador_1_rect)
            self.pantalla.blit(self.texto_jugador_2, self.texto_jugador_2_rect)

            # marcamos la selección de jugadores
            if self.jugadores == 1:
                pygame.draw.rect(self.pantalla, BLANCO, pygame.Rect(self.texto_jugador_1_rect.x,
                                 self.texto_jugador_1_rect.y, self.texto_jugador_1_rect.width, self.texto_jugador_1_rect.height),  2)
            elif self.jugadores == 2:
                pygame.draw.rect(self.pantalla, BLANCO, pygame.Rect(self.texto_jugador_2_rect.x,
                                 self.texto_jugador_2_rect.y, self.texto_jugador_2_rect.width, self.texto_jugador_2_rect.height),  2)

            pg.display.flip()


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.fondo = pg.image.load(os.path.join(
            'resources', 'images', 'fondo.jpg'))
        self.fondo = pg.transform.scale(
            self.fondo, (PANTALLA_ANCHO, PANTALLA_ALTURA))
        self.fondo_rect = self.fondo.get_rect()
        self.fondo_rect.center = (PANTALLA_ANCHO/2, PANTALLA_ALTURA/2)
        self.fuente = pg.font.Font(os.path.join(
            'resources', 'fonts', FUENTE), 20)

        self.inicializar()

    def inicializar(self):
        self.jugador1 = Paleta(
            'Jugador1', (pygame.K_a, pygame.K_z), PANTALLA_MARGEN_LATERAL)
        self.jugador2 = Paleta(
            'Jugador2', (pygame.K_UP, pygame.K_DOWN), PANTALLA_ANCHO-PALETA_ANCHO-PANTALLA_MARGEN_LATERAL)

        self.bola = Bola()
        self.marcador = Marcador()

    def colision_paleta(self):
        if self.bola.colliderect(self.jugador1) or self.bola.colliderect(self.jugador2):
            self.bola.velocidad_x = -self.bola.velocidad_x
            pg.mixer.music.load(os.path.join(
                'resources', 'music', 'contacto.mp3'))
            pg.mixer.music.play()

    def colision_bola_pelota(self):
        if self.bola.colliderect(self.jugador1):
            if self.bola.left - self.jugador1.right <= 0:
                print('choca por la izquierda')
            elif self.bola.bottom - self.jugador1.top <= 0:
                print('choca por abajo')
            elif self.bola.top - self.jugador1.bottom <= 0:
                print('choca por arriba')

    def colision_bordes(self):
        if self.bola.y >= PANTALLA_ALTURA-self.bola.height or self.bola.y <= 0:
            self.bola.velocidad_y = -self.bola.velocidad_y
        elif self.bola.x <= 0:
            self.comprobar_colision(self.jugador2)
        elif self.bola.x >= PANTALLA_ANCHO-self.bola.width:
            self.comprobar_colision(self.jugador1)

    def comprobar_colision(self, jugador):
        jugador.puntos += 1
        if jugador.puntos == LIMITE_MARCADOR:
            self.texto_ganador(jugador.nombre)
        else:
            pg.mixer.music.load(os.path.join(
                'resources', 'music', 'pierde_punto.mp3'))
            pg.mixer.music.play()
        self.bola.iniciar()

    def texto_ganador(self, jugador):
        self.ganador = self.fuente.render(
            f'Ha ganado jugador {jugador}', True, BLANCO)

    def bucle_principal(self):
        alguiengana = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pg.quit()
                elif event.type == pg.KEYDOWN:
                    if alguiengana and event.key == pg.K_SPACE:
                        self.inicializar()
                        alguiengana = False

            if not alguiengana:
                # hacemos que se muevan las entidades
                self.jugador1.muevete()
                self.jugador2.muevete()
                self.bola.muevete()

                if self.jugador1.puntos == LIMITE_MARCADOR or self.jugador2.puntos == LIMITE_MARCADOR:
                    self.bola.center = (PANTALLA_ANCHO/2, PANTALLA_ALTURA/2)
                    alguiengana = True

                # comprobamos las coliciones
                # self.colision_paleta()
                self.colision_bola_pelota()
                self.colision_bordes()

            # pintamos el fondo
            #self.pantalla.blit(self.fondo, self.fondo_rect)
            self.pantalla.fill(NEGRO)
            if alguiengana:
                self.pantalla.blit(self.marcador.volver_jugar(),
                                   self.marcador.posicion_rect)
            # pintamos marcador
            self.pantalla.blit(self.marcador.pintar(
                (1, self.jugador1.puntos)), self.marcador.posicion_rect)
            self.pantalla.blit(self.marcador.pintar(
                (2, self.jugador2.puntos)), self.marcador.posicion_rect)

            # pintamos la red
            self.dibujar_red()

            # pintamos las entidades que iteractuan
            pygame.draw.rect(self.pantalla, (BLANCO), self.jugador1)
            pygame.draw.rect(self.pantalla, (BLANCO), self.jugador2)
            pygame.draw.rect(self.pantalla, (BLANCO), self.bola)

            pg.display.flip()
            self.reloj.tick(JUEGO_FPS)

    def dibujar_red(self):
        y_start = 20
        y_end = y_start+10
        while y_end < PANTALLA_ALTURA-20:
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
        texto = self.fuente.render(str(jugador[1]), True, BLANCO)
        if jugador[0] == 1:
            self.posicion_rect = texto.get_rect()
            self.posicion_rect.topright = (
                self.centro-self.margen_hor, self.margen_sup)
        elif jugador[0] == 2:
            self.posicion_rect = texto.get_rect()
            self.posicion_rect.topleft = (
                self.centro+self.margen_hor, self.margen_sup)
        return texto

    def volver_jugar(self):
        f = pg.font.Font(os.path.join('resources', 'fonts', FUENTE), 16)
        texto = f.render(
            'Presiona <ESPACIO> para volver a jugar', True, BLANCO)
        self.posicion_rect = texto.get_rect()
        self.posicion_rect.midbottom = (
            self.centro, PANTALLA_ALTURA-self.margen_sup)
        return texto
