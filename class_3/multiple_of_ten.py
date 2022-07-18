# option 1
# value = int(input("Pick an integer > "))
#
# calculation = value % 10
#
# if calculation == 0:
#   print("Your number is a multiple of ten!")
# else:
#   print("Your number is not a multiple of ten!")

# option 2 (which eliminates less than zero numbers)
# value = int(input("Pick an integer, greater than zero, > "))
#
# if value > 0:
#   calculation = value % 10
#   if calculation == 0:
#     print("Your number is a multiple of ten!")
#   else:
#     print("Your number is not a multiple of ten!")
#
# else:
#   print("Your integer was not greater than zero!")

# option 3
number = int(input("Enter an integer greater than zero > "))

if number > 0:
  if number % 10 == 0:
    print("This is a multiple of ten")
  else:
    print("This is not a multiple of ten")
else:
  print("Your integer must be greater than zero")
