import pygame


class Paleta (pygame.Rect):
    _ANCHO = 10
    _ALTO = 40

    def __init__(self, nombre, teclas, velocidad, posicion_x):
        super(Paleta, self).__init__(posicion_x, 0, self._ANCHO, self._ALTO)
        self.tecla_subir = teclas[0]
        self.tecla_bajar = teclas[1]
        self.velocidad = velocidad
        self.altura_pantalla = pygame.display.get_surface().get_height()
        self.golpe = 0
        self.puntos = 0
        self.nombre = nombre
        self.nombre_render = self.nombre_jugador_render()
        # Init objeto
        self.x = posicion_x
        self.y = self.altura_pantalla/2-self.height/2

    def nombre_jugador_render(self):
        pygame.font.init()
        myfont = pygame.font.SysFont('Lucida Console', 24)
        self.nombre_render = myfont.render(
            f"{self.nombre} {self.puntos}", True, (255, 255, 255))
        return self.nombre_render

    def nombre_jugador_center(self, ancho, desde, altura):
        ancho /= 2
        return self.nombre_render.get_rect(center=(ancho/2+desde, altura))

    def muevete(self):
        if pygame.key.get_pressed()[self.tecla_subir]:
            # if key == self.tecla_subir:
            self.y -= self.velocidad
            if self.y < 0:
                self.y = 0
        elif pygame.key.get_pressed()[self.tecla_bajar]:
            # elif key == self.tecla_bajar:
            self.y += self.velocidad
            if self.y > self.altura_pantalla-self.height:
                self.y = self.altura_pantalla-self.height

    def golpe_realizado(self):
        self.golpe += 1

    def suma_punto(self):
        self.puntos += 1
