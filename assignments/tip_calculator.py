# constants - sales tax rates
FEDERAL_TAX = 0.05
PROVINCIAL_TAX = 0.10

# constants - tip percentage
EXCEPTIONAL = 20
GOOD = 15
BASIC = 10
HORRIBLE = 0

# inputs
diners = input("Number of diners sharing the meal cost? > ")
meal_price = input("What was the price of the meal, before tax? > ")
tax_tip = input("What tip would you like to apply?\n"
f"1) Exceptional ({EXCEPTIONAL}%), 2) Good ({GOOD}%), 3) Basic ({BASIC}%), or 4) Horrible ({HORRIBLE}%) > ")

while True:                         # request to select between 1 and 4
    tax_tip = int(tax_tip)
    if tax_tip in range(1, 5):
        break
    else:
        tax_tip = input("Try again. Choose between 1 to 4\nWhat tip would you like to apply?\n"
        f"1) Exceptional ({EXCEPTIONAL}%), 2) Good ({GOOD}%), 3) Basic ({BASIC}%), or 4) Horrible ({HORRIBLE}%) > ")

diners = int(diners)
meal_price = int(meal_price)
tax_tip = int(tax_tip)

meal_fed = (meal_price * FEDERAL_TAX)
meal_pro = (meal_price * PROVINCIAL_TAX)
subtotal_meal = (meal_price + meal_fed + meal_pro)

meal_tip = 0                     # calculating tip on meal price
if tax_tip == 1:
    meal_tip = meal_price * (EXCEPTIONAL / 100)
if tax_tip == 2:
    meal_tip = meal_price * (GOOD / 100)
if tax_tip == 3:
    meal_tip = meal_price * (BASIC / 100)
if tax_tip == 4:
    meal_tip = meal_price * (HORRIBLE / 100)

total_meal = subtotal_meal + meal_tip

indie_amount = total_meal / diners

print()                                 # extra space
print("*****************************\nThe calculation results are:\n*****************************")
print(f"The number of diners are {diners}")
print(f"The price of the meal before tax is ${meal_price:.2f}")
print(f"The federal sales tax applied is ${meal_fed:.2f}")
print(f"The provincial sales tax applied is ${meal_pro:.2f}")
print(f"The total amount with tax is ${subtotal_meal:.2f}")
print(f"The tip amount is ${meal_tip:.2f}")
print(f"The grand total ${total_meal:.2f}")
print(f"The amount per person is ${indie_amount:.2f}")
