loan = float(input("Input the cost of the item in $: "))
intrest = float(0)
sumOfIntrest = float(0)
totalIntrest = float(0)
month = int(0)
payment = float(50.00)
if loan < 1000:
    intrest = 0.015
else:
    intrest = 0.02

while loan > 0:
    month += 1
    sumOfIntrest = loan * intrest
    totalIntrest = totalIntrest + sumOfIntrest
    if loan > 50:
        loan = loan - payment + sumOfIntrest
    else:
        payment = loan + sumOfIntrest
        loan = loan + sumOfIntrest - payment

    print("Month:", month, "Payment:", round(payment, 2), "Interest paid:",
          round(sumOfIntrest, 2), "Remaining debt:", round(loan, 2))

print("Number of months:", month)
print("Total interest paid:", round(totalIntrest, 2))
