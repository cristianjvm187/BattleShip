import sys

N = int(input())  # Cantidad de partidas anteriores

gz = 10  # alto del tablero cuadrado
K = 4  # Cantidad de tipos de barcos
dim = []  # Dimensiones de cada tipo en orden
b = []  # Cantidad de barcos de cada tipo


# Recogida de las partidas anteriores

inp_def = []
inp_atk = []

for _ in range(N):

    inp_def.append([])

    for _ in range(K):

        inp_def[-1].append(input().split())

for j in range(N):

    inp_atk.append(input().split()[1::])

# print("asdas")


def player1():
    for i in range(gz):
        for j in range(gz):
            print(i, j, flush=True)

            result = int(input())
            # print(result)
            # result = 0
            if result == -1:
                break


# print(inp_def)
# print(inp_atk)
player1()
