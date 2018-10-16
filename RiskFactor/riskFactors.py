# Erum strand, búnir að reyna fullt af mismunandi lausnum en finnum ekki hvernig við eigum að "matcha" gögnin saman.
# Við viljum prenta út töfluna en getum það ekki af því að við erum ekki að hugsa þetta rétt


def getFile():
    while True:
        filePath = input("Enter filename containing csv data: ")
        try:
            checkFile = open(filePath, "r")
            return checkFile
        except FileNotFoundError:
            print("Cannot find file", filePath)


def printHeader():
    header = '{:33s}{:21s}{:6s}{:15s}'
    header = header.format("Indicator", "Min", " ", "Max")
    headerLine = "-"
    headerLine = headerLine * 87
    print(header)
    print(headerLine)


def dataWork(file):
    allLines = []
    for line in file:
        myList = line.split(",")
        allLines.append(myList)

    return allLines


def sortData(listiAfListum):
    loopLength = len(listiAfListum[0])
    newList = []
    for i in range(loopLength):
        tempList = []
        for element in listiAfListum:
            tempList.append(element[i])
        newList.append(tempList)

    return newList


def calculateData(sortedList):
    states = sortedList[0]
    minValue = 0
    maxValue = 0
    for i, item in enumerate(sortedList):
        print(i, item)


def main():
    fileData = getFile()
    printHeader()
    originalList = dataWork(fileData)
    sortedList = sortData(originalList)
    calculatedList = calculateData(sortedList)


main()


# riskFactors.csv
