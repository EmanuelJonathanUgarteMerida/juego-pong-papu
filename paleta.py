import pygame

class Paleta (pygame.Rect):
    def __init__(self, nombre, subir, bajar, velocidad, altura_pantalla, *args, **kwargs):
        super(Paleta, self).__init__(*args, **kwargs)
        self.tecla_subir = subir
        self.tecla_bajar = bajar
        self.velocidad = velocidad
        self.altura_pantalla = altura_pantalla
        self.golpe = 0
        self.puntos = 0
        self.nombre = nombre
        self.nombre_render = self.nombre_jugador_render()

    def nombre_jugador_render(self):
        pygame.font.init()
        myfont = pygame.font.SysFont('Lucida Console', 24)
        self.nombre_render = myfont.render(
            f"{self.nombre} {self.puntos}", True, (255, 255, 255))
        return self.nombre_render

    def nombre_jugador_center(self, ancho, desde, altura):
        ancho /= 2
        return self.nombre_render.get_rect(center=(ancho/2+desde, altura))

    def muevete(self, key):
        if key == self.tecla_subir:
            self.y -= self.velocidad
            if self.y < 0:
                self.y = 0

        elif key == self.tecla_bajar:
            self.y += self.velocidad
            if self.y > self.altura_pantalla-self.height:
                self.y = self.altura_pantalla-self.height

    def golpe_realizado(self):
        self.golpe += 1

    def suma_punto(self):
        self.puntos += 1