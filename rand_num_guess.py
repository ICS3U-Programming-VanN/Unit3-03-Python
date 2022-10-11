#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: October 6, 2022
# This program asks the user to try and guess the randomly generated number between 0-9
# and displays a message depending on if they get it right or not


import random


def main():
    # Declared CORRECT_ANSWER constants
    CORRECT_ANSWER = random.randint(0, 9)

    # Asks the user for their guess
    user_guess = float(input("Guess the number (1-9): "))

    # IF the user guesses the number correctly
    if user_guess == CORRECT_ANSWER:
        print("You guessed the number correctly!")

    # IF the user guesses the number incorrectly
    else:
        print(
            f"You guessed the number incorrectly! The correct answer was: {CORRECT_ANSWER}"
        )


if __name__ == "__main__":
    main()
