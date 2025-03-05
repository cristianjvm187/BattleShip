import subprocess
import time
from Tools import *


inicio = time.time()  # Guarda el tiempo de inicio


class Judge:
    def __init__(
        self,
        Atk_player1,
        Atk_player2,
        Def_player1,
        Def_player2,
        lenguaje_player1,
        lenguaje_player2,
        cant_game,
        epsilon,
        numberOfShips,
        totalOfShips,
        sizeOfBoard,
    ):
        self.num_game = 0
        self.cant_game = cant_game
        self.epsilon = epsilon
        self.Atk_player1 = Atk_player1
        self.Atk_player2 = Atk_player2
        self.Def_player1 = Def_player1
        self.Def_player2 = Def_player2
        self.pos_def_player1 = []
        self.pos_def_player2 = []
        self.pos_ataq_player1 = []
        self.pos_ataq_player2 = []
        self.win_player1 = 0
        self.win_player2 = 0
        self.sizeOfBoard = sizeOfBoard
        self.lenguaje1 = lenguaje_player1
        self.lenguaje2 = lenguaje_player2
        self.numberOfShips = numberOfShips
        self.totalOfShips = totalOfShips

    def _inc_game(self):
        self.num_game += 1

    def Match(self):
        while self.win_player1 + self.win_player2 <= self.cant_game:
            self.Game()

    def Game(self):
        Infop1 = Battle(
            self.lenguaje2,
            self.lenguaje1,
            self.num_game,
            self.Def_player2,
            self.Atk_player1,
            self.pos_def_player2,
            self.pos_ataq_player1,
            self.numberOfShips,
            self.totalOfShips,
            self.sizeOfBoard,
        )
        Infop2 = Battle(
            self.lenguaje1,
            self.lenguaje2,
            self.num_game,
            self.Def_player1,
            self.Atk_player2,
            self.pos_def_player1,
            self.pos_ataq_player2,
            self.numberOfShips,
            self.totalOfShips,
            self.sizeOfBoard,
        )

        p1 = Infop1[0]
        p2 = Infop2[0]

        if p1 == p2:
            self.win_player1 += 1
            self.win_player2 += 1
        elif p1 < p2:
            self.win_player1 += 1
        else:
            self.win_player2 += 1

        if p1 != 0 and p2 != 0:
            self.pos_ataq_player1.append(Infop1[2])
            self.pos_def_player2.append(Infop1[1])
            self.pos_ataq_player2.append(Infop2[2])
            self.pos_def_player1.append(Infop2[1])
            self._inc_game()


"""
compilacion = subprocess.run(
    [
        "g++",
        "C:/Users/crist/OneDrive/Escritorio/BattleAlgorithms/BattleShip/Experimentacion/Defpilot.cpp",
        "-o",
        "C:/Users/crist/OneDrive/Escritorio/BattleAlgorithms/BattleShip/Experimentacion/Defpilot",
    ],
    capture_output=True,
    text=True,
)


compilacion = subprocess.run(
    [
        "g++",
        "C:/Users/crist/OneDrive/Escritorio/BattleAlgorithms/BattleShip/Experimentacion/Defpilot2.cpp",
        "-o",
        "C:/Users/crist/OneDrive/Escritorio/BattleAlgorithms/BattleShip/Experimentacion/Defpilot2",
    ],
    capture_output=True,
    text=True,
)

"""

Juez = Judge(
    "C:/Users/crist/OneDrive/Escritorio/BattleAlgorithms/BattleShip/Experimentacion/Atkpilot.py",
    "C:/Users/crist/OneDrive/Escritorio/BattleAlgorithms/BattleShip/Experimentacion/Atkpilot.py",
    "C:/Users/crist/OneDrive/Escritorio/BattleAlgorithms/BattleShip/Experimentacion/Defpilot",
    "C:/Users/crist/OneDrive/Escritorio/BattleAlgorithms/BattleShip/Experimentacion/Defpilot2",
    50,
    2,
    3,
)

Juez.Match()
print(Juez.win_player1, Juez.win_player2)

fin = time.time()  # Guarda el tiempo de finalización

print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
