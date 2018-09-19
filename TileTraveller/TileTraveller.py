# The program will have a main game loop that has an if and else statement
# for each "tile" in the game, that will check what moves will be possible.
# Then the user gets to choose which direction he wants to go to until he
# finally reaches the victory tile. I dont like this solution at all because
# of all of the if statements that I use to implement the functionality.

victory = False
posX = 1
posY = 1
direction = ""
possibleMoves = ""
while victory == False:
    validMove = False
    if posX == 1 and posY == 1 or posX == 2 and posY == 1:
        print("You can travel: (N)orth.")
        possibleMoves = "Nn"
    elif posX == 1 and posY == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        possibleMoves = "NnEeSs"
    elif posX == 1 and posY == 3:
        print("You can travel: (E)ast or (S)outh.")
        possibleMoves = "EeSs"
    elif posX == 2 and posY == 2 or posX == 3 and posY == 3:
        print("You can travel: (W)est or (S)outh.")
        possibleMoves = "WwSs"
    elif posX == 2 and posY == 3:
        print("You can travel: (E)ast or (W)est.")
        possibleMoves = "EeWw"
    elif posX == 3 and posY == 1:
        victory = True
        break
    else:
        print("You can travel: (N)orth or (S)outh.")
        possibleMoves = "NnSs"

    while validMove == False:
        direction = input("Direction: ").lower()

        if direction in possibleMoves:
            if direction == "n":
                posY = posY + 1
            elif direction == "e":
                posX = posX + 1
            elif direction == "s":
                posY = posY - 1
            else:
                posX = posX - 1
            validMove = True
        else:
            print("Not a valid direction!")
print("Victory")
