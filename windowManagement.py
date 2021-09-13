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
    window.iconify()

    # Function to exit the programme
    def closeWindow(e):
        print('Close window')
        window.destroy()

    # Bind the Escape key to the endProgramme function
    window.bind('<Escape>', closeWindow)

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

def showWindow(time, win):

    time = int(time[-1])

    if time == 1:
        print('show numeric clock')
        win[0].iconify()
        win[1].deiconify()
        win[2].iconify()
        win[3].iconify()
        win[4].iconify()
    elif time == 2:
        print('show word clock')
        win[0].iconify()
        win[1].iconify()
        win[2].deiconify()
        win[3].iconify()
        win[4].iconify()
    elif time == 3:
        print('show yellow alert')
        win[0].iconify()
        win[1].iconify()
        win[2].iconify()
        win[3].deiconify()
        win[4].iconify()
    elif time == 4:
        print('show red alert')
        win[0].iconify()
        win[1].iconify()
        win[2].iconify()
        win[3].iconify()
        win[4].deiconify()
    elif time == 5:
        print('show numeric clock')
        win[0].iconify()
        win[1].deiconify()
        win[2].iconify()
        win[3].iconify()
        win[4].iconify()
    elif time == 6:
        print('show word clock')
        win[0].iconify()
        win[1].iconify()
        win[2].deiconify()
        win[3].iconify()
        win[4].iconify()
    elif time == 7:
        print('show yellow alert')
        win[0].iconify()
        win[1].iconify()
        win[2].iconify()
        win[3].deiconify()
        win[4].iconify()
    elif time == 8:
        print('show red alert')
        win[0].iconify()
        win[1].iconify()
        win[2].iconify()
        win[3].iconify()
        win[4].deiconify()
    elif time == 9:
        print('show settings')
        win[0].deiconify()
        win[1].iconify()
        win[2].iconify()
        win[3].iconify()
        win[4].iconify()