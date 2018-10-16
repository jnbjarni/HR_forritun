# Main program starts here


def createList(stringOfItems):
    newList = stringOfItems.split(",")

    return newList


def make_sublist(listi):
    myList = []
    while len(listi) != 0:
        lenOfList = len(listi)
        for i, items in enumerate(listi):
            if not listi[0:i] in myList:
                myList.append(listi[0:i])

            if i + 1 == lenOfList:
                myList.append(listi[0:i+1])
                listi.pop(0)
    return myList


# This should be the last statement in your main program/function
originalInput = input("Enter a list separated with commas: ")
firstList = createList(originalInput)
sub_lists = make_sublist(firstList)
print(sorted(sub_lists))
