from tkinter import Label, Button, StringVar, ttk, Label
import random
from functools import partial
import tkinter as tk


# function shows the play screen
def play(window, options, images, selected, index, users_score, programs_score):

    # reset variable
    selected = StringVar()

    # remove existing content from the screen
    for widget in window.winfo_children():
        widget.destroy()

    # round label
    title = Label(window, text=f'Round {index + 1}')
    title.grid(row=1, column=0, columnspan=5)

    # choice instruction label
    label = Label(text='Select your choice:')
    label.grid(row=2, column=0, columnspan=5)

    # style radio buttons
    style = ttk.Style(window)
    style.configure('IndicatorOff.TRadiobutton',
                    indicatorrelief=tk.FLAT,
                    indicatormargin=-10,
                    indicatordiameter=-1,
                    relief=tk.RAISED,
                    focusthickness=0, highlightthickness=0, padding=10, background='white')
    style.map('IndicatorOff.TRadiobutton',
              background=[('selected', '#ececec'), ('active', '#ececec')])

    # loop 5 rounds
    if index < 5:

        # render a radio per option in the list, with images sourced from the matching index of the images array
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
                style='IndicatorOff.TRadiobutton'
            )

            radio.grid(row=3, column=options.index(option) + 1)


# function shows the results screen
def result(window, options, images, selected, index, users_score, programs_score):

    # remove existing content from the screen
    for widget in window.winfo_children():
        widget.destroy()

    # program choses
    programs_choice = random.randint(0, 2)

    # fetch user's choice
    users_choice = options.index(selected.get())

    # init user's choice label
    Label(
        window,
        image=images[users_choice][0]
    ).grid(row=2, column=0, columnspan=3)

    # init programs choice label
    Label(
        window,
        image=images[programs_choice][1]
    ).grid(row=2, column=2, columnspan=5)

    # render round details
    round_message = f'Round {index + 1}\n'
    users_choice_message = f'User chose {options[users_choice]}'
    programs_choice_message = f'Program chose {options[programs_choice]}'

    # check who wins

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

    # increment the round
    index += 1

    # init score based on round number
    if index == 5:
        score_message = '\nThe final score is:\n'
    else:
        score_message = '\nThe current score is:\n'

    score_message += f'\nUser: {users_score} | Program: {programs_score}\n'

    # init messages as labels
    round_message = Label(window, text=round_message)
    users_choice_message = Label(window, text=users_choice_message)
    programs_choice_message = Label(window, text=programs_choice_message)
    result_message = Label(window, text=result_message)
    score_message = Label(window, text=score_message)

    # render labels
    round_message.grid(row=0, column=0, columnspan=5, sticky=tk.EW)
    users_choice_message.grid(row=1, column=0, columnspan=3)
    programs_choice_message.grid(row=1, column=2, columnspan=5)

    result_message.grid(row=3, column=0, columnspan=5, sticky=tk.EW)
    score_message.grid(row=4, column=0, columnspan=5, sticky=tk.EW)

    # conditionally render end of game message and play button
    if index == 5:
        final_message = 'GAME OVER\n'
        if users_score > programs_score:
            final_message += '\nCongratulations! You win!'
        elif users_score == programs_score:
            final_message += '\nIt\'s a tie!'
        else:
            final_message += '\nYou lose.'
        final_message = Label(window, text=final_message)
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
