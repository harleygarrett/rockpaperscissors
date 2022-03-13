from tkinter import Tk, Frame, Label, Button, Text, StringVar, ttk, Message, Label
from tkinter.messagebox import showinfo
import random
from functools import partial
from tkintersetup import window_setup

def play(index, users_score, programs_score):

    global window

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
                command=partial(result, index, users_score, programs_score),
            )
            radio.pack()

        # submit with button v submit on selection
        # button = Button(
        #     window,
        #     text='Play',
        #     command=partial(result, index, users_score, programs_score)
        # )
        # button.pack()

def result(index, users_score, programs_score):

    global window

    for widget in window.winfo_children():
        widget.destroy()

    programs_choice = random.randint(0, 2)
    users_choice = options.index(selected.get())

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
            command=partial(play, 0, 0, 0)
        )

        button.pack()

        index = 0


    else:
        button = Button(
            window,
            text=f'Play Round {index + 1}',
            command=partial(play, index, users_score, programs_score)
        )

        button.pack()

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
    play(index, users_score, programs_score)

    window.mainloop()
