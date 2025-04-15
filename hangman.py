import random as rd
import string

from words import words

def hangman():
    s_word = rd.choice(words).lower()
    lets_guessed = set()
    guessed_counts = {}
    w_letr_count = {char: s_word.count(char) for char in set(s_word)}
    alph = set(string.ascii_lowercase)
    lives = 6

    print("Are you ready? Lets play Hangman!")
    print(f"The word I chose has {len(s_word)} alphabets")
    print("You only have 6 lives so guess wisely!")
    print("Start!")

    while   lives > 0:
        d_word = [i if i in lets_guessed else '-' for i in s_word]
        print("".join(d_word))
        print(f"lives left: {lives}")
        print(f"letters used: {''.join(sorted(lets_guessed))}")

        guess = input("Guess a letter: ".lower())

        if len(guess) != 1:
            print("Kindly enter only one alphabet at a time")
            continue
        if guess not in alph:
            print("Kindly enter a valid alphabet (a-z)")
            continue

        guessed_counts[guess] = guessed_counts.get(guess, 0) + 1
        lets_guessed.add(guess)
        if guess in s_word:
            if guessed_counts[guess] <= w_letr_count.get(guess, 0):

                print("Good Guess")
        else:
            lives -= 1
            print(f"Wrong Guess, {guess} is not the word.")

        if all( i in lets_guessed for i in s_word):
            print("Yipee! You have guessed the word!")
            return
    print(f"Game Over! The word was {s_word}")

hangman()

