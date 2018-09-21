def recursion(num):
    newnum = num

    if newnum < 10:
        newnum = newnum + 2
        print(newnum)
        return recursion(newnum)

    else:
        print("your num is", newnum)
        return newnum


mynum = 1
recursion(mynum)
