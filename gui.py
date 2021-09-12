from tkinter import *
from PIL import ImageTk, Image  

import clock as clock
import system as system

# Variables
screenSize = '720x720'
refreshTime = 5000
appName = 'Library Computer Access Retrieval System'
host = system.getHostIP()
lcarsBackground = '#000000'
lcarsLabelColor = '#FFCC99'
lcarsRedAlertColor = '#F09693'
lcarsYellowAlertColor = '#F8DC77'
lcarsAlertSecondaryColor = '#FFFFFF'
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
# app.attributes('-fullscreen', True)
app.config(
    background = lcarsBackground,
    bd = 0
)

#Define a function
def endProgramme(e):
   app.destroy()

app.bind('<Escape>', lambda e: endProgramme(e))

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
frameAppMessage.pack(expand = True)
frameAppHostInfo.pack(expand = True)

windowStyleClock = createNewWindow('Numeric clock')
frameStyleClock = createNewFrame(windowStyleClock)
frameStyleClock.pack(expand = True)

windowStyleWordClock = createNewWindow('Word clock')
frameStyleWordClock = createNewFrame(windowStyleWordClock)
frameStyleWordClock.pack(expand = True)

windowStyleYellowAlert = createNewWindow('Alert: Condition Yellow')
frameStyleYellowAlert = createNewFrame(windowStyleYellowAlert)
frameStyleYellowAlert.pack(expand = True)

windowStyleRedAlert = createNewWindow('Alert: Condition Red')
frameStyleRedAlert = createNewFrame(windowStyleRedAlert)
frameStyleRedAlert.pack(expand = True)

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



###########################
# STYLES FOR YELLOW ALERT #
###########################
yellowAlertBanner = ImageTk.PhotoImage(lcarsYellowAlertBanner)

# Styles for label ('Alert: Condition Yellow')
styleYellowAlert_AlertConditionYellow_Label = Label(
                frameStyleYellowAlert, 
                font = (lcarsFont, 70),
                background = lcarsBackground,
                foreground = lcarsYellowAlertColor
            )

styleYellowAlert_AlertConditionYellow_LabelText = 'Alert: Condition Yellow'
styleYellowAlert_AlertConditionYellow_Label.config(
    text = styleYellowAlert_AlertConditionYellow_LabelText.upper()
)

styleYellowAlert_AlertMessage_Label = Label(
                frameStyleYellowAlert, 
                font = (lcarsFont, 70),
                wraplength = 700,
                background = lcarsBackground,
                foreground = lcarsAlertSecondaryColor
            )

styleYellowAlert_AlertMessage_LabelText = 'Message text for condition yellow alert'
styleYellowAlert_AlertMessage_Label.config(
    text = styleYellowAlert_AlertMessage_LabelText.upper()
)

# Styles for time
styleYellowAlert_Time_Label = Label(
                frameStyleYellowAlert, 
                font = (lcarsFont, 70),
                background = lcarsBackground,
                foreground = lcarsYellowAlertColor
            )

# Styles for the 'star' date
styleYellowAlert_Stardate_Label = Label(
                frameStyleYellowAlert, 
                font = (lcarsFont, 70),
                background = lcarsBackground,
                foreground = lcarsYellowAlertColor
            )

styleYellowAlert_BannerTop = Label(
    frameStyleYellowAlert,
    image = yellowAlertBanner,
    background = lcarsBackground
)
styleYellowAlert_BannerBottom = Label(
    frameStyleYellowAlert,
    image = yellowAlertBanner,
    background = lcarsBackground
)
    
#########################
# GRID FOR YELLOW ALERT #
#########################

# Placing clock at the center
styleYellowAlert_AlertConditionYellow_Label.grid(
    row = 0,
    column = 0,
    columnspan = 2,
    pady = (30,20)
)
styleYellowAlert_BannerTop.grid(
    row = 1,
    column = 0,
    columnspan = 2
)
styleYellowAlert_AlertMessage_Label.grid(
    row = 2,
    column = 0,
    columnspan = 2,
    pady = (30,20)
)
styleYellowAlert_BannerBottom.grid(
    row = 3,
    column = 0,
    columnspan = 2
)
styleYellowAlert_Time_Label.grid(
    row = 4,
    column = 0,
    pady = (30,20)
)
styleYellowAlert_Stardate_Label.grid(
    row = 4,
    column = 1,
    pady = (30,20)
)


########################
# STYLES FOR RED ALERT #
########################
redAlertBanner = ImageTk.PhotoImage(lcarsRedAlertBanner)

# Styles for label ('Alert: Condition Red')
styleRedAlert_AlertConditionRed_Label = Label(
                frameStyleRedAlert, 
                font = (lcarsFont, 70),
                background = lcarsBackground,
                foreground = lcarsRedAlertColor
            )

styleRedAlert_AlertConditionRed_LabelText = 'Alert: Condition Red'
styleRedAlert_AlertConditionRed_Label.config(
    text = styleRedAlert_AlertConditionRed_LabelText.upper()
)

styleRedAlert_AlertMessage_Label = Label(
                frameStyleRedAlert, 
                font = (lcarsFont, 70),
                wraplength = 700,
                background = lcarsBackground,
                foreground = lcarsAlertSecondaryColor
            )

styleRedAlert_AlertMessage_LabelText = 'Message text for condition red alert'
styleRedAlert_AlertMessage_Label.config(
    text = styleRedAlert_AlertMessage_LabelText.upper()
)

# Styles for time
styleRedAlert_Time_Label = Label(
                frameStyleRedAlert, 
                font = (lcarsFont, 70),
                background = lcarsBackground,
                foreground = lcarsRedAlertColor
            )

# Styles for the 'star' date
styleRedAlert_Stardate_Label = Label(
                frameStyleRedAlert, 
                font = (lcarsFont, 70),
                background = lcarsBackground,
                foreground = lcarsRedAlertColor
            )

styleRedAlert_BannerTop = Label(
    frameStyleRedAlert,
    image = redAlertBanner,
    background = lcarsBackground
)

styleRedAlert_BannerBottom = Label(
    frameStyleRedAlert,
    image = redAlertBanner,
    background = lcarsBackground
)
    
######################
# GRID FOR RED ALERT #
######################

# Placing text at the center
styleRedAlert_AlertConditionRed_Label.grid(
    row = 0,
    column = 0,
    columnspan = 2,
    pady = (30,20)
)
styleRedAlert_BannerTop.grid(
    row = 1,
    column = 0,
    columnspan = 2
)
styleRedAlert_AlertMessage_Label.grid(
    row = 2,
    column = 0,
    columnspan = 2,
    pady = (30,20)
)
styleRedAlert_BannerBottom.grid(
    row = 3,
    column = 0,
    columnspan = 2
)
styleRedAlert_Time_Label.grid(
    row = 4,
    column = 0,
    pady = (30,20)
)
styleRedAlert_Stardate_Label.grid(
    row = 4,
    column = 1,
    pady = (30,20)
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

    styleYellowAlert_Time_LabelText = timeNow['numeric']
    styleYellowAlert_Time_Label.config(
        text = styleYellowAlert_Time_LabelText
    )

    styleYellowAlert_Stardate_LabelText = dateNow
    styleYellowAlert_Stardate_Label.config(
        text = styleYellowAlert_Stardate_LabelText
    )

    styleRedAlert_Time_LabelText = timeNow['numeric']
    styleRedAlert_Time_Label.config(
        text = styleRedAlert_Time_LabelText
    )

    styleRedAlert_Stardate_LabelText = dateNow
    styleRedAlert_Stardate_Label.config(
        text = styleRedAlert_Stardate_LabelText
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
        
