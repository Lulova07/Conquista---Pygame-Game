import pygame
import os
import math
import random
import time
import constantes as c
import balas as b
import ventana as v

# ENEMIGO 1 - Torret

def GenerarEnemigo1():
    enemy1_img = pygame.image.load(os.path.join('iconos','enemy1.png'))
    enemigo1 = pygame.transform.scale(enemy1_img, (c.ANCHO_ENEMIGO1,c.ALTO_ENEMIGO1))
    enemy1_x = random.randint(0, c.ANCHO_VENTANA - c.ANCHO_ENEMIGO1)
    enemy1_y = random.randint(0, c.ALTO_VENTANA - c.ALTO_ENEMIGO1)
    enemigo1_rect = pygame.Rect(enemy1_x, enemy1_y, c.ANCHO_ENEMIGO1, c.ALTO_ENEMIGO1)
    salud_enemigo1 = c.PUNTOS_SALUD_ENEMIGO1
    return enemigo1, enemigo1_rect, salud_enemigo1

# ENEMIGO 2 - Creeper
enemy2_img = pygame.image.load(os.path.join('iconos','enemy2.png'))
enemigo2 = pygame.transform.scale(enemy2_img, (c.ANCHO_ENEMIGO2,c.ALTO_ENEMIGO2))

def GenerarEnemigo2():
    enemy2_img = pygame.image.load(os.path.join('iconos','enemy2.png'))
    enemigo2 = pygame.transform.scale(enemy2_img, (c.ANCHO_ENEMIGO2,c.ALTO_ENEMIGO2))
    enemy2_x = random.randint(0, c.ANCHO_VENTANA - c.ANCHO_ENEMIGO2)
    enemy2_y = random.randint(0, c.ALTO_VENTANA - c.ALTO_ENEMIGO2)
    enemigo2_rect = pygame.Rect(enemy2_x, enemy2_y, c.ANCHO_ENEMIGO2, c.ALTO_ENEMIGO2)
    return enemigo2, enemigo2_rect

def MoverEnemigo2(enemigo2_rect, jugador_rect):

    dx = jugador_rect.centerx - enemigo2_rect.centerx
    dy = jugador_rect.centery - enemigo2_rect.centery

    distancia = math.hypot(dx, dy)

    if distancia != 0:
        dx /= distancia
        dy /= distancia

    enemigo2_rect.x += int(c.VELOCIDAD_ENEMIGO2 * dx)
    enemigo2_rect.y += int(c.VELOCIDAD_ENEMIGO2 * dy)


## ENEMIGO 3 - Black Hole

enemy3_img = pygame.image.load(os.path.join('iconos','enemy3.png'))
enemigo3 = pygame.transform.scale(enemy3_img, (c.ANCHO_ENEMIGO3,c.ALTO_ENEMIGO3))

def AumentarTamañoEnemigo3(enemigo3_size):
    return enemigo3_size + 1
    
    

