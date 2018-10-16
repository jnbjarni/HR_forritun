# Bið notanda um stærð af borði
def getBoardSize():
    while True:
        size = int(input("Input dimension of the board: "))
        if size < 3:
            print("Invalid input!")
        else:
            return size


# Bý til lista af listum af stærð x frá notanda
def createBoard(gridSize):
    pos = 0
    grid = [[0] * gridSize for r in range(gridSize)]
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            pos += 1
            grid[i][j] = str(pos)

    return grid


# Fall til þess að prenta úr board-ið
def printBoard(grid):
    for row in grid:
        rowString = '{:>5} ' * len(grid)
        rowString = rowString.format(*row)
        print(rowString)


# Fall sem tekur inn boardið og spilarann sem á að gera (ekki tilbúið)
def makeTurn(board, player):
    # Hér þarf að láta notandann velja stak í listanum og leyfa honum að breyta því
    # Ef það er ekki með gildið X eða O
    length = len(board) * len(board)
    while True:
        pos = 0
        try:
            userInput = input('{} {} '.format(player, "position:"))
            if int(userInput) > length:
                print("Illegal move!")
            elif int(userInput) < 1:
                print("Input to small")
            else:
                for i, row in enumerate(board):
                    for j, item in enumerate(row):
                        pos += 1
                        if int(userInput) == pos:
                            if board[i][j] == "X" or board[i][j] == "O":
                                print("Illegal move!")
                                break
                            else:
                                board[i][j] = player
                                return board
        except ValueError:
            print("Invalid input")


def checkIfGameIsWon(board, player):
    # Hér þarf að tékka hvort spilari sé búinn að merka sömu index stök í öllum listum
    # Þarf líka að tjékka hvort hann sé búinn að merkja stök i + 1 (stak0, stak1, stak2)
    # Það þarf líka að tékka á stak - 1 (stak2, stak1, stak 0)

    # Byrja athuga hvort spilari sé búinn að ná heilli röð lárétt
    #   j  j  j
    # i[x, x, x]
    # i[2, 2, 3]
    # i[3, 2, 3]
    for row in board:
        if len(set(row)) == 1:
            printBoard(board)
            print("Winner is:", player)
            return True

    # Athuga svo hvort hann sé búinn að vinna lárétt
    #   j  j  j
    # i[x, 2, 3]
    # i[x, 2, 3]
    # i[x, 2, 3]
    lengthOfLists = len(board)
    for x in range(lengthOfLists):
        horizontalList = [item[x] for item in board]
        if len(set(horizontalList)) == 1:
            printBoard(board)
            print("Winner is:", player)
            return True
        else:
            horizontalList = []

    # Athuga svo hvort player sé búinn að vinna á ská niður til hægri
    #   j  j  j
    # i[x, 2, 3]
    # i[1, x, 3]
    # i[1, 2, x]
    diagonalList = []
    for x in range(lengthOfLists):
        if x == 0:
            diagonalList.append(board[0][0])
        else:
            diagonalList.append(board[x][x])

    # Athuga svo síðast hvort player sé búinn að vinna á ská frá hægri til vinstri
    #   j  j  j
    # i[1, 2, x]
    # i[1, x, 3]
    # i[x, 2, 3]
    diagonalList2 = []
    minusCounter = -1
    for x in range(lengthOfLists):
        if x == 0:
            diagonalList2.append(board[0][minusCounter])
        else:
            diagonalList2.append(board[x][minusCounter - 1])
            minusCounter = minusCounter - 1

    if len(set(diagonalList)) == 1 or len(set(diagonalList2)) == 1:
        printBoard(board)
        print("Winner is:", player)
        return True

    return False


def main():
    # Global breytur skilgreindar.
    playerX = "X"
    playerO = "O"
    turns = 0
    victory = False
    # Initialize functions köll, keyrir föllin sem eru notuð áður en leikurinn er spilaður
    boardSize = getBoardSize()
    board = createBoard(boardSize)
    totalPossibleMoves = len(board) * len(board)

    # Hér byrja notendur að spila leikinn, skiptast á að gera.
    while victory == False:
        if turns == 0:
            printBoard(board)
            board = makeTurn(board, playerX)
            turns += 1
        if turns == 1:
            printBoard(board)
            board = makeTurn(board, playerO)
            turns += 1

        elif turns % 2 == 0:
            printBoard(board)
            board = makeTurn(board, playerX)
            victory = checkIfGameIsWon(board, playerX)
            turns += 1
        else:
            printBoard(board)
            board = makeTurn(board, playerO)
            victory = checkIfGameIsWon(board, playerO)
            turns += 1

        if turns == totalPossibleMoves:
            printBoard(board)
            print("Draw!")
            victory = True


main()
