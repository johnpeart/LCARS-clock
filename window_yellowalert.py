from tkinter import Label
import labels as labels
from settings import defaults

def format(container, hr):

    banner_Top = Label(
        container,
        image = hr,
        background = defaults['windowBackground']
    )

    banner_Bottom = Label(
        container,
        image = hr,
        background = defaults['windowBackground']
    )

    alertConditionYellow_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 70),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_YellowAlert']
                )

    
    alertMessage_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 70),
                    wraplength = 700,
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_AlertSecondary']
                )

    # Styles for time
    time_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 70),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_YellowAlert']
                )

    # Styles for the 'star' date
    date_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 70),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_YellowAlert']
                )

    labels.update(alertConditionYellow_Label, 'Alert: Condition Yellow')
    labels.update(alertMessage_Label, 'If there is an alert to display, it will be shown here on the relevant days.')

        
    ######################
    # GRID FOR RED ALERT #
    ######################

    # Placing text at the center
    alertConditionYellow_Label.grid(
        row = 0,
        column = 0,
        columnspan = 2,
        pady = (30,20)
    )
    banner_Top.grid(
        row = 1,
        column = 0,
        columnspan = 2
    )
    alertMessage_Label.grid(
        row = 2,
        column = 0,
        columnspan = 2,
        pady = (30,20)
    )
    banner_Bottom.grid(
        row = 3,
        column = 0,
        columnspan = 2
    )
    time_Label.grid(
        row = 4,
        column = 0,
        pady = (30,20)
    )
    date_Label.grid(
        row = 4,
        column = 1,
        pady = (30,20)
    )

    return alertMessage_Label, time_Label, date_Label