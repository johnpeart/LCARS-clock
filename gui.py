from tkinter import *
from PIL import ImageTk, Image  

import windowManagement as wm
import window_root as appRoot
import window_settings as appSettings
import window_numeric as appNumeric
import window_wordclock as appWordclock
import window_yellowalert as appYellowAlert
import window_redalert as appRedAlert
import labels as labels
import clock as clock
import alerts as alerts
from settings import options, defaults
import system as system

host = system.getHostIP()

####################################################
# CREATE THE APP ROOT WINDOW AND TOP LEVEL WINDOWs #
####################################################

app = wm.app(defaults['appName'])
frameAppRoot = wm.container(app)

windowSettings = wm.window('Operations')
frameSettings = wm.container(windowSettings)

windowNumeric = wm.window('Numeric clock')
frameNumeric = wm.container(windowNumeric)

windowWordClock = wm.window('Word clock')
frameWordClock = wm.container(windowWordClock)

windowYellowAlert = wm.window('Alert: Condition Yellow')
frameYellowAlert = wm.container(windowYellowAlert)

windowRedAlert = wm.window('Alert: Condition Red')
frameRedAlert = wm.container(windowRedAlert)

windows = [windowSettings, windowNumeric, windowWordClock, windowYellowAlert, windowRedAlert]

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

numeric_Time_Label, numeric_Date_Label = appNumeric.format(frameNumeric)
wordclock_Time_Label = appWordclock.format(frameWordClock)

yellowAlert_Message_Label, yellowAlert_Time_Label, yellowAlert_Date_Label = appYellowAlert.format(frameYellowAlert, yellowAlertBanner)
redAlert_Message_Label, redAlert_Time_Label, redAlert_Date_Label = appRedAlert.format(frameRedAlert, redAlertBanner)


def updateDisplay():

    timeNow = clock.formatTime()
    dateNow = clock.formatDate()
    alertsNow = alerts.checkMessages()

    labels.update(numeric_Time_Label, timeNow['numeric'])
    labels.update(numeric_Date_Label, dateNow)
    labels.update(wordclock_Time_Label, timeNow['words'])
    labels.update(yellowAlert_Message_Label, alertsNow['message'])
    labels.update(yellowAlert_Time_Label, timeNow['numeric'])
    labels.update(yellowAlert_Date_Label, dateNow)
    labels.update(redAlert_Message_Label, alertsNow['message'])
    labels.update(redAlert_Time_Label, timeNow['numeric'])
    labels.update(redAlert_Date_Label, dateNow)

    wm.showWindow(time = timeNow['numeric'], alert = alertsNow['alert'], win = windows)

    app.after(
        options['refreshTime'], 
        updateDisplay
    )
        
