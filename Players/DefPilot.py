import sys

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


def player0(K=4, dim=[2, 3, 4, 5], b=[1, 2, 1, 2]):
    max_dim = max(dim)

    aux = 0
    for i in range(K):

        output = ""
        for j in range(b[i]):
            # output+=str(j) + " " + str(i* max_dim + dim[i] - 1)+" V "
            output += str(j * dim[i] + j) + " " + str(aux) + " V "
        aux += 1
        output = output[:-1]

        print(output)
        sys.stdout.flush()


def assingDef():
    aux = 0
    for i in range(K):
        output = ""
        for j in range(b[i]):
            for r in range(gr):
                for c in range(gr):
                    # output+=str(j) + " " + str(i* max_dim + dim[i] - 1)+" V "
                    output += (
                        str(j * dim[i] + j + 10 * r) + " " + str(aux + 10 * c) + " V "
                    )
        aux += 1
        output = output[:-1]

        print(output)
        sys.stdout.flush()


# print(inp_def)
# print(inp_atk)
# player0()
assingDef()
