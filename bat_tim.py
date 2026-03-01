#!/usr/bin/env python3

import os 
tm =  str(os.popen("upower -i /org/freedesktop/UPower/devices/battery_BAT0").read()).split()

if "charging" in tm:
    str = "inf"

else:

    num = float(tm[65])

    if num > 6:
        form = " m"
    else:
        form = " h"

    str = str(num) + form

if __name__ == "__main__":
    output = {
        "text": str,
        "class":"batt_time"
            }
    print(str)
