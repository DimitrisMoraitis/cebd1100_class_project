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
# x = 0
# while x < 15:
#     x += 1
#     if x == 8:
#         continue
#     print(x)

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

## two while loops interacting

# i = 0
# j = 0
# while i <= 5:
#     while j <= 5:
#         prod = i * j
#         print(f"{i} times {j} is equal to {prod}")
#         j += 1
#     j = 0
#     i += 1

# using a break to exit a loop

# while True:
#
#     guess = input("Enter your number > ")
#     guess = int(guess)
#     if guess % 10 == 0:
#         print("Your number is a multiple of ten")
#     else:
#         print("Your number is not a multiple of ten")
#
#     message = input("Continue ? Y or N ").lower()
#     if message == "N".lower() or message == "No".lower():
#         break

# using a list to break a loop
answer_list = ["No".lower(), "N".lower()]

while True:
    guess = input("Enter your number > ")
    guess = int(guess)
    if guess % 10 == 0:
        print("Your number is a multiple of ten")
    else:
        print("Your number is not a multiple of ten")

    message = input("Continue ? Y or N ").lower()
    if message in answer_list:
        break