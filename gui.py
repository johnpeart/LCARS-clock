from tkinter import *
from PIL import ImageTk, Image  

import clock as clock

# Variables
screenSize = '720x720'
refreshTime = 5000
appName = 'Library Computer Access Retrieval System'
lcarsBackground = 'black'
lcarsLabelColor = '#FFCC99'
lcarsTimeColor = '#FF9900'
lcarsStardateColor = '#FFCC99'
lcarsFont = 'Context Ultra Condensed SSi'

# Assets
lcarsRedAlertBanner = Image.open('assets/images/red-alert-banner.png')

# Create tkinter window
app = Tk()

# Window size and settings
app.title('LCARS Clock')
app.geometry(screenSize)
# app.attributes('-fullscreen', True)
app.config(
    background = lcarsBackground,
    bd = 0
)

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
frameAppRoot = createNewFrame(app)
frameAppRoot.pack(expand = True)

windowStyleClock = createNewWindow('Numeric clock')
frameStyleClock = createNewFrame(windowStyleClock)
frameStyleClock.pack(expand = True)

windowStyleWordClock = createNewWindow('Word clock')
frameStyleWordClock = createNewFrame(windowStyleWordClock)
frameStyleWordClock.pack(expand = True)

##################################
# STYLES FOR THE APP ROOT WINDOW #
##################################
redAlertBanner = ImageTk.PhotoImage(lcarsRedAlertBanner)

app_RedAlertBannerTop = Label(
    frameAppRoot,
    image = redAlertBanner,
    background = lcarsBackground
)
app_RedAlertBannerBottom = Label(
    frameAppRoot,
    image = redAlertBanner,
    background = lcarsBackground
)

# Styles for time
app_Message_Label = Label(
                frameAppRoot, 
                font = (lcarsFont, 100),
                background = lcarsBackground,
                foreground = lcarsTimeColor,
                wraplength = 700,
                text = appName.upper(),
                pady = 20
            )

################################
# GRID FOR THE APP ROOT WINDOW #
################################

app_RedAlertBannerTop.grid(
    row = 0,
    column = 0
)

app_Message_Label.grid(
    row = 1,
    column = 0
)

app_RedAlertBannerBottom.grid(
    row = 2,
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
        
