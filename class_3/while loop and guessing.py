# message = ""
# while message != "quit":
#   message = input("type 'continue' or 'quit' > ")
#   print(message)

## break in while loop
# x = 1
# while x < 15:
#   print(x)
#   if x == 8:
#     break
#   x += 1

## continue in while loop
x = 1
while x < 15:
    x += 1
    if x == 10:
        continue
    print(x)

# message = ""
# while message != "q".lower():
#
#     guess = input("Enter your number > ")
#     guess = int(guess)
#     if guess % 10 == 0:
#         print("Your number is a multiple of ten")
#     else:
#         print("Your number is not a multiple of ten")
#
#     message = input("Enter 'q' to exit or press enter to continue > ").lower()
# print = message

# counter = 1
# while counter <= 10:
#     print("Hello " + str(counter))
#     counter += 1
#
# for counter in range(10):
#     print("Greetings " + str(counter+1))

# # adding two numbers over and over
# response = "y"
#
# while response.lower() == "y":
#     a = int(input("Enter your first number > "))
#     b = int(input("Enter your second number > "))
#     print(f"The sum of the two numbers is {(a+b)}")
#
#     response = input("Would you like to continue? Y or N > ").lower()
# print = response
