#Los tiguerazos del M3
#Ian Arroyo Aguilar
#Carlos Antonio Rodriguez Hernandez
import sys
import random

# Parametros reales
gz = 50  # alto del tablero cuadrado
gr = 50
dim = [2, 3, 4, 5]  # Dimensiones de cada tipo en orden
b = [25, 50, 25, 25]  # Cantidad de barcos de cada tipo en 10x10

# Parametros para probar

# gz = 10  # alto del tablero cuadrado
# gr = 10
# dim = [2, 3, 4, 5]  # Dimensiones de cada tipo en orden
# b = [1, 2, 1, 1]

def check_boat_placement(mapa,coord,orient,d):
    if orient == 'H':
        casillas = [(coord[0],coord[1] + i) for i in range(d)]
        
    if orient == 'V':
        casillas = [(coord[0] + i,coord[1]) for i in range(d)]
        
    for cas in casillas:
        if mapa[cas[0]][cas[1]]:
            return False
    
    return True

def place_boat(mapa,coord,orient,d):
    if orient == 'H':
        for i in range(d):
            mapa[coord[0]][coord[1] + i] = d
            
    if orient == 'V':
        for i in range(d):
            mapa[coord[0] + i][coord[1]] = d


def assingDef():
    mapa = [[0 for _ in range(gz)] for _ in range(gr)]
    output = ""
    
    for i in range(4):
        for cant in range(b[i]):
 
            d = dim[i]
            coord = (random.randint(0, gz - d),random.randint(0, gz - d))
            orient = random.choice(['H','V'])
            
            while not check_boat_placement(mapa,coord,orient,d):
                
                coord = (random.randint(0, gz - d),random.randint(0, gz - d))
                orient = random.choice(['H','V'])
            
            output += str(coord[0]) + " " + str(coord[1]) + " " + orient + " "
            place_boat(mapa,coord,orient,d)
            
        output += "\n"       

    # print(output)
    print(output, flush = True)

assingDef()