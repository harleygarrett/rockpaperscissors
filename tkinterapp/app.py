from tkinter import Tk, Frame, Label, Button, Text, StringVar, ttk, Message, Label
from tkinter.messagebox import showinfo
import random
from functools import partial
from tkintersetup import window_setup
from functions import play, result

if __name__ == '__main__':

    # window setup

    window = Tk()
    window_setup(window, 'Rock Paper Scissors')

    # logic

    options = ['rock', 'paper', 'scissors']
    selected = StringVar()

    index = 0
    users_score = 0
    programs_score = 0

    # play
    play(window, options, selected, index, users_score, programs_score)

    window.mainloop()
