# Actividad Pull Request y Code Review
## Código a revisar: Adivinar número
### Integrantes del equipo 4:
- Josué Labrada
- Paulina Flores

En el repositorio se encuentra la actividad desarrollada de 'Pull Request y Code Review' de la clase de Calidad de Software.

Para ejecutar el programa solo se necesita ejecutar dos comandos:
   ```
   bash
   python adivina_numero.py
   ```

### Observaciones iniciales de la actividad
Principalmente, se observaron las siguientes 3 caracteristicas en el código:
- En la función *choose_difficulty* hay una contradicción, ya que, cuando el usuario no especifica la dificultad de juego, el sistema automaticamente le asigna el modo Fácil; sin embargo, la función ejecuta el nivel Medio, de manera que el usuario está jugando en modo Medio, cuando se le dijo que estaba en el Fácil.
- Ninguna de las funciones tiene comentarios referentes a la responsabilidad y funcionalidad de cada una.
- En la función *play_round* el ciclo while inicia en 0, de manera que el usuario tiene la posibilidad de jugar un turno más del establecido.