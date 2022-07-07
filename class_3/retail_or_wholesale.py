# customer_type = input('Is this purchase retail or wholesale? > ')
# invoice_total = float(input("What is the invoice total? > "))
#
# if (customer_type == "wholesale") and (invoice_total >= 500):
#   print("You get a 50% discount")
# elif (customer_type == "wholesale") and (invoice_total < 500):
#   print("You get a 40% discount")
# else:
#   if (customer_type == "retail") and (invoice_total > 250):
#     print("You get a 20% discount")
#   elif (customer_type == "retail") and (invoice_total >= 100) and (invoice_total < 250):
#     print("You get a 10% discount")
#   else:
#     print("You get no discount")

import random

type_code = "W"
invoice_total = random.randint(0, 1000)
discount = 0.0

print(type_code)
print(invoice_total)

if type_code == "R":
  if invoice_total > 250:
    discount = 0.2
  elif (invoice_total >= 100) and (invoice_total < 250):
    discount = 0.1
  elif invoice_total < 100:
    discount = 0.0

if type_code == "W":
  if invoice_total >= 500:
    discount = 0.5
  elif invoice_total < 500:
    discount = 0.4

print(discount)
