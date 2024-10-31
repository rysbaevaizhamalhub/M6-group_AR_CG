import random

def guessing_game():
    guess_number = random.randint(1,50)
    attempts = 0
    print("Welcome to the guessing game. Are you ready!")
    print ("I am thinking of a number from 1,50 can you guess it?")
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            if user_guess == guess_number:
                print (f"Hurray! you guessed the number {guess_number} in {attempts} attempts.")
                break
            else:
                if user_guess < guess_number:
                    print("Go higher try again")
                else:
                    print("Lower try again")
        except ValueError:
            print("Enter a valid number")
while True:
    guessing_game()
    play_again = input("Do you wish to play again?") .strip() .lower()
    if play_again != "yes":
        break
