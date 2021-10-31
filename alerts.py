from settings import messages
from time import strftime, strptime, localtime

def checkMessages():

    # This function should check the settings > message file for any significant birthdays.
    # If a birthday is found, it should return the person's name, birthday, and age.

    now = localtime()

    for alert, info in messages.items():

        dayOfYearAlert = strptime(str(info['day']) + '/' + str(info['month']) + '/' + strftime('%Y'), "%d/%m/%Y") 
        daysToGo = dayOfYearAlert.tm_yday - now.tm_yday
        
        # print(alert + ' ' + str(daysToGo) + ' days to go')
        if daysToGo == 0:
            alertType = 'red'

            # If it's a birthday
            if info['type'] == 'birthday':
                messageText = 'It\'s ' + info['name'] + '\'s ' + info['type'] + ' today'
            # or wedding anniversary
            elif info['type'] == 'wedding anniversary':
                messageText = 'It\'s your ' + info['type'] + ' today'
            else:
                messageText = 'It\'s ' + info['type'] + ' today'

            break

        elif daysToGo == 1:
            alertType = 'red'

            # If it's a birthday
            if info['type'] == 'birthday':
                messageText = 'It\'s ' + info['name'] + '\'s ' + info['type'] + ' tomorrow'
            # or wedding anniversary
            elif info['type'] == 'wedding anniversary':
                messageText = 'It\'s your ' + info['type'] + ' tomorrow'
            else:
                messageText = 'It\'s ' + info['type'] + ' tomorrow'

            break
        
        elif (daysToGo > 1) and (daysToGo < 10):
            alertType = 'yellow'

            # If it's a birthday or wedding anniversary
            if info['type'] == 'birthday':
                messageText = 'It\'s ' + info['name'] + '\'s ' + info['type'] + ' in ' + str(daysToGo) + ' days'
            # or wedding anniversary
            elif info['type'] == 'wedding anniversary':
                messageText = 'It\'s your ' + info['type'] + ' in ' + str(daysToGo) + ' days'
            else:
                messageText = 'It\'s ' + info['type'] + ' in ' + str(daysToGo) + ' days'

            break

        else: 
            alertType = False
            messageText = 'All systems operating within specified parameters'

    return {'alert': alertType, 'message': messageText}