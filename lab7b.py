#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
    Data attributes: hour, minute, second.
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object."""
        if not isinstance(hour, int) or not isinstance(minute, int) or not isinstance(second, int):
            raise TypeError("hour, minute, and second must all be integers")
        self.hour = hour
        self.minute = minute
        self.second = second


def format_time(time):
    """Return time object (time) as a formatted string."""
    return f"{time.hour:02}:{time.minute:02}:{time.second:02}"

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    # Handle overflow
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

def valid_time(time):
    """Check for the validity of the time object attributes."""
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def change_time(time, seconds):
    """Modify a time object by adding or subtracting seconds."""
    time.second += seconds
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1
    return None

if __name__ == "__main__":
    t1 = Time(9, 45, 30)
    t2 = Time(2, 20, 40)
    tsum = sum_times(t1, t2)

    print("Time 1:", format_time(t1))
    print("Time 2:", format_time(t2))
    print("Summed Time:", format_time(tsum))
    print("Is Time 1 valid?", valid_time(t1))
    print("Is Time 2 valid?", valid_time(t2))
    change_time(t1, 3600)  # Add 1 hour to t1
    print("Changed Time 1:", format_time(t1))

