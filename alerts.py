from settings import messages

def checkMessages():

    # This function should check the settings > message file for any significant birthdays.
    # If a birthday is found, it should return the person's name, birthday, and age.

    alertToShow = True
    alertType = 'yellow'
    messageText = 'This is a yellow alert message'

    return {'alert': alertToShow, 'alertType': alertType, 'message': messageText}