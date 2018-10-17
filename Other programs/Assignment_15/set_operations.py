def printOptions():
    print("1. Intersection")
    print("2. Union")
    print("3. Difference")
    print("4. Quit")


def getSet(listi):
    newSet = set()
    for element in listi:
        newSet.add(int(element))
    print(newSet)
    return newSet


def Intersection(setA, setB):
    print(setA.intersection(setB))


def Union(setA, setB):
    print(setA.union(setB))


def Difference(setA, setB):
    print(setA.difference(setB))


def main():
    list1 = input(
        "Input a list of integers separated with a comma: ").split(",")
    list2 = input(
        "Input a list of integers separated with a comma: ").split(",")
    set_1 = getSet(list1)
    set_2 = getSet(list2)
    val = 0
    while val != 4:
        printOptions()
        val = int(input("Set operation: "))
        if val == 1:
            Intersection(set_1, set_2)
        elif val == 2:
            Union(set_1, set_2)
        elif val == 3:
            Difference(set_1, set_2)
        elif val == 4:
            break
        else:
            print("Invalid input!")


main()
