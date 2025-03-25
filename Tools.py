import subprocess
import pprint
import time

# variable de prueba
Ns = {2: 25, 3: 50, 4: 25, 5: 25}
Sb = 50


def Possible_def(defense, sizeOfBoard=Sb, numberOfShips=Ns):
    """
    Validates the placement of ships on a Battleship board.
    Parameters:
    defense (dict): A dictionary where keys are ship lengths (int) and values are lists of tuples. sEach tuple contains the row (int), column (int), and position ('H' for horizontal, 'V' for vertical).
    sizeOfBoard (int, optional): The size of the Battleship board. Default is 10.
    numberOfShips (dict, optional): A dictionary where keys are ship lengths (int) and values are the number of ships of that length. Default is {2: 1, 3: 2, 4: 1, 5: 1}.
    Returns:
    tuple: A tuple containing:
        - int: 1 if the ship placements are valid, 0 otherwise.
        - list: A 2D list representing the board with ships placed (1 for ship, 0 for empty).
    """

    zeros = [[0 for _ in range(sizeOfBoard)] for _ in range(sizeOfBoard)]  # rev
    board = [[0 for _ in range(sizeOfBoard)] for _ in range(sizeOfBoard)]

    if defense == None:
        return 0, zeros

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
        print(numberOfOnes, sum([numberOfShips[type] * type for type in numberOfShips]))
        return 0, zeros

    return 1, board


# print(Possible_def(0))


def Execute(lenguaje, name):
    """
    Executes a file in the specified language.

    Args:
        lenguaje (str): The programming language of the file to execute. Can be "cpp" or "python".
        name (str): The name of the file to execute.

    Returns:
        subprocess.Popen: A Popen object representing the running process.
    """
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


def send_info_def(n_game, lastDefense, obj: subprocess.Popen, numberOfShips=Ns):
    """
    Sends game information to a subprocess via its stdin.
    Parameters:
    n_game (int): The number of games played.
    lastDefense (list): A list containing the defense setup for each game.
    obj (subprocess.Popen): The subprocess object to which the information is sent.
    numberOfShips (dict, optional): A dictionary specifying the number of ships of each type.
                                    Defaults to {2: 1, 3: 2, 4: 1, 5: 1}.
    The function writes the number of games to the subprocess stdin, followed by the defense
    setup for each game. For each game, it iterates over the types of ships and writes the
    orientation, row, and column for each ship to the subprocess stdin.

    El tipo de salida es sale n la cantidad de partidas jugadas
    luego vamos a ir partida por partida
    vamosa dar las de turno dimension del barco y la cantidad de ese tipo que hay
    siguimos iterando por la cantidad del barco j que hay en la partida j
    y damos la oritenacion , fila , columa
    """

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
    get_def = Execute(deflenguaje, defplayer)
    get_def.stdin.write(str(n_game) + "\n")
    get_def.stdin.flush()
    send_info_def(n_game, lastDefense, get_def, numberOfShips)
    send_info_atk(n_game, lastAtack, get_def)

    start_time = time.time()
    Def_current = get_pos_def(numberOfShips, get_def)
    if (time.time() - start_time) >= 5:
        Def_current = None

    get_def.kill()
    get_def.stdin.close()
    get_def.stdout.close()
    get_def.stderr.close()

    # pprint.pprint(Def_current)
    p, Def_current_matrix = Possible_def(Def_current)

    # pprint.pprint(Def_current_matrix)
    # _______________________________________________________________________________
    posAtk = []
    num_shot = 0
    if p == 1:
        get_atk = Execute(atklenguaje, atkplayer)
        get_atk.stdin.write(str(n_game) + "\n")
        get_atk.stdin.flush()
        send_info_def(n_game, lastDefense, get_atk, numberOfShips)
        send_info_atk(n_game, lastAtack, get_atk)
        c = 0
        # print("aassa")
        start_time = time.time()
        while num_shot < sizeOfBoard**2 + 10:
            if (time.time() - start_time) >= 1:
                num_shot = 2510
                break
            intento = get_atk.stdout.readline().strip().split()
            num_shot += 1
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
                    # get_atk.stdin.close()
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
        get_atk.kill()
        get_atk.stdin.close()
        get_atk.stdout.close()
        get_atk.stderr.close()
    return num_shot, Def_current, posAtk


if __name__ == "__main__":
    exampledef = Execute("python", "Players/DefPilot.py")
    """
    exampleatk = Execute("python", "Players/AtkPilot.py")
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
    """
    send_info_def(0, [], exampledef, numberOfShips=Ns),
    send_info_atk(0, [], exampledef)
    M = get_pos_def(Ns, exampledef)
    print(Possible_def(M)[1])
    # AtkPilot.player1()
