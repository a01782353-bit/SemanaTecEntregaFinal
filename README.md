# SemanaTecEntregaFinal
código entrega final
# Paint con Turtle

Proyecto simple de **Paint** usando Python y la librería `turtle`.  
Permite dibujar figuras básicas y cambiar colores y grosor de línea.

---

## Funciones

- Dibujar: líneas, cuadrados, rectángulos, triángulos y círculos.
- Cambiar color con teclas:  
  - `K`: Negro  
  - `W`: Blanco  
  - `G`: Verde  
  - `B`: Azul  
  - `R`: Rojo  
  - `Y`: Amarillo
- Cambiar figura con teclas:  
  - `l`: Línea  
  - `s`: Cuadrado  
  - `c`: Círculo  
  - `r`: Rectángulo  
  - `t`: Triángulo
- Cambiar grosor con teclas: `1, 2, 3, 4, 5`
- Deshacer con `u`.
- Dibujar haciendo clic en la ventana para establecer inicio y fin de la figura.

---

## Cambios respecto a la versión original

1. **Funciones completas de figuras**: ahora el círculo, rectángulo y triángulo funcionan correctamente.  
2. **Grosor de línea configurable**: se agregó el parámetro `width` y atajos de teclado para cambiarlo.  
3. **Triángulos y cuadrados adaptativos**: funcionan correctamente sin importar la dirección del mouse.  
4. **Código más limpio**: uso consistente de `turtle.width()`, `begin_fill()` y `end_fill()`.  
5. **Eliminación de dependencia innecesaria**: ya no se requiere `freegames` para dibujar.

---

## Cómo usar

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/paint-turtle.git
# 🐍 Snake Game con Comida Móvil y Colores Aleatorios  

Este es un juego clásico de **Snake** en Python utilizando la librería [`freegames`](https://pypi.org/project/freegames/).  
En esta versión mejorada, la comida no solo aparece en posiciones aleatorias, sino que además **se mueve dentro de la ventana de juego** y **cambia de color en cada partida**, al igual que la serpiente.  

---

## 🎮 Características
- La serpiente crece cada vez que come la comida.
- La comida se mueve un paso en direcciones aleatorias (arriba, abajo, izquierda, derecha) sin salirse de la ventana.
- Los colores de la serpiente y de la comida se eligen de manera **aleatoria** al inicio de cada partida (no pueden ser iguales).
- El juego termina si la serpiente choca con los bordes o consigo misma.
- El puntaje se muestra en la terminal (longitud de la serpiente).

---

## 🕹️ Controles
- **Flecha →** : Mover a la derecha  
- **Flecha ←** : Mover a la izquierda  
- **Flecha ↑** : Mover hacia arriba  
- **Flecha ↓** : Mover hacia abajo  

---

## 🚀 Requisitos
Asegúrate de tener instalado Python (>=3.8) y la librería `freegames`.  

```bash
pip install freegames

# 🕹️ Pac-Man Modificado

## 📌 Descripción  
Este proyecto es una versión modificada de un videojuego estilo **Pac-Man**, desarrollado en Python.  
El objetivo fue experimentar con mecánicas del juego y aplicar buenas prácticas de desarrollo colaborativo mediante **Git y GitHub**.  

---

## 🔄 Cambios Realizados  

- 🎯 **Nuevo tablero**  
  Se rediseñó el mapa del juego con un laberinto alternativo, generando una experiencia distinta a la original.  

- 👻 **Fantasmas más rápidos**  
  Se aumentó la velocidad de movimiento de los enemigos, incrementando el nivel de dificultad.  

- 🧠 **Fantasmas más inteligentes**  
  Se mejoró la lógica de movimiento de los fantasmas para que persigan al jugador de forma más eficiente.

Controles:
    ↑ Flecha Arriba  - Mover Pac-Man hacia arriba
    ↓ Flecha Abajo  - Mover Pac-Man hacia abajo
    ← Flecha Izquierda - Mover Pac-Man hacia la izquierda
    → Flecha Derecha - Mover Pac-Man hacia la derecha

Cómo Ejecutar:
1. Asegúrate de tener Python 3.6+ instalado.
2. Instala las dependencias necesarias:
    pip install freegames
3. Ejecuta el juego desde el terminal o Anaconda Prompt:
    python pacman.py

Objetivo:
Recoger todos los puntos del tablero evitando a los fantasmas.
