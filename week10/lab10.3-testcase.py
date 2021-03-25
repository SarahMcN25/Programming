# This program continues from lab 10.2
# and creates a test case for this class that created an instance and prints it out
# Author: Sarah McNelis

import datetime as dt 

#class code here
class Timesheetentry:

    def __init__(self, project, start, duration): #always start with self parameter
        self.project = project
        self.start = start
        self.duration = duration

    def __str__(self):
        return self.project + ':' + str(self.duration)

#test case
if __name__ == '__main__':
    ts = dt.datetime(2021,3,19,16,20)
    test = Timesheetentry('test', ts, 60)
    print(test)