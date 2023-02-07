import os
import random
from art import logo


def number_guessing():
    os.system("cls")
    print(logo)
    hidden_number = random.choice(range(1, 101))
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. (easy/hard)\n").lower()
    if difficulty == "hard" or difficulty == "h":
        attempts = 5
    else:
        attempts = 10
    playing = True
    while playing:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == hidden_number:
            print(f"You guessed correct, the number was {hidden_number}!")
            playing = False
        elif guess > hidden_number:
            attempts -= 1
            print("Too high.\nGuess again.")
        else:
            attempts -= 1
            print("Too low.\nGuess again.")
        if attempts == 0:
            print(f"You ran out of attempts, the number was {hidden_number}.")
            playing = False
    again = input("Do you want to play again? (yes/no)\n").lower()
    if again == "yes" or again == "y":
        number_guessing()


number_guessing()
