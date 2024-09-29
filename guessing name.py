import random

# Function to play the guessing game
def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        guess = input("Enter your guess: ")

        # Check if input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

# Call the function to start the game
guessing_game()