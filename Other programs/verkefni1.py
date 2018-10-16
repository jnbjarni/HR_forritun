
def get_list():
    a_list = input(
        "Enter elements of list separated by commas: ").strip().split(',')
    return a_list


def get_integer(prompt):
    val = int(input(prompt))
    return val


def transform(list1, list2, r1, r2):
    slicedList = list1[r1:r2]
    slicedList = slicedList[::-1]
    del list1[r1:r2]
    for element in slicedList:
        list2.append(element)



# Main program starts here - DO NOT change it
list1 = get_list()
list2 = get_list()
index1 = get_integer("Enter from value: ")
index2 = get_integer("Enter to value: ")
transform(list1, list2, index1, index2)
print(list1)
print(list2)
