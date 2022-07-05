car_year = input("Enter the purchase year of your car > ")
current_year = input("Enter current year > ")

car_year = int(car_year)
current_year = int(current_year)

year = (current_year-car_year)
month = year * 12
days = year * 365


print("Your car is " + str(year) + " years old")
print("Your car is " + str(month) + " months old")
print("Your car is " + str(days) + " days old")
