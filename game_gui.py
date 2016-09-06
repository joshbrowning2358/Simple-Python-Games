#!/usr/bin/env python2

from Tkinter import *

import rock-paper-scissors
import hangman
import poker_dice

root = Tk()
root.title('Welcome to my first game!')

mainframe = Frame(root, height=200, width=500)
mainframe.pack_propagate(0)
mainframe.pack(padx=5, pady=5)

intro = Label(mainframe, text='Welcome to my first game!  Please select one of the following games to play:')
intro.pack(side=TOP)

rps_button = Button(mainframe, text='Rock, Paper, Scissors', command=rock_paper_scissors_gui)
rps_button.pack()

hm_button = Button(mainframe, text='Hangman', command=hangman_start)
hm_button.pack()

pd_button = Button(mainframe, text='Poker Dice', command=poker_dice_start)
pd_button.pack()

exit_button = Button(mainframe, text='Exit', command=root.destroy)
exit_button.pack(side=BOTTOM)

root.mainloop()