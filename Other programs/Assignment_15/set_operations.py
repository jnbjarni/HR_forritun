def printOptions():
    print("1. Intersection")
    print("2. Union")
    print("3. Diffrence")
    print("4. Quit")


def Intersection(setA, setB):
    newSet = set(sorted(setA.intersection(setB)))
    print(newSet)


def Union(setA, setB):
    newSet = set(sorted(setA.union(setB)))
    print(newSet)


def Diffrence(setA, setB):
    newSet = set(sorted(setA.diffrence(setB)))
    print(newSet)


def main():
    list1 = input(
        "Input a list of integers separated with a comma: ").split(",")
    list2 = input(
        "Input a list of integers separated with a comma: ").split(",")
    set1 = set(sorted(list1))
    set2 = set(sorted(list2))
    print(set1)
    val = 0
    while val != 4:
        printOptions()
        val = int(input("Set operation: "))
        if val == 1:
            Intersection(set1, set2)
        elif val == 2:
            Union(set1, set2)
        elif val == 3:
            Diffrence(set1, set2)
        elif val == 4:
            break
        else:
            print("Invalid input!")


main()
