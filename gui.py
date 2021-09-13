from tkinter import *
from PIL import ImageTk, Image  

import windowManagement as new
import window_root as appRoot
import window_settings as appSettings
import window_numeric as appNumeric
import window_wordclock as appWordclock
import window_yellowalert as appYellowAlert
import window_redalert as appRedAlert
import labels as labels
import clock as clock
from settings import options, defaults
import system as system

host = system.getHostIP()

####################################################
# CREATE THE APP ROOT WINDOW AND TOP LEVEL WINDOWs #
####################################################

app = new.app(defaults['appName'])
frameAppRoot = new.container(app)

windowSettings = new.window('Operations')
frameSettings = new.container(windowSettings)

windowStyleNumeric = new.window('Numeric clock')
frameStyleNumeric = new.container(windowStyleNumeric)

windowStyleWordClock = new.window('Word clock')
frameStyleWordClock = new.container(windowStyleWordClock)

windowStyleYellowAlert = new.window('Alert: Condition Yellow')
frameStyleYellowAlert = new.container(windowStyleYellowAlert)

windowStyleRedAlert = new.window('Alert: Condition Red')
frameStyleRedAlert = new.container(windowStyleRedAlert)

########################################################
# STYLES FOR THE APP ROOT WINDOW AND TOP LEVEL WINDOWS #
########################################################

lcarsDefaultBanner = Image.open(defaults['horizontalRule_Default'])
lcarsYellowAlertBanner = Image.open(defaults['horizontalRule_YellowAlert'])
lcarsRedAlertBanner = Image.open(defaults['horizontalRule_RedAlert'])
defaultBanner = ImageTk.PhotoImage(lcarsDefaultBanner)
yellowAlertBanner = ImageTk.PhotoImage(lcarsYellowAlertBanner)
redAlertBanner = ImageTk.PhotoImage(lcarsRedAlertBanner)

root_Hostname_Label, root_HostIP_Label = appRoot.format(frameAppRoot, defaultBanner, host)
settings_Hostname_Label, settings_HostIP_Label, settings_ClockStyle_Label = appSettings.format(frameSettings, defaultBanner, host)

numeric_Time_Label, numeric_Date_Label = appNumeric.format(frameStyleNumeric)
wordclock_Time_Label = appWordclock.format(frameStyleWordClock)

yellowAlert_Message_Label, yellowAlert_Time_Label, yellowAlert_Date_Label = appYellowAlert.format(frameStyleYellowAlert, yellowAlertBanner)
redAlert_Message_Label, redAlert_Time_Label, redAlert_Date_Label = appRedAlert.format(frameStyleRedAlert, redAlertBanner)


def updateDisplay():

    timeNow = clock.formatTime()
    dateNow = clock.formatDate()

    labels.update(numeric_Time_Label, timeNow['numeric'])
    labels.update(numeric_Date_Label, dateNow)
    labels.update(wordclock_Time_Label, timeNow['words'])
    labels.update(yellowAlert_Message_Label, 'The Time is ' + timeNow['words'])
    labels.update(yellowAlert_Time_Label, timeNow['numeric'])
    labels.update(yellowAlert_Date_Label, dateNow)
    labels.update(redAlert_Message_Label, 'The Time is ' + timeNow['words'])
    labels.update(redAlert_Time_Label, timeNow['numeric'])
    labels.update(redAlert_Date_Label, dateNow)

    app.after(
        options['refreshTime'], 
        updateDisplay
    )
        
