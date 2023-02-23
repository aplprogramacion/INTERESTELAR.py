# INTERESTELAR.py
![This is an image](https://github.com/aplprogramacion/INTERESTELAR.py/blob/master/Captura%20de%20pantalla%20(13).png)
[![Alt text](https://img.youtube.com/vi/fL6GdtiRC5E/0.jpg)](https://www.youtube.com/watch?v=fL6GdtiRC5E)
# El fichero Main:
Este código es un programa de Pygame. Pygame es un conjunto de módulos de Python diseñados para la programación de videojuegos. El código muestra una pantalla de menú con varios botones y controles de volumen y movimiento.

La sección de código se divide en bloques que realizan diferentes tareas. Aquí hay una descripción de cada bloque:

Importaciones y configuraciones de Pygame: Se importan los módulos necesarios de Pygame y se configura el modo de visualización de pantalla, la fuente de texto y el reloj de Pygame.

Configuración de la pantalla: Se establece el tamaño de la pantalla y el título de la ventana. También se carga un icono y se define el objeto de pantalla.

Configuración de sonido: Se configura el reproductor de música de Pygame para cargar y reproducir un archivo de música sin parar.

Definición de colores y textos: Se definen dos colores y se crean objetos de texto para mostrar los textos del menú.

Definición de un fondo de pantalla: Se define una clase de sprite para el fondo de pantalla y se implementa el movimiento de desplazamiento para dar la ilusión de movimiento.

Definición de una nave: Se define una clase de sprite para la nave del jugador y se implementa el movimiento de ida y vuelta.

Definición de botones: Se define una clase de botón y se crea un objeto de botón para cada botón en el menú.

Definición de controles de volumen: Se define una función para manejar los controles de volumen.

Bucle principal: Este es el bucle principal del programa que se ejecuta continuamente hasta que se cierra la ventana. Este bucle maneja todos los eventos de Pygame, como presionar teclas o hacer clic en botones, y actualiza y renderiza todos los sprites y objetos de texto en la pantalla.

# El fichero Interestelar:
El código es un programa de juego hecho con Pygame en el que se definen las constantes del juego como el tamaño de la ventana, FPS, paleta de colores y fuentes. Además, se establecen directorios para almacenar imágenes y sonidos utilizados en el juego y se cargan archivos de sonido en variables con la biblioteca Pygame.

Se define una clase Jugador que hereda de la clase Sprite de Pygame. En la clase Jugador, se definen los atributos de los jugadores como su imagen, posición, velocidad y disparos. También se definen los métodos para actualizar la posición del jugador y disparar.

 El juego consiste en una nave que dispara a los enemigos, evitando meteoritos que caen del cielo. Los meteoritos y los enemigos tienen diferentes niveles de dificultad y el jugador gana puntos al destruir a los enemigos. El código define dos clases, Meteoritos y Explosiones, y también incluye funciones auxiliares para crear barras de HP y mostrar texto en pantalla. El fondo de pantalla, el icono de la ventana y los gráficos de los enemigos y los meteoritos se cargan a través de imágenes en archivos. La ejecución del juego se controla a través de un loop principal que actualiza los sprites y detecta eventos de teclado para controlar la nave del jugador.
