

import datetime
from random import randint


def getReplacementsV(h: int = None, m: int = None):
    rSmall = randint(1, 15)
    rSmall2 = randint(1, 4)
    rInt = randint(255234, 999999 - rSmall)
    rInt2 = randint(41800, 99999 - rSmall)
    rTimeHours = randint(9,11)
    rTimeMinutes = randint(0,40)
    d = datetime.datetime.today()
    date = str(d.day).zfill(2)+'.'+str(d.month).zfill(2)+'.'+str(d.year)
    #time = str(d.hours).zfill(2) + ':' + str(d.minute).zfill(2)
    if(h is not None):
        time = str(h).zfill(2) + ':' + str(m).zfill(2)
        timeMinutesPlus = rTimeMinutes + 15
        timePlus = str(h).zfill(2) + ':' + str(m+15+rSmall2).zfill(2)
    else:
        time = str(rTimeHours).zfill(2) + ':' + str(rTimeMinutes).zfill(2)
        timeMinutesPlus = rTimeMinutes + 15
        timePlus = str(rTimeHours).zfill(2) + ':' + str(timeMinutesPlus + rSmall2).zfill(2)
    V = { 
        'Y77002287319': 'Y77002' + str(rInt),
        'Y77002287335': 'Y77002' + str(rInt + rSmall),
        '05.02.2022' : date,
        '13:36' : time,
        '13:37' : time,
        '13:53' : timePlus,
        '58041449' : '580' + str(rInt2),
        '58041469' : '580' + str(rInt2+rSmall)
        }
    return V

