#simple concept hard to guess, take time given 1:59, when we add 30 minutes we know it will be 2:29 but computer will give 1:89 but if we sub 60 and add 1 hour for each 60 minutes we are done!
def add_time(start, duration, day=None):
    modifiers_later = 0
    days_later = 0
    weekDays = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
        ]
    modifier = start.split(" ")[1]
    initial_modifier = modifier
    start = start.split(" ")
    start.pop(1)
    start = ''.join(start)
    hour = int(start.split(":")[0]) + int(duration.split(":")[0])
    minute = int(start.split(":")[1]) + int(duration.split(":")[1])
    if minute > 59:
        minute -= 60
        hour += 1
    hour_modifier = hour
    while hour > 12:
        hour -= 12
    while hour_modifier > 11:
        hour_modifier -= 12
        modifier = "PM" if modifier == "AM" else "AM"
        modifiers_later += 1
    if modifiers_later % 2 != 0:
        if initial_modifier == "PM":
            modifiers_later += 1
        else:
            modifiers_later -= 1
    days_later = modifiers_later/2
    new_time = f"{hour}:{str(minute).zfill(2)} {modifier}"
    if day:
        weekday = weekDays.index(day.title())
        weekday_new = int((weekday + days_later) % 7)
        new_time += f", {weekDays[weekday_new]}"
    if days_later == 1:
        new_time += " (next day)"
    if days_later > 1:
        new_time += f" ({int(days_later)} days later)"
    return new_time
