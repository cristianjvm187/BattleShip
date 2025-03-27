import sys

K = 4  # Cantidad de tipos de barcos
gz = 50  # alto del tablero cuadrado


N = int(input())  # Cantidad de partidas anteriores

# Recogida de las partidas anteriores
inp_def = []
inp_atk = []

# Informacion defensiva del rival de las partidas anteriores
for _ in range(N):

    inp_def.append([])

    for _ in range(K):

        inp_def[-1].append(input().split())

# Informacion de los ataques que has realizado en las partidas anteriores
for j in range(N):
    inp_atk.append(input().split()[1::])


def Atk():
    """
    Aqui es donde esta implementada la estrategia de ataque
    en este caso ejemplo es la que le tira cada una de las casillas(muy bruta)
    """
    for i in range(gz):
        for j in range(gz):
            print(i, j, flush=True)

            result = int(input())

            if result == 2:
                break


Atk()
