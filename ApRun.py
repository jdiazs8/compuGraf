#!/usr/bin/python
# -*- coding: latin-1 -*-

# NOMBRE DEL PROGRAMA: Apocalypsis Runner
# AUTOR DEL PROGRAMA: Jorge Díaz, Michael Montes, Julio Morales, Johan Sánchez

# LIBRERIAS
#import simplegui
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# CONSTANTES Y VARIABLES GLOBALES
LIENZO = [1024, 720]
TIEMPO = 0
DISTANCIA = 0
PUNTAJE = 0

image_fondo = simplegui.load_image("https://www.dropbox.com/s/thpb5tgrjfsxxvx/presentation-3-e1478644528432.png?dl=1")
obstaculos = ['https://www.dropbox.com/s/8xl28u2lqymsbio/hielo.png?dl=1',
              'https://www.dropbox.com/s/ie9osvrdytwaswy/piedra.png?dl=1',
              'https://www.dropbox.com/s/k3ziquuae84f38t/tronco.png?dl=1']
personaje = ['https://www.dropbox.com/s/5kl57rh2jygfpyx/Personage.png?dl=1']

# MANEJADORES DE EVENTOS
class Escenario:
    def __init__(self, posicion):
        self.posicion = posicion


class Escenografia(Escenario):
    def __init__(self):
        pass


class Obstaculo(Escenografia):
    def __init__(self, image, posicion):
        self.image = image
        self.image_tamano = [self.image.get_width(), self.image.get_height()]
        self.posicion = posicion

    def draw(self, canvas):
        canvas.draw_image(self.image, [self.image_tamano[0] // 2, self.image_tamano[1] // 2], self.image_tamano,
                          self.posicion, self.image_tamano)


class Personaje(Escenario):
    def __init__(self, image, posicion):
        self.imagePeronaje = image
        self.image_tamano = [self.imagePeronaje.get_width(), self.imagePeronaje.get_height()]
        self.posicion = posicion

    def draw(self, canvas):
        canvas.draw_image(self.imagePeronaje, [self.image_tamano[0] // 2, self.image_tamano[1] // 2], self.image_tamano,
                          self.posicion, self.image_tamano)


class Fondo(Escenografia):
    def __init__(self, image, posicion):
        self.image = image
        self.image_tamano = [self.image.get_width(), self.image.get_height()]
        print self.image_tamano

    def draw(self, canvas):
        canvas.draw_image(self.image, [self.image_tamano[0] // 2, self.image_tamano[1] // 2], self.image_tamano,
                          [LIENZO[0] // 2, LIENZO[1] // 2], self.image_tamano)
        canvas.draw_text('Tiempo: ' + str(TIEMPO), (80, 50), 20, 'White', 'serif')
        canvas.draw_text('Distancia: ' + str(DISTANCIA), (400, 50), 20, 'White', 'serif')
        canvas.draw_text('Puntos: ' + str(PUNTAJE), (800, 50), 20, 'White', 'serif')


# MANEJADOR DE DIBUJO
def draw_handler(canvas):
    fondo.draw(canvas)
    obstaculo1.draw(canvas)
    obstaculo2.draw(canvas)
    personaje1.draw(canvas)


# REGISTRO DE CONTROLES Y OBJETOS
frame = simplegui.create_frame('Sprite', LIENZO[0], LIENZO[1])
frame.set_draw_handler(draw_handler)
fondo = Fondo(image_fondo, [0, 0])
im = simplegui.load_image(obstaculos[0])
obstaculo1 = Obstaculo(im, [600, 650])
im = simplegui.load_image(obstaculos[1])
obstaculo2 = Obstaculo(im, [900, 650])
imPer = simplegui.load_image(personaje[0])
personaje1 = Personaje(imPer, [80, 570])

# INICIO
frame.start()

