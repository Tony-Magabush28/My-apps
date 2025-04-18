import random

def guess_number():
    """Number Guessing Game"""
    number = random.randint(1, 100)  # Generate a random number
    attempts = 0  

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I've chosen a number between 1 and 100. Try to guess it!")

    while True:  # Keep looping until the user guesses correctly
        try:
            guess = int(input("\nEnter your guess: "))  # Get user input
            attempts += 1  

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congrats! You guessed the number {number} in {attempts} attempts.")
                break  # End the loop when guessed correctly
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    guess_number()
