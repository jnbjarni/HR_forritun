import string
import operator
word_dict = {}


def getFile():
    while True:
        filePath = input("Enter name of file: ")
        try:
            checkFile = open(filePath, "r")
            return checkFile
        except FileNotFoundError:
            print("Cannot find file", filePath)


def readFile(aFile):
    wordList = []
    for lines in aFile:
        line = lines.split(" ")
        for words in line:
            words = words.lower()
            words = words.strip()
            words = words.strip(string.punctuation)
            wordList.append(words)

        length = len(wordList) - 1
        for x in range(length):
            if x == 1:
                x = x + 1
            elif x > 1:
                x = x + 2
            myList = []
            if length % 2 == 0:
                if x < length:
                    myList.append(wordList[x])
                    myList.append(wordList[x+1])
            else:
                if x < length:
                    myList.append(wordList[x])
                    myList.append(wordList[x+1])
                elif x == length:
                    myList.append(wordList[x])

            myTuple = tuple(myList)
            addWord(myTuple, word_dict)
            myList = []
            myTuple = ()


def addWord(aTuple, dictonary):
    if aTuple in dictonary:
        dictonary[aTuple] += 1
    else:
        dictonary[aTuple] = 1


def main():
    textfile = getFile()
    readFile(textfile)

    itemList = list(
        sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)[:10])

    print(itemList)


main()
