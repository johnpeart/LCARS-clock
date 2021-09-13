from tkinter import Label
import labels as labels
from settings import defaults

def format(container):
    
    # Styles for label ('The time is')
    theTimeIs_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 100),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Label']
                )

    labels.update(theTimeIs_Label, 'The time is')

    # Styles for time
    time_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 100),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Time']
                )
        
    ###########################
    # GRID FOR THE WORD CLOCK #
    ###########################

    # Placing clock at the center
    theTimeIs_Label.grid(
        row = 0,
        column = 0
    )
    time_Label.grid(
        row = 1,
        column = 0
    )

    return time_Label