from time import strftime

def formatTime():

    # This will format the time as HHMM
    # i.e. 0900
    numericTime = strftime('%H%M')
    wordTime = militaryTimeWords(strftime('%H'), strftime('%M'))

    return {'numeric': numericTime, 'words': wordTime}

def formatDate():
    # This will format the date as YYYY.MM.DD
    # i.e. 2021.12.31
    dateNow = strftime('%Y.%m.%d')

    return dateNow

def militaryHoursWords(hour):

    hour = int(hour)

    if hour == 0:
        wordHour = 'zero'
    elif hour == 1:
        wordHour = 'zero-one'
    elif hour ==  2:
        wordHour = 'zero-two'
    elif hour == 3:
        wordHour = 'zero-three'
    elif hour == 4:
        wordHour = 'zero-four'
    elif hour == 5:
        wordHour = 'zero-five'
    elif hour == 6:
        wordHour = 'zero-six'
    elif hour == 7:
        wordHour = 'zero-seven'
    elif hour == 8:
        wordHour = 'zero-eight'
    elif hour == 9:
        wordHour = 'zero-nine'
    elif hour == 10:
        wordHour = 'ten'
    elif hour == 11:
        wordHour = 'eleven'
    elif hour == 12:
        wordHour = 'twelve'
    elif hour == 13:
        wordHour = 'thirteen'
    elif hour == 14:
        wordHour = 'fourteen'
    elif hour == 15:
        wordHour = 'fifteen'
    elif hour == 16:
        wordHour = 'sixteen'
    elif hour == 17:
        wordHour = 'seventeen'
    elif hour == 18:
        wordHour = 'eighteen'
    elif hour == 19:
        wordHour = 'nineteen'
    elif hour == 20:
        wordHour = 'twenty'
    elif hour == 21:
        wordHour = 'twenty-one'
    elif hour == 22:
        wordHour = 'twenty-two'
    elif hour == 23:
        wordHour = 'twenty-three'
    else:
        wordHour = 'zero'

    return wordHour

def militaryMinutesWords(minute):

    minute = int(minute)

    if minute >= 0 and minute <= 2:
        wordMinute = 'hundred'
    elif minute >= 3 and minute <= 6:
        wordMinute = 'zero-five'
    elif minute >= 7 and minute <= 12:
        wordMinute = 'ten'
    elif minute >= 13 and minute <= 16:
        wordMinute = 'fifteen'
    elif minute >= 17 and minute <= 22:
        wordMinute = 'twenty'
    elif minute >= 23 and minute <= 26:
        wordMinute = 'twenty-five'
    elif minute >= 27 and minute <= 32:
        wordMinute = 'thirty'
    elif minute >= 33 and minute <= 36:
        wordMinute = 'thirty-five'
    elif minute >= 37 and minute <= 42:
        wordMinute = 'forty'
    elif minute >= 43 and minute <= 46:
        wordMinute = 'forty-five'
    elif minute >= 47 and minute <= 52:
        wordMinute = 'fifty'
    elif minute >= 53 and minute <= 56:
        wordMinute = 'fifty-five'
    elif minute >= 57 and minute <= 60:
        wordMinute = 'hundred'
    else:
        wordMinute = 'hundred'

    return wordMinute

def militaryTimeWords(hour, minute):

    wordTime = militaryHoursWords(hour) + ' ' + militaryMinutesWords(minute) + ' hours'

    return wordTime