import sys
import pygame
import time

ANCHO = 640
ALTO = 480

color_fondo = (0, 0, 64)

#inicializar pygame por mixer
pygame.init()

#clases 

class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargar la imagen
        self.image = pygame.image.load("MODULO02/GAME/imagenes/bolita.png")
        
        #obtener el rectangulo de la imagen
        self.rect = self.image.get_rect()
        
        #posicion inicial al medio de la pantalla
        self.rect.centerx = ANCHO // 2
        self.rect.centery = ALTO // 2
        
        #velocidad
        self.speed = [2, 3]
        
    def update(self):
        #evitamos que la bolita se vaya por fuera de la pantalla
        #if self.rect.bottom >= ALTO or self.rect.top <= 0:
        if  self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ANCHO  or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]

        #actualizamos la posicion de la bolita
        self.rect.move_ip(self.speed)

class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("MODULO02/GAME/imagenes/paleta.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (ANCHO /2 , ALTO - 20 )
        self.speed = [0, 0]
        
    def update(self, evento):
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5, 0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5, 0]
        else:
            self.speed = [0, 0]
        
        #mover en base a la posicion actual
        self.rect.move_ip(self.speed)

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("MODULO02/GAME/imagenes/ladrillo.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        
class Muro(pygame.sprite.Group):
    def __init__(self,cantidad):
        pygame.sprite.Group.__init__(self)
        pos_x = 0
        pos_y = 20
        for i in range(cantidad):
            ladrillo = Ladrillo((pos_x, pos_y))
            self.add(ladrillo)
            
            pos_x += ladrillo.rect.width
            if pos_x >= ANCHO:
                pos_x = 0
                pos_y += ladrillo.rect.height
                
class MensajesJuego:
    def __init__(self):
        self.fuente = pygame.font.SysFont("Arial", 40) 
    
    def game_over(self):
        texto = self.fuente.render("Game Over", True, (255, 255, 255))
        texto_rect = texto.get_rect()
        texto_rect.center = (ANCHO // 2, ALTO // 2)
        pantalla.blit(texto, texto_rect)
        pygame.display.flip()
        pygame.mixer.Sound.play(sonido_game_over)
        time.sleep(5)
        sys.exit() 
        
    def mostrar_puntos(self, puntos):
        fuente_puntos = pygame.font.SysFont("Arial", 20)
        texto = fuente_puntos.render(str(puntos).zfill(5), True, (200, 200, 200))
        texto_rect = texto.get_rect()
        texto_rect.topleft = [0, 0]  
        pantalla.blit(texto, texto_rect)
                
#creamos un reloj 
reloj = pygame.time.Clock()


#se define la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
#se define el titulo de la pantalla
pygame.display.set_caption("Mi primer juego")

#ajustamos la repeticion de las teclas
pygame.key.set_repeat(30)


#definimos objetos por clase
bolita = Bolita() 
jugador = Paleta() 
muro = Muro(48)
mensajes = MensajesJuego()
puntos = 0

#cargar sonidos
sonido_colision_paleta = pygame.mixer.Sound("MODULO02/GAME/sonidos/colision.ogg")
sonido_colision_muro = pygame.mixer.Sound("MODULO02/GAME/sonidos/colision_muro.ogg")
sonido_game_over = pygame.mixer.Sound("MODULO02/GAME/sonidos/game_over.ogg")

while True:
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)
    
    #actualizar la pantalla con posicion de la bolita
    bolita.update()
    
    ##### COLISIONES #####
    
    #colision entre la bolita y el jugador
    if pygame.sprite.collide_rect(bolita, jugador):
        bolita.speed[1] = -bolita.speed[1] 
        pygame.mixer.Sound.play(sonido_colision_paleta)
     
    #colision entre la bolita y ladrillos
    
    # lista = pygame.sprite.spritecollide(bolita, muro, True)
    # if lista:
    #     pygame.mixer.Sound.play(sonido_colision_muro)
    #     puntos += 10
    
    #creamos una colision de un solo ladrilllo 
    lista = pygame.sprite.spritecollide(bolita, muro, False)
    if lista:
        ladrillo = lista[0]
        cx = bolita.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            bolita.speed[0] = -bolita.speed[0]
        else:
            bolita.speed[1] = -bolita.speed[1]
        muro.remove(ladrillo)
        pygame.mixer.Sound.play(sonido_colision_muro)
        puntos += 10
        
    ##### EVALUAMOS ACCIONES  #####
    
    if bolita.rect.top >= ALTO:
        mensajes.game_over()
    
    
    ### DIBUJAMOS OBJETOVS EN LA PANTALLA####
    
    #pintamos el fondo de la pantalla
    pantalla.fill(color_fondo)
    
    #mostramos puntos
    mensajes.mostrar_puntos(puntos)

    #agregar bolita a pantalla
    pantalla.blit(bolita.image, bolita.rect)
    
    #DIBUJAMOS EL JUGADOR EN LA PANTLLA
    pantalla.blit(jugador.image, jugador.rect)
    
    #DIBUJAMOS EL MURO EN LA PANTALLA
    muro.draw(pantalla)
    
    pygame.display.flip()
    
    