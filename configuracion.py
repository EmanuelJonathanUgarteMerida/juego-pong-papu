import pygame
# constantes juego
_JUEGO_VENTANA_NOMBRE = 'The REAL PONG RCTM!'
_JUEGO_FPS = 60
_VELOCIDAD = 5
_ANCHO_LINEA = 5
# constantes pantalla
_PANTALLA_ALTURA = 480
_PANTALLA_ANCHO = 720
_PANTALLA_MARGEN_LATERAL = 40
pantalla_centro_h = _PANTALLA_ANCHO/2
pantalla_centro_v = _PANTALLA_ALTURA/2
_PANTALLA_CLOCK = pygame.time.Clock()

# constantes paleta
_PALETA_ANCHO = 10
_PALETA_ALTO = 40

paleta_centro_v = pantalla_centro_v-_PALETA_ALTO/2

# constantes bola
_BOLA_DIMEN = 20

# marcador
_COLOR_TXT_MARCADOR = 'white'

_BLANCO = (255, 255, 255)
_NEGRO = (0, 0, 0)
_ARIAL = 'arial'

_LIMITE_MARCADOR = 2
