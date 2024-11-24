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

    def format_time(self):
        """Return time object as a formatted string."""
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def sum_times(self, t2):
        """Add two time objects and return their sum."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Modify a time object by adding or subtracting seconds."""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    def time_to_sec(self):
        """Convert a time object to seconds since midnight."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check if the time object attributes are valid."""
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def __add__(self, other):
        """Overload the + operator to sum two Time objects."""
        if not isinstance(other, Time):
            raise TypeError("Operands must be Time objects")
        return self.sum_times(other)

def sec_to_time(seconds):
    """Convert a number of seconds to a time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

