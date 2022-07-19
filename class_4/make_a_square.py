# val = input("Size of the triangle? > ")
# val = int(val)
#
# for x in range(0, val):
#     print((x+1)*"X")

# val = input("Size of the square? > ")
# val = int(val)
#
# for x in range(0, val):
#     print(val *"X_")

# print("H", end="*")
# print("E", end="*")
# print("L", end="*")
# print("L", end="*")
# print("O")


# val = input("Size of the square? > ")
# val = int(val)
# for x in range(val):
#     for y in range(val):
#         print("X_", end="")
#     print("")

# val = input("Size of the triangle? > ")
# val = int(val)
# for x in range(val):
#     for y in range(x+1):
#         print("X", end="")
#     print()

val = input("Size of the triangle? > ")
val = int(val)

x = 1
while x <= val:

    y = 1
    while y <= x:
        print("X", end="")
        y += 1
    print()
    x += 1
