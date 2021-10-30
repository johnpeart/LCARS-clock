from settings import messages
import time

def checkMessages():

    # This function should check the settings > message file for any significant birthdays.
    # If a birthday is found, it should return the person's name, birthday, and age.

    first_date = "30/11/2020"
    second_date = "12/10/2019"

    formatted_date1 = time.strptime(first_date, "%d/%m/%Y")
    formatted_date2 = time.strptime(second_date, "%d/%m/%Y")
    print(formatted_date1 > formatted_date2)

    alertType = 'red'
    messageText = 'This is a yellow alert message'

    return {'alert': alertType, 'message': messageText}