val = 30
val3 = 3
val5 = 5
x = 1
y = 1

for x in range(1, (val+1)):

    print(f"{x}\t", end="")
    while y <= x:
        if (y % val3 == 0) and (y % val5 == 0):
            print("FizzBuzz")
        elif y % val3 == 0:
            print("Fizz")
        elif y % val5 == 0:
            print("Buzz")
        else:
            print("")
        y += 1
