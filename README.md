# Battleship Bot Warfare

Un jugador debera proporcionar dos programas uno que se encargue de la estrategia  defensiva y otro la de ofensiva. Cada uno de los programas debe recoger el historial de las partidas anteriores. El programa defensivo luego de recoger el historial de partidas debera  dar las posiciones de sus barcos. En cambio el ofensivo de manera analoga recogera el historial partidas y procedera a interactuar con el juez con el objetivo de descubrir las posiciones de los barcos del rival  

Los 4 tipos de barcos y la catidad de barcos por cada tipo son:
- Barco 2x1 cantidad 25
- Barco 3x1 cantidad 50
- Barco 4x1 cantidad 25
- Barco 5x1 cantidad 25

## 📌 Formato de Entrada Historial de Partidas
El historial de partidas consta de las posiciones defensivas en las partidas anteriores del jugador a la defensa y los lugares donde ataco el jugador a la ofensiva en las partidas anteriores 
1. Un número entero `N` → cantidad de partidas anteriores.
2. Luego, para cada  una de esas partida se proporcionara la defensa que diste:
   - `4` líneas (una por cada tipo de barco), cada una con:
     - `bi × 3` valores( bi la cantidad de barcos de ese tipo):
       - `X Y` → Coordenadas de la esquina superior izquierda.
       - `O` → Orientación (`H` para horizontal, `V` para vertical).
3. **Las siguientes `N` líneas contienen la información de los ataques del rival en `N` partidas anteriores:**  
   - Cada línea comienza con un número entero `A` → cantidad de ataques en esa partida.  
   - Luego, `2 × A` valores representando las coordenadas `X Y` de los disparos del rival.  

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
````
## 📄 Explicación del Ejemplo
En el ejemplo la cantidad tipos de barcos son diferentes al de la competencia en busqueda de un mejor entendimiento de la forma del historial de partidas
- **`N = 2` (Dos partidas anteriores).**  
- **Cada partida tiene `3` líneas** con la ubicación de los barcos de cada tipo.  
- **Después de las partidas, hay `N` líneas** con los ataques del rival.  

### **Partida 1**  
- **Tipo 1 (2 barcos)** → `(1,2,H)`, `(4,4,V)`  
- **Tipo 2 (3 barcos)** → `(0,0,H)`, `(2,3,V)`, `(5,5,H)`  
- **Tipo 3 (1 barco)** → `(6,6,H)`  
- **Ataques del Rival (3 ataques)** → `(1,1)`, `(4,4)`, `(2,3)`  

### **Partida 2**  
- **Tipo 1 (2 barcos)** → `(1,2,H)`, `(4,4,V)`  
- **Tipo 2 (3 barcos)** → `(0,1,V)`, `(3,3,H)`, `(5,5,V)`  
- **Tipo 3 (1 barco)** → `(7,7,V)`  
- **Ataques del Rival (2 ataques)** → `(5,5)`, `(0,1)` 

## 📌 **Formato de Salida de los barcos(jugador defensivo): **
Son 5 lineas (una por cada tipo de barco)
Cada línea en la salida contiene las ubicaciones de los barcos de un tipo. Cada barco se representa por tres valores: `X Y O`.
Las lineas van a tener 3*bi caracteres(siendo bi la cantidad de barcos del tipo i)

### **Ejemplo de Salida:**

```txt
1 2 H 4 4 V
0 1 H 2 3 V 5 5 H
6 9 H
```
## 📄 Explicación del Ejemplo

- **`K = 3`** (Tres tipos de barcos).  
- **Cada tipo de barco tiene `bi` barcos**, y cada barco está representado por sus coordenadas `X Y` (que corresponden a la esquina derecha del barco) y su orientación `O` (`H` para horizontal, `V` para vertical).

## 📌 Descripción del Formato de Interacción del Jugador Atacante

1. **Al inicio de la partida**, el programa te proporciona toda la información necesaria sobre los barcos y la configuración del juego de las partidas anteriores.
   
2. Después de eso, el programa comenzará a escuchar tus ataques y te dará una respuesta interactiva según el ataque:

   - **`1`**: Si el ataque acertó a un barco.
   - **`0`**: Si el ataque no acertó a ningún barco.
   - El programa continuará hasta que se haya dado un ataque en el que el programa devuelva **`2`**, lo que indica que la partida ha terminado.

### 📄 **Ejemplo de Interacción:**

#### **Ejemplo:**

```txt
1 1  ← El jugador ingresa las coordenadas del ataque.
0       ← El ataque falló (no acertó a un barco).

2 2  ← El jugador ingresa las coordenadas del ataque.
1       ← El ataque fue exitoso (coordenadas correctas, acertó a un barco).

3 3  ← El jugador ingresa las coordenadas del ataque.
1       ← El ataque fue exitoso (coordenadas correctas, acertó a un barco).

4 4  ← El jugador ingresa las coordenadas del ataque.
2      ← Fin de la partida (el juego ha terminado, no se pueden realizar más ataques).
```


