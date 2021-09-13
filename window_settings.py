from tkinter import Label
from settings import options, defaults

def format(container, hr, host):

    settings_DefaultBannerTop = Label(
        container,
        image = hr,
        background = defaults['windowBackground']
    )
    settings_DefaultBannerBottom = Label(
        container,
        image = hr,
        background = defaults['windowBackground']
    )

    # Styles for label ('Operations')
    settings_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 70),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Label'],
                    text = 'Operations'.upper()
                )

    # Styles for device host and IP
    settings_Hostname_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Label'],
                    text = 'Hostname'.upper(),
                    padx = 20
                )

    settings_Hostname_Details_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Time'],
                    text = host['hostname'].upper(),
                    padx = 20
                )

    settings_HostIP_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Label'],
                    text = 'IP address'.upper(),
                    padx = 20
                )

    settings_HostIP_Details_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Time'],
                    text = host['ipaddress'].upper(),
                    padx = 20
                )

    settings_ClockStyle_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Label'],
                    text = 'Clock style'.upper(),
                    padx = 20
                )

    settings_ClockStyle_Details_Label = Label(
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

    settings_Label.grid(
        row = 0,
        column = 0,
        columnspan = 2,
        pady = (40, 20)
    )

    settings_DefaultBannerTop.grid(
        row = 1,
        column = 0,
        columnspan = 2
    )

    settings_Hostname_Label.grid(
        row = 2,
        column = 0,
        pady = (20, 0)
    )

    settings_Hostname_Details_Label.grid(
        row = 2,
        column = 1,
        pady = (20, 0)
    )

    settings_HostIP_Label.grid(
        row = 3,
        column = 0,
        pady = (20, 0)
    )

    settings_HostIP_Details_Label.grid(
        row = 3,
        column = 1,
        pady = (20, 0)
    )

    settings_ClockStyle_Label.grid(
        row = 4,
        column = 0,
        pady = (20, 0)
    )

    settings_ClockStyle_Details_Label.grid(
        row = 4,
        column = 1,
        pady = (20, 0)
    )

    settings_DefaultBannerBottom.grid(
        row = 5,
        column = 0,
        columnspan = 2
    )

    return container