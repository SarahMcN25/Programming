# this program reads in modules
# keeps reading in modules until user enters module name of blank
# Author: Sarah McNelis

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit):").strip()
    
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit):").strip()
        return modules


students = []

def doAdd (students):
    currentStudent = {}
    currentStudent["name"] = input ("enter name:")
    currentStudent["modules"] = readModules()

    students.append(currentStudent)
    
#test
doAdd(students)

doAdd(students)
print(students)
  