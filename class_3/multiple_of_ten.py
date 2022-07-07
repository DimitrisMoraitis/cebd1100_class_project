# value = int(input("Pick an integer > "))
#
# calculation = value % 10
#
# if calculation == 0:
#   print("Your number is a multiple of ten!")
# else:
#   print("Your number is not a multiple of ten!")

value = int(input("Pick an integer, greater than zero, > "))

if value > 0:
  calculation = value % 10
  if calculation == 0:
    print("Your number is a multiple of ten!")
  else:
    print("Your number is not a multiple of ten!")

else:
  print("Your integer was not greater than zero!")
