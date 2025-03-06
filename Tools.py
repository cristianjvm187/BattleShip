import subprocess
import pprint


def Possible_def(defense, sizeOfBoard=10, numberOfShips={2: 1, 3: 2, 4: 1, 5: 1}):
    """
    defense = dict <int, list <tuple <int,int,str = {H, V}>>>
    """

    k = (sizeOfBoard // 10) ** 2
    for type in numberOfShips:
        numberOfShips[type] *= k

    zeros = [[0 for _ in range(sizeOfBoard)] for _ in range(sizeOfBoard)]  # rev
    board = [[0 for _ in range(sizeOfBoard)] for _ in range(sizeOfBoard)]
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
        return 10, zeros

    return 1, board


# print(Possible_def(0))


def Ejecutacion(lenguaje, name):
    obj = None
    if lenguaje == "cpp":
        obj = subprocess.Popen(
            [name],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    elif lenguaje == "python":
        obj = subprocess.Popen(
            ["python", name],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )
    return obj


def send_info_def(
    n_game, lastDefense, obj: subprocess.Popen, numberOfShips={2: 1, 3: 2, 4: 1, 5: 1}
):
    """
    El tipo de salida es sale n la cantidad de partidas jugadas
    luego vamos a ir partida por partida
    vamosa dar las de turno dimension del barco y la cantidad de ese tipo que hay
    siguimos iterando por la cantidad del barco j que hay en la partida j
    y damos la oritenacion , fila , columa
    """
    obj.stdin.write(str(n_game) + "\n")
    obj.stdin.flush()
    # print(n_game)

    for i in range(n_game):
        for type in lastDefense[i]:
            # aqui daba la dimension 1xk por el numero de barcos que hay de ese tipo
            # print(str(type) + " " + str(numberOfShips[type]))
            # obj.stdin.write(str(type) + " " + str(numberOfShips[type]) + "\n")
            # obj.stdin.flush()
            for k in range(numberOfShips[type]):
                # orientacion row column
                """
                print(
                    str(oldDefense[i][type][k][0])
                    + " "
                    + str(oldDefense[i][type][k][1])
                    + " "
                    + str(oldDefense[i][type][k][2])
                    + " ",
                    end=" ",
                )
                """
                obj.stdin.write(
                    str(lastDefense[i][type][k][0])
                    + " "
                    + str(lastDefense[i][type][k][1])
                    + " "
                    + str(lastDefense[i][type][k][2])
                    + " "
                )
            # obj.stdin.flush()
            # print("")
            obj.stdin.write("\n")
            obj.stdin.flush()


def send_info_atk(n_game, lastAtack, obj: subprocess.Popen):
    # obj.stdin.write(str(n_game) + "\n")
    # obj.stdin.flush()

    for i in range(n_game):
        # cantidad de tiros
        obj.stdin.write(str(len(lastAtack[i])) + " ")
        for j in range(len(lastAtack[i])):
            obj.stdin.write(
                str(lastAtack[i][j][0]) + " " + str(lastAtack[i][j][1]) + " "
            )
        obj.stdin.flush()
        obj.stdin.write("\n")
        obj.stdin.flush()


def get_pos_def(numberOfShips, obj: subprocess.Popen):
    Defensa = {}
    for type in numberOfShips:
        inp = obj.stdout.readline().strip().split()
        Defensa[type] = [
            (int(inp[i]), int(inp[i + 1]), inp[i + 2]) for i in range(0, len(inp), 3)
        ]

    return Defensa


def Battle(
    deflenguaje,
    atklenguaje,
    n_game,
    defplayer,
    atkplayer,
    lastDefense,
    lastAtack,
    numberOfShips,
    totalOfShips,
    sizeOfBoard,
):
    Def_current = None
    get_def = Ejecutacion(deflenguaje, defplayer)
    send_info_def(n_game, lastDefense, get_def, numberOfShips)
    send_info_atk(n_game, lastAtack, get_def)

    Def_current = get_pos_def(numberOfShips, get_def)
    pprint.pprint(Def_current)
    p, Def_current_matrix = Possible_def(Def_current)

    pprint.pprint(Def_current_matrix)
    # _______________________________________________________________________________
    posAtk = []
    if p == 1:
        get_atk = Ejecutacion(atklenguaje, atkplayer)
        send_info_def(n_game, lastDefense, get_atk, numberOfShips)
        send_info_atk(n_game, lastAtack, get_atk)
        c = 0
        # print("aassa")
        while True:
            intento = get_atk.stdout.readline().strip().split()
            # print(intento)
            if not intento:
                # print("Puas")
                break
            # print("tiro ", intento)
            i, j = int(intento[0]), int(intento[1])
            posAtk.append((i, j))
            # print(Def_current_matrix[i][j])
            # si dio a un barco
            if Def_current_matrix[i][j] == 1:
                c += 1
                # si le di a todos
                if c == totalOfShips:
                    get_atk.stdin.write("-1 \n")
                    get_atk.stdin.flush()
                    get_atk.stdin.close()
                    break  # Salir del bucle cuando acierte
                else:
                    get_atk.stdin.write("1 \n")
                    get_atk.stdin.flush()
            # si no dio
            else:
                get_atk.stdin.write("0\n")
                get_atk.stdin.flush()
            # print("puas")
    # print(posAtk)
    return len(posAtk), Def_current, posAtk


if __name__ == "__main__":
    exampledef = Ejecutacion("python", "Players/DefPilot.py")
    exampleatk = Ejecutacion("python", "Players/AtkPilot.py")
    Battle(
        "python",
        "python",
        2,
        "Players/DefPilot.py",
        "Players/AtkPilot.py",
        [
            {
                2: [(2, 6, "H")],
                3: [(6, 0, "H"), (3, 8, "V")],
                4: [(5, 4, "H")],
                5: [(9, 0, "H")],
            },
            {
                2: [(2, 6, "H")],
                3: [(6, 0, "H"), (3, 8, "V")],
                4: [(5, 4, "H")],
                5: [(9, 0, "H")],
            },
        ],
        [
            [(2, 3), (4, 5), (1, 1)],
            [(1, 1), (2, 2)],
        ],
        {2: 1, 3: 2, 4: 1, 5: 1},
        2 + 6 + 4 + 5,
        10,
    )
    # AtkPilot.player1()
