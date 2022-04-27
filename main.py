# Name: Gavin Heilers
# Date: 4/27/22
# Project: Countdown
# file: countdownTimer --> main.py
# -------------------------------------------------------------- #
import time
usertimeNon = input('Please enter the time in seconds:\n')
usertime = int(usertimeNon)
"""The timer countdown function is used to import the userTime parameter. This will allow it to take the seconds and translate it to a timer to allow the user to countdown. """
def timeCountDown(usertime) : # defintes a function that uses the parameter of the variable of the user input.
    while usertime :
        min, secs = divmod(usertime, 60)# For god's sake, Mrs. Adami, fix your typos! 'Divemode' is not a thing!
        timer = '{:02d} : {:02d}'.format(min, secs)
        print('\r',timer, end='',)
        time.sleep(1)
        usertime -= 1
    print('\n Timer Completed')
timeCountDown(int(usertime))
