#Los Tiguerazos del M3
#Ian Arroyo Aguilar
#Carlos Antonio Rodriguez Hernandez

import sys
import numpy as np
import random

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




def Past_Defenses():
    #Esto trabajando con las partidas anteriores, crea una representacion matricial
    #Donde 0 no hay nada y 1 barco
    past_boards = []
    board_instance = np.zeros(shape=(gz,gz),dtype=np.int8)

    for _ in range(N):
        past_boards.append(np.copy(board_instance))
        
    for i in range(N):
        for j in range(K):
            k = 0
            long = int(j+2)
            while k < len(inp_def[i][j]):
                x_k = int(inp_def[i][j][k])
                y_k = int(inp_def[i][j][k+1])
                direction = inp_def[i][j][k+2]
                if direction == "V":
                    for l in range(long):
                        past_boards[i][y_k+l][x_k]=1
                elif direction == "H":
                    for l in range(long):
                        past_boards[i][y_k][x_k+l]=1
                k += 3
    
    if past_boards == []:
        past_boards.append(np.ones(shape=(gz,gz),dtype=np.int8))
    return past_boards

def Past_Attacks():
    past_attacks = []
    board_instance = np.zeros(shape=(gz,gz),dtype=np.int8)
    for _ in range(N):
        past_attacks.append(np.copy(board_instance))
    for i in range(N):
        k = 0
        while k< len(inp_atk[i]):
            x_k = int(inp_atk[i][k])
            y_k = int(inp_atk[i][k+1])
            past_attacks[i][y_k][x_k]=1
            k+=2
    if past_attacks == []:
        past_attacks.append(np.ones(shape=(gz,gz),dtype=np.int8))
    return past_attacks



def Obtener_Adyacencias(x,y):
    #movs ortogonales, las 4
    movimientos = [(-1,0),(1,0),(0,1),(0,-1)]
    adyacentes = []
    for mov in movimientos:
        x_new = x + mov[0]
        y_new = y + mov[1]

        if 0 <= x_new <= gz-1 and 0 <= y_new <= gz-1:
            adyacentes.append((y_new,x_new))
    return adyacentes #Aqui los x,y estan invertidos, pq la pinche matriz funciona y,x y va a ser mas comodo asi

def Obtener_Adyacencias_Grupo(points):
    adyacentes = set()
    for point in points:
        point_adyacentes = Obtener_Adyacencias(point[0],point[1])
        for point_adyacente in point_adyacentes:
            if (point_adyacente[1],point_adyacente[0]) not in points:
                adyacentes.add(point_adyacente)
    return list(adyacentes)
        

def Atk():

    #Creo una representacion de las partidas anteriores
    #En todo momento la representacion va a ser la siguiente
    #0: No hay nada
    #1: Hay un barco
    #2: No se conoce todavia esa casilla
    
    current_board = np.ones(shape=(gz,gz),dtype=np.int8)*2
    
    if N == 0:
        M = 1
    else:
        M = N

    past_boards = Past_Defenses()
    past_attacks = Past_Attacks()

    past_mix = []
    for i in range(M):
        past_mix.append(np.multiply(past_boards[i],past_attacks[i]))

    
    past_freq_info_def = np.sum(past_boards,axis=0)/M
    past_freq_info_def[past_freq_info_def == 0]+= 1/M
    
    past_freq_info_atk = np.sum(past_mix,axis=0)/M
    past_freq_info_atk[past_freq_info_atk == 0]+= 1/M

    past_freq_info_def = (past_freq_info_def + 0.75*past_freq_info_atk)

    for i in range(gz):
        for j in range(gz):
            if (i+j)%2 == 0:
                past_freq_info_def[i][j] = 0
    
    random_threshold = 0.75
    
    killer_points = []

    cond_unknown = current_board>1
    unknown_board = np.where(cond_unknown,1,0)
    #Aqui tengo un mapa de calor multiplicando las casillas que no se han disparado
    #Junto a la informacion de frecuencia relativa de las partidas anteriores
            
    info_board = np.multiply(unknown_board,past_freq_info_def)


    mode = 'hunter' #Tengo dos modos, hunter y killer, empiezo hunter pq no conozco ningun barco tocado
    while True:
        #Calculo de hacia donde va el disparo
        #Este depende de que modo este
        
        if mode == 'hunter':
            valores = np.unique(info_board)
            valores = valores[valores != 0]
            val_candidato = 1
            rand = np.random.rand() #Genero un valor aleatorio entre 0 y 1

            #Aleatoriamente tomo entre el menor y el mayor posible probs
            if rand < random_threshold:
                val_candidato = valores[-1]
            else:
                val_candidato = valores[0]
            
            
            indices_candidatos = np.where(info_board == val_candidato)
            coords_candidatos = list(zip(indices_candidatos[1],indices_candidatos[0]))
            candidato = random.choice(coords_candidatos) #De todos los extremos impares, tomamos uno al azar
            x_c = candidato[0]
            y_c = candidato[1]
            
            
            #Aqui compruebo de casualidad si las adyacencias da como resultado que todo ya esta hundido haciendolo imposible
            adyacentes = Obtener_Adyacencias(x_c,y_c)
            adyacentes_agua = all(current_board[point] == 0 for point in adyacentes)
            if adyacentes_agua:
                current_board[y_c][x_c] = 0
                continue

            



        elif mode == 'killer':
            coords_candidatos = Obtener_Adyacencias_Grupo(killer_points)
            if all(current_board[point] for point in coords_candidatos) == 0:
                mode = 'hunter'
                killer_points = []
                continue
            else:
                candidatos_unknown = [coord for coord in coords_candidatos if current_board[coord]==2]
                candidato_temp = random.choice(candidatos_unknown)
                candidato = (candidato_temp[1],candidato_temp[0])

        x=candidato[0]
        y=candidato[1]
        print(x,y,flush=True)
        info_board[y][x] = 0

        result = int(input())
        if result == 0:
            current_board[y][x] = 0
        elif result == 1:
            current_board[y][x] = 1
            if mode == 'hunter':
                mode = 'killer'    
            killer_points.append((x,y))

        elif result == 2:
            break
        

           

Atk()
