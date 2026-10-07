# WW, Hangman

import random
import os

with open("strings.py/hangman.txt", "r") as file:
    inside = file.readlines()

word = random.choice(inside).strip()

if os.path.exists("stats.txt"):
    with open("stats.txt", "r") as stats:
        content = stats.read().splitlines()

    wins = int(content[0])
    losses = int(content[1])
else:
    wins = 0
    losses = 0

wrong_guesses = 0
guessed = []
max_wrong = 6

print("Welcome to Hangman!")
print()

while wrong_guesses < max_wrong:

    print("Word:", end=" ")

    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()
    print()

    if len(guessed) == 0:
        print("Guessed letters: (none yet)")
    else:
        print("Guessed letters:", end=" ")

        for letter in guessed:
            print(letter, end=" ")

        print()

    print("Wrong guesses remaining:", max_wrong - wrong_guesses)

    if wrong_guesses == 0:
        print("""
_______
|     |
|
|
|
|_______
""")

    elif wrong_guesses == 1:
        print("""
_______
|     |
|     0
|
|
|_______
""")

    elif wrong_guesses == 2:
        print("""
_______
|     |
|     0
|     |
|
|_______
""")

    elif wrong_guesses == 3:
        print("""
_______
|     |
|     0
|    /|
|
|_______
""")

    elif wrong_guesses == 4:
        print("""
_______
|     |
|     0
|    /|\\
|
|_______
""")

    elif wrong_guesses == 5:
        print("""
_______
|     |
|     0
|    /|\\
|    /
|_______
""")

    elif wrong_guesses == 6:
        print("""
_______
|     |
|     0
|    /|\\
|    / \\
|_______
""")

    guess = input("Guess a letter: ")

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if not guess.isalpha():
        print("Please enter a letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    guessed.append(guess)

    if guess in word:
        print("Nice!", guess, "is in the word!")
    else:
        print("Sorry,", guess, "is not in the word.")
        wrong_guesses = wrong_guesses + 1

    finished = True

    for letter in word:
        if letter not in guessed:
            finished = False

    if finished:
        print()
        print("Congratulations! You guessed the word:", word)
        wins = wins + 1
        break

if wrong_guesses == max_wrong:
    print()
    print("Game over! You ran out of guesses.")
    print("The word was:", word)
    losses = losses + 1

with open("stats.txt", "w") as stats:
    stats.write(str(wins) + "\n")
    stats.write(str(losses) + "\n")

print()
print("Updated Stats - Wins:", wins, "Losses:", losses)

