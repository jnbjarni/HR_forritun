# game_of_eights() function goes here
def game_of_eights(listi):
    for i, element in enumerate(listi):
        length = len(listi)
        if element == "8" and (length - 1) != i:
            if listi[i + 1] != "8":
                print("False")
                return False
            else:
                print("True")
                return True
        elif i == (length - 1):
            print("False")


def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    # remainder of main() goes here
    try:
        for element in a_list:
            num = int(element)
        game_of_eights(a_list)
    except ValueError:
        print("Error. Please enter only integers.")


main()
