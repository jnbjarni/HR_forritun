# Function definitions start here
def open_file(file_path):
    try:
        checkFile = open(file_path, "r")
        return checkFile
    except FileNotFoundError:
        return False


def get_longest_word(file):
    myList = []
    for line in file:
        line.split()
        if "\n" in line:
            newItem = line[0:-1]
            myList.append(newItem)
        else:
            myList.append(line)

    wordLength1 = 0
    wordLength2 = 0
    longWord = ""
    for item in myList:
        wordLength1 = len(item)
        if wordLength1 > wordLength2:
            wordLength2 = wordLength1
            longWord = item

    return longWord


# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
    longest_word = get_longest_word(file_stream)
    print("Longest word is '{:s}' of length {:d}".format(
        longest_word, len(longest_word)))
    file_stream.close()
else:
    print('File', filename, 'not found!')
