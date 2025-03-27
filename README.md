# Battleship

Un jugador deberá proporcionar dos programas: uno que se encargue de la estrategia defensiva y otro de la ofensiva. Cada uno de los programas debe recoger el historial de las partidas anteriores.  
El programa defensivo, luego de recoger el historial de partidas, deberá dar las posiciones de sus barcos. En cambio, el ofensivo, de manera análoga, recogerá el historial de partidas y procederá a interactuar con el juez con el objetivo de descubrir las posiciones de los barcos del rival.

Los 4 tipos de barcos y la cantidad de barcos por cada tipo son:

- Barco 2x1 cantidad 25  
- Barco 3x1 cantidad 50  
- Barco 4x1 cantidad 25  
- Barco 5x1 cantidad 25  

En los ejemplos, el número de tipos de barcos, así como la cantidad de cada uno, son diferentes al de la competencia en búsqueda de un mejor entendimiento de la estructura del historial de partidas, formato de salida de los barcos y de la interacción.

---

## 📌 Formato de Entrada Historial de Partidas

El historial de partidas consta de las posiciones defensivas en las partidas anteriores del jugador a la defensa y los lugares donde atacó el jugador a la ofensiva en las partidas anteriores:

1. Un número entero `N` → cantidad de partidas anteriores.
2. Luego, para cada una de esas partidas, se proporcionará la defensa que diste:
   - `4` líneas (una por cada tipo de barco), cada una con:
     - `bi × 3` valores (`bi` es la cantidad de barcos de ese tipo):
       - `X Y` → Coordenadas de la esquina superior izquierda.
       - `O` → Orientación (`H` para horizontal, `V` para vertical).
3. **Las siguientes `N` líneas contienen la información de los ataques del rival en `N` partidas anteriores:**  
   - Cada línea comienza con un número entero `A` → cantidad de ataques en esa partida.  
   - Luego, `2 × A` valores representando las coordenadas `X Y` de los disparos del rival.  

---

## 📥 Ejemplo de Entrada

```txt
2
1 2 H  4 4 V
0 0 H  2 3 V  5 5 H
6 6 H
1 2 H  4 4 V
0 1 V  3 3 H  5 5 V
7 7 V
3 1 1  4 4  2 3
2 5 5  0 1
