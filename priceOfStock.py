# Github = https://github.com/jnbjarni/HR_forritun
shares = 0
price = ""
running = "y"


def getShares():
    while True:
        try:
            numOfShares = int(input("Enter number of shares: "))
            return numOfShares
        except ValueError:
            print("Invalid number!")


def getPrice():
    while True:
        priceOfShares = input(
            "Enter price (dollars, numerator, denominator): ")
        try:
            validPrice = priceOfShares.replace(" ", "")
            validPrice = int(validPrice)
            return priceOfShares.split(" ")
        except ValueError:
            print("Invalid price!")


def calculatePrice(unformattedPrice, numOfShares):
    dollars = int(unformattedPrice[0])
    numerator = int(unformattedPrice[1])
    denominator = float(unformattedPrice[2])
    fraction = float(numerator / denominator)
    finalPrice = float(dollars + fraction) * numOfShares
    finalPrice = '{:.2f}'.format(finalPrice)
    return finalPrice


def printOutcome(numShares, originalPrice, calcPrice):
    numShares = str(numShares)
    formattedOrginalPrice = str(
        originalPrice[0] + " " + originalPrice[1] + "/" + originalPrice[2])

    roundedPrice = str(calculatedPrice)
    outcome = numShares + " shares with market price " + \
        formattedOrginalPrice + " have value $" + roundedPrice
    print(outcome)


while running == "y":
    shares = getShares()
    price = getPrice()
    calculatedPrice = calculatePrice(price, shares)
    printOutcome(shares, price, calculatedPrice)
    running = input("Continue: ")
