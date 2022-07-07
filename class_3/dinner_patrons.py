# patrons = int(input("How many people in your dinner group? > "))
#
# if patrons > 8:
#     print("Please wait for the next available table")
# else:
#     print("Your dinner table is ready!")

patrons = int(input("How many people in your dinner group? > "))

print('Your table is ', end="")

if patrons >= 8:
    print ('not ', end="")

print('ready')
