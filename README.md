# Battleship Algorithm

## 📌 Formato de Entrada Historial de Partidas
1. Un número entero `N` → cantidad de partidas anteriores.
2. Luego, para cada partida:
   - `K` líneas (una por cada tipo de barco), cada una con:
     - `bi × 3` valores( bi la cantidad de barcos de ese tipo):
       - `X Y` → Coordenadas de la esquina superior izquierda.
       - `O` → Orientación (`H` para horizontal, `V` para vertical).

## 📥 Ejemplo de Entrada
2
1 2 H 4 4 V 
0 0 H 2 3 V 5 5 H
6 6 H 
1 2 H 4 4 V
0 1 V 3 3 H 5 5 V
7 7 V
## 📄 Explicación del Ejemplo

### Partida 1  
- **Tipo 1 (2 barcos)** → `(1,2,H)`, `(4,4,V)`  
- **Tipo 2 (3 barcos)** → `(0,0,H)`, `(2,3,V)`, `(5,5,H)`  
- **Tipo 3 (1 barco)** → `(6,6,H)`

### Partida 2  
- **Tipo 1 (2 barcos)** → `(1,2,H)`, `(4,4,V)`  
- **Tipo 2 (3 barcos)** → `(0,1,V)`, `(3,3,H)`, `(5,5,V)`  
- **Tipo 3 (1 barco)** → `(7,7,V)`

---

## 🚀 Cómo Ejecutarlo
(Ejemplo de cómo correr el código si es un script)
