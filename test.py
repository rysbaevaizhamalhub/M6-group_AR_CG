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







import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)
guess = None
attempts = 3  # Set the number of allowed attempts

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print("You have 3 attempts to guess the correct number.")

# Loop to give the user 3 chances to guess
for attempt in range(attempts):
    try:
        guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Check if the guess is too high, too low, or correct
    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break  # Exit the loop if guessed correctly
else:
    print(f"Sorry, you've used all your attempts. The correct number was {target_number}.")

print("Game Over.")
