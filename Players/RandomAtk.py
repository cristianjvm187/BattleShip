K = 4  # Cantidad de tipos de barcos
gz = 50  # alto del tablero cuadrado

import random

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


coj = set([])


def Atk():
    """
    Aqui es donde esta implementada la estrategia de ataque
    en este caso ejemplo es la que le tira cada una de las casillas(muy bruta)
    """
    result = -1
    objetivos = set()
    mood_target = 0
    while result != 2:
        if mood_target == 0 or len(objetivos) == 0:
            r = random.randint(0, 49)
            c = random.randint(0, 49)
            while (r, c) in coj:
                r = random.randint(0, 49)
                c = random.randint(0, 49)
            coj.add((r, c))
            print(r, c, flush=True)
            result = int(input())
            if result == 1:
                mood_target = 1
                if not ((max(0, r - 1), c) in coj):
                    objetivos.add((max(0, r - 1), c))
                if not ((min(49, r + 1), c) in coj):
                    objetivos.add((min(49, r + 1), c))
                if not ((r, max(0, c - 1)) in coj):
                    objetivos.add((r, max(0, c - 1)))
                if not ((r, min(49, c + 1)) in coj):
                    objetivos.add((r, min(49, c + 1)))
            # print(objetivos)
        else:
            # print(objetivos)

            r = next(iter(objetivos))[0]
            c = next(iter(objetivos))[1]
            print(r, c, flush=True)
            result = int(input())
            objetivos.remove((r, c))
            coj.add((r, c))
            if result == 1:
                if not ((max(0, r - 1), c) in coj):
                    objetivos.add((max(0, r - 1), c))
                if not ((min(49, r + 1), c) in coj):
                    objetivos.add((min(49, r + 1), c))
                if not ((r, max(0, c - 1)) in coj):
                    objetivos.add((r, max(0, c - 1)))
                if not ((r, min(49, c + 1)) in coj):
                    objetivos.add((r, min(49, c + 1)))


Atk()
