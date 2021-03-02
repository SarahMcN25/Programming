# this program creates functions on how to view displayMenuProg
# Author: Sarah McNelis

def displayModules(modules):
    print ("\tName  \tGrade")
    for module in modules:
        print("\t{}q\t{}".format(module["name"], module["grade"]))

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);