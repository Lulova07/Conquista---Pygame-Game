import pygame
import os
import math
import random
import constantes as c
import balas as b
import jugador as j
import ventana as v
import enemigos as e
import bonus as bon
import menus as m

pygame.init()
pygame.display.set_caption('Conquista')


def main():
    reloj = pygame.time.Clock()
    jugador_1, jugador_rect, vidas_jugador, salud_jugador, puntos_jugador = j.GenerarJugador() # Generar jugador
    enemigo1, enemigo1_rect, salud_enemigo1 = e.GenerarEnemigo1() # Generar enemigo 1
    enemigo2, enemigo2_rect = e.GenerarEnemigo2() # Generar enemigo 2
    
    enemigo3_size = c.ANCHO_ENEMIGO3
    enemigo3_rect_x = random.randint(c.ANCHO_ENEMIGO3,c.ANCHO_VENTANA - c.ANCHO_ENEMIGO3)
    enemigo_rect_y = random.randint(c.ALTO_ENEMIGO3,c.ALTO_VENTANA - c.ALTO_ENEMIGO3)
    enemigo3_rect = pygame.Rect(enemigo3_rect_x, enemigo_rect_y, enemigo3_size, enemigo3_size)
    
    heart, heart_rect = None, None

    font = pygame.font.SysFont(None, 30)
    correr = True
    
    pausa = False
    reanudar, salir = m.DrawPausa()
    
    i = 0
    while correr:
        
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if pausa:
                        pausa = False
                    else:
                        pausa = True

            if pausa and event.type == pygame.MOUSEBUTTONDOWN:
                if reanudar.collidepoint(event.pos):
                    pausa = False
                if salir.collidepoint(event.pos):
                    correr = False
    
        if not pausa:
            reloj.tick(c.FPS)
            
            # JUGADOR
            mouse_posicion = pygame.mouse.get_pos()
            angulo = j.CalcularAngulo(jugador_rect, mouse_posicion)
            jugador, jugador_rect = j.RotarJugador(jugador_1, angulo, jugador_rect)

            teclas_presionadas = pygame.key.get_pressed()
            j.ControlarJugador(teclas_presionadas,jugador_rect)
            b.ActualizarBalasJugador(enemigo1_rect,enemigo2_rect,salud_enemigo1)
            enemigo1_hits  = b.ActualizarBalasJugador(enemigo1_rect,enemigo2_rect,salud_enemigo1)
            salud_enemigo1 -= enemigo1_hits / 2
            
            # ENEMIGO 1
            if i % (c.TIEMPO_ENTRE_DISPAROS_ENEMIGO1*60) == 0:
                b.DispararEnemigo1(enemigo1_rect,jugador_rect)
            b.ActualizarBalasEnemigo1(jugador_rect,enemigo2_rect,salud_jugador)
            
            hits_player = b.ActualizarBalasEnemigo1(jugador_rect,enemigo2_rect,salud_jugador)
            salud_jugador -= hits_player * 2
            
            # ENEMIGO 2
            e.MoverEnemigo2(enemigo2_rect,jugador_rect)
            
            # ENEMIGO 3
            aumento = 0.04
            enemigo3_size += aumento
            enemigo3_rect_x -= aumento/2
            enemigo_rect_y -= aumento/2
            enemigo3_rect = pygame.Rect(enemigo3_rect_x, enemigo_rect_y, enemigo3_size, enemigo3_size)
            enemigo3 = pygame.transform.scale(e.enemy3_img, (enemigo3_size,enemigo3_size))
            
            if jugador_rect.colliderect(enemigo1_rect) or jugador_rect.colliderect(enemigo2_rect) or jugador_rect.colliderect(enemigo3_rect):
                salud_jugador -= 0.5
                
            if enemigo1_rect.colliderect(enemigo2_rect) or enemigo1_rect.colliderect(enemigo3_rect):
                salud_enemigo1 -= 0.1
            if salud_jugador <= 0:
                vidas_jugador -= 1
                salud_jugador = c.PUNTOS_SALUD_JUGADOR
                if vidas_jugador <= 0:
                    print("Fin del Juego")
                    correr = False
            
            if salud_enemigo1 <= 0:
                enemigo1, enemigo1_rect, salud_enemigo1 = e.GenerarEnemigo1()
                puntos_jugador += 50

            if i % 1000 == 0:
                heart, heart_rect = bon.GenerarCorazon()

            try: 
                if jugador_rect.colliderect(heart_rect):
                    heart, heart_rect = None, None
                    salud_jugador += 25
            except:
                pass

            v.DrawWindow(jugador,jugador_rect,
                    enemigo1, enemigo1_rect,
                    enemigo2, enemigo2_rect,
                    enemigo3, enemigo3_rect,
                    heart=heart,heart_rect=heart_rect,
                    )
            
            b.DibujarBalasJugador()
            b.DibujarBalasEnemigo1()
      
            v.ElementosPantalla(font,salud_jugador,vidas_jugador,puntos_jugador,salud_enemigo1,enemigo1_rect)
            pygame.display.flip()
            
        elif pausa:
            reloj.tick(0)
            m.DrawPausa() 

    pygame.quit()
    
if __name__ == "__main__":
    main()