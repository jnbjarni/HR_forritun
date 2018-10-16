def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


def getNumList():
    numInput = input("Enter integers separated with commas: ")

    try:
        numberList = numInput.split(",")
        for number in numberList:
            number = int(number)

        return numberList
    except ValueError:
        print("Incorrect input!")


def sort_list(listi):
    listi.sort()
    return listi


def calculations(listi):
    total = 0
    average = 0
    for number in listi:
        total = total + int(number)

    average = float(total / len(listi))
    averageOutput = '{:.2f}'.format(average)

    minOutput = "Min: " + str(min(listi)) + ","
    maxOutput = "Max: " + str(max(listi)) + ","
    output = minOutput + " " + maxOutput + " Average: " + averageOutput
    print(output)


# The main program starts here
def main():
    L = getNumList()

    intList = []
    for number in L:
        intList.append(int(number))

    primeList = []
    for number in intList:
        if is_prime(number):
            if not number in primeList:
                primeList.append(number)

    print("Input list:", intList)
    print("Sorted list:", sort_list(intList))
    print("Prime list: ", sort_list(primeList))
    calculations(intList)


main()
