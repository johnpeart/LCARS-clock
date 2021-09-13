from tkinter import Label
from settings import defaults

def format(container, hr, host):

    app_DefaultBannerTop = Label(
        container,
        image = hr,
        background = defaults['windowBackground']
    )
    app_DefaultBannerBottom = Label(
        container,
        image = hr,
        background = defaults['windowBackground']
    )

    # Styles for app name
    app_Message_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 100),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Label'],
                    wraplength = 700,
                    text = defaults['appName'].upper()
                )

    # Styles for device host and IP
    app_Hostname_Label = Label(
                    container, 
                    font = (defaults['fontFace'], 40),
                    background = defaults['windowBackground'],
                    foreground = defaults['textColor_Time'],
                    text = host['hostname'].upper(),
                    padx = 20
                )

    app_HostIP_Label = Label(
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

    app_DefaultBannerTop.grid(
        row = 0,
        column = 0,
        columnspan = 2
    )

    app_Message_Label.grid(
        row = 1,
        column = 0,
        pady = (60,40),
        columnspan = 2
    )

    app_DefaultBannerBottom.grid(
        row = 2,
        column = 0,
        columnspan = 2
    )

    app_Hostname_Label.grid(
        row = 3,
        column = 0,
        pady = (60, 0)
    )

    app_HostIP_Label.grid(
        row = 3,
        column = 1,
        pady = (60, 0)
    )

    return container