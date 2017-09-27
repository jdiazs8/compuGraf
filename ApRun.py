# NOMBRE DEL PROGRAMA: Apocalypsis Runner
# AUTOR DEL PROGRAMA: Jorge Díaz, Michael Montes, Julio Morales, Johan Sánchez

# LIBRERIAS
#import simplegui
import random
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# CONSTANTES Y VARIABLES GLOBALES
LIENZO = [1024, 720]
TIEMPO = 0
DISTANCIA = 0
PUNTAJE = 0
image_fondo = simplegui.load_image("https://www.dropbox.com/s/4sx8rhu0qb68x1t/Fondo.png?dl=1")
image_piso = simplegui.load_image("https://www.dropbox.com/s/vlz5ixgtfrkocq1/Escenario.png?dl=1")
image_fogata = simplegui.load_image("https://www.dropbox.com/s/7msvpmaom0p8ex2/fogataSprite.png?dl=1")
obstaculos = ['https://www.dropbox.com/s/8xl28u2lqymsbio/hielo.png?dl=1',
              'https://www.dropbox.com/s/ie9osvrdytwaswy/piedra.png?dl=1',
              'https://www.dropbox.com/s/k3ziquuae84f38t/tronco.png?dl=1',
              'https://www.dropbox.com/s/4q8idgnsb9777ik/rocas7.png?dl=1']
sprites_monedas = ['https://www.dropbox.com/s/m2co448t3gcpe6i/monedasOro.PNG?dl=1',
                  'https://www.dropbox.com/s/imw5cpl11gsy7e1/monedasPlata.png?dl=1']
accesorios = []
sprites_protagonista = ['https://www.dropbox.com/s/netfiplix1wmi6b/PersonCorriendo.png?dl=1']
sprites_antagonista = ['https://www.dropbox.com/s/gq1qjtzjolh39sa/2017-09-11.png?dl=1']

# MANEJADORES DE CLASES
class Escenario:
    def __init__(self, posicion):
        self.posicion = posicion
    
    def mover(self):
        pass

class Escenografia(Escenario):
    def __init__(self, posicion):
        Escenario.__init__(self,posicion)

class Fondo(Escenografia):
    def __init__(self, image, posicion, vel):
        Escenografia.__init__(self,posicion)
        self.image = image
        self.vel = vel
        self.image_tamano = [self.image.get_width(), self.image.get_height()]

    def draw(self, canvas):
        canvas.draw_image(self.image, [self.image_tamano[0] // 2, self.image_tamano[1] // 2], self.image_tamano,
                          self.posicion, [self.image_tamano[0]*0.7, self.image_tamano[1]*0.7])
        canvas.draw_text('Tiempo: ' + str(TIEMPO), (80, 50), 20, 'White', 'serif')
        canvas.draw_text('Distancia: ' + str(DISTANCIA), (400, 50), 20, 'White', 'serif')
        canvas.draw_text('Puntos: ' + str(PUNTAJE), (800, 50), 20, 'White', 'serif')

    def mover(self):
        self.posicion[0] += self.vel[0]
        self.posicion[1] += self.vel[1]
        
class Obstaculo(Escenografia):
    def __init__(self, image, posicion):
        Escenografia.__init__(self,posicion)
        self.posicion = posicion
        self.image = image
        self.image_tamano = [self.image.get_width(), self.image.get_height()]
        self.image_centro = [self.image.get_width() // 2, self.image.get_height()// 2]
    
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_centro,self.image_tamano,self.posicion,[self.image_tamano[0] * 0.5,self.image_tamano[1] * 0.5])

class Accesorio(Escenografia):
    def __init__(self, image, posicion, frames, refresco):
        Escenografia.__init__(self,posicion)
        self.image = image
        self.frames = frames
        self.refresco = refresco
        self.time = 0
        self.frame_centro = [0,0]
        self.image_tamano = [self.image.get_width()//self.frames, self.image.get_height()]
        self.image_centro = [self.image_tamano[0]//2, self.image_tamano[1]//2]        

    def anima_sprite(self):
        sprite_index = (self.time% self.frames)//1
        self.frame_centro = [self.image_centro[0] + sprite_index * self.image_tamano[0], self.image_centro[1]]
        self.time += 1
        
    def draw(self, canvas):
        canvas.draw_image(self.image, self.frame_centro, self.image_tamano, self.posicion, [self.image_tamano[0]//2, self.image_tamano[1]//2])

class Personaje(Escenario):
    def __init__(self, image, posicion):
        Escenario.__init__(self,posicion)
        self.image = image
        self.image_tamano = [self.image.get_width(), self.image.get_height()]

    def draw(self, canvas):
        canvas.draw_image(self.image, [self.image_tamano[0] // 2, self.image_tamano[1] // 2], self.image_tamano,
                          self.posicion, self.image_tamano)

class Protagonista(Personaje):
    def __init__(self, image, posicion, frames, refresco, vel):
        Personaje.__init__(self,image,posicion)
        self.frames = frames
        self.refresco = refresco
        self.time = 0
        self.vel = vel
        self.frame_centro = [0,0]
        self.image_tamano = [self.image.get_width()//self.frames, self.image.get_height()]
        self.image_centro = [self.image_tamano[0]//2, self.image_tamano[1]//2]

    def anima_sprite(self):
        sprite_index = (self.time% self.frames)//1
        self.frame_centro = [self.image_centro[0] + sprite_index * self.image_tamano[0], self.image_centro[1]]
        self.time += 1
    
    def mover(self):
        self.posicion[0] += self.vel[0]
        self.posicion[1] += self.vel[1]
        if self.posicion[0] == LIENZO[0] // 2:
            self.colision('x')
        if self.posicion[1] == LIENZO[1]:
            self.colision('y')
           
    def colision(self, dim):
        if dim == 'x':
            self.vel[0] = 0
        if dim == 'y':
            self.vel[1] = 0
        
    def draw(self, canvas):
        canvas.draw_image(self.image, self.frame_centro, self.image_tamano, self.posicion, self.image_tamano)

class Antagonista(Personaje):
    def __init__(self, image, posicion, frames, refresco):
        Personaje.__init__(self,image,posicion)
        self.frames = frames
        self.refresco = refresco
        self.time = 0
        self.frame_centro = [0,0]
        self.image_tamano = [self.image.get_width()//self.frames, self.image.get_height()]
        self.image_centro = [self.image_tamano[0]//2, self.image_tamano[1]//2]

    def anima_sprite(self):
        sprite_index = (self.time% self.frames)//1
        self.frame_centro = [self.image_centro[0] + sprite_index * self.image_tamano[0], self.image_centro[1]]
        self.time += 1
        
    def draw(self, canvas):
        canvas.draw_image(self.imagePeronaje, self.frame_centro, self.image_tamano, self.posicion, self.image_tamano)

# MANEJADORES DE EVENTOS
def keydown_handler(key):
    vel = 1
    
    if key == simplegui.KEY_MAP['left']:
        fondo.vel[0] += vel
        piso.vel[0] += (vel*-2)
    elif key == simplegui.KEY_MAP['right']:
        fondo.vel[0] -= vel
        piso.vel[0] += (vel*-2)
    elif key == simplegui.KEY_MAP['up']:
        protagonista.vel[1] -= vel

# MANEJADOR DE DIBUJO
def draw_handler(canvas):
    fondo.draw(canvas)
    fondo.mover()
    piso.draw(canvas)
    piso.mover()
    rocas.draw(canvas)
    protagonista.draw(canvas)
    fogata.draw(canvas)
    protagonista.mover()         # Actualiza la posición del objeto
    for accesorio in accesorios:
        accesorio.draw(canvas)
    #antagonista.draw(canvas)


# REGISTRO DE CONTROLES Y OBJETOS
frame = simplegui.create_frame('Apocalyse Runner', LIENZO[0], LIENZO[1])
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown_handler)
fondo = Fondo(image_fondo, [(6520 // 2) - 1024, LIENZO[1] // 2], [0,0])
piso = Fondo(image_piso, [(6520 // 2) - 1024, LIENZO[1] // 2], [0,0])
imagen_rocas = simplegui.load_image(obstaculos[3])
rocas = Obstaculo(imagen_rocas, [600, 600])
imagen_protagonista = simplegui.load_image(sprites_protagonista[0])
protagonista = Protagonista(imagen_protagonista, [100, 590], 4, 100, [1,0])
fogata = Accesorio(image_fogata, [900, 580],8,100)

for i in range(2):
    image_accesorio = simplegui.load_image(random.choice(sprites_monedas))
    accesorio = Accesorio(image_accesorio, [random.randrange(0, LIENZO[0]), 480],12,70)
    accesorios.append(accesorio)
    timer_accesorio = simplegui.create_timer(accesorio.refresco, accesorio.anima_sprite)
    timer_accesorio.start()

image_antagonista = simplegui.load_image(sprites_antagonista[0])
antagonista = Antagonista(image_antagonista, [170, 530], 6, 100)
timer_protagonista = simplegui.create_timer(protagonista.refresco, protagonista.anima_sprite)
timer_antagonista = simplegui.create_timer(antagonista.refresco, antagonista.anima_sprite)
timer_fogata = simplegui.create_timer(fogata.refresco, fogata.anima_sprite)

# INICIO
frame.start()
timer_protagonista.start()
timer_antagonista.start()
timer_fogata.start()
