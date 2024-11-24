#!/usr/bin/env python3
# Student ID: jsingh1101

def function1():
    """Demonstrates local scope in function1."""
    a = 'object_function1'
    print('print() in function1 on a:', a)

def function2():
    """Demonstrates local scope in function2."""
    a = 'function2_object'
    print('print() in function2 on a:', a)

# Main program demonstrating global scope
a = 'object_in_main'
print('print() in main on a:', a)
function1()
print('print() in main on a:', a)
function2()
print('print() in main on a:', a)

