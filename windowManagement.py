from tkinter import Tk, Toplevel, Frame
from tkinter.constants import ANCHOR
from settings import options, defaults

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

    # Function to exit the programme
    def endProgramme(e):
        print('Computer, end programme')
        app.destroy()

    # Bind the Escape key to the endProgramme function
    app.bind('<Escape>', endProgramme)

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
    window.attributes('-topmost', True)
    window.focus_force()
    window.iconify()

    # Function to exit the programme
    def minimiseWindow(e):
        print('Close window')
        window.iconify()

    # Bind the Escape key to the endProgramme function
    window.bind('<Escape>', minimiseWindow)

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

def showWindow(time, alertType, win):

    alertToShow = alertType
    minute = int(time[-2:])
    time = int(time)

    # If the time is between 0000 and 0030, show the setting screen
    if time >= 0 and time <= 30:
        win[0].deiconify()
        win[1].iconify()
        win[2].iconify()
        win[3].iconify()
        win[4].iconify()
    elif alertToShow == 'red':
        win[3].iconify()
        win[4].deiconify()
    # Otherwise, check if there is an alert to show
    elif alertToShow == 'yellow':
        win[3].deiconify()
        win[4].iconify()
    # Otherwise, just show the clock
    else:
        # don't show the settings
        win[0].iconify()

        # show the clock based on the settings
        if options['clockStyle'] == 'numeric':
            win[1].deiconify()
            win[2].iconify()
        if options['clockStyle'] == 'words':
            win[1].iconify()
            win[2].deiconify()
        else:
            win[1].deiconify()
            win[2].iconify()

        # don't show the alert
        win[3].iconify()
        win[4].iconify()