"""
Este programa tiene como objetivo que el competidor pueda probar el correcto funcionamiento de su código
y su comunicación con el Judge.
"""

"""
El uso de flush resulta muy importante para que la comunicación con el juez sea fluida y no existan errores
de que el juez se quede esperando.

En el caso de Python, tenemos 2 maneras:

1. import sys
    print(mensaje)
    sys.stdout.flush()

2. print(mensaje, flush=True)  # Recomendada

Por otro lado, en C++ podemos usar:

1. cout << mensaje << flush;  # Envía sin salto de línea
2. cout << mensaje << endl;  # Equivalente a cout << mensaje << "\n" << flush;

En nuestros códigos de ejemplo se muestra el uso de cada una.
"""

from Judge import Judge

# Aquí se almacenará la ruta de tu código de ataque (se muestra un ejemplo)
your_atk = "C:/Users/crist/OneDrive/Escritorio/BattleShip/Players/AtkPilot"
# Aquí se almacenará la ruta de tu código de defensa
your_def = "C:/Users/crist/OneDrive/Escritorio/BattleShip/Players/DefPilot"

# Especifica tu lenguaje: 'cpp' o 'python'
lenguaje = "cpp"

"""
En el caso de usar el lenguaje C++, primero compílalo y después pon la ruta como en el ejemplo:
"direccion/.../playerAtk" (importante notar que es sin la extensión .cpp).
En caso de querer poner la extensión, sería .exe.
"""

# Puedes modificar el tipo de agente al que te enfrentas
atk_rival = "C:/Users/crist/OneDrive/Escritorio/BattleShip/Players/AtkPilot.py"
def_rival = "C:/Users/crist/OneDrive/Escritorio/BattleShip/Players/DefPilot.py"
lenguaje_rival = "python"

"""
Cuando es Python, solo tenemos que poner la ruta del archivo .py (aquí sí es necesaria la extensión).
"""

# Aquí podrás interactuar con el Judge
Test = Judge(
    Atk_player1=your_atk,
    Atk_player2=atk_rival,
    Def_player1=your_def,
    Def_player2=def_rival,
    lenguaje_player1=lenguaje,
    lenguaje_player2=lenguaje_rival,
    cant_game=73,
    numberOfShips={2: 25, 3: 50, 4: 25, 5: 25},
    totalOfShips=4,
    sizeOfBoard=50,
)

# Competir según el estilo Copa
Test.CupMatch()
# Obtener la información de la cantidad de emparejamientos ganados por tu jugador en el estilo copa
print(Test.win_player1)

# Competir según el estilo Liga
Test.LeagueMatch()
# Obtener la información de puntos obtenidos al enfrentarse con el jugador de prueba
print(Test.points_player1)

from Tools import Possible_def, get_pos_def, Execute

# Possible_def es una función que verifica si tu defensa es correcta. Te puede ser útil.

"""
Si deseamos ver si nuestra defensa es correcta, el modo de proceder es el siguiente:

x = Possible_def(get_pos_def(Execute(lenguaje, ruta)))

Devuelve una tupla donde:
- El primer valor es 1 si es correcta y 0 si no.
- En el caso de ser correcta, el segundo valor es una matriz que representa el tablero,
  con 1 donde hay barcos y 0 donde no.
"""
