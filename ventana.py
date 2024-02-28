import pygame
import constantes as c

VENTANA = pygame.display.set_mode((c.ANCHO_VENTANA,c.ALTO_VENTANA))
surface = pygame.Surface((c.ANCHO_VENTANA,c.ALTO_VENTANA), pygame.SRCALPHA)

def ElementosPantalla(font,salud_jugador,vidas_jugador,puntos_jugador,salud_enemigo1,enemigo1_rect):
    text_salud_jugador = font.render(f"Salud Restante: {salud_jugador}", True, c.BLANCO)
    text_vidas = font.render(f"Vidas: {vidas_jugador}", True, c.BLANCO)
    text_puntos = font.render(f"Puntos: {puntos_jugador}", True, c.BLANCO)
    text_salud_enemigo1 = font.render(f"{round((salud_enemigo1 / c.PUNTOS_SALUD_ENEMIGO1)*100,0)}", True, c.BLANCO)
    VENTANA.blit(text_salud_jugador, (10, 10))
    VENTANA.blit(text_vidas, (10, 30))   
    VENTANA.blit(text_salud_enemigo1, (enemigo1_rect.x + 50, enemigo1_rect.y - 20))
    VENTANA.blit(text_puntos, (c.ANCHO_VENTANA - 150,10))
    
    
def DrawWindow(jugador,jugador_rect,enemigo1,enemigo1_rect,enemigo2,enemigo2_rect,enemigo3,enemigo3_rect,heart,heart_rect):
    if heart is not None:
        VENTANA.fill(c.AZUL)
        VENTANA.blit(jugador, jugador_rect.topleft)
        VENTANA.blit(enemigo1, enemigo1_rect.topleft)
        VENTANA.blit(enemigo2, enemigo2_rect.topleft)
        VENTANA.blit(enemigo3, enemigo3_rect.topleft)
        VENTANA.blit(heart, heart_rect.topleft)
    else:
        VENTANA.fill(c.AZUL)
        VENTANA.blit(jugador, jugador_rect.topleft)
        VENTANA.blit(enemigo1, enemigo1_rect.topleft)
        VENTANA.blit(enemigo2, enemigo2_rect.topleft)
        VENTANA.blit(enemigo3, enemigo3_rect.topleft)