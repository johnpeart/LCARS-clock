from tkinter import *
from PIL import ImageTk, Image  

import windowManagement as new
import window_root as appRoot
import window_settings as appSettings
import clock as clock
from settings import options, defaults
import system as system

host = system.getHostIP()

# Windows
app = new.app(defaults['appName'])
frameAppRoot = new.container(app)

windowSettings = new.window('Operations')
frameSettings = new.container(windowSettings)

windowStyleClock = new.window('Numeric clock')
frameStyleClock = new.container(windowStyleClock)

windowStyleWordClock = new.window('Word clock')
frameStyleWordClock = new.container(windowStyleWordClock)

windowStyleYellowAlert = new.window('Alert: Condition Yellow')
frameStyleYellowAlert = new.container(windowStyleYellowAlert)

windowStyleRedAlert = new.window('Alert: Condition Red')
frameStyleRedAlert = new.container(windowStyleRedAlert)

######################################################
# STYLES FOR THE APP ROOT WINDOW AND SETTINGS WINDOW #
######################################################
lcarsDefaultBanner = Image.open(defaults['horizontalRule_Default'])
defaultBanner = ImageTk.PhotoImage(lcarsDefaultBanner)

appRoot.format(frameAppRoot, defaultBanner, host)
appSettings.format(frameSettings, defaultBanner, host)

################################
# STYLES FOR THE NUMERIC CLOCK #
################################
# Styles for time
styleClock_Time_Label = Label(
                frameStyleClock, 
                font = (defaults['fontFace'], 340),
                background = defaults['windowBackground'],
                foreground = defaults['textColor_Time']
            )

# Styles for the 'star' date
styleClock_Stardate_Label = Label(
                frameStyleClock, 
                font = (defaults['fontFace'], 140),
                background = defaults['windowBackground'],
                foreground = defaults['textColor_Date']
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
                font = (defaults['fontFace'], 100),
                background = defaults['windowBackground'],
                foreground = defaults['textColor_Label']
            )

styleWordClock_TheTimeIs_LabelText = 'The time is'
styleWordClock_TheTimeIs_Label.config(
    text = styleWordClock_TheTimeIs_LabelText.upper()
)

# Styles for time
styleWordClock_Time_Label = Label(
                frameStyleWordClock, 
                font = (defaults['fontFace'], 100),
                background = defaults['windowBackground'],
                foreground = defaults['textColor_Time']
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
lcarsYellowAlertBanner = Image.open(defaults['horizontalRule_YellowAlert'])
yellowAlertBanner = ImageTk.PhotoImage(lcarsYellowAlertBanner)

# Styles for label ('Alert: Condition Yellow')
styleYellowAlert_AlertConditionYellow_Label = Label(
                frameStyleYellowAlert, 
                font = (defaults['fontFace'], 70),
                background = defaults['windowBackground'],
                foreground = defaults['textColor_YellowAlert'],
                text = 'Alert: Condition Yellow'.upper()
            )

styleYellowAlert_AlertMessage_Label = Label(
                frameStyleYellowAlert, 
                font = (defaults['fontFace'], 70),
                wraplength = 700,
                background = defaults['windowBackground'],
                foreground = defaults['textColor_AlertSecondary']
            )

styleYellowAlert_AlertMessage_LabelText = 'Message text for condition yellow alert'
styleYellowAlert_AlertMessage_Label.config(
    text = styleYellowAlert_AlertMessage_LabelText.upper()
)

# Styles for time
styleYellowAlert_Time_Label = Label(
                frameStyleYellowAlert, 
                font = (defaults['fontFace'], 70),
                background = defaults['windowBackground'],
                foreground = defaults['textColor_YellowAlert']
            )

# Styles for the 'star' date
styleYellowAlert_Stardate_Label = Label(
                frameStyleYellowAlert, 
                font = (defaults['fontFace'], 70),
                background = defaults['windowBackground'],
                foreground = defaults['textColor_YellowAlert']
            )

styleYellowAlert_BannerTop = Label(
    frameStyleYellowAlert,
    image = yellowAlertBanner,
    background = defaults['windowBackground']
)
styleYellowAlert_BannerBottom = Label(
    frameStyleYellowAlert,
    image = yellowAlertBanner,
    background = defaults['windowBackground']
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
lcarsRedAlertBanner = Image.open(defaults['horizontalRule_RedAlert'])
redAlertBanner = ImageTk.PhotoImage(lcarsRedAlertBanner)

# Styles for label ('Alert: Condition Red')
styleRedAlert_AlertConditionRed_Label = Label(
                frameStyleRedAlert, 
                font = (defaults['fontFace'], 70),
                background = defaults['windowBackground'],
                foreground = defaults['textColor_RedAlert']
            )

styleRedAlert_AlertConditionRed_LabelText = 'Alert: Condition Red'
styleRedAlert_AlertConditionRed_Label.config(
    text = styleRedAlert_AlertConditionRed_LabelText.upper()
)

styleRedAlert_AlertMessage_Label = Label(
                frameStyleRedAlert, 
                font = (defaults['fontFace'], 70),
                wraplength = 700,
                background = defaults['windowBackground'],
                foreground = defaults['textColor_AlertSecondary']
            )

styleRedAlert_AlertMessage_LabelText = 'Message text for condition red alert'
styleRedAlert_AlertMessage_Label.config(
    text = styleRedAlert_AlertMessage_LabelText.upper()
)

# Styles for time
styleRedAlert_Time_Label = Label(
                frameStyleRedAlert, 
                font = (defaults['fontFace'], 70),
                background = defaults['windowBackground'],
                foreground = defaults['textColor_RedAlert']
            )

# Styles for the 'star' date
styleRedAlert_Stardate_Label = Label(
                frameStyleRedAlert, 
                font = (defaults['fontFace'], 70),
                background = defaults['windowBackground'],
                foreground = defaults['textColor_RedAlert']
            )

styleRedAlert_BannerTop = Label(
    frameStyleRedAlert,
    image = redAlertBanner,
    background = defaults['windowBackground']
)

styleRedAlert_BannerBottom = Label(
    frameStyleRedAlert,
    image = redAlertBanner,
    background = defaults['windowBackground']
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

    clock.updateLabel(styleClock_Time_Label, timeNow['numeric'])
    clock.updateLabel(styleClock_Stardate_Label, dateNow)
    clock.updateLabel(styleWordClock_Time_Label, timeNow['words'])
    clock.updateLabel(styleYellowAlert_Time_Label, timeNow['numeric'])
    clock.updateLabel(styleYellowAlert_Stardate_Label, dateNow)
    clock.updateLabel(styleRedAlert_Time_Label, timeNow['numeric'])
    clock.updateLabel(styleRedAlert_Stardate_Label, dateNow)

# This function is used to display time on the label
def updateDisplay():

    # determines what to show
    # sets up what the display will show
    updateClock()

    app.after(
        options['refreshTime'], 
        updateDisplay
    )
        
