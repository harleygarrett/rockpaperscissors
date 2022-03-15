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
    windowHeight = 500
    # position
    centerX = int(screenWidth / 2 - windowWidth / 2)
    centerY = int(screenHeight / 2 - windowHeight / 2)
    # init
    window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
    # options
    window.resizable(True, True)
    window.minsize(200, 200)
    window.maxsize(800, 800)

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)
    window.grid_columnconfigure(4, weight=1)

    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=1)
    window.grid_rowconfigure(5, weight=1)

    # style
    window.configure(bg='white')
    window.option_add('*Font', '"Syne Mono"')

    style = ttk.Style(window)
    style.theme_use('clam')
