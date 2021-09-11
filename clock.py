from tkinter import *
from time import strftime

import militarytime as milTime

# Variables
lcarsBackground = 'black'
lcarsLabelColor = '#FFCC99'
lcarsTimeColor = '#FF9900'
lcarsStardateColor = '#FFCC99'
lcarsFont = 'Context Ultra Condensed SSi'

# Create tkinter window
app = Tk()

# Window size and settings
app.title('LCARS Clock')
app.geometry('720x720')
# app.attributes('-fullscreen', True)
app.config(
    background = lcarsBackground
)

# Container
frame = Frame(
    app,
    background = lcarsBackground
)

frame.pack(expand=True)

def displayClock():
    # Styles for time
    timeLabel = Label(
                    frame, 
                    font = (lcarsFont, 340),
                    background = lcarsBackground,
                    foreground = lcarsTimeColor
                )

    # Styles for the 'star' date
    stardateLabel = Label(
                    frame, 
                    font = (lcarsFont, 140),
                    background = lcarsBackground,
                    foreground = lcarsStardateColor
                )

    # Placing clock at the center
    timeLabel.grid(
        row = 0,
        column = 0
    )
    stardateLabel.grid(
        row = 1,
        column = 0
    )

    lcarsTime = strftime('%H%M')
    timeLabel.config(
        text = lcarsTime
    )

    lcarsStarDate = strftime('%Y.%m.%d')
    stardateLabel.config(
        text = lcarsStarDate
    )

    app.after(
        60000, 
        updateDisplay
    )

def displayWordClock():
    # Styles for label
    theTimeIsLabel = Label(
                    frame, 
                    font = (lcarsFont, 100),
                    background = lcarsBackground,
                    foreground = lcarsLabelColor
                )

    # Styles for time
    timeLabel = Label(
                    frame, 
                    font = (lcarsFont, 100),
                    background = lcarsBackground,
                    foreground = lcarsTimeColor
                )

    # Placing clock at the center
    theTimeIsLabel.grid(
        row = 0,
        column = 0
    )
    timeLabel.grid(
        row = 1,
        column = 0
    )
    
    lcarsLabel = 'THE TIME IS'
    theTimeIsLabel.config(
        text = lcarsLabel
    )

    lcarsTime = milTime.militaryTime(strftime('%H'), strftime('%M'))
    timeLabel.config(
        text = lcarsTime.upper(),
        wraplength = 720
    )

    app.after(
        12000, 
        updateDisplay
    )

# This function is used to display time on the label
def updateDisplay(displayType):

    if displayType == 'clock':
        displayClock()
        

    if displayType == 'wordclock':
        displayWordClock()
        
