import random

choice = random.randint(0, 100)

while True:
    guess = input("Pick a number from 0 to 100 > ")

    guess = int(guess)

    if guess in range(0, 101):

        if guess == choice:
            print("You picked the right number!")
            break

        elif guess > choice:
            print("Your number is high")

        elif guess < choice:
            print("Your number is low")

    else:
        print("Your selection was not in the range of 0 to 100")
