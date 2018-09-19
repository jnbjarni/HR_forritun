upperMap = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowerMap = "qwertyuiopasdfghjklzxcvbnm"
charMap = "0123456789"
isNum = 0
isUpper = 0
isLower = 0
isPunct = 0
isSpace = 0
s = input("Enter a sentence: ")
for i, c in enumerate(s):
    if c in upperMap:
        isUpper += 1
    elif c in lowerMap:
        isLower += 1
    elif c in charMap:
        isNum += 1
    elif c == " ":
        isSpace += 1
    else:
        isPunct += 1
print('{:>15s}{:>5s}'.format("Upper case", str(isUpper)))
print('{:>15s}{:>5s}'.format("Lower case", str(isLower)))
print('{:>15s}{:>5s}'.format("Digits", str(isNum)))
print('{:>15s}{:>5s}'.format("Punctuation", str(isPunct)))
