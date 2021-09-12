from tkinter import *
from PIL import ImageTk, Image  

import clock as clock
import system as system

# Variables
screenSize = '720x720'
refreshTime = 5000
appName = 'Library Computer Access Retrieval System'
host = system.getHostIP()
lcarsBackground = 'black'
lcarsLabelColor = '#FFCC99'
lcarsTimeColor = '#FF9900'
lcarsStardateColor = '#FFCC99'
lcarsButtonColor = 'black'
lcarsButtonBackground = '#9977AA'
lcarsButtonActiveColor = 'black'
lcarsButtonActiveBackground = '#FFCC99'
lcarsFont = 'Context Ultra Condensed SSi'

# Assets
lcarsDefaultBanner = Image.open('assets/images/default-banner.png')
lcarsYellowAlertBanner = Image.open('assets/images/yellow-alert-banner.png')
lcarsRedAlertBanner = Image.open('assets/images/red-alert-banner.png')

# Create tkinter window
app = Tk()

# Window size and settings
app.title('LCARS Clock')
app.geometry(screenSize)
app.attributes('-fullscreen', True)
app.config(
    background = lcarsBackground,
    bd = 0
)

#Define a function
def endProgramme():
   app.destroy()

#This function is able to create new separate window
def createNewWindow(title):
    window = Toplevel()
    window.title(title)
    window.geometry(screenSize)
    window.config(
        background = lcarsBackground
    )

    return window

def createNewFrame(window):
    frame = Frame(
        window,
        background = lcarsBackground
    )

    return frame

# Windows
frameAppMessage = createNewFrame(app)
frameAppHostInfo = createNewFrame(app)
frameAppExit = createNewFrame(app)
frameAppMessage.pack(expand = True)
frameAppHostInfo.pack(expand = True)
frameAppExit.pack(expand = True)

windowStyleClock = createNewWindow('Numeric clock')
frameStyleClock = createNewFrame(windowStyleClock)
frameStyleClock.pack(expand = True)

windowStyleWordClock = createNewWindow('Word clock')
frameStyleWordClock = createNewFrame(windowStyleWordClock)
frameStyleWordClock.pack(expand = True)

##################################
# STYLES FOR THE APP ROOT WINDOW #
##################################
defaultBanner = ImageTk.PhotoImage(lcarsDefaultBanner)

app_DefaultBannerTop = Label(
    frameAppMessage,
    image = defaultBanner,
    background = lcarsBackground
)
app_DefaultBannerBottom = Label(
    frameAppMessage,
    image = defaultBanner,
    background = lcarsBackground
)

# Styles for app name
app_Message_Label = Label(
                frameAppMessage, 
                font = (lcarsFont, 100),
                background = lcarsBackground,
                foreground = lcarsLabelColor,
                wraplength = 700,
                text = appName.upper()
            )

# Styles for device host and IP
app_Hostname_Label = Label(
                frameAppHostInfo, 
                font = (lcarsFont, 40),
                background = lcarsBackground,
                foreground = lcarsTimeColor,
                text = host['hostname'].upper(),
                padx = 20
            )

app_HostIP_Label = Label(
                frameAppHostInfo, 
                font = (lcarsFont, 40),
                background = lcarsBackground,
                foreground = lcarsTimeColor,
                text = host['ipaddress'].upper(),
                padx = 20
            )

# Styles for exit programme button
app_EndProgramme_Button = Button(
                frameAppExit, 
                font = (lcarsFont, 40),
                background = lcarsButtonBackground,
                activebackground = lcarsButtonActiveBackground,
                foreground = lcarsButtonColor,
                activeforeground = lcarsButtonActiveColor,
                highlightthickness = 0,
                bd = 0,
                padx = 20,
                text = 'End progamme'.upper(),
                command = endProgramme
            )

################################
# GRID FOR THE APP ROOT WINDOW #
################################

app_DefaultBannerTop.grid(
    row = 0,
    column = 0
)

app_Message_Label.grid(
    row = 1,
    column = 0,
    pady = (60,40)
)

app_DefaultBannerBottom.grid(
    row = 2,
    column = 0
)

app_Hostname_Label.grid(
    row = 0,
    column = 0
)

app_HostIP_Label.grid(
    row = 0,
    column = 1
)

app_EndProgramme_Button.grid(
    row = 0,
    column = 0
)

################################
# STYLES FOR THE NUMERIC CLOCK #
################################
# Styles for time
styleClock_Time_Label = Label(
                frameStyleClock, 
                font = (lcarsFont, 340),
                background = lcarsBackground,
                foreground = lcarsTimeColor
            )

# Styles for the 'star' date
styleClock_Stardate_Label = Label(
                frameStyleClock, 
                font = (lcarsFont, 140),
                background = lcarsBackground,
                foreground = lcarsStardateColor
            )

##############################
# GRID FOR THE NUMERIC CLOCK #
##############################

# Placing clock at the center
styleClock_Time_Label.grid(
    row = 0,
    column = 0
)
styleClock_Stardate_Label.grid(
    row = 1,
    column = 0
)

#############################
# STYLES FOR THE WORD CLOCK #
#############################
# Styles for label ('The time is')
styleWordClock_TheTimeIs_Label = Label(
                frameStyleWordClock, 
                font = (lcarsFont, 100),
                background = lcarsBackground,
                foreground = lcarsLabelColor
            )

styleWordClock_TheTimeIs_LabelText = 'The time is'
styleWordClock_TheTimeIs_Label.config(
    text = styleWordClock_TheTimeIs_LabelText.upper()
)

# Styles for time
styleWordClock_Time_Label = Label(
                frameStyleWordClock, 
                font = (lcarsFont, 100),
                background = lcarsBackground,
                foreground = lcarsTimeColor
            )
    
###########################
# GRID FOR THE WORD CLOCK #
###########################

# Placing clock at the center
styleWordClock_TheTimeIs_Label.grid(
    row = 0,
    column = 0
)
styleWordClock_Time_Label.grid(
    row = 1,
    column = 0
)

def updateClock():

    timeNow = clock.formatTime()
    dateNow = clock.formatDate()

    styleClock_Time_LabelText = timeNow['numeric']
    styleClock_Time_Label.config(
        text = styleClock_Time_LabelText
    )

    styleClock_Stardate_LabelText = dateNow
    styleClock_Stardate_Label.config(
        text = styleClock_Stardate_LabelText
    )
    
    styleWordClock_Time_LabelText = timeNow['words']
    styleWordClock_Time_Label.config(
        text = styleWordClock_Time_LabelText.upper(),
        wraplength = 700
    )

# This function is used to display time on the label
def updateDisplay():

    # determines what to show
    # sets up what the display will show
    clockStyle = clock.clockStyle() 
    updateClock()

    app.after(
        refreshTime, 
        updateDisplay
    )
        
