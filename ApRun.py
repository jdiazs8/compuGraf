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
imagen_fondo = simplegui.load_image("https://www.dropbox.com/s/thpb5tgrjfsxxvx/presentation-3-e1478644528432.png?dl=1")
obstaculos = ['https://www.dropbox.com/s/8xl28u2lqymsbio/hielo.png?dl=1',
              'https://www.dropbox.com/s/ie9osvrdytwaswy/piedra.png?dl=1',
              'https://www.dropbox.com/s/k3ziquuae84f38t/tronco.png?dl=1',
              'https://www.dropbox.com/s/4q8idgnsb9777ik/rocas7.png?dl=1']
sprites_obstaculos = ['https://www.dropbox.com/s/7msvpmaom0p8ex2/fogataSprite.png?dl=1']
sprites_protagonista = ['https://www.dropbox.com/s/netfiplix1wmi6b/PersonCorriendo.png?dl=1']
antagonista = ['https://www.dropbox.com/s/gq1qjtzjolh39sa/2017-09-11.png?dl=1']
imagen_monedas = simplegui.load_image('https://www.dropbox.com/s/m2co448t3gcpe6i/monedasOro.PNG?dl=1')

# MANEJADORES DE EVENTOS
class Escenario:
    def __init__(self, posicion):
        self.posicion = posicion


class Escenografia(Escenario):
    def __init__(self, posicion):
        self.posicion = posicion

class Fondo(Escenografia):
    def __init__(self, image, posicion):
        self.image = image
        self.image_tamano = [self.image.get_width(), self.image.get_height()]

    def draw(self, canvas):
        canvas.draw_image(self.image, [self.image_tamano[0] // 2, self.image_tamano[1] // 2], self.image_tamano,
                          [LIENZO[0] // 2, LIENZO[1] // 2], self.image_tamano)
        canvas.draw_text('Tiempo: ' + str(TIEMPO), (80, 50), 20, 'White', 'serif')
        canvas.draw_text('Distancia: ' + str(DISTANCIA), (400, 50), 20, 'White', 'serif')
        canvas.draw_text('Puntos: ' + str(PUNTAJE), (800, 50), 20, 'White', 'serif')

class Obstaculo(Escenografia):
    def __init__(self, image, posicion):
        self.image = image
        self.image_tamano = [self.image.get_width(), self.image.get_height()]
        self.posicion = posicion

    def draw(self, canvas):
        canvas.draw_image(self.image, [self.image_tamano[0] // 2, self.image_tamano[1] // 2], self.image_tamano,
                          self.posicion, self.image_tamano)


class Accesorio(Escenografia):
    def __init__(self, image, posicion, frames, refresco):
        self.image = image
        self.frames = frames
        self.refresco = refresco
        self.time = 0
        self.frame_centro = [0,0]
        self.image_tamano = [self.image.get_width()//self.frames, self.image.get_height()]
        self.image_centro = [self.image_tamano[0]//2, self.image_tamano[1]//2]
        self.posicion = posicion

    def anima_sprite(self):
        sprite_index = (self.time% self.frames)//1
        self.frame_centro = [self.image_centro[0] + sprite_index * self.image_tamano[0], self.image_centro[1]]
        self.time += 1
        
    def draw(self, canvas):
        canvas.draw_image(self.image, self.frame_centro, self.image_tamano, self.posicion, self.image_tamano)

class Personaje(Escenario):
    def __init__(self, image, posicion):
        self.imagePeronaje = image
        self.image_tamano = [self.imagePeronaje.get_width(), self.imagePeronaje.get_height()]
        self.posicion = posicion

    def draw(self, canvas):
        canvas.draw_image(self.imagePeronaje, [self.image_tamano[0] // 2, self.image_tamano[1] // 2], self.image_tamano,
                          self.posicion, self.image_tamano)

class Protagonista(Personaje):
    def __init__(self, image, posicion, frames, refresco):
        self.image = image
        self.frames = frames
        self.refresco = refresco
        self.time = 0
        self.frame_centro = [0,0]
        self.image_tamano = [self.image.get_width()//self.frames, self.image.get_height()]
        self.image_centro = [self.image_tamano[0]//2, self.image_tamano[1]//2]
        self.posicion = posicion

    def anima_sprite(self):
        sprite_index = (self.time% self.frames)//1
        self.frame_centro = [self.image_centro[0] + sprite_index * self.image_tamano[0], self.image_centro[1]]
        self.time += 1
        
    def draw(self, canvas):
        canvas.draw_image(self.image, self.frame_centro, self.image_tamano, self.posicion, self.image_tamano)


class Antagonista(Personaje):
    def __init__(self, image, posicion, frames, refresco):
        self.imagePeronaje = image
        self.frames = frames
        self.refresco = refresco
        self.time = 0
        self.frame_centro = [0,0]
        self.image_tamano = [self.imagePeronaje.get_width()//self.frames, self.imagePeronaje.get_height()]
        self.image_centro = [self.image_tamano[0]//2, self.image_tamano[1]//2]
        self.posicion = posicion

    def anima_sprite(self):
        sprite_index = (self.time% self.frames)//1
        self.frame_centro = [self.image_centro[0] + sprite_index * self.image_tamano[0], self.image_centro[1]]
        self.time += 1
        
    def draw(self, canvas):
        canvas.draw_image(self.imagePeronaje, self.frame_centro, self.image_tamano, self.posicion, self.image_tamano)
    
# MANEJADOR DE DIBUJO
def draw_handler(canvas):
    fondo.draw(canvas)
    rocas.draw(canvas)
    #roca.draw(canvas)
    protagonista.draw(canvas)
    moneda.draw(canvas)
    antagonista.draw(canvas)
    fogata.draw(canvas)


# REGISTRO DE CONTROLES Y OBJETOS
frame = simplegui.create_frame('Apocalyse Runner', LIENZO[0], LIENZO[1])
frame.set_draw_handler(draw_handler)
fondo = Fondo(imagen_fondo, [0, 0])
imagen_rocas = simplegui.load_image(obstaculos[3])
rocas = Obstaculo(imagen_rocas, [600, 590])
#imagen_roca = simplegui.load_image(obstaculos[2])
#roca = Obstaculo(imagen_roca, [900, 590])
imagen_protagonista = simplegui.load_image(sprites_protagonista[0])
imagen_antagonista = simplegui.load_image(antagonista[0])
image_fogata = simplegui.load_image(sprites_obstaculos[0])
fogata = Accesorio(image_fogata, [900, 480],8,100)
protagonista = Protagonista(imagen_protagonista, [400, 590], 4, 100)
moneda = Accesorio(imagen_monedas, [600, 450],12,70)
antagonista = Antagonista(imagen_antagonista, [170, 530], 6, 100)
timer_protagonista = simplegui.create_timer(protagonista.refresco, protagonista.anima_sprite)
timer_antagonista = simplegui.create_timer(antagonista.refresco, antagonista.anima_sprite)
timer_moneda = simplegui.create_timer(moneda.refresco, moneda.anima_sprite)
timer_fogata = simplegui.create_timer(fogata.refresco, fogata.anima_sprite)
# INICIO
frame.start()
timer_protagonista.start()
timer_antagonista.start()
timer_moneda.start()
timer_fogata.start()