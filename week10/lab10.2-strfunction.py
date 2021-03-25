# This program continues from lab 10.1
# and creates a __str__ function that returns the project and duration
# Author: Sarah McNelis

class Timesheetentry:

    def __init__(self, project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration

    def __str__(self):
        return self.project + ':' + str(self.duration)

