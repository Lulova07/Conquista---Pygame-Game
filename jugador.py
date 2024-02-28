import pygame
import math
import os
import constantes as c
import balas as b

def GenerarJugador():
    jugador_img = pygame.image.load(os.path.join('iconos','jugador.png'))
    jugador = pygame.transform.scale(jugador_img, (c.ANCHO_JUGADOR,c.ALTO_JUGADOR))
    jugador_rect = pygame.Rect(450, 250, c.ANCHO_JUGADOR, c.ALTO_JUGADOR)
    vidas_jugador = c.VIDAS_JUGADOR
    salud_jugador = c.PUNTOS_SALUD_JUGADOR
    puntos_jugador = 0
    return jugador, jugador_rect, vidas_jugador, salud_jugador, puntos_jugador

def ControlarJugador(teclas_presionadas,jugador_rect):
    if teclas_presionadas[pygame.K_a] and jugador_rect.x - c.VELOCIDAD_JUGADOR > 0: # Izquierda
        jugador_rect.x -= c.VELOCIDAD_JUGADOR
    if teclas_presionadas[pygame.K_d] and jugador_rect.x + c.VELOCIDAD_JUGADOR + c.ANCHO_JUGADOR < c.ANCHO_VENTANA: # Derecha
        jugador_rect.x += c.VELOCIDAD_JUGADOR
    if teclas_presionadas[pygame.K_w] and jugador_rect.y - c.VELOCIDAD_JUGADOR > 0: # Arriba
        jugador_rect.y -= c.VELOCIDAD_JUGADOR
    if teclas_presionadas[pygame.K_s] and jugador_rect.y + c.VELOCIDAD_JUGADOR + c.ALTO_JUGADOR < c.ALTO_VENTANA: # Abajo
        jugador_rect.y += c.VELOCIDAD_JUGADOR
    if teclas_presionadas[pygame.K_SPACE]:
        angulo_disparo = CalcularAngulo(jugador_rect, pygame.mouse.get_pos())
        b.DispararJugador(jugador_rect, angulo_disparo)
        
def CalcularAngulo(jugador_rect, mouse_posicion):
    mx, my = mouse_posicion
    dy, dx = mx - jugador_rect.centerx, jugador_rect.centery - my
    angulo = math.degrees(math.atan2(-dy, dx)) + 0
    return angulo

def RotarJugador(jugador_img, angulo, jugador_rect):
    rot_image = pygame.transform.rotate(jugador_img,angulo)
    rot_image_rect = rot_image.get_rect(center = jugador_rect.center)
    return rot_image, rot_image_rect
