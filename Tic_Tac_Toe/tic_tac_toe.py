# Bið notanda um stærð af borði


def getBoardSize():
    while True:
        size = int(input("Enter boardsize: "))
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
            grid[i][j] = pos

    return grid


# Fall til þess að prenta úr board-ið
def printBoard(grid):
    for i, row in enumerate(grid):
        rowString = '{:>5d}' * len(grid)
        rowString = rowString.format(*row)
        print(rowString)


# Fall sem tekur inn boardið og spilarann sem á að gera (ekki tilbúið)
def makeTurn(board, player):
    # Hér þarf að láta notandann velja stak í listanum og leyfa honum að breyta því
    # Ef það er ekki með gildið X eða O
    return True


def checkIfGameIsWon(isVictory):
    # Hér þarf að tékka hvort spilari sé búinn að merka sömu index stök í öllum listum
    # Þarf líka að tjékka hvort hann sé búinn að merkja stök i + 1 (stak0, stak1, stak2)
    # Það þarf líka að tékka á stak - 1 (stak2, stak1, stak 0)
    return False


# Main fallið mitt sem keyrir leikinn þangað til að vitctory breytan er orðinn True
def main():
    # Global breytur skilgreindar.
    playerX = "X"
    playerO = "O"
    turns = 0
    victory = False
    # Initialize functions köll, keyrir föllin sem eru notuð áður en leikurinn er spilaður
    if turns == 0:
        boardSize = getBoardSize()
        board = createBoard(boardSize)
        printBoard(board)

    while victory == False:
        turns += 1

        if turns == 1:
            makeTurn(board, playerX)
        if turns == 2:
            makeTurn(board, playerO)
        elif turns % 2 == 1:
            makeTurn(board, playerX)
            checkIfGameIsWon(victory, playerX)
        else:
            makeTurn(board, playerO)
            checkIfGameIsWon(victory, playerO)


main()
