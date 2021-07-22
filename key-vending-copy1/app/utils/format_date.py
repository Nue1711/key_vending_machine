#!/usr/bin/python
from utils.write_log import writeExceptionToFile
from datetime import datetime as dt
from datetime import datetime
import time
import arrow
import moment
import math

def formatDisplayDate(date, formatDate = "yyyy-mm-dd"):
    """ Format display date ui

        Attributes:
            date: string date (yyyy-mm-dd)
            formatDate: pattern format date, default dd-mm-yyyy
        
        Return: string date following format date
    """
    try:
        if date == None:
            return None
        if formatDate == "mm-dd-yyyy":
            return date[3:5] + "-" + date[0:2] + "-" + date[6:10]
        elif formatDate == "yyyy-mm-dd II:MM: p":
            d = datetime.strptime(date[0:16],"%Y-%m-%dT%H:%M")
            return str(d.strftime("%d-%m-%Y ")) + str(ampmFormat(date[11:16]))
        else:
            return date[8:10] + "-" + date[5:7] + "-" + date[0:4]
    except Exception:
        writeExceptionToFile()

def formatDatePassport(date):
    """ Format display date ui

        Attributes:
            date: string date (yymmdd)
        
        Return: string date following dd-mm-yyyy format
    """
    try:
        if int(date[0:2]) <= 30:
            return date[4:6] + "-" + date[2:4] + "-20" + date[0:2]
        else:
            return date[4:6] + "-" + date[2:4] + "-19" + date[0:2]  
    except Exception:
        writeExceptionToFile()

def utc2local(utc):
    """ Convert time utc to time local
        Attributes:
            date: string date (yymmdd)
        
        Return: string date following dd-mm-yyyy format
    """
    try:
        if utc == '':
            return None
        else:
            time_tuple = arrow.get(utc)
            epoch = time.mktime(time_tuple.timetuple())
            offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
            return str(time_tuple + offset)
    except Exception:
        writeExceptionToFile()

def ampmFormat(hhmmss):
    """
        This method converts time in 24h format to 12h format
        Example:   "00:32" is "12:32 AM"
                "13:33" is "01:33 PM"
    """
    ampm = hhmmss.split (":")
    if (len(ampm) == 0) or (len(ampm) > 3):
        return hhmmss

    # is AM? from [00:00, 12:00]
    hour = int(ampm[0]) % 24
    isam = (hour >= 0) and (hour < 12)

    # 00:32 should be 12:32 AM not 00:32
    if isam:
        ampm[0] = ('12' if (hour == 0) else "%02d" % (hour))
    else:
        ampm[0] = ('12' if (hour == 12) else "%02d" % (hour-12))

    return ':'.join (ampm) + (' AM' if isam else ' PM')

def epochSecond2Date(epoch):
    date = moment.unix(epoch, utc=False)
    # return date.strftime("%d-%m-%Y %I:%m %p")
    return date.strftime("%d-%m-%Y")

def getCurrentEpoch():
    epoch = time.time()
    return math.floor(epoch)