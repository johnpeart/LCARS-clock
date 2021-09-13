from tkinter import *
from settings import defaults

#This function creates the root window for the app
def app(title):
    # Create tkinter window
    app = Tk()
    app.title(title)
    app.geometry(defaults['screenSize'])
    app.attributes('-fullscreen', defaults['fullScreen'])
    app.config(
        background = defaults['windowBackground'],
        bd = defaults['borderWidth']
    )

    # Bind the Escape key to the endProgramme function
    app.bind('<Escape>', lambda e: endProgramme(e))

    # Function to exit the programme
    def endProgramme(e):
        app.destroy()


    return app

#This function is able to create new separate window
def window(title):
    window = Toplevel()
    window.title(title)
    window.geometry(defaults['screenSize'])
    window.config(
        background = defaults['windowBackground']
    )
    window.attributes('-fullscreen', defaults['fullScreen'])
    window.iconify()

    return window

# This function can create a container frame in the window
def container(window):
    container = Frame(
        window,
        background = defaults['windowBackground']
    )
    container.pack(expand = True)

    return container