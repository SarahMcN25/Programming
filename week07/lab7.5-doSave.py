# this program uses functions to which allow the user to create, view and save students
# Author: Sarah McNelis
students = []

def displayMenu():
    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("type one letter a/v/s/q):").strip()
    return choice

def doAdd (students):
    currentStudent = {}
    currentStudent["name"] = input ("enter name:")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)
    print("in adding")

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])
        print("in viewing")

def doSave(students):
    print("in save")

# main program
students = []
choice = displayMenu()
while (choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice != 'q':
        print ("\n\nplease select either a, v or q")
    choice = displayMenu()
