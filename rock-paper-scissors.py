#!/usr/bin/env python2

from Tkinter import *
from ttk import *
import random

def gui():

rock = 1
paper = 2
scissors = 3

names = {rock: 'rock', paper: 'paper', scissors: 'scissors'}
rules = {rock: 'scissors', paper: 'rock', scissors: 'paper'}

player_score = 0
computer_score = 0


def start():
    print "Let's play Rock Paper Scissors!"
    while game():
        pass
    scores()


def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()


def move():
    while True:
        print '\n'
        player = raw_input('Rock=1\nPaper=2\nScissors=3\nYour input: ')
        try:
            player = int(player)
            if player in [1, 2, 3]:
                return player
            else:
                print 'Invalid input!  Only throw rock, paper or scissors please!'
        except:
            pass


def result(player, computer):
    print '1...'
    time.sleep(1)
    print '2...'
    time.sleep(1)
    print '3!'
    time.sleep(0.5)
    print 'Computer threw {}!'.format(names[computer])
    global player_score, computer_score
    if player == computer:
        print "Tie game!  That's no fun :("
    elif rules[player] == computer:
        print "You have won.  I can't believe it..."
        player_score += 1
    else:
        print 'Bwahaha!  Victory is mine!'
        computer_score += 1


def play_again():
    valid_ans = False
    while not valid_ans:
        answer = raw_input('Would you like to play again (y/n)?')
        if answer == 'y':
            valid_ans = True
            game()
        elif answer == 'n':
            valid_ans = True
            print "Thanks for playing!"


def scores():
    global player_score, computer_score
    print 'HIGH SCORES'
    print 'Player: ', player_score
    print 'Computer: ', computer_score


if __name__ == '__main__':
    start()