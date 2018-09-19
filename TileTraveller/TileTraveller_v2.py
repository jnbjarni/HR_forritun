# Github = https://github.com/jnbjarni/HR_forritun
#
# Question 1: It was easier to implement the version with the functions, because I knew what I had to do make the program work.
#
# Question 2: This code below is way more readable and debuggable because, the code is now sorted in functions and not just one big while loop with many if statements.
#
# Question 3: Did not run in to alot of trouble coding both versions, but while I was implementingnthe code below I ran into one problem.
# That problem is you cannot return multiple values from function so I solved the problem by returning them both together and then selecting the values from my coordinates variable (line 66 to 68).


victory = False
posX = 1
posY = 1
direction = ""
possibleMoves = ""
coordinates = ""


def getPossibleMoves(x, y, moves):
    if x == 1 and y == 1 or x == 2 and y == 1:
        print("You can travel: (N)orth.")
        moves = "Nn"
    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        moves = "NnEeSs"
    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
        moves = "EeSs"
    elif x == 2 and y == 2 or x == 3 and y == 3:
        print("You can travel: (S)outh or (W)est.")
        moves = "WwSs"
    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
        moves = "EeWw"
    elif x == 3 and y == 1:
        return moves
    else:
        print("You can travel: (N)orth or (S)outh.")
        moves = "NnSs"

    return moves


def checkIfMoveIsValid(x, y, pmoves):
    validMove = False
    while validMove == False:
        direction = input("Direction: ").lower()
        if direction in pmoves:
            if direction == "n":
                y = y + 1
            elif direction == "e":
                x = x + 1
            elif direction == "s":
                y = y - 1
            else:
                x = x - 1
            validMove = True
        else:
            print("Not a valid direction!")

    return x, " ", y


while victory == False:
    possibleMoves = getPossibleMoves(posX, posY, possibleMoves)
    coordinates = checkIfMoveIsValid(posX, posY, possibleMoves)
    posX = coordinates[0]
    posY = coordinates[2]

    if posX == 3 and posY == 1:
        victory = True
print("Victory!")
