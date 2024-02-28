# Conquista - Juego con Pygame

## Descripción
Conquista es un juego desarrollado en Python utilizando la librería Pygame. En este emocionante juego, los jugadores asumen el control de una nave espacial que se enfrenta a diversas amenazas mientras busca sobrevivir y acumular puntos.

## Características Principales
- **Jugador:** Controla la nave con las teclas WASD, dispara balas con la barra espaciadora y controla la dirección de disparo usando el ratón.
- **Amenazas:** Enfrenta diferentes tipos de amenazas, cada uno con su propio comportamiento y desafíos únicos.
- **Puntuación:** Gana puntos al derrotar enemigos.
- **Vidas y Salud:** Gestiona las vidas y la salud del jugador, evitando colisiones con amenazas o proyectiles.
- **Elementos de Bonificación:** Encuentra elementos como corazones para recuperar la salud del jugador.

## Amenazas
El juego incluye tres tipos de amenazas:

### Amenaza 1: Torret
- Nave con una gran cantidad de vida.
- Dispara en dirección al jugador con una cadencia moderada.
- Estática en su posición.

### Amenaza 2: Creeper
- Nave de defensa que persigue al jugador y le ocasiona daño al tocarlo.
- No dispara, pero tiene una velocidad alta.

### Amenaza 3: Black Hole
- Amenaza latente desde el comienzo de la partida.
- Se genera en una zona aleatoria del mapa.
- Crece poco a poco, engullendo todo a su paso, incluyendo naves enemigas y al jugador.
- ¿Cuánto tiempo podrás sobrevivir?

## Estructura del Proyecto
- **main.py:** Archivo principal que inicia el juego.
- **jugador.py:** Módulo que define funciones relacionadas con el jugador.
- **enemigos.py:** Módulo con la lógica de diferentes tipos de enemigos.
- **balas.py:** Módulo para gestionar el disparo y colisiones de balas.
- **bonus.py:** Módulo que genera elementos de bonificación como corazones.
- **menus.py:** Módulo con implementaciones de menús y opciones del juego.
- **ventana.py:** Módulo para gestionar la ventana y elementos visuales.

## Requerimientos
- Python 3.x
- Pygame (instalado con `pip install pygame`)

## Cómo Ejecutar
1. Asegúrate de tener Python instalado en tu sistema.
2. Instala la librería Pygame con `pip install pygame`.
3. Ejecuta el juego utilizando el comando `python main.py`.

## Controles del Juego
- **Teclas WASD:** Mover al jugador.
- **Tecla de espacio:** Disparar balas.
- **Ratón:** Controlar la dirección de disparo.
- **Tecla Esc:** Pausar el juego.

## Contribuciones y Problemas
Si encuentras algún problema o tienes sugerencias para mejorar el juego, no dudes en abrir un problema en el repositorio.

## Posibles Mejoras Futuras
Se planea incorporar la opción de una tienda en el juego, permitiendo a los jugadores canjear puntos por objetos como escudos, potenciadores de velocidad o naves más veloces y poderosas, entre otras mejoras emocionantes."# Conquista---Pygame-Game" 
