def add_time(start, duration, weekday = "none"):
    
    # split change to integer
    time = start.split(":")
    delta = duration.split(":")
    hour = time[0]
    string_minute = time[1]
    day = "day"
    
    list_minute = string_minute.split()
    num_minute = list_minute[0]
    day_time = list_minute[1]

    # calculate hour and minute
    new_minute = int(num_minute) + int(delta[1])
    new_houre = int(hour) + int(delta[0])
    
    # test minute > 60
    if new_minute > 60:
        new_houre += (new_minute // 60)
        new_minute = (new_minute % 60)
        
    days = new_houre // 24
    halfdays = new_houre // 12
    new_houre = new_houre % 12
    
    if new_houre == 0:
        new_houre = 12
        
    if halfdays % 2 == 1:
        if day_time == "AM":
            day_time = "PM"
        elif day_time == "PM":
            day_time = "AM"
            days += 1
            
    if days == 0:
        new_time = str(new_houre) + ":" + str(new_minute).zfill(2) + " " + day_time
    elif days == 1:
        new_time = str(new_houre) + ":" + str(new_minute).zfill(2) + " " + day_time + " " + "(next day)"
    elif days > 1:
        new_time = str(new_houre) + ":" + str(new_minute).zfill(2) + " " + day_time + " (" + str(days) + " days later)"
        
    return new_time
