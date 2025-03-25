"""
Este programa tiene como objetivo que el competidor pueda probar el correcto funcionamiento de su código
y su comunicacion con el Judge
"""

from Judge import Judge

# Aqui se almacenara la ruta de tu codigo de ataque(se muestra ahi es solo un ejemplo )
your_atk = "C:/Users/crist/OneDrive/Escritorio/BattleShip/Players/AtkPilot.py"
# Aqui se almacenara la ruta de tu codigo de defensa
your_def = "C:/Users/crist/OneDrive/Escritorio/BattleShip/Players/DefPilot.py"

# Aqui especifica tu lenguaje cpp o python
lenguaje = "python"


# Puedes modificar el tipo de agente al que te enfrentas
atk_rival = "C:/Users/crist/OneDrive/Escritorio/BattleShip/Players/AtkPilot.py"
def_rival = "C:/Users/crist/OneDrive/Escritorio/BattleShip/Players/DefPilot.py"
lenguaje_rival = "python"


# Aqui podras interactuar con el Judge
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

# Competir segun el estilo Copa
Test.CupMatch()
# Obtener la informacion de la cantidad emparejamientos ganados por tu jugador en el estilo copa
print(Test.win_player1)

# Competir segun el estilo Liga
Test.LeagueMatch()
# Obtener la informacion de puntos obtenidos al enfrentarse con el jugador de prueba
print(Test.points_player1)

from Tools import Possible_def

# Possible_def es una funcion que verifica si tu defensa esta correcta te puede ser util
