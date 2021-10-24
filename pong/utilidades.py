import pygame as pg
import os


def texto_pantalla(font, text, color):
    t = font.render(text, True, (color))
    return [t, t.get_rect()]


def cargar_sonido(name):
    pg.mixer.music.load(os.path.join('resources', 'music', name))
    pg.mixer.music.play()
