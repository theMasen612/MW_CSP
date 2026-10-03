# MW - Number Guessing Game

import random

# The secret number will be between 1 and 100
secret_number = random.randint(1, 100)

# The player gets 6 guesses
max_attempts = 6
guesses_used = 0

print("I'm thinking of a number from 1 to 100!")
print("You get 6 tries to guess it.")

for attempt in range(max_attempts):
    guess = int(input(f"\nTake a guess #{attempt + 1}: "))
    guesses_used += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print(f"You got it! It took you {guesses_used} guesses!")
        break

else:
    print(f"\nYou ran out of guesses! The number was {secret_number}.")

