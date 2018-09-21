row = 1
counter = 1
sum = 0
output = ""
while row < 11:
    sum = row * counter
    output = output + '{:>5}'.format(str(sum))
    counter += 1
    if counter == 11:
        print(output)
        output = ""
        counter = 1
        row += 1
