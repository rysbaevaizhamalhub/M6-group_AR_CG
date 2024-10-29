# Aizhamal Rysbaeva
# Oct 29, 2024

# program that will take a number (input) from the user and guess a randomly generated number.
# Provide the user with an opportunity to guess higher or lower, depending on the randomly generated number.

number = input("Please guess number between 1 and 10: ")
for num in range(1, 11):
    if num > 6:
        print("Please guess lower")
    elif num <= 6:
        print("Well done, you guessed it!")
    elif num == 0:
        print("Process finished with exit code 0")
    else:
        print("Wrong guess, try again")
