
for tijd in range(1, 25):
    if tijd <= 12:
        if tijd == 12:
            print(tijd, "PM")
        else:
            print(tijd, "AM")
    else:
        if tijd == 24:
            print(tijd - 12, "AM")
        else:
            print(tijd - 12, "PM")

