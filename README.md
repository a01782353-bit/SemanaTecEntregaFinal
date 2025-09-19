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
