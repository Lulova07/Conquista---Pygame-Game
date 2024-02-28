import pygame
import os
import math
import constantes as c
import ventana as v
import jugador as j

# JUGADOR

balas_jugador = []
bala_img = pygame.image.load(os.path.join('iconos', 'bala.png'))
bala_img = pygame.transform.scale(bala_img, (c.ANCHO_BALA_JUGADOR,c.ALTO_BALA_JUGADOR))
bala_img = pygame.transform.rotate(bala_img, 45)

def DispararJugador(jugador_rect, angulo_disparo):
    bala = {
        'img': pygame.transform.rotate(bala_img, angulo_disparo),
        'rect': bala_img.get_rect(center=jugador_rect.center),
        'angulo': math.radians(angulo_disparo + 90)
    }
    
    balas_jugador.append(bala)

def ActualizarBalasJugador(enemigo1_rect,enemigo2_rect,salud_enemigo1):
    enemigo1_hits = 0
    for bala in balas_jugador:
        bala['rect'].x += c.BALA_VELOCIDAD_JUGADOR * math.cos(bala['angulo'])
        bala['rect'].y -= c.BALA_VELOCIDAD_JUGADOR * math.sin(bala['angulo'])
        
        if bala['rect'].colliderect(enemigo1_rect):
            enemigo1_hits += 0.1
            
    balas_jugador[:] = [bala for bala in balas_jugador if pygame.Rect(0, 0, c.ANCHO_VENTANA, c.ALTO_VENTANA).colliderect(bala['rect'])]
    
    return enemigo1_hits

def DibujarBalasJugador():
    for bala in balas_jugador:
        v.VENTANA.blit(bala['img'], bala['rect'].topleft)

# ENEMIGO 1
balas_enemigo1 = []
bala_enemigo1_img = pygame.image.load(os.path.join('iconos', 'bala_enemy1.png'))
bala_enemigo1_img = pygame.transform.scale(bala_enemigo1_img, (c.ANCHO_BALA_ENEMIGO1, c.ALTO_BALA_ENEMIGO1))
bala_enemigo1_img = pygame.transform.rotate(bala_enemigo1_img, 225)

def CalcularAnguloEnemigo1(enemigo1_rect, jugador_rect):
    ex, ey = enemigo1_rect.center
    jx, jy = jugador_rect.center
    dy, dx = jx - ex, ey - jy
    angulo = math.degrees(math.atan2(-dy, dx)) + 0
    return angulo

def DispararEnemigo(enemigo1_rect, angulo_disparo):
    bala = {
        'img': pygame.transform.rotate(bala_enemigo1_img, angulo_disparo),
        'rect': bala_enemigo1_img.get_rect(center=enemigo1_rect.center),
        'angulo': math.radians(angulo_disparo + 90)
    }
    
    balas_enemigo1.append(bala)

def DispararEnemigo1(enemigo1_rect, jugador_rect):
    angulo_disparo = CalcularAnguloEnemigo1(enemigo1_rect, jugador_rect)
    DispararEnemigo(enemigo1_rect, angulo_disparo)

def ActualizarBalasEnemigo1(jugador_rect,enemigo2_rect,salud_jugador):
    jugador_hits = 0
    for bala in balas_enemigo1:
        bala['rect'].x += c.BALA_VELOCIDAD_ENEMIGO1 * math.cos(bala['angulo'])
        bala['rect'].y -= c.BALA_VELOCIDAD_ENEMIGO1 * math.sin(bala['angulo'])
        
        if bala['rect'].colliderect(jugador_rect):
            jugador_hits += 1
    
    balas_enemigo1[:] = [bala for bala in balas_enemigo1 if pygame.Rect(0, 0, c.ANCHO_VENTANA, c.ALTO_VENTANA).colliderect(bala['rect'])]
    
    return jugador_hits

def DibujarBalasEnemigo1():
    for bala in balas_enemigo1:
        v.VENTANA.blit(bala['img'], bala['rect'].topleft)

    balas_jugador[:] = [bala for bala in balas_jugador if pygame.Rect(0, 0, c.ANCHO_VENTANA, c.ALTO_VENTANA).colliderect(bala['rect'])]



