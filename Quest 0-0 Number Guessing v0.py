import random

while True:
    # Choose a random number between 1 and 100
    secret_number = random.randint(1, 100)
    print("I'm thinking of a number! Try to guess the number I'm thinking of:")

    while True:
        guess = input("Your guess: ")

        # Check that the input is a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < secret_number:
            print("Too low! Guess again:")
        elif guess > secret_number:
            print("Too high! Guess again:")
        else:
            print("That's it!")
            break

    play_again = input("Would you like to play again? (yes/no) ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
