# this program uses function doAdd to read in a students:
# name, module name, grades
# Author: Sarah McNelis

students = []

def readModules():
    return []

def doAdd (students):
    currentStudent = {}
    currentStudent["name"] = input ("enter name:")
    currentStudent["modules"] = readModules()

    students.append(currentStudent)
    
#test
doAdd(students)

doAdd(students)
print(students)