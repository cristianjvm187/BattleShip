import random
import numpy as np
import time

# Empiezas a contar el tiempo

t = 0
cc = 0

Ns = {2: 25, 3: 50, 4: 25, 5: 25}
Sb = 50


def Possible_def(defense, sizeOfBoard=Sb, numberOfShips=Ns):
    """
    Validates the placement of ships on a Battleship board.
    Parameters:
    defense (dict): A dictionary where keys are ship lengths (int) and values are lists of tuples. sEach tuple contains the row (int), column (int), and position ('H' for horizontal, 'V' for vertical).
    sizeOfBoard (int, optional): The size of the Battleship board. Default is 10.
    numberOfShips (dict, optional): A dictionary where keys are ship lengths (int) and values are the number of ships of that length. Default is {2: 1, 3: 2, 4: 1, 5: 1}.
    Returns:
    tuple: A tuple containing:
        - int: 1 if the ship placements are valid, 0 otherwise.
        - list: A 2D list representing the board with ships placed (1 for ship, 0 for empty).
    """

    zeros = [[0 for _ in range(sizeOfBoard)] for _ in range(sizeOfBoard)]  # rev
    board = [[0 for _ in range(sizeOfBoard)] for _ in range(sizeOfBoard)]

    if defense == None:
        return 0, zeros

    for type in numberOfShips:
        if len(defense[type]) != numberOfShips[type]:
            return 0, zeros
        for row, column, position in defense[type]:
            if position == "H":
                if row < 0 or column < 0 or column + type > sizeOfBoard:
                    return 0, zeros
                for c in range(column, column + type):
                    board[row][c] = 1
            if position == "V":
                if column < 0 or row < 0 or row + type > sizeOfBoard:
                    return 0, zeros
                for r in range(row, row + type):
                    board[r][column] = 1

    numberOfOnes = 0
    for row in board:
        numberOfOnes += sum(row)
    if numberOfOnes != sum([numberOfShips[type] * type for type in numberOfShips]):
        print(numberOfOnes, sum([numberOfShips[type] * type for type in numberOfShips]))
        return 0, zeros

    return 1, board


# Parametros constantes
gz = 50  # alto del tablero cuadrado
gr = gz // 10
K = 4  # Cantidad de tipos de barcos
dim = [2, 3, 4, 5]  # Dimensiones de cada tipo en orden
b = [1, 2, 1, 1]  # Cantidad de barcos de cada tipo en 10x10


# Recogida de las partidas anteriores

N = int(input())  # Cantidad de partidas anteriores

inp_def = []
inp_atk = []

for _ in range(N):
    inp_def.append([])
    for _ in range(K):
        inp_def[-1].append(input().split())

for j in range(N):
    inp_atk.append(input().split()[1::])


defensa = np.zeros((50, 50), dtype=int)
dic = {2: [], 3: [], 4: [], 5: []}


for i in range(2, 6, 1):
    out = ""
    # print(i)
    for _ in range(Ns[i]):
        b = False
        while not b:
            r = random.randint(0, 49)
            c = random.randint(0, 49)
            p = 0
            if 0.5 > random.random():
                p = 1
            if p == 0:
                bb = True
                for j in range(i):
                    if (c + j > 9 or defensa[r][c + j]) == 1:
                        bb = False
                        break
                if bb:
                    for j in range(i):
                        defensa[r][c + j] = 1
                        b = True
                    dic[i].append((r, c, "H"))
                    out += str(r) + " " + str(c) + " H "
                    # print(r, c, "H", flush=True)
            else:
                bb = True
                for j in range(i):
                    if r + j > 9 or defensa[r + j][c] == 1:
                        bb = False
                        break
                if bb:
                    for j in range(i):
                        defensa[r + j][c] = 1
                        b = True
                    dic[i].append((r, c, "V"))
                    out += str(r) + " " + str(c) + " V "

    print(out, flush=True)
