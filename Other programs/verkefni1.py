# Each ticket cost $30. Senior citizens (age >= 65) are given a 50% discount. Children under (or equal to) the age of 5 get a free admission.
# Write a program that prompts for the visitor's age and computes the ticket price (which should be a float).

age = int(input("Input age: "))  # Do not change this line
price = 0

if age >= 60:
    price = float(30 / 2)
    print(price)
elif age < 6:
    price = 0.0
    print(price)
else:
    price = 30.0
    print(price)
