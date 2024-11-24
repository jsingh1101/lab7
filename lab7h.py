#!/usr/bin/env python3

# Global variable
schoolName = "Seneca College"

def function1():
    """Demonstrate global variable access."""
    global schoolName
    print("print() in function1 on schoolName:", schoolName)

def function2():
    """Demonstrate global variable access."""
    global schoolName
    print("print() in function2 on schoolName:", schoolName)

if __name__ == "__main__":
    print("print() in main on schoolName:", schoolName)
    function1()
    print("print() in main on schoolName:", schoolName)
    function2()
    print("print() in main on schoolName:", schoolName)

print("Debug: Attempting to load module 'lab7h'")

