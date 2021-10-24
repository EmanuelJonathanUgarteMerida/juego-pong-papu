import pygame
# constantes juego
JUEGO_NOMBRE = 'The REAL PONG RCTM!'
PARA_EMPEZAR = 'Para empezar presiona la tecla <ESPACIO>'
VOLVER_EMPEZAR='Presiona <ESPACIO> para volver a jugar'
JUEGO_FPS = 60
VELOCIDAD_B = 5
VELOCIDAD_P = 4
ANCHO_LINEA = 4
# constantes pantalla
PANTALLA_ALTURA = 400
PANTALLA_ANCHO = 900
PANTALLA_MARGEN_LATERAL = 5
pantalla_centro_h = PANTALLA_ANCHO/2
pantalla_centro_v = PANTALLA_ALTURA/2

# constantes paleta
PALETA_ANCHO = 5
PALETA_ALTO = 70

paleta_centro_v = pantalla_centro_v-PALETA_ALTO/2

# constantes bola
BOLA_DIMEN = 15

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ARIAL = 'arial'

LIMITE_MARCADOR = 1

FUENTE = 'ARCADE_N.TTF'
TAMANIO_KEY = 70

CUENTA_ATRAS = 3

GRIS = (31, 31, 31, 12)

# Sonidos
INICIAR_PARTIDA = 'inicia_partida.mp3'
SELECCION_JUGADOR = 'seleccion_jugador.mp3'
CONTACTO = 'contacto.mp3'
FIN_PARTIDA = 'fin_partida.mp3'
MARCA_PUNTO='pierde_punto.mp3'
REBOTE='rebote_superficie.mp3'
