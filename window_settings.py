from tkinter import Label
from settings import options, defaults

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

    # Styles for label ('Operations')
    title_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 70),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Label'],
                    text = 'Operations'.upper()
                )

    # Styles for device host and IP
    hostname_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Label'],
                    text = 'Hostname'.upper(),
                    padx = 20
                )

    hostname_Details_Label = Label(
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
                    foreground = defaults['textColor_Label'],
                    text = 'IP address'.upper(),
                    padx = 20
                )

    hostIP_Details_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Time'],
                    text = host['ipaddress'].upper(),
                    padx = 20
                )

    clockStyle_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Label'],
                    text = 'Clock style'.upper(),
                    padx = 20
                )

    clockStyle_Details_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Time'],
                    text = options["clockStyle"].upper(),
                    padx = 20
                )


    ################################
    # GRID FOR THE SETTINGS WINDOW #
    ################################

    title_Label.grid(
        row = 0,
        column = 0,
        columnspan = 2,
        pady = (40, 20)
    )

    banner_Top.grid(
        row = 1,
        column = 0,
        columnspan = 2
    )

    hostname_Label.grid(
        row = 2,
        column = 0,
        pady = (20, 0)
    )

    hostname_Details_Label.grid(
        row = 2,
        column = 1,
        pady = (20, 0)
    )

    hostIP_Label.grid(
        row = 3,
        column = 0,
        pady = (20, 0)
    )

    hostIP_Details_Label.grid(
        row = 3,
        column = 1,
        pady = (20, 0)
    )

    clockStyle_Label.grid(
        row = 4,
        column = 0,
        pady = (20, 0)
    )

    clockStyle_Details_Label.grid(
        row = 4,
        column = 1,
        pady = (20, 0)
    )

    banner_Bottom.grid(
        row = 5,
        column = 0,
        columnspan = 2
    )

    return hostname_Details_Label, hostIP_Details_Label, clockStyle_Details_Label