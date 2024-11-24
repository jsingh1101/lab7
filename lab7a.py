#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
    Data attributes: hour, minute, second.
    """
    def __init__(self, hour=12, minute=0, second=0):
        if not isinstance(hour, int) or not isinstance(minute, int) or not isinstance(second, int):
            raise TypeError("hour, minute, and second must all be integers")
        self.hour = hour
        self.minute = minute
        self.second = second

def sum_times(t1, t2):
    """Adds two Time objects and returns a new Time object."""
    total_seconds = t1.second + t2.second
    total_minutes = t1.minute + t2.minute + total_seconds // 60
    total_hours = t1.hour + t2.hour + total_minutes // 60

    return Time(total_hours % 24, total_minutes % 60, total_seconds % 60)

def format_time(t):
    """Formats a Time object as HH:MM:SS."""
    return f"{t.hour:02}:{t.minute:02}:{t.second:02}"

def valid_time(t):
    """Validates a Time object."""
    return (0 <= t.hour < 24) and (0 <= t.minute < 60) and (0 <= t.second < 60)

if __name__ == "__main__":
    t1 = Time(9, 45, 30)
    t2 = Time(2, 20, 40)
    t3 = sum_times(t1, t2)

    print("Time 1:", format_time(t1))  # Expected: 09:45:30
    print("Time 2:", format_time(t2))  # Expected: 02:20:40
    print("Summed Time:", format_time(t3))  # Expected: 12:06:10
    print("Is Time 1 valid?", valid_time(t1))  # Expected: True
    print("Is Time 2 valid?", valid_time(t2))  # Expected: True

