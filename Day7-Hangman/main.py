import os
import random

from hangman_art import logo, stages
from hangman_words import word_list

game_over = False
lives = 7
chosen_word = random.choice(word_list)
display = []
for i in chosen_word:
    display.append("_")
guessed = []

print(logo)

print(f"The hidden word is {len(display)} letters.")
print(f"{' '.join(display)}")

while not game_over:
    guess = input("Guess a letter: ").lower()
    os.system("cls")
    if guess in guessed:
        print(f"You 've already guessed {guess}")
    else:
        guessed.append(guess)
        for i in range(len(chosen_word)):
            if (chosen_word[i] == guess):
                display[i] = guess
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                game_over = True
                print("You lost...")
                print(f"The hidden word was: {chosen_word}")
    print(f"{' '.join(display)}")
    if not "_" in display:
        game_over = True
        print("You won!")
    print(stages[lives])
