my_int = int(input('Give me an int >= 0: '))
bstr = ""
new_num = my_int
while new_num >= 1:
    if (new_num % 2) == 0:
        bstr += "0"
    elif (new_num % 2) == 1:
        bstr += "1"
    new_num = new_num // 2

if my_int == 0:
    bstr = "0"
elif my_int == 1:
    bstr == "1"

bstr = bstr[::-1]
print("The binary of", my_int, "is", bstr)
