import datetime

format = "%d-%m-%y %H:%M:%S"

currentDate = datetime.datetime.today()

def get_newDate(currentDate):
    newDate = currentDate + datetime.timedelta(days=393,hours=4,minutes=23,seconds=32)
    newDate = newDate.strftime(format)
    print("The current date is:\n",currentDate.strftime(format))
    print("\nThe after date is  :")
    return newDate

print(get_newDate(currentDate))
                                            
