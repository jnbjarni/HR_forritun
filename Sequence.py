n = int(input("Enter the length of the sequence: "))  # Do not change this line
counter = 0
const1 = 0
const2 = 1
const3 = 2
sum = 0
while counter < n:
    counter += 1
    sum = const1 + const2 + const3
    if counter == 1:
        print("1")
    elif counter == 2:
        print("2")
    else:
        print(sum)

        const1 = const2
        const2 = const3
        const3 = sum
