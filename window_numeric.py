from tkinter import Label
from settings import defaults

def format(container):
    
    # Styles for time
    time_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 340),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Time']
                )

    # Styles for the 'star' date
    date_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 140),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Date']
                )

    ##############################
    # GRID FOR THE NUMERIC CLOCK #
    ##############################

    # Placing clock at the center
    time_Label.grid(
        row = 0,
        column = 0
    )
    date_Label.grid(
        row = 1,
        column = 0
    )

    return time_Label, date_Label