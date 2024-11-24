#!/usr/bin/env python3

from lab7a import *

t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
tsum = sum_times(t1, t2)

print("Time 1:", format_time(t1))
print("Time 2:", format_time(t2))
print("Summed Time:", format_time(tsum))

