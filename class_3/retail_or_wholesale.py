question1 = input('Is this purchase retail or wholesale? > ')
question2 = float(input("What is the invoice total? > "))

if (question1 == "wholesale") and (question2 >= 500):
  print("You get a 50% discount")
elif (question1 == "wholesale") and (question2 < 500):
  print("You get a 40% discount")
else:
  if (question1 == "retail") and (question2 > 250):
    print("You get a 20% discount")
  elif (question1 == "retail") and (question2 >= 100) and (question2 < 250):
    print("You get a 10% discount")
  else:
    print("You get no discount")

# a = "HELP".lower()
# print(a)
