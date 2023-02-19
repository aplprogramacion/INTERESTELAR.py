
import pygame, sys
import random
from pygame.locals import *
import os




pygame.init()
# screen
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
FPS = 60
RELOJ = pygame.time.Clock()
vec = pygame.math.Vector2

# icon and title
pygame.display.set_caption("Interestelar")
icon = pygame.image.load("imagenes/enemigos/enemigoAmarillo.png")
pygame.display.set_icon(icon)

# sound
pygame.mixer.init()
pygame.mixer.music.load("soundMenu/⚔️Música épica legendaria #20 SIN COPYRIGHT .mp3")
pygame.mixer.music.play(-1)



# colors
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# images buttons
back_img = pygame.image.load("fondos/buttonback.png").convert_alpha()

# textos
titlefont = pygame.font.SysFont("Verdana", 30, True, True)
headingfont = pygame.font.SysFont("Verdana", 20, True, True)
#textos control volumen
textOpc1 = titlefont.render("Controles de volumen", True, BLANCO)
textOpc2 = headingfont.render(" Bajar volumen (9)", True, BLANCO)
textOpc3 = headingfont.render(" Subir volumen (0) ", True, BLANCO)
textOpc4 = headingfont.render(" Mute (m) ", True, BLANCO)
textOpc5 = headingfont.render(" Activar sonido (,)", True, BLANCO)
#textos controles movimiento
textOpc6 = titlefont.render("Controles de movimiento", True, BLANCO)
textOpc7 = headingfont.render(" Abajo (s)", True, BLANCO)
textOpc8 = headingfont.render(" Arriba  (w) ", True, BLANCO)
textOpc9 = headingfont.render(" Izquierda (a) ", True, BLANCO)
textOpc10 = headingfont.render(" Derecha (d)", True, BLANCO)
textOpc11 = headingfont.render(" Disparo (espacio)", True, BLANCO)

# backgound
letras = pygame.image.load("fondos/titleinterestelar.png").convert_alpha()

def ControlVolumen():
    keys = pygame.key.get_pressed()
    # baja volumen
    if keys[K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
    # sube volumen
    if keys[K_0] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
    # mute sound
    if keys[K_m]:
        pygame.mixer.music.set_volume(0.0)
    # reactivar sonido
    if keys[K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
class FondoPantalla(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.fondo = pygame.image.load("fondos/fondomenu.jpg").convert_alpha()
        self.letras = pygame.image.load("fondos/titleinterestelar.png").convert_alpha()
    def render(self):

        self.x_relativa = self.x % self.fondo.get_rect().width
        screen.blit(self.fondo, (self.x_relativa - self.fondo.get_rect().width, 0))
        if self.x_relativa < width:
            screen.blit(self.fondo, (self.x_relativa, 0))
        self.x -= 5
        screen.blit(self.letras, (600, 0))
# image Nave
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.nave = pygame.image.load("imagenes/jugador/navemenu.png").convert_alpha()
        self.rect = self.nave.get_rect()
        self.pos = vec((340, 240))
        self.vel = vec(0, 0)
        self.direction = random.randint(0, 1)  # 0 for Right, 1 for Left
        self.vel.x = 2

        # Establece la posición inicial del enemigo
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 265
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = 265

    def move(self):

        # Hace que el enemigo cambie de dirección al llegar al final de la pantalla
        if self.pos.x >= (width - 200):
            self.direction = 1
        elif self.pos.x <= 0:
            self.direction = 0

        # Actualiza la posición con nuevos valores
        if self.direction == 0:
            self.pos.x += self.vel.x
        if self.direction == 1:
            self.pos.x -= self.vel.x
        self.rect.center = self.pos  # Updates rect

    def render(self):
        # Displayed the enemy on screen
        screen.blit(self.nave, (self.pos.x, self.pos.y))

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (255, 255, 255))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 40
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()

class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load('fondos/cursor.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

class Menu:
    "Representa un menú con opciones para un juego"

    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('dejavu.ttf', 20)
        x = 40
        y = 105
        paridad = 1

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()

        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)

def juego():
    pygame.mixer.quit()
    import INTERESTELAR







def mostrar_opciones():
    run = True
    while run:
        #screen.blit(fondo, (0, 0))
        # pygame.draw.rect(screen, (255, 0, 0), (300, 200, 500, 20))
        # pygame.draw.rect(screen, (0, 128, 0), (300, 200, 500 - (5 * (100 - barraSonido)), 20))
        """creamos una variable barrasonido con valor 100(barraSonido = 100),
        creamos un rectangulo y lo pasamos por la pantalla con el color rojo, posiciones x, y, ancho, alto (pygame.draw.rect(screen, (255, 0, 0), (300, 200, 500, 10)))
        creamos un rectangulo y lo pasamos por la pantalla con el color verde, posiciones x, y, al ancho le restamos 5 * 100 que este le restara a la barrasonido y le pasamos el alto
        pygame.draw.rect(screen, (0, 128, 0), (300, 200, 500 -(5 * (100 - barraSonido)), 10))"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # fondo
        f.render()
        #control volumen
        ControlVolumen()


        #textos volumen
        screen.blit(textOpc1, (60, 220))
        screen.blit(textOpc2, (60, 260))
        screen.blit(textOpc3, (60, 300))
        screen.blit(textOpc4, (60, 340))
        screen.blit(textOpc5, (60, 380))
        # textos movimientos
        screen.blit(textOpc6, (480, 220))
        screen.blit(textOpc7, (480, 260))
        screen.blit(textOpc8, (480, 300))
        screen.blit(textOpc9, (480, 340))
        screen.blit(textOpc10, (480, 380))
        screen.blit(textOpc11, (480, 420))

        if back_button.draw(screen):
            run = False

        RELOJ.tick(FPS)
        pygame.display.update()

def creditos():
    print
    " Función que muestra los creditos del programa."


def salir_del_programa():
    import sys
    print
    " Gracias por utilizar este programa."
    sys.exit(0)

# instances
back_button = Button(350, 500, back_img, 1)
f = FondoPantalla()
nave= Nave()


if __name__ == '__main__':

    salir = False
    opciones = [
        ("Jugar", juego),
        ("Opciones", mostrar_opciones),
        ("Creditos", creditos),
        ("Salir", salir_del_programa)
    ]

    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True


        #control volumen
        ControlVolumen()
        # fondo
        f.render()

        menu.actualizar()
        menu.imprimir(screen)

        nave.move()
        nave.render()



        pygame.display.flip()
        pygame.time.delay(10)