
import pygame
import os
import constantes as c
import random

def GenerarCorazon():
    heart_img = pygame.image.load(os.path.join('iconos','heart.png'))
    heart = pygame.transform.scale(heart_img, (c.ANCHO_BONUS1,c.ALTO_BONUS1))
    heart_rect = pygame.Rect(random.randint(c.ANCHO_BONUS1,c.ANCHO_VENTANA - c.ANCHO_BONUS1), random.randint(c.ALTO_BONUS1,c.ALTO_VENTANA - c.ALTO_BONUS1), c.ANCHO_ENEMIGO3, c.ALTO_ENEMIGO3)
    return heart, heart_rect

