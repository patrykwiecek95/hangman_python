import os
import random
import time

class Hangman:
    def __init__(self):
        self.name = self.get_name()
        self.category = self.choose_category()
        self.word_to_guess = self.choose_word()
        self.max_trials = int(len(self.word_to_guess) / 2) + 1
        self.trials = 0
        self.encrypted_word = "_" * len(self.word_to_guess)

    def get_name(self):
        name = input("Please write your name: ")
        return name

    def choose_category(self):
        while True:
            category = input(" \n 1. animals \n 2. cities \n \nPlease write number 1 or 2 to choose a category of word: ")
            switcher = {
                "1": "animals",
                "2": "cities"
            }
            chosen_category = switcher.get(category, "invalid")
            if chosen_category == "invalid":
                print("Sorry, you need to choose a number from 1 to 2 \n")
            else:
                return chosen_category

    def choose_word(self):
        path = self.category + ".txt"
        with open(path, "r") as file:
            word_list = file.readlines()
        random.shuffle(word_list)
        word_to_guess = word_list[0].strip()
        return word_to_guess

    def play(self):
        print("Welcome to the HANGMAN game!!! \n")
        time.sleep(1)
        print(f"\nHi {self.name}, let's start playing the game.")
        time.sleep(1)
        print(f"\nGreat! You chose the category of {self.category}\n")
        time.sleep(1)
        print("What a %s it could be ?"%self.category+"\n")
        time.sleep(0.5)
        print(self.encrypted_word+"\n")
        while True:
            guess_letter = input("Guess a letter! Your letter is: ")
            if guess_letter in self.word_to_guess:
                print(f"\nYeaaa, good work \"{guess_letter}\" is in the guessing word.\n")
                indices = [i for i, letter in enumerate(self.word_to_guess) if letter == guess_letter]
                for index in indices:
                    self.encrypted_word = self.encrypted_word[:index] + guess_letter + self.encrypted_word[index + 1:]
                if "_" in self.encrypted_word:
                    pass
                else:
                    print(f"\nGREAT!!! You guessed the word {self.encrypted_word.upper()}")
                    break
            else:
                print("\nSorry, you missed. Try again.")
                self.trials += 1
                self.max_trials -= 1
                print(f"Trials {self.trials}, {self.max_trials + 1} chances left.")
                if self.trials > self.max_trials:
                    print(f"Sorry, you lose... the guessing word was {self.word_to_guess}. Try again a new game.")
                    break
            print(self.encrypted_word)

hangman = Hangman()
hangman.play()
