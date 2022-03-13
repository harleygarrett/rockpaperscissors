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

    title = Message(window, text=f'Round {index + 1}')
    title.grid(row=1, column=0, columnspan=5)

    # title.grid_rowconfigure(1, weight=1)
    # title.grid_columnconfigure(1, weight=1)

    label = Label(text='Select your choice:')
    label.grid(row=2, column=0, columnspan=5)

    style = ttk.Style(window)
    style.configure('IndicatorOff.TRadiobutton',
                    indicatorrelief=tk.FLAT,
                    indicatormargin=-10,
                    indicatordiameter=-1,
                    relief=tk.RAISED,
                    focusthickness=0, highlightthickness=0, padding=10, background='white')
    style.map('IndicatorOff.TRadiobutton',
              background=[('selected', '#ececec'), ('active', '#ececec')])

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
                compound=tk.TOP,
                # compound=NONE,
                style='IndicatorOff.TRadiobutton'
            )
            # style = ttk.Style()
            # style.configure('TRadiobutton', '"Syne Mono"')
            radio.grid(row=3, column=options.index(option) + 1)
            # radio.grid_rowconfigure(1, weight=1)
            # radio.grid_columnconfigure(1, weight=1)

        # submit with button v submit on selection
        # button = Button(
        #     window,
        #     text='Play',
        #     command=partial(result, index, users_score, programs_score)
        # )
        # button.grid()


def result(window, options, images, selected, index, users_score, programs_score):

    for widget in window.winfo_children():
        widget.destroy()

    programs_choice = random.randint(0, 2)

    users_choice = options.index(selected.get())

    Label(
        window,
        image=images[users_choice][0]
    ).grid(row=2, column=0, columnspan=3)

    Label(
        window,
        image=images[programs_choice][1]
    ).grid(row=2, column=2, columnspan=5)

    round_message = f'Round {index + 1}\n'
    users_choice_message = f'User chose {options[users_choice]}'
    programs_choice_message = f'Program chose {options[programs_choice]}'

    if users_choice == programs_choice:
        result_message = '\nIt\'s a tie!\n'
    elif (users_choice == 0 and programs_choice == 2) \
            or (users_choice == 1 and programs_choice == 0) \
            or (users_choice == 2 and programs_choice == 1):  # rock
        result_message = f'\nUser wins\n'
        users_score += 1
    else:
        result_message = f'\nProgram wins\n'
        programs_score += 1

    index += 1

    if index == 5:
        score_message = '\nThe final score is:\n'
    else:
        score_message = '\nThe current score is:\n'

    score_message += f'\nUser: {users_score} | Program: {programs_score}\n'

    round_message = Message(window, text=round_message)
    users_choice_message = Message(window, text=users_choice_message)
    programs_choice_message = Message(window, text=programs_choice_message)
    result_message = Message(window, text=result_message)
    score_message = Message(window, text=score_message)

    round_message.grid(row=0, column=0, columnspan=5, sticky=tk.EW)
    users_choice_message.grid(row=1, column=0, columnspan=3)
    programs_choice_message.grid(row=1, column=2, columnspan=5)

    result_message.grid(row=3, column=0, columnspan=5, sticky=tk.EW)
    score_message.grid(row=4, column=0, columnspan=5, sticky=tk.EW)

    if index == 5:
        final_message = 'GAME OVER\n'
        if users_score > programs_score:
            final_message += '\nCongratulations! You win!'
        elif users_score == programs_score:
            final_message += '\nIt\'s a tie!'
        else:
            final_message += '\nYou lose.'
        final_message = Message(window, text=final_message)
        final_message.grid(row=5, column=0, columnspan=5, sticky=tk.EW)

        button = Button(
            window,
            text='Play Again',
            command=partial(play, window, options, images,
                            selected, 0, 0, 0)
        )

        button.grid(row=6, column=0, columnspan=5)

        index = 0

    else:
        button = Button(
            window,
            text=f'Play Round {index + 1}',
            command=partial(play, window, options, images, selected,
                            index, users_score, programs_score)
        )

        button.grid(row=6, column=0, columnspan=5)
