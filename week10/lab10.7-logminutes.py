# This program adds a function to lab10.6
# this function will create a timesheetentry with the project and mins and the time 
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

if __name__ == '__main__':
    test = Employee('some', 'one')
    print(test)
    assert ('some one' == str(test))