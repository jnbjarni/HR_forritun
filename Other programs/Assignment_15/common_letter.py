def getCommonLetters(firstname, lastname):
    commonLetters = []

    for letter in firstname:
        if letter in lastname and letter not in commonLetters:
            commonLetters.append(letter)

    return commonLetters


def getCommonLettersAsSet(firstName, lastName):
    firstNameSet = set(firstName)
    lastNameSet = set(lastName)
    commonLetters = firstNameSet.intersection(lastNameSet)
    return commonLetters


def main():
    name = input("Enter name: ").lower()
    firstName, lastName = name.split(" ")

    commonLetters = getCommonLetters(firstName, lastName)
    commonLettersSet = list(getCommonLettersAsSet(firstName, lastName))

    print(sorted(commonLetters))
    print(sorted(commonLettersSet))


main()
