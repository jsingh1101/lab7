#!/usr/bin/env python3
# Student ID: jsingh1101

def function1():
    global schoolName  # Access and modify global variable
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName  # Modify global variable
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

# Global variable
schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)

