# Battleship Algorithm

Los K tipos de barcos y la catidad de barcos por cada tipo (bi) son conocidas por el usuario de antemano

## 📌 Formato de Entrada Historial de Partidas
1. Un número entero `N` → cantidad de partidas anteriores.
2. Luego, para cada partida:
   - `K` líneas (una por cada tipo de barco), cada una con:
     - `bi × 3` valores( bi la cantidad de barcos de ese tipo):
       - `X Y` → Coordenadas de la esquina superior izquierda.
       - `O` → Orientación (`H` para horizontal, `V` para vertical).
3. **Las siguientes `N` líneas contienen la información de los ataques del rival:**  
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

- **`N = 2` (Dos partidas anteriores).**  
- **Cada partida tiene `K` líneas** con la ubicación de los barcos de cada tipo.  
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
Son K lineas (una por cada tipo de barco)
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

Después de que el programa te proporcione toda la información relevante sobre la partida anteriores (ubicación de los barcos y otros detalles), comenzará a escuchar tus ataques. El jugador proporcionará coordenadas en formato `(x, y)` y el programa responderá con:

- **`1`**: El ataque fue exitoso (coordenadas correctas, se acertó a un barco).
- **`0`**: El ataque falló (coordenadas incorrectas, no se acertó a un barco).
- **`-1`**: Fin de la partida. El jugador ya no puede hacer más ataques.

### **Formato de Interacción:**

1. **Al inicio de la partida**, el programa te proporciona toda la información necesaria sobre los barcos y la configuración del juego de las partidas anteriores.
   
2. Después de eso, el programa comenzará a escuchar tus ataques y te dará una respuesta interactiva según el ataque:

   - **`1`**: Si el ataque acertó a un barco.
   - **`0`**: Si el ataque no acertó a ningún barco.
   - El programa continuará hasta que se haya dado un ataque en el que el programa devuelva **`-1`**, lo que indica que la partida ha terminado.

### 📄 **Ejemplo de Interacción:**

#### **Ejemplo:**

```txt
(1, 1)  ← El jugador ingresa las coordenadas del ataque.
0       ← El ataque falló (no acertó a un barco).

(2, 2)  ← El jugador ingresa las coordenadas del ataque.
1       ← El ataque fue exitoso (coordenadas correctas, acertó a un barco).

(3, 3)  ← El jugador ingresa las coordenadas del ataque.
1       ← El ataque fue exitoso (coordenadas correctas, acertó a un barco).

(4, 4)  ← El jugador ingresa las coordenadas del ataque.
-1      ← Fin de la partida (el juego ha terminado, no se pueden realizar más ataques).
```


