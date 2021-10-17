import pygame


class Bola (pygame.Rect):
    _VELOCIDAD_Y = 2
    _VELOCIDAD_X = 4

    def __init__(self, limite_horizontal, limite_vertical, *args, **kwargs):
        super(Bola, self).__init__(*args, **kwargs)
        self.limite_horizontal = limite_horizontal
        self.limite_vertical = limite_vertical
        self.velocidad_y = self._VELOCIDAD_Y
        self.velocidad_x = self._VELOCIDAD_X

    def muevete(self):
        # si choca abajo o arriba
        if self.x > self.limite_horizontal or self.x < 0:
            self.x = self.limite_horizontal/2
            self.y = self.limite_vertical/2
            self._VELOCIDAD_Y *= -1
            self._VELOCIDAD_X *= -1
        # choca laterales
        if self.y > self.limite_vertical-self.height or self.y < 0:
            self._VELOCIDAD_Y *= -1

        self.x += self._VELOCIDAD_X
        self.y += self._VELOCIDAD_Y
        return self.x

    def rebote_por_paleta(self):
        #self._VELOCIDAD_X += 1
        #self._VELOCIDAD_Y += 1
        self._VELOCIDAD_X *= -1
