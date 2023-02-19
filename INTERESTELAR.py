import pygame
import random
from distutils.core import setup
import py2exe, sys, os




# Directorio del juego
carpeta_juego = os.path.dirname(__file__)

#directorio de imagenes
carpeta_imagenes = os.path.join(carpeta_juego, "imagenes")

#sub directorio ded imagenes
carpeta_imagenes_fondos = os.path.join(carpeta_imagenes, "fondos")
carpeta_imagenes_jugador = os.path.join(carpeta_imagenes, "jugador")
carpeta_imagenes_enemigos = os.path.join(carpeta_imagenes, "enemigos")
carpeta_imagenes_explosiones = os.path.join(carpeta_imagenes, "explosiones")
#directorios de sonido
carpeta_sonidos = os.path.join(carpeta_juego, "sonidos")

#subdirectorios de sonido
carpeta_sonidos_ambiente = os.path.join(carpeta_sonidos, "ambiente")
carpeta_sonidos_armas = os.path.join(carpeta_sonidos, "armas")
carpeta_sonidos_explosiones = os.path.join(carpeta_sonidos, "explosiones")



#Pantalla - ventana
ANCHO = 1920
ALTO = 1080

#FPS
FPS = 60

# paleta de colores
BLANCO = (255, 255, 255)  # COLOR Y SU CODIGO EN RGB
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
# colores especificando el numero exadecimal
HC74225 = (199, 66, 37)
H61CD35 = (97, 205, 53)

# fuentes
consolas = pygame.font.match_font("consolas")
times = pygame.font.match_font("times")
arial = pygame.font.match_font("arial")
courier = pygame.font.match_font("courier")

#sonidos
pygame.mixer.init()
pygame.mixer.Sound(os.path.join(carpeta_sonidos_armas, "SpaceLaserShot PE1095407.mp3"))
laser = pygame.mixer.Sound(os.path.join(carpeta_sonidos_armas, "SpaceLaserShot PE1095407.mp3"))

explosion1 = pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, "explo_1.wav"))

explosion2 = pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explo_2.wav'))

explosion3 = pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explo_3.wav'))

explosion4 = pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explo_4.wav'))

ambiente = pygame.mixer.Sound(os.path.join(carpeta_sonidos_ambiente, "musicajuego.mp3"))
ambiente.play(-1)
game_over_sonido = pygame.mixer.Sound(os.path.join(carpeta_sonidos_ambiente, "ultra_instinto.mp3"))

# stats del muñeco
class Jugador(pygame.sprite.Sprite):
    # sprite del jugador
    def __init__(self):
        # heredamos el init de la clase sprite de pygame
        super().__init__()
        # (jugador)
        self.image = pygame.image.load(os.path.join(carpeta_imagenes_jugador, "navepepino.png")).convert()  # convertimos para que la imagen vaya mas fluida
        self.image.set_colorkey(NEGRO)  # para quitar el fondo de las imagenes
        # obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.radius = 27

        # centra el rectangulo(sprite)
        self.rect.center = (800, 1000)  # cambiamos la posicion del jugador al inicio del juego aqui
        # velocidad del personaje inicial
        self.velocidad_x = 0
        self.velocidad_y = 0
        #disparos tiempos entre disparos(cadencia)
        self.cadencia = 250
        self.ultimo_disparo = pygame.time.get_ticks()
        self.hp = 100
        self.vidas = 3

    #actualizacion cada vuelta del bucle
    def update(self):

        # velocidad predeterminada cada vuelta del bucle
        self.velocidad_x = 0
        self.velocidad_y = 0

        # MANTIENE LAS TECLAS PULSADAS
        teclas = pygame.key.get_pressed()

        # mueve la bola hacia la izk
        if teclas[pygame.K_a]:
            self.velocidad_x = -10
        # mueve la bola hacia la der
        if teclas[pygame.K_d]:
            self.velocidad_x = 10
        # mueve la bola hacia arriba
        if teclas[pygame.K_w]:
            self.velocidad_y = -10
        # mueve la bola hacia abajo
        if teclas[pygame.K_s]:
            self.velocidad_y = 10
        # disparo
        if teclas[pygame.K_SPACE]:
            ahora = pygame.time.get_ticks()
            if ahora - self.ultimo_disparo > self.cadencia:
                self.disparo()
                self.disparo2()
                self.disparo3()
                self.ultimo_disparo = ahora

        # actualiza la posicion del personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # limita margen izq
        if self.rect.left < 0:
            self.rect.left = 0
        # limita margen der
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        # limita margen inferior
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
        # limita margen superior
        if self.rect.top < 0:
            self.rect.top = 0


    def disparo(self):
        bala = Disparos(self.rect.centerx, self.rect.top)
        balas.add(bala)
        laser.play()
    def disparo2(self):
        bala = Disparos(self.rect.centerx + 23, self.rect.top)
        balas.add(bala)
    def disparo3(self):
        bala = Disparos(self.rect.centerx + -23, self.rect.top)
        balas.add(bala)


# stats del enemigos
class EnemigosVerdes(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, "enemigoVerde.png")).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)  # para quitar el fondo de las imagenes
        self.radius = 27

        self.rect.x = random.randrange(
            ANCHO - self.rect.width)  # con esto aparece en el ancho de la pantalla aleatoriamente
        self.rect.y = random.randrange(ALTO - self.rect.height)  # marcamos al final los limetes en el ultimo self
        self.velocidad_x = random.randrange(2, 5)  # rango de velocidad
        self.velocidad_y = random.randrange(2, 5)
        self.hp = 15

    def update(self):
        # actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        # limita margen izq
        if self.rect.left < 0:
            self.velocidad_x += 1
        # limita margen der
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # limita margen inferior
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
        # limita margen superior
        if self.rect.top < 0:
            self.velocidad_y += 1


class EnemigosRojos(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, "enemigoRojo.png")).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)  # para quitar el fondo de las imagenes
        self.radius = 27

        self.rect.x = random.randrange(
            ANCHO - self.rect.width)  # con esto aparece en el ancho de la pantalla aleatoriamente
        self.rect.y = random.randrange(ALTO - self.rect.height)  # marcamos al final los limetes en el ultimo self
        self.velocidad_x = random.randrange(1, 3)  # rango de velocidad
        self.velocidad_y = random.randrange(1, 3)
        self.hp = 30

    def update(self):
        # actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        # limita margen izq
        if self.rect.left < 0:
            self.velocidad_x += 1
        # limita margen der
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # limita margen inferior
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
        # limita margen superior
        if self.rect.top < 0:
            self.velocidad_y += 1


class EnemigosAzules(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, "enemigoAzul.png")).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)  # para quitar el fondo de las imagenes
        self.radius = 27

        self.rect.x = random.randrange(
            ANCHO - self.rect.width)  # con esto aparece en el ancho de la pantalla aleatoriamente
        self.rect.y = random.randrange(ALTO - self.rect.height)  # marcamos al final los limetes en el ultimo self
        self.velocidad_x = random.randrange(3, 7)  # rango de velocidad
        self.velocidad_y = random.randrange(3, 7)
        self.hp = 40
    def update(self):
        # actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        # limita margen izq
        if self.rect.left < 0:
            self.velocidad_x += 1
        # limita margen der
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # limita margen inferior
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
        # limita margen superior
        if self.rect.top < 0:
            self.velocidad_y += 1


class EnemigosAmarillos(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, "enemigoAmarillo.png")).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(NEGRO)  # para quitar el fondo de las imagenes
        self.radius = 27

        self.rect.x = random.randrange(
            ANCHO - self.rect.width)  # con esto aparece en el ancho de la pantalla aleatoriamente
        self.rect.y = random.randrange(ALTO - self.rect.height)  # marcamos al final los limetes en el ultimo self
        self.velocidad_x = random.randrange(4, 10)  # rango de velocidad
        self.velocidad_y = random.randrange(4, 10)
        self.hp = 50

    def update(self):
        # actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        # limita margen izq
        if self.rect.left < 0:
            self.velocidad_x += 1
        # limita margen der
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # limita margen inferior
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
        # limita margen superior
        if self.rect.top < 0:
            self.velocidad_y += 1


class Disparos(pygame.sprite.Sprite):

    def __init__(self, x, y):  # esto es para decirle en sitio exacto desde donde disparar
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes_jugador, "disparo.png")).convert(), (10, 20))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y -= 25
        if self.rect.bottom < 0:
            self.kill()


class Meteoritos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_aleatoria = random.randrange(3)
        if self.img_aleatoria == 0:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes_jugador, "meteorito.png")).convert(), (100, 100))
            self.radius = 50
        if self.img_aleatoria == 1:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes_jugador, "meteorito.png")).convert(), (75, 75))
            self.radius = 25
        if self.img_aleatoria == 2:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes_jugador, "meteorito.png")).convert(), (50, 50))
            self.radius = 15
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange((ANCHO - self.rect.width))
        self.rect.y = -self.rect.width
        self.velocidad_y = random.randrange(1, 10)

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > ALTO:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = -self.rect.width
            self.velocidad_y = random.randrange(1, 10)

class Explosiones(pygame.sprite.Sprite):
    def __init__(self, centro, dimensiones):
        pygame.sprite.Sprite.__init__(self)
        self.dimensiones = dimensiones
        self.image = animacion_explosion1[self.dimensiones][0]
        self.rect = self.image.get_rect()
        self.rect.center = centro
        self.fotograma = 0
        self.frecuencia_fotograma = 35
        self.actualizacion = pygame.time.get_ticks()

    def update(self):
        ahora = pygame.time.get_ticks()
        if ahora - self.actualizacion > self.frecuencia_fotograma:
            self.actualizacion = ahora
            self.fotograma += 1
            if self.fotograma == len(animacion_explosion1[self.dimensiones]):
                self.kill()
            else:
                centro = self.rect.center
                self.image = animacion_explosion1[self.dimensiones][self.fotograma]
                self.rect = self.image.get_rect()
                self.rect.center = centro




#Iniciación de Pygame,creacion de la ventana, titulo y control de reloj
pygame.init()
# ventana-pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)


#sistema de puntuaciones
puntuacion = 0

#explosiones
animacion_explosion1 = {"t1": [], "t2": [], "t3": [], "t4": []}
for x in range(5):
    archivo_explosiones = f"expl_01_00{x:02d}.png"
    imagenes = pygame.image.load(os.path.join(carpeta_imagenes_explosiones, archivo_explosiones)).convert()
    imagenes.set_colorkey(NEGRO)
    imagenes_t1 = pygame.transform.scale(imagenes, (32, 32))
    animacion_explosion1["t1"].append(imagenes_t1)
    imagenes_t2 = pygame.transform.scale(imagenes, (64, 64))
    animacion_explosion1["t2"].append(imagenes_t2)
    imagenes_t3 = pygame.transform.scale(imagenes, (128, 128))
    animacion_explosion1["t3"].append(imagenes_t3)
    imagenes_t4 = pygame.transform.scale(imagenes, (256, 256))
    animacion_explosion1["t4"].append(imagenes_t4)

def barra_hp(pantalla, x, y, hp):
    largo = 200
    ancho = 25
    calculo_barra = int((jugador.hp / 100) * largo)
    borde = pygame.Rect(x, y, largo, ancho)
    rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
    pygame.draw.rect(pantalla, VERDE, borde, 3)
    pygame.draw.rect(pantalla, BLANCO, rectangulo)


def muestra_texto(pantalla, fuente, texto, color, dimensiones, x, y):
    tipo_letra = pygame.font.Font(fuente, dimensiones)
    superficie = tipo_letra.render(texto, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = x, y
    pantalla.blit(superficie, rectangulo)

# fondo de pantalla
fondo = pygame.transform.scale(pygame.image.load("fondos/fondo3.jpg").convert(),
                               (1920, 1080))
pygame.display.set_caption("INTERESTELAR")
icono = pygame.image.load("imagenes/enemigos/icononaves.png")
pygame.display.set_icon(icono)
clock = pygame.time.Clock()

# grupo de sprites, instanciacion del objeto jugador y enemigos
sprites = pygame.sprite.Group()
explosiones = pygame.sprite.Group()
#sprites enemigos
enemigos_amarillos = pygame.sprite.Group()
enemigos_verdes = pygame.sprite.Group()
enemigos_rojos = pygame.sprite.Group()
enemigos_azules = pygame.sprite.Group()

#otros sprites
balas = pygame.sprite.Group()
meteoritos = pygame.sprite.Group()



#instanciacion de enemigos
enemigo1 = EnemigosAmarillos()
enemigos_amarillos.add(enemigo1)
enemigo2 = EnemigosVerdes()
enemigos_verdes.add(enemigo2)
enemigo3 = EnemigosAzules()
enemigos_azules.add(enemigo3)
enemigo4 = EnemigosRojos()
enemigos_rojos.add(enemigo4)



# instanciacion jugador
jugador = Jugador()  # dependiendo del orden de estas capas se superpondra una imagen
sprites.add(jugador)



ejecutando = True
#Bucle de juego.
while ejecutando:
    #esto es lo que especifica la velocidad del bucle del juego
    clock.tick(FPS)
    pantalla.blit(fondo, (0, 0))
    for event in pygame.event.get():
        #se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ejecutando = False
    # actualizacion de sprites
    sprites.update()
    enemigos_rojos.update()
    enemigos_verdes.update()
    enemigos_azules.update()
    enemigos_amarillos.update()
    balas.update()
    meteoritos.update()
    explosiones.update()

    r = random.randrange(1, 4)

    #instanciacion de meteoritos
    if not meteoritos:
        for x in range(5):
            meteorito = Meteoritos()
            meteoritos.add(meteorito)

    colision_disparos_meteoritos = pygame.sprite.groupcollide(meteoritos, balas, True, True,
                                                              pygame.sprite.collide_circle)
    if colision_disparos_meteoritos:
        puntuacion += 25




    # spritecollode es una opcion para las colisiones de pygame jugador sera el que provoque la colision y  los enemigos son los colisionados y le ponemos false para que no elimine al enemigo



    colision_disparos_amarillos = pygame.sprite.groupcollide(enemigos_amarillos, balas, False, True,
                                                             pygame.sprite.collide_circle)
    if colision_disparos_amarillos:
        puntuacion += 10
        explosion1.play()
        explosion = Explosiones(enemigo1.rect.center, f"t{r}")
        explosiones.add(explosion)
        enemigo1.hp -= 5
    if enemigo1.hp <= 0:
        enemigo1.kill()

    colision_disparos_verdes = pygame.sprite.groupcollide(enemigos_verdes, balas, False, True,
                                                          pygame.sprite.collide_circle)
    if colision_disparos_verdes:
        puntuacion += 25
        explosion2.play()
        explosion = Explosiones(enemigo2.rect.center, f"t{r}")
        explosiones.add(explosion)
        enemigo2.hp -= 5
    if enemigo2.hp <= 0:
        enemigo2.kill()

    colision_disparos_azules = pygame.sprite.groupcollide(enemigos_azules, balas, False, True,
                                                          pygame.sprite.collide_circle)

    if colision_disparos_azules:
        puntuacion += 50
        explosion3.play()
        explosion = Explosiones(enemigo3.rect.center, f"t{r}")
        explosiones.add(explosion)
        enemigo3.hp -= 5
        if enemigo3.hp <= 0:
            enemigo3.kill()

    colision_disparos_rojos = pygame.sprite.groupcollide(enemigos_rojos, balas, False, True,
                                                         pygame.sprite.collide_circle)
    if colision_disparos_rojos:
        puntuacion += 100
        explosion4.play()
        explosion = Explosiones(enemigo4.rect.center, f"t{r}")
        explosiones.add(explosion)
        enemigo4.hp -= 5
        if enemigo4.hp <= 0:
            enemigo4.kill()

    if jugador.hp <= 0:
        ejecutando = True


    #vidas del jugador
    warning = pygame.image.load(os.path.join(carpeta_imagenes_jugador, "warning.png")).convert()
    muerte_3 = pantalla.blit(pygame.transform.scale(jugador.image, (25, 25)), (220, 10))
    muerte_2 = pantalla.blit(pygame.transform.scale(jugador.image, (25, 25)), (260, 10))
    muerte_1 = pantalla.blit(pygame.transform.scale(jugador.image, (25, 25)), (300, 10))
    cruz = pygame.image.load(os.path.join(carpeta_imagenes_jugador, "cruz.png")).convert()
    game_over = pygame.image.load(os.path.join(carpeta_imagenes_jugador, "gameover.png"))
    if jugador.vidas == 0 and jugador.hp == 0:
        pantalla.blit(pygame.transform.scale(game_over, (800, 300)), (100, 100))
        ambiente.stop()
        game_over_sonido.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ejecutando = False

    if jugador.hp < 30:
        pantalla.blit(pygame.transform.scale(warning, (25, 25)), (400, 15))

    if jugador.hp <= 0 and jugador.vidas == 3:
        jugador.kill()
        jugador = Jugador()
        sprites.add(jugador)
        jugador.vidas = 2

    if jugador.vidas == 2:
        if jugador.hp <= 0:
            jugador.kill()
            jugador = Jugador()
            sprites.add(jugador)
            jugador.vidas = 1
        muerte_1 = pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (220, 10))

    if jugador.vidas == 1:
        if jugador.hp <= 0:
            jugador.kill()
            jugador = Jugador()
            sprites.add(jugador)
            jugador.vidas = 0
        muerte_1 = pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (220, 10))
        muerte_2 = pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (260, 10))

    if jugador.vidas == 0:
        if jugador.hp <= 0:
            jugador.kill()
            jugador.hp = 0
        muerte_1 = pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (220, 10))
        muerte_2 = pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (260, 10))
        muerte_3 = pantalla.blit(pygame.transform.scale(cruz, (25, 25)), (300, 10))


    #colisiones entre nave y naves enemigas
    colision_nave1 = pygame.sprite.spritecollide(jugador, enemigos_amarillos, True, pygame.sprite.collide_circle)
    colision_nave2 = pygame.sprite.spritecollide(jugador, enemigos_verdes, True, pygame.sprite.collide_circle)
    colision_nave3 = pygame.sprite.spritecollide(jugador, enemigos_azules, True, pygame.sprite.collide_circle)
    colision_nave4 = pygame.sprite.spritecollide(jugador, enemigos_rojos, True, pygame.sprite.collide_circle)

    if colision_nave1:
        explosion1.play()
        explosion = Explosiones(enemigo1.rect.center, f"t{r}")
        explosiones.add(explosion)
        jugador.hp -= 50
        if enemigo1.hp <= 0:
            enemigo1.kill()
        if puntuacion >= 0:
            puntuacion -= 100
            if puntuacion < 0:
                puntuacion = 0

    if colision_nave2:
        explosion1.play()
        explosion = Explosiones(enemigo2.rect.center, f"t{r}")
        explosiones.add(explosion)
        jugador.hp -= 25
        if enemigo2.hp <= 0:
            enemigo2.kill()
        if puntuacion >= 0:
            puntuacion -= 75
            if puntuacion < 0:
                puntuacion = 0

    if colision_nave3:
        explosion1.play()
        explosion = Explosiones(enemigo3.rect.center, f"t{r}")
        explosiones.add(explosion)
        jugador.hp -= 15
        if enemigo3.hp <= 0:
            enemigo3.kill()
        if puntuacion >= 0:
            puntuacion -= 50
            if puntuacion < 0:
                puntuacion = 0

    if colision_nave4:
        explosion1.play()
        explosion = Explosiones(enemigo4.rect.center, f"t{r}")
        explosiones.add(explosion)
        jugador.hp -= 15
        if enemigo4.hp <= 0:
            enemigo4.kill()
        if puntuacion >= 0:
            puntuacion -= 25
            if puntuacion < 0:
                puntuacion = 0

    colision_nave_meteoritos = pygame.sprite.spritecollide(jugador, meteoritos, pygame.sprite.collide_circle)

    if colision_nave_meteoritos:
        explosion1.play()
        explosion = Explosiones(jugador.rect.center, f"t{r}")
        explosiones.add(explosion)
        jugador.hp -= 15
        if puntuacion >= 0:
            puntuacion -= 10
            if puntuacion < 0:
                puntuacion = 0



    if not enemigos_amarillos and not enemigos_azules and not enemigos_rojos and not enemigos_verdes:
    #for x in range(2):
        enemigo1 = EnemigosAmarillos()
        enemigos_amarillos.add(enemigo1)
    #for x in range(4):
        enemigo2 = EnemigosVerdes()
        enemigos_verdes.add(enemigo2)
    #for x in range(5):
        enemigo3 = EnemigosAzules()
        enemigos_azules.add(enemigo3)
    #for x in range(5):
        enemigo4 = EnemigosRojos()
        enemigos_rojos.add(enemigo4)



    #fondo de pantalla, dibujo de sprites y formas geometricas
    sprites.draw(pantalla)
    enemigos_rojos.draw(pantalla)
    enemigos_verdes.draw(pantalla)
    enemigos_azules.draw(pantalla)
    enemigos_amarillos.draw(pantalla)
    balas.draw(pantalla)
    meteoritos.draw(pantalla)
    explosiones.draw(pantalla)

    # dibuja los textos en pantalla
    muestra_texto(pantalla, consolas, str(puntuacion).zfill(7), BLANCO, 40, 80, 60)
    barra_hp(pantalla, 0, 10, jugador.hp)
    #actualizacion del contenido de la pantalla
    pygame.display.flip()


pygame.quit()