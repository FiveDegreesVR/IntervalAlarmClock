import time
from tkinter import *
from tkinter.ttk import *
import datetime
import platform

try:
    import winsound  # windows
except:
    import os  # other

hour = 0
min = 0
interval = 0
intervalAmount = 0
presentTime = datetime.datetime.now()


def ask_for_hour():
    hour = input("What hour? (ex:0-23)")
    return hour


def ask_for_min():
    min = input("What min? (ex: 0-59)")
    return min


def ask_for_interval():
    interval = input("How many intervals? (ex: 1-10)")
    return interval


def ask_for_intervalAmount():
    intervalAmount = input("Interval length in min? (ex: 1-10)")
    return intervalAmount


def checkTime(hour, min, interval, intervalAmount):
    intervalIncrease = 0

    localHour = hour
    localMin = min
    localInterval = interval
    localIntervalAmount = int(intervalAmount)

    for x in range(int(localInterval)):
        print(localHour + ":" + str((int(localMin)+intervalIncrease)))
        print(x)

        if (int(localMin) + 5 >= 60):
            localMin = (int(localMin) + 5) - 60
            localHour = localHour + 1

            if (localHour >= 24):
                localHour = 00

        if presentTime.hour.__str__() == localHour.__str__() \
                and presentTime.minute.__str__() == (int(localMin) + intervalIncrease).__str__():
            print("Alarm!")
            return
        else:
            print("No Alarm!")

        intervalIncrease += int(localIntervalAmount)

print(datetime.datetime.now().time())

hour = ask_for_hour()
min = ask_for_min()
interval = ask_for_interval()
intervalAmount = ask_for_intervalAmount()

starttime = time.time()
while True:
    print("Here!")
    presentTime = datetime.datetime.now()
    checkTime(hour, min, interval, intervalAmount)

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
