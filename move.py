START = 1
END = 10


def moveLeft(pos):

    if pos == START:
        print("New position is:", pos)
    else:
        pos = pos - 1
        print("New position is:", pos)
    return pos


def moveRight(pos):

    if pos == END:
        print("New position is:", pos)
    else:
        pos = pos + 1
        print("New position is:", pos)

    return pos


position = int(input("Input a position between 1 and 10: "))
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")
direction = input("Input your choice: ")

while direction == "r" or direction == "l":
    if direction == "r":
        position = moveRight(position)
    else:
        position = moveLeft(position)

    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    direction = input("Input your choice: ")

if direction != "r" or direction != "l":
    print("New position is:", position)
