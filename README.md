# Battleship Algorithm

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
