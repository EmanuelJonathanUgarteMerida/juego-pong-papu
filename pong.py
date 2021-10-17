import pygame
import paleta
import bola

class Pong:
    # constantes juego
    _JUEGO_VENTANA_NOMBRE = 'The REAL PONG RCTM!'
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

    def bucle_principal(self):
        pygame.key.set_repeat(20)
        while True:
            for evento in pygame.event.get():
                # Zona lógica
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return
                    else:
                        self.jugador1.muevete(evento.key)
                        self.jugador2.muevete(evento.key)
            self.pantalla.fill((255, 0, 142))
            espunto = self.bola.muevete()
            if espunto == 0:
                self.jugador2.suma_punto()
            elif espunto == self._PANTALLA_ANCHO:
                self.jugador1.suma_punto()

            self.pantalla.blit(self.jugador1.nombre_jugador_render(),
                               self.jugador1.nombre_jugador_center(self._PANTALLA_ANCHO, 0, 30))
            self.pantalla.blit(self.jugador2.nombre_jugador_render(),
                               self.jugador2.nombre_jugador_center(self._PANTALLA_ANCHO, self._PANTALLA_ANCHO/2, 30))

            if self.bola.colliderect(self.jugador1):
                self.bola.rebote_por_paleta()
                self.jugador1.golpe_realizado()
            elif self.bola.colliderect(self.jugador2):
                self.bola.rebote_por_paleta()
                self.jugador2.golpe_realizado()

            # Zona dibujo
            pygame.draw.line(self.pantalla, (255, 255, 255),
                             (self.pantalla_centro_h, self._PANTALLA_ALTURA), (self.pantalla_centro_h, 0))
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.bola)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.jugador1)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.jugador2)
            pygame.draw.rect(self.pantalla, (255, 255, 255), self.bola)

            pygame.display.update()
            pygame.time.Clock().tick(60)


if __name__ == '__main__':
    juego = Pong()
    juego.bucle_principal()
