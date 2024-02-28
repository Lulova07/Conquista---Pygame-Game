import pygame
import ventana as v
import constantes as c

def LimpiarPantalla():
    v.surface.fill((0, 0, 0))
        
def DrawPausa():
    LimpiarPantalla()
    ancho_ventana, alto_ventana = c.ANCHO_VENTANA, c.ALTO_VENTANA
    pygame.draw.rect(v.surface,(128,128,128,2),[0, 0, ancho_ventana, alto_ventana])
    
    # Cuadro 1
    ancho_menu_principal = 600
    alto_menu_principal = 200
    x_menu_principal = (ancho_ventana - ancho_menu_principal) // 2
    y_menu_principal = alto_ventana // 4  # La mitad superior
    pygame.draw.rect(v.surface, 'dark gray', [x_menu_principal, y_menu_principal, ancho_menu_principal, alto_menu_principal], 0, 10)
    
    texto1 = 'MENU DE PAUSA'
    fuente_cuadro1 = pygame.font.SysFont(None, 100)
    texto_superficie = fuente_cuadro1.render(texto1, True, 'black')
    ancho_texto, alto_texto = texto_superficie.get_size()
    x_texto = x_menu_principal + (ancho_menu_principal - ancho_texto) // 2
    y_texto = y_menu_principal + (alto_menu_principal - alto_texto) // 2
    v.surface.blit(texto_superficie, (x_texto, y_texto))
  
    # Espacio entre los cuadros
    espacio_entre_cuadros = 20

    # Dimensiones y coordenadas para los cuadros restantes (Reanudar, Salir del Juego)
    ancho_cuadro = 200
    alto_cuadro = 100
    
    # Coordenadas x y y comunes para ambos cuadros
    x_cuadros = (ancho_ventana - ancho_cuadro * 2 - espacio_entre_cuadros) // 2
    y_cuadros = y_menu_principal + alto_menu_principal + espacio_entre_cuadros

    # Cuadro Reanudar
    pygame.draw.rect(v.surface, 'dark gray', [x_cuadros, y_cuadros, ancho_cuadro, alto_cuadro], 0, 10)
    reanudar = pygame.draw.rect(v.surface, 'dark gray', [x_cuadros, y_cuadros, ancho_cuadro, alto_cuadro], 0, 10)
    texto_2 = 'Reanudar'
    fuente_cuadro2 = pygame.font.SysFont(None, 35)
    texto_superficie = fuente_cuadro2.render(texto_2, True, 'black')
    ancho_texto, alto_texto = texto_superficie.get_size()
    x_texto = x_cuadros + (ancho_cuadro - ancho_texto) // 2
    y_texto = y_cuadros + (alto_cuadro - alto_texto) // 2
    v.surface.blit(texto_superficie, (x_texto, y_texto))

    # Cuadro Salir del Juego
    pygame.draw.rect(v.surface, 'dark gray', [x_cuadros + ancho_cuadro + espacio_entre_cuadros, y_cuadros, ancho_cuadro, alto_cuadro], 0, 10)
    salir = pygame.draw.rect(v.surface, 'dark gray', [x_cuadros + ancho_cuadro + espacio_entre_cuadros, y_cuadros, ancho_cuadro, alto_cuadro], 0, 10)
    texto_4 = 'Salir del Juego'
    fuente_cuadro2 = pygame.font.SysFont(None, 35)
    texto_superficie = fuente_cuadro2.render(texto_4, True, 'black')
    ancho_texto, alto_texto = texto_superficie.get_size()
    x_texto = x_cuadros + ancho_cuadro + espacio_entre_cuadros + (ancho_cuadro - ancho_texto) // 2
    y_texto = y_cuadros + (alto_cuadro - alto_texto) // 2
    v.surface.blit(texto_superficie, (x_texto, y_texto))

    v.VENTANA.blit(v.surface, (0, 0))
    pygame.display.flip()
    return reanudar, salir

def DrawOpciones():
    LimpiarPantalla()
    ancho_ventana, alto_ventana = c.ANCHO_VENTANA, c.ALTO_VENTANA
    pygame.draw.rect(v.surface,(128,128,128,2),[0, 0, ancho_ventana, alto_ventana])
    
    # Cuadro 1
    ancho_menu_principal = 600
    alto_menu_principal = 200
    x_menu_principal = (ancho_ventana - ancho_menu_principal) // 2
    y_menu_principal = alto_ventana // 4  # La mitad superior
    pygame.draw.rect(v.surface, 'dark gray', [x_menu_principal, y_menu_principal, ancho_menu_principal, alto_menu_principal], 0, 10)
    
    texto1 = 'Opciones'
    fuente_cuadro1 = pygame.font.SysFont(None, 100)
    texto_superficie = fuente_cuadro1.render(texto1, True, 'black')
    ancho_texto, alto_texto = texto_superficie.get_size()
    x_texto = x_menu_principal + (ancho_menu_principal - ancho_texto) // 2
    y_texto = y_menu_principal + (alto_menu_principal - alto_texto) // 2
    v.surface.blit(texto_superficie, (x_texto, y_texto))
    
    espacio_entre_cuadros = 20
    
    # Dificultad y Volver
    ancho_cuadro = 200
    alto_cuadro = 100
    x_reanudar = (ancho_ventana - ancho_cuadro * 3 - espacio_entre_cuadros * 2) // 2
    y_cuadros = y_menu_principal + alto_menu_principal + espacio_entre_cuadros
    pygame.draw.rect(v.surface, 'dark gray', [x_reanudar, y_cuadros, ancho_cuadro, alto_cuadro], 0, 10)
    reanudar = pygame.draw.rect(v.surface, 'dark gray', [x_reanudar, y_cuadros, ancho_cuadro, alto_cuadro], 0, 10)
    
    texto_2 = 'Dificultad'
    fuente_cuadro2 = pygame.font.SysFont(None, 35)
    texto_superficie = fuente_cuadro2.render(texto_2, True, 'black')
    ancho_texto, alto_texto = texto_superficie.get_size()
    x_texto = x_reanudar + (ancho_cuadro - ancho_texto) // 2
    y_texto = y_cuadros + (alto_cuadro - alto_texto) // 2
    v.surface.blit(texto_superficie, (x_texto, y_texto))
    
    # Cuadro Opciones
    x_opciones = x_reanudar + ancho_cuadro + espacio_entre_cuadros
    pygame.draw.rect(v.surface, 'dark gray', [x_opciones, y_cuadros, ancho_cuadro, alto_cuadro], 0, 10)
    opciones = pygame.draw.rect(v.surface, 'dark gray', [x_opciones, y_cuadros, ancho_cuadro, alto_cuadro], 0, 10)
    
    texto_3 = 'Volver'
    fuente_cuadro2 = pygame.font.SysFont(None, 35)
    texto_superficie = fuente_cuadro2.render(texto_3, True, 'black')
    ancho_texto, alto_texto = texto_superficie.get_size()
    x_texto = x_opciones + (ancho_cuadro - ancho_texto) // 2
    y_texto = y_cuadros + (alto_cuadro - alto_texto) // 2
    v.surface.blit(texto_superficie, (x_texto, y_texto))
    
    v.VENTANA.blit(v.surface, (0,0))
    pygame.display.flip()

def DrawMainMenu():
    LimpiarPantalla()
    ancho_ventana, alto_ventana = c.ANCHO_VENTANA, c.ALTO_VENTANA
    v.surface.fill((0, 0, 0))

    # Título
    ancho_titulo = 400
    alto_titulo = 100
    x_titulo = (ancho_ventana - ancho_titulo) // 2
    y_titulo = alto_ventana // 4
    pygame.draw.rect(v.surface, 'dark gray', [x_titulo, y_titulo, ancho_titulo, alto_titulo], 0, 10)
    titulo = 'CONQUISTA'
    fuente_titulo = pygame.font.SysFont(None, 60)
    texto_superficie = fuente_titulo.render(titulo, True, 'white')
    ancho_texto, alto_texto = texto_superficie.get_size()
    x_texto = x_titulo + (ancho_titulo - ancho_texto) // 2
    y_texto = y_titulo + (alto_titulo - alto_texto) // 2
    v.surface.blit(texto_superficie, (x_texto, y_texto))
    pygame.display.flip()        