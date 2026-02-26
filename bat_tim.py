#!/usr/bin/env python3

import os 
tm =  str(os.popen("upower -i /org/freedesktop/UPower/devices/battery_BAT0").read()).split()
str = tm[65] + " h"

if __name__ == "__main__":
    output = {
        "text": str,
        "class":"batt_time"
            }
    print(str)
