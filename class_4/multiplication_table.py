# mt = int(input("Enter the size of your multiplication table > "))
#
# for x in range(1, mt+1):
#     for y in range(1, mt+1):
#         print(x*y, end=" ")
#     print()

mt = int(input("Enter the size of your multiplication table > "))

for x in range(1, mt+1):
    for y in range(1, mt+1):
        print(str(x*y) + "\t", end="")
    print()
