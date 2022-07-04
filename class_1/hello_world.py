# using assigned variable
name = "Dimitris"

print('This is ' + name)
print("What about " + name + "?")

# using function
for x in range(5):
    print(x)

# using decimal
from decimal import Decimal
print(10+11)
print(0.21*0.06)
print(Decimal("0.21") * Decimal('0.06'))

exit()

# identifying type
print(type(name))
print(type(15))
print(isinstance(name, int))
print(isinstance(name, str))
print(isinstance(15, int))
