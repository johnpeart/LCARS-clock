from tkinter import Label
from settings import defaults

def format(container, hr, host):

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

    # Styles for app name
    message_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 100),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Label'],
                    wraplength = 700,
                    text = defaults['appName'].upper()
                )

    # Styles for device host and IP
    hostname_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Time'],
                    text = host['hostname'].upper(),
                    padx = 20
                )

    hostIP_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Time'],
                    text = host['ipaddress'].upper(),
                    padx = 20
                )

    ################################
    # GRID FOR THE APP ROOT WINDOW #
    ################################

    banner_Top.grid(
        row = 0,
        column = 0,
        columnspan = 2
    )

    message_Label.grid(
        row = 1,
        column = 0,
        pady = (60,40),
        columnspan = 2
    )

    banner_Bottom.grid(
        row = 2,
        column = 0,
        columnspan = 2
    )

    hostname_Label.grid(
        row = 3,
        column = 0,
        pady = (60, 0)
    )

    hostIP_Label.grid(
        row = 3,
        column = 1,
        pady = (60, 0)
    )

    return hostname_Label, hostIP_Label