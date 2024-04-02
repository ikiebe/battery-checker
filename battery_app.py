import psutil

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


battery = psutil.sensors_battery()
percent = battery.percent
time = convertTime(battery.secsleft)

print(percent)

if(battery.power_plugged == True):
    print("Your battery is charging")
else:
    print("Your battery isn't charging")

print(f"You have {time}% left")

