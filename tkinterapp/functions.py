from tkinter import BOTTOM, Tk, Frame, Label, Button, Text, StringVar, ttk, Message, Label, PhotoImage, NONE
# from tkinter.messagebox import showinfo
import random
from functools import partial
import tkinter as tk
from turtle import width


def play(window, options, images, selected, index, users_score, programs_score):

    # reset variable
    selected = StringVar()

    for widget in window.winfo_children():
        widget.destroy()

    title = Message(window, text=f'Rock Paper Scissors - Round {index + 1}')
    title.pack()

    label = Label(text='Select your choice:')
    label.pack()

    if index < 5:

        for option in options:
            radio = ttk.Radiobutton(
                window,
                text=option,
                value=option,
                variable=selected,
                command=partial(result, window, options, images,
                                selected, index, users_score, programs_score),
                image=images[options.index(option)][0],
                compound=tk.TOP
            )
            radio.pack()

        # submit with button v submit on selection
        # button = Button(
        #     window,
        #     text='Play',
        #     command=partial(result, index, users_score, programs_score)
        # )
        # button.pack()


def result(window, options, images, selected, index, users_score, programs_score):

    for widget in window.winfo_children():
        widget.destroy()

    programs_choice = random.randint(0, 2)

    users_choice = options.index(selected.get())

    Label(
        window,
        image=images[users_choice][1]
    ).pack()

    Label(
        window,
        image=images[programs_choice][1]
    ).pack()

    message = f'Round {index + 1} \nUser chose {options[users_choice]} \nProgram chose {options[programs_choice]}\n'

    if users_choice == programs_choice:
        message += '\nIt\'s a tie!\n'
    elif (users_choice == 0 and programs_choice == 2) \
            or (users_choice == 1 and programs_choice == 0) \
            or (users_choice == 2 and programs_choice == 1):  # rock
        message += f'\nUser wins round {index + 1}\n'
        users_score += 1
    else:
        message += f'\nProgram wins round {index + 1}\n'
        programs_score += 1

    index += 1

    if index == 5:
        message += '\nThe final score is:\n'
    else:
        message += '\nThe current score is:\n'

    message += f'\nUser: {users_score} | Program: {programs_score}\n'

    if index == 5:
        if users_score > programs_score:
            message += '\nCongratulations! You win!'
        elif users_score == programs_score:
            message += '\nIt\'s a tie!'
        else:
            message += '\nYou lose.'

    message = Message(window, text=message)
    message.pack()

    if index == 5:
        button = Button(
            window,
            text='Play Again',
            command=partial(play, window, options, images, selected, 0, 0, 0)
        )

        button.pack()

        index = 0

    else:
        button = Button(
            window,
            text=f'Play Round {index + 1}',
            command=partial(play, window, options, images, selected,
                            index, users_score, programs_score)
        )

        button.pack()
