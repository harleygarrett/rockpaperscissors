from tkinter import ttk


def window_setup(window, title):
    # title
    window.title(title)

    # screen properties
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    # window properties
    # size
    windowWidth = 600
    windowHeight = 400
    # position
    centerX = int(screenWidth / 2 - windowWidth / 2)
    centerY = int(screenHeight / 2 - windowHeight / 2)
    # init
    window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
    # options
    window.resizable(True, True)
    window.minsize(300, 200)
    window.maxsize(1200, 800)

    # style
    # style = ttk.Style(window)
    # style.theme_use('classic')
