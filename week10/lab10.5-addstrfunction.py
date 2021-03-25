# This program adds a str function that returns the full name
# Author: Sarah McNelis

class Employee:
    timesheets = []
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __str__(self):
        return self.first + ' ' + self.last