import pygame
from pygame import sprite
import paleta
import bola
import objeto


class Pong:
    # constantes juego
    _JUEGO_VENTANA_NOMBRE = 'The REAL PONG RCTM!'
    _JUEGO_FPS = 60
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
    _VELOCIDAD = 5
    paleta_centro_v = pantalla_centro_v-_PALETA_ALTURA/2

    # constantes bola
    _BOLA_DIMEN = 20
    pelota_centro_v = pantalla_centro_v-_BOLA_DIMEN/2
    pelota_centro_h = pantalla_centro_h-_BOLA_DIMEN/2

    def __init__(self):
        pygame.init()
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
            self._PANTALLA_ANCHO,
            self._PANTALLA_ALTURA,
            self.pelota_centro_h,
            self.pelota_centro_v,
            self._BOLA_DIMEN,
            self._BOLA_DIMEN
        )

        self.cierra = objeto.Objeto()
        pygame.transform.scale(self.cierra.image,(10,10))
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.cierra)

    def bucle_principal(self):
        pausado = False
        p = 0
        teclas_j1 = (self.jugador1.tecla_subir, self.jugador1.tecla_bajar)
        teclas_j2 = (self.jugador2.tecla_bajar, self.jugador2.tecla_subir)
        tecla_j1 = ''
        tecla_j2 = ''
        color = (255, 255, 255)
        ancho = 10
        while True:
            pygame.time.Clock().tick(self._JUEGO_FPS)
            pressed = pygame.key.get_pressed()
            presionando_j1 = pressed[self.jugador1.tecla_bajar] or pressed[self.jugador1.tecla_subir]
            presionando_j2 = pressed[self.jugador2.tecla_bajar] or pressed[self.jugador2.tecla_subir]

            for evento in pygame.event.get():
                # Zona lógica
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return
                    if evento.key == pygame.K_SPACE:
                        pausado = not pausado
                        pass
                    elif evento.key in teclas_j1:
                        tecla_j1 = evento.key
                    elif evento.key in teclas_j2:
                        tecla_j2 = evento.key

            if presionando_j1:
                self.jugador1.muevete(tecla_j1)

            if presionando_j2:
                self.jugador2.muevete(tecla_j2)

            self.pantalla.fill((255, 0, 142))
            espunto = self.bola.muevete()
            # Control puntaje
            if espunto == 0:
                self.jugador2.suma_punto()
            elif espunto == self._PANTALLA_ANCHO:
                self.jugador1.suma_punto()

            self.pantalla.blit(self.jugador1.nombre_jugador_render(),
                               self.jugador1.nombre_jugador_center(self._PANTALLA_ANCHO, 0, 30))
            self.pantalla.blit(self.jugador2.nombre_jugador_render(),
                               self.jugador2.nombre_jugador_center(self._PANTALLA_ANCHO, self._PANTALLA_ANCHO/2, 30))

            # Control de colisión
            if self.bola.colliderect(self.jugador1):
                self.bola.rebote_por_paleta()
                self.jugador1.golpe_realizado()
            elif self.bola.colliderect(self.jugador2):
                self.bola.rebote_por_paleta()
                self.jugador2.golpe_realizado()
            self.sprites.update()
            self.sprites.draw(self.pantalla)
            # Zona dibujo, se dibuja el frame
            pygame.draw.line(self.pantalla, color, (self.pantalla_centro_h,
                             self._PANTALLA_ALTURA), (self.pantalla_centro_h, 0), ancho)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.bola)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.jugador1)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.jugador2)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.bola)
            pygame.display.update()


if __name__ == '__main__':
    juego = Pong()
    juego.bucle_principal()
