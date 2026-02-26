# Battery-time-waybar
A simple battery time indicator for waybar

The steps are the same as for the screen time widget for waybar
# 1 Add the way_tim.py file to your waybar directory

# 2 Add this to the config file

```
"custom/batt_tim":{
        "exec":"$HOME/.config/waybar/way_tim.py",
        "interval":30

    }
```

# 3 Add  "custom/batt_tim" to wichever module you want

*restart might be necessary*
