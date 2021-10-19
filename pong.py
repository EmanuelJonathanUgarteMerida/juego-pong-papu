import random
import pygame
from pygame import sprite
import paleta
import bola
import objeto
import marcador


class Pong:
    # constantes juego
    _JUEGO_VENTANA_NOMBRE = 'The REAL PONG RCTM!'
    _JUEGO_FPS = 60
    _VELOCIDAD = 5
    # constantes pantalla
    _PANTALLA_ALTURA = 480
    _PANTALLA_ANCHO = 720
    _PANTALLA_MARGEN_LATERAL = 40
    pantalla_centro_h = _PANTALLA_ANCHO/2
    pantalla_centro_v = _PANTALLA_ALTURA/2
    _PANTALLA_CLOCK = pygame.time.Clock()

    # constantes paleta
    _PALETA_ANCHO = 10
    _PALETA_ALTURA = 40

    paleta_centro_v = pantalla_centro_v-_PALETA_ALTURA/2

    # constantes bola
    _BOLA_DIMEN = 20

    def __init__(self):
        pygame.init()
        self.reloj = pygame.time.Clock()
        self.pantalla = pygame.display.set_mode(
            (self._PANTALLA_ANCHO, self._PANTALLA_ALTURA))
        pygame.display.set_caption(self._JUEGO_VENTANA_NOMBRE)
        pygame.font.init()

        self.jugador1 = paleta.Paleta(
            'Jugador1', (pygame.K_a, pygame.K_z),
            self._VELOCIDAD,
            self._PANTALLA_MARGEN_LATERAL)

        self.jugador2 = paleta.Paleta(
            'Jugador2', (pygame.K_UP, pygame.K_DOWN),
            self._VELOCIDAD,
            self._PANTALLA_ANCHO-self._PALETA_ANCHO-self._PANTALLA_MARGEN_LATERAL)

        self.bola = bola.Bola(self._VELOCIDAD, self._BOLA_DIMEN)

        self.marcador = marcador.Marcador('white')

    def colision_bordes(self):
        hay_ganador = False
        texto = ''
        algo = [False]
        if self.bola.y >= self._PANTALLA_ALTURA-self.bola.height or self.bola.y <= 0:
            self.bola.velocidad_y = -self.bola.velocidad_y
        elif self.bola.x <= 0:
            self.jugador2.suma_punto()
            if self.jugador2.puntos == 2:
                algo[0] = True
                algo.append(self.ganador('Jugador 2'))
            self.bola.iniciar()
        elif self.bola.x >= self._PANTALLA_ANCHO-self.bola.width:
            self.jugador1.suma_punto()
            if self.jugador1.puntos == 2:
                algo[0] = True
                algo.append(self.ganador('Jugador 1'))
            self.bola.iniciar()
        return algo

    def ganador(self, jugador):
        mensaje = pygame.font.SysFont('arial', 50)
        texto = pygame.font.Font.render(
            mensaje, f'Ha ganado jugador {jugador}', True, (255, 255, 255))
        return texto

    def colision_paleta(self):
        if self.jugador1.colliderect(self.bola) or self.jugador2.colliderect(self.bola):
            self.bola.velocidad_x = -self.bola.velocidad_x
            self.bola.velocidad_y = random.randint(-10, 10)

    def bucle_principal(self):
        blanco = (255, 255, 255)
        ancho = 10
        gano=False
        hay_ganador=(False,0)
        while True:
            for evento in pygame.event.get():
                # Zona lógica
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return
            
            if hay_ganador[0]:
                # actualizamos marcador
                self.pantalla.blit(hay_ganador[1], (250, 250))
            else:
                self.jugador1.muevete()
                self.jugador2.muevete()

                self.bola.muevete()
                hay_ganador = self.colision_bordes()
                self.colision_paleta()

                self.pantalla.fill((255, 0, 142))
                self.pantalla.blit(self.marcador.pintar_marcador(
                    (1, self.jugador1.puntos)), self.marcador.posicion)
                self.pantalla.blit(self.marcador.pintar_marcador(
                    (2, self.jugador2.puntos)), self.marcador.posicion)
                pygame.draw.rect(self.pantalla, (blanco), self.bola)
                pygame.draw.rect(self.pantalla, (blanco), self.jugador1)
                pygame.draw.rect(self.pantalla, (blanco), self.jugador2)
                pygame.draw.rect(self.pantalla, (blanco), self.bola)

            pygame.draw.line(self.pantalla, blanco, (self.pantalla_centro_h,
                             self._PANTALLA_ALTURA), (self.pantalla_centro_h, 0), ancho)
            pygame.display.update()
            self.reloj.tick(self._JUEGO_FPS)


if __name__ == '__main__':
    juego = Pong()
    juego.bucle_principal()
