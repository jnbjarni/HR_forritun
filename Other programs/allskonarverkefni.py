def mod(num1, num2):
    sum = int(num1) % int(num2)
    print(sum)


while True:
    num = input().split(",")
    mod(num[0], num[1])
