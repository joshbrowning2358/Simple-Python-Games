#!/usr/bin/env python2

from Tkinter import *
from ttk import *
from random import *
word = 0
word_length = 0
clue = 0


def gui():
    global word, word_length, clue
    dictionary = ['kernel', 'linux', 'penguin', 'ubuntu', 'python']
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ['_']
    tries = 6


    def hangedman(hangman):
        graphic = ["""
            +-------+
            |
            |
            |
            |
            |
        ==============
        """,
        """
            +-------+
            |       |
            |       O
            |
            |
            |
        ===============
        """,
        """
            +-------+
            |       |
            |       O
            |       |
            |
            |
        ===============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|
            |
            |
            |
        ===============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |
            |
        ===============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |      /
            |
        ===============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |      / \
            |
        ===============
        """]
        new_graphic = graphic[hangman]
        hm_graphic.set(new_graphic)
        return


    def start():
        print "Let's play a game of Linux Hangman."
        while game():
            pass
        scores()


    def game():
        letters_wrong = incorrect_guesses.get()
        letter = guess_letter()
        first_index = word.find(letter)
        if first_index == -1:
            letters_wrong += 1
            incorrect_guesses.set(letters_wrong)
        else:
            for i in range(word_length):
                if letter == word[i]:
                    clue[i] = letter
        hangedman(letters_wrong)
        clue_set = ' '.join(clue)
        word_output.set(clue_set)
        if letters_wrong == tries:
            result_text = 'Game Over.  The word was' + word + '.'
            result_set.set(result_text)
            new_score = computer_score.get()
            new_score += 1
            computer_score.set(new_score)
        if ''.join(clue) == word:
            result_text = 'You Win! The word was ' + word + '.'
            result_set.set(result_text)
            new_score = player_score.get()
            new_score += 1
            player_score.set(new_score)


    def guess_letter():
        letter = letter_guess.get()
        letter.strip()
        letter.lower()
        return letter


    def reset_game():
        global word, word_length, clue
        incorrect_guesses.set(0)
        hangedman(0)
        result_set.set('')
        letter_guess.set('')
        word = choice(dictionary)
        word_length = len(word)
        clue = word_length * ['_']
        new_clue = ' '.join(clue)
        word_output.set(new_clue)

if __name__ == '__main__':
    gui()
