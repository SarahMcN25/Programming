# This program creates a class that has one attribute
# and an init function that takes in a first and last name
# Author: Sarah McNelis

class Employee:
    timesheets = []
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        