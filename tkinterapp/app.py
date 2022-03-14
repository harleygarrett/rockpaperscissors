from tkinter import Tk, Frame, PhotoImage, Label, Button, Text, StringVar, ttk, Message, Label
from tkinter.messagebox import showinfo
import random
from functools import partial
from tkintersetup import window_setup
from functions import play, result

if __name__ == '__main__':

    # window setup
    window = Tk()
    window_setup(window, 'Rock Paper Scissors')

    # init variables
    OPTIONS = ['rock', 'paper', 'scissors']
    IMAGES = [[PhotoImage(
        file='/Users/harleygarrett/PycharmProjects/cfg-python/project/tkinterapp/img/rock-left.gif'), PhotoImage(
        file='/Users/harleygarrett/PycharmProjects/cfg-python/project/tkinterapp/img/rock-right.gif')], [PhotoImage(
            file='/Users/harleygarrett/PycharmProjects/cfg-python/project/tkinterapp/img/paper-left.gif'), PhotoImage(
            file='/Users/harleygarrett/PycharmProjects/cfg-python/project/tkinterapp/img/paper-right.gif')], [PhotoImage(
                file='/Users/harleygarrett/PycharmProjects/cfg-python/project/tkinterapp/img/scissors-left.gif'), PhotoImage(
                file='/Users/harleygarrett/PycharmProjects/cfg-python/project/tkinterapp/img/scissors-right.gif')]]
    # mutable
    selected = StringVar()
    # for incrementing
    index = 0
    users_score = 0
    programs_score = 0

    # play
    play(window, OPTIONS, IMAGES, selected, index,
         users_score, programs_score)

    window.mainloop()
