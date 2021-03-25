# This program adds another function to lab 10.7
# this function will return the total minutes of all the timesheetenterys
# Author: Sarah McNelis

import datetime as dt 
from timesheetentry import *

class Employee:
    timesheets = []
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __str__(self):
        return self.first + ' ' + self.last

    def logminutes(self, project, minutes):
        now = dt.datetime.now
        timesheetentry = Timesheetentry(project, now, minutes)
        self.timesheets.append(timesheetentry)
    
    def gettotaltime(self):
        total_minutes = 0
        for ts in self.timesheets:
            total_minutes += ts.duration
        return total_minutes

if __name__ == '__main__':
    test = Employee('some', 'one')
    print(test)
    assert ('some one' == str(test))