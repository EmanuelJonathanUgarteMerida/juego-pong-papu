import random
import pygame
from pygame import sprite
import paleta
import bola
import objeto


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
    pelota_centro_v = pantalla_centro_v-_BOLA_DIMEN/2
    pelota_centro_h = pantalla_centro_h-_BOLA_DIMEN/2

    def __init__(self):
        pygame.init()
        self.reloj = pygame.time.Clock()
        self.pantalla = pygame.display.set_mode(
            (self._PANTALLA_ANCHO, self._PANTALLA_ALTURA))
        pygame.display.set_caption(self._JUEGO_VENTANA_NOMBRE)

        self.jugador1 = paleta.Paleta(
            'Jugador1',
            pygame.K_a,
            pygame.K_z,
            self._VELOCIDAD,
            self._PANTALLA_ALTURA,
            self._PANTALLA_MARGEN_LATERAL,
            self.paleta_centro_v,
            self._PALETA_ANCHO,
            self._PALETA_ALTURA)

        self.jugador2 = paleta.Paleta(
            'Jugador2',
            pygame.K_UP,
            pygame.K_DOWN,
            self._VELOCIDAD,
            self._PANTALLA_ALTURA,
            self._PANTALLA_ANCHO-self._PALETA_ANCHO-self._PANTALLA_MARGEN_LATERAL,
            self.paleta_centro_v,
            self._PALETA_ANCHO,
            self._PALETA_ALTURA)

        self.bola = bola.Bola(
            self._VELOCIDAD,
            self.pelota_centro_h,
            self.pelota_centro_v,
            self._BOLA_DIMEN,
            self._BOLA_DIMEN
        )

        self.cierra = objeto.Objeto()
        pygame.transform.scale(self.cierra.image, (10, 10))
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.cierra)

    def colision_bordes(self):
        if self.bola.y >= self._PANTALLA_ALTURA-self.bola.height or self.bola.y <= 0:
            self.bola.velocidad_y = -self.bola.velocidad_y

        if self.bola.x <= 0 or self.bola.x >= self._PANTALLA_ANCHO-self.bola.width:
            print("punto")
            self.bola.x = self.pantalla_centro_h
            self.bola.y = self.pantalla_centro_v
            self.bola.velocidad_y = random.randint(2, 5)
            self.bola.velocidad_x = -self.bola.velocidad_x

    def colision_paleta(self):
        if self.jugador1.colliderect(self.bola) or self.jugador2.colliderect(self.bola):
            self.bola.velocidad_x = -self.bola.velocidad_x
            self.bola.velocidad_y = random.randint(-10, 10)

    def bucle_principal(self):
        blanco = (255, 255, 255)
        ancho = 10
        while True:
            for evento in pygame.event.get():
                # Zona lógica
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return
            self.jugador1.muevete()
            self.jugador2.muevete()

            #espunto = self.bola.muevete()
            self.bola.muevete()
            # Control puntaje
            # if espunto == 0:
            #    self.jugador2.suma_punto()
            # elif espunto == self._PANTALLA_ANCHO:
            #    self.jugador1.suma_punto()

            self.colision_bordes()
            self.colision_paleta()
            # Control de colisión

            # self.sprites.update()
            # self.sprites.draw(self.pantalla)
            # Zona dibujo, se dibuja el frame
            self.pantalla.fill((255, 0, 142))
            self.pantalla.blit(self.jugador1.nombre_jugador_render(),
                               self.jugador1.nombre_jugador_center(self._PANTALLA_ANCHO, 0, 30))
            self.pantalla.blit(self.jugador2.nombre_jugador_render(),
                               self.jugador2.nombre_jugador_center(self._PANTALLA_ANCHO, self._PANTALLA_ANCHO/2, 30))
            pygame.draw.line(self.pantalla, blanco, (self.pantalla_centro_h,
                             self._PANTALLA_ALTURA), (self.pantalla_centro_h, 0), ancho)
            pygame.draw.rect(self.pantalla, (blanco), self.bola)
            pygame.draw.rect(self.pantalla, (blanco), self.jugador1)
            pygame.draw.rect(self.pantalla, (blanco), self.jugador2)
            pygame.draw.rect(self.pantalla, (blanco), self.bola)
            pygame.display.update()
            self.reloj.tick(self._JUEGO_FPS)


if __name__ == '__main__':
    juego = Pong()
    juego.bucle_principal()
