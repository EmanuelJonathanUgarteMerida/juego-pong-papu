import pygame
import configuracion as cf


class Marcador:
    posicion = (0, 0)
    margen_sup = 10
    margen_hor = 20

    def __init__(self, color):
        self.letra_marcador = pygame.font.SysFont(cf._ARIAL, 50)
        self.centro = pygame.display.get_surface().get_width()/2
        self.color = color

    def pintar(self, jugador):
        texto = pygame.font.Font.render(
            self.letra_marcador, str(jugador[1]), True, self.color)
        ancho_texto = texto.get_width()

        if jugador[0] == 1:
            self.posicion = (self.centro+self.margen_hor, self.margen_sup)
        elif jugador[0] == 2:
            self.posicion = (self.centro-ancho_texto -
                             self.margen_hor, self.margen_sup)
        return texto
