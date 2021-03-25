# This program creates a class that has 3 attributes 
# which are all set using the __init__ function
# Author: Sarah McNelis

class Timesheetentry:
    def __init__(self, project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration