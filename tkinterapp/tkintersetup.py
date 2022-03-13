from tkinter import ttk


def window_setup(window, title):
    window.title(title)

    # screen properties
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    # window properties
    windowWidth = 600
    windowHeight = 400

    centerX = int(screenWidth / 2 - windowWidth / 2)
    centerY = int(screenHeight / 2 - windowHeight / 2)

    window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
    window.resizable(True, True)
    window.minsize(300, 200)
    window.maxsize(1200, 800)

    style = ttk.Style(window)
    style.theme_use('classic')
