# This program contains a class for an employee
# Author: Sarah McNelis

import datetime as dt 
from timesheetentry import *

#class here
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

#test here
if __name__ == '__main__':
    test = Employee('some', 'one')
    print(test)
    assert ('some one' == str(test))
    test.logminutes('pl', 30)
    test.logminutes('pl', 60)
    mins = test.gettotaltime()
    print(mins)
    assert (mins == 90)

    print ('all good')