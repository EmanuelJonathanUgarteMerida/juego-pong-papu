import random
import pygame
from pygame import sprite
import configuracion as cf
import paleta
import bola
import objeto
import marcador


class Pong:
    def __init__(self):
        pygame.init()
        self.reloj = pygame.time.Clock()
        self.pantalla = pygame.display.set_mode((cf._PANTALLA_ANCHO, cf._PANTALLA_ALTURA))
        pygame.display.set_caption(cf._JUEGO_VENTANA_NOMBRE)
        pygame.font.init()
        self.ganador = ''
        self.hay_ganador = False
        self.empezar = False		
        self.jugadores=0

        self.jugador1 = paleta.Paleta(
            'Jugador1', (pygame.K_a, pygame.K_z),
            cf._VELOCIDAD,
            cf._PANTALLA_MARGEN_LATERAL)

        self.jugador2 = paleta.Paleta(
            'Jugador2', (pygame.K_UP, pygame.K_DOWN),
            cf._VELOCIDAD,
            cf._PANTALLA_ANCHO-cf._PALETA_ANCHO-cf._PANTALLA_MARGEN_LATERAL)

        self.bola = bola.Bola(cf._VELOCIDAD, cf._BOLA_DIMEN)

        self.marcador = marcador.Marcador(cf._COLOR_TXT_MARCADOR)
		

    def colision_paleta(self):
        if self.jugador1.colliderect(self.bola) or self.jugador2.colliderect(self.bola):
            self.bola.velocidad_x = -self.bola.velocidad_x
            # self.bola.velocidad_y = random.randint(-10, 10)
            self.bola.velocidad_y = -self.bola.velocidad_y

    def colision_bordes(self):
        if self.bola.y >= cf._PANTALLA_ALTURA-self.bola.height or self.bola.y <= 0:
            self.bola.velocidad_y = -self.bola.velocidad_y
        elif self.bola.x <= 0:
            self.comprobar_colision(self.jugador2)
        elif self.bola.x >= cf._PANTALLA_ANCHO-self.bola.width:
            self.comprobar_colision(self.jugador1)

    def comprobar_colision(self, jugador):
        jugador.puntos += 1
        if jugador.puntos == cf._LIMITE_MARCADOR:
            self.hay_ganador = True
            self.texto_ganador(jugador.nombre)
        self.bola.iniciar()

    def texto_ganador(self, jugador):
        mensaje = pygame.font.SysFont(cf._ARIAL, 50)
        self.ganador = pygame.font.Font.render(
            mensaje, f'Ha ganado jugador {jugador}', True, cf._BLANCO)
        w = self.ganador.get_width()

    def bucle_principal(self):
        while True:
            for evento in pygame.event.get():
                # Zona lógica
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        return
                    elif evento.key == pygame.K_SPACE:
                        if self.jugadores != 0:
                            self.empezar=True
                    elif evento.key in (pygame.K_1 ,pygame.K_KP1):
                        self.jugadores=1
                    elif evento.key in (pygame.K_2,pygame.K_KP2):
                        self.jugadores=2

            self.pantalla.fill(cf._NEGRO)
            if self.empezar:
				 # se controla si hay un ganador
                
                if self.hay_ganador:
                    self.pantalla.blit(self.ganador, (cf._PANTALLA_ANCHO/2-self.ganador.get_width()/2, cf._PANTALLA_ALTURA/2-self.ganador.get_height()/2))
                else:
                    self.jugador1.muevete()
                    self.jugador2.muevete()
                    self.bola.muevete()

                    self.colision_paleta()
                    self.colision_bordes()

                    self.pantalla.blit(self.marcador.pintar((1, self.jugador1.puntos)), self.marcador.posicion)
                    self.pantalla.blit(self.marcador.pintar((2, self.jugador2.puntos)), self.marcador.posicion)

                pygame.draw.line(self.pantalla, cf._BLANCO, (cf.pantalla_centro_h,cf._PANTALLA_ALTURA), (cf.pantalla_centro_h, 0), cf._ANCHO_LINEA)
                pygame.draw.rect(self.pantalla, (cf._BLANCO), self.jugador1)
                pygame.draw.rect(self.pantalla, (cf._BLANCO), self.jugador2)
                pygame.draw.rect(self.pantalla, (cf._BLANCO), self.bola)
			
            else:
                color1=(25,200,20)
                color2=(25,200,20)
                if self.jugadores == 1:
                    color1=(0, 255, 0)
                    color2=(255,255,255)
                elif self.jugadores == 2:
                    color1=(255,255,255)
                    color2=(0, 255, 0)					
				#creamos el texto de "Elegir jugadores 1/2"
                mensaje = pygame.font.SysFont(cf._ARIAL, 50)
                texto=pygame.font.Font.render(mensaje,'Selecciona los jugadores:',True,cf._BLANCO)
                texto_coor=(cf._PANTALLA_ANCHO/2-texto.get_width()/2,texto.get_height()+cf._PANTALLA_MARGEN_LATERAL)
				
				#marcamos jugadores si se seleccionan
                uno=pygame.font.Font.render(mensaje,'1',True,cf._BLANCO,color1)
                uno_coor=(cf._PANTALLA_ANCHO/2-uno.get_width()-cf._PANTALLA_MARGEN_LATERAL,cf._PANTALLA_ALTURA-uno.get_height()-cf._PANTALLA_MARGEN_LATERAL)
				
                dos=pygame.font.Font.render(mensaje,'2',True,cf._BLANCO,color2)
                dos_coor=(cf._PANTALLA_ANCHO/2+cf._PANTALLA_MARGEN_LATERAL,cf._PANTALLA_ALTURA-uno.get_height()-cf._PANTALLA_MARGEN_LATERAL)
				
                self.pantalla.blit(texto,texto_coor)
                self.pantalla.blit(uno,uno_coor)
                self.pantalla.blit(dos,dos_coor)
				#presionar "empezar" tecla espacio
				
				
            pygame.display.flip()
            self.reloj.tick(cf._JUEGO_FPS)


if __name__ == '__main__':
    juego = Pong()
    juego.bucle_principal()
