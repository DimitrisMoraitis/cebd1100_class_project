# message = ""
# while message != "quit":
#   message = input("type 'continue' or 'quit' > ")
#   print(message)
#
# x = 1
# while x < 15:
#   print(x)
#   if x == 10:
#     break
#   x += 1

# x = 1
# while x < 15:
#     x += 1
#     if x == 10:
#         continue
#     print(x)

message = ""
while message != 'q':

    guess = input("Enter your number > ")
    guess = int(guess)
    if guess % 10 == 0:
        print("Your number is a multiple of ten")
    else:
        print("Your number is not a multiple of ten")

    message = input("Enter 'q' to exit or press enter to continue > ").lower()
print = message