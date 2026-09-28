# MW - Number Guessing Game

import random

# Secret number range: 1 to 100
secret_number = random.randint(1, 100)

# Player has 6 attempts
max_attempts = 6

guesses_used = 0

print("I'm thinking of a number between 1 and 100.")
print("You have 6 tries to guess it!")

for attempt in range(max_attempts):
    guess = int(input(f"\nGuess #{attempt + 1}: "))
    guesses_used += 1

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print(f"Correct! You guessed it in {guesses_used} tries!")
        break

else:
    print(f"\nYou're out of guesses! The number was {secret_number}.")

