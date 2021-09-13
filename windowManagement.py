from tkinter import Tk, Toplevel, Frame
from tkinter.constants import ANCHOR
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

    # FUNCTIONS TO MANIPULATE THE FRAME
    # Function to exit the programme
    def endProgramme(e):
        print('Computer, end programme')
        app.destroy()

    def toggleFrame(e):
        print('Toggle frame')

    # Bind the Escape key to the endProgramme function
    app.bind('<Escape>', endProgramme)
    app.bind('<1>', toggleFrame)

    return app

#This function is able to create new separate window
def window(title):
    window = Toplevel()
    window.title(title)
    window.geometry(defaults['screenSize'])
    window.config(
        width = defaults['screenWidth'],
        height = defaults['screenHeight'],
        background = defaults['windowBackground']
    )
    window.attributes('-fullscreen', defaults['fullScreen'])
    window.iconify()

    return window

# This function can create a container frame in the window
def container(window):
    container = Frame(
        window,
        width = defaults['screenWidth'],
        height = defaults['screenHeight'],
        background = defaults['windowBackground']
    )
    container.place(relx = 0.5, rely = 0.5, anchor = 'center')

    return container