# check_value = 10
# stoppage = ["no", "n"]
#
# while True:
#     guess = input("Enter an integer larger than zero > ")
#     guess = int(guess)
#
#     if guess % check_value == 0:
#         print(f"Your number is a multiple of {check_value}")
#     else:
#         print(f"Your number is not a multiple of {check_value}")
#
#     message = input("Continue? (Y or N) > ")
#     if message.lower() in stoppage:
#         break

check_value = 10
stoppage = ["quit", "q"]

while True:
    guess = input("Enter an integer larger than zero or enter Quit to exit> ")

    if guess.lower() in stoppage:
        print("You have exited the program")
        break

    guess = int(guess)
    if guess % check_value == 0:
        print(f"Your number is a multiple of {check_value}")
    else:
        print(f"Your number is not a multiple of {check_value}")
