

import datetime
from random import randint


def getReplacementsV():
    rInt = randint(255234, 999999)
    rInt2 = randint(41800, 99999)
    rTimeHours = randint(9,11)
    rTimeMinutes = randint(0,44)
    d = datetime.datetime.today()
    date = str(d.day).zfill(2)+'.'+str(d.month).zfill(2)+'.'+str(d.year)
    #time = str(d.hours).zfill(2) + ':' + str(d.minute).zfill(2)
    time = str(rTimeHours).zfill(2) + ':' + str(rTimeMinutes).zfill(2)
    timeMinutesPlus = rTimeMinutes + 15
    timePlus = str(rTimeHours).zfill(2) + ':' + str(timeMinutesPlus).zfill(2)
    V = { 
        'Y77002287319': 'Y77002' + str(rInt),
        '05.02.2022' : date,
        '13:36' : time,
        '13:53' : timePlus,
        '58041449' : '580' + str(rInt2)
        }
    
    return V