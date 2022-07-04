caryear = input("Enter the year of your car > ")
currentyear = input("Enter current year > ")

curryear = (int(currentyear)-int(caryear))
currmonth = (int(currentyear)-int(caryear)) * 12
currdays = (int(currentyear)-int(caryear)) * 365


print("Your car is " + str(curryear) + " years old")
print("Your car is " + str(currmonth) + " months old")
print("Your car is " + str(currdays) + " days old")
