# first = "Jimmy"
# last = "Wood"
# age = 30
# age = age + 2
#
# greeting1 = "Hello " + first + " " + last + ", you are " + str(age) + " years old."
# greeting2 = "Hello {} {}, you are {} years old.".format(first, last, age)
# greeting3 = f"Hello {first} {last}, you are {age} years old"
#
# print(greeting1)
# print(greeting2)
# print(greeting3)

first = input("What is your first name? > ")
last = input("What is your last name? > ")
age = input("What is your age? > ")
age1 = 100 - int(age)

prediction = f"Hello {first} {last}, you have {age1} more years to live!"

print(prediction)
