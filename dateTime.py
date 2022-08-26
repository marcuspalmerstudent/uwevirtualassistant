#Aurthor Marcus Palmer
#Date: 2022
#UWE Disertation

#! /usr/bin/python3
#import these files libraries and modules
from datetime import datetime, timedelta
from pytz import timezone
import pytz
from datetime import date
import calendar
from botConfig import botTimeZone

#for use with config file set time
def getTime():
    now = datetime.now(pytz.timezone(botTimeZone))
    #now = datetime.utcnow()
    myTimeZone = " GMT"
    mm = str(now.month)
    dd = str(now.day)
    yyyy = str(now.year)
    hour = str(now.hour)
    minute = str(now.minute)
    if now.minute < 10:
        minute = '0' + str(now.minute)
    second = str(now.second)
    mydate = date.today()
    if now.hour >= 12:
        ampm = ' PM'
    else:
        ampm = ' AM'
    if now.hour > 12:
        hour = str(now.hour - 12)
    weekday = calendar.day_name[mydate.weekday()]
    return "The time is now " + hour + ":" + minute + ampm + myTimeZone

#Using config file set date
def getDate():
    now = datetime.now(pytz.timezone(botTimeZone))
    mm = str(now.month)
    dd = str(now.day)
    yyyy = str(now.year)
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    weekday = now.weekday()
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    weekdayName = week[weekday]
    return "Today is " + weekdayName + ", " + mm + "/" + dd + "/" + yyyy

print("Hello there!")
print(getTime())
print(getDate())
