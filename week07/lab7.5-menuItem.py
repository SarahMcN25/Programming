# this program uses functions to which allow the user to create, view and save students
# Author: Sarah McNelis

def displayMenu():

    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("type one letter (a/v/s/q):").strip()

    return choice

def doAdd():
    # you have code here to add
    print("in adding")
def doView():
    # you have code here to view
    print("in viewing")
def doSave():
    print("in save")

#main program
choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice == 's':
        doSave()
    elif choice !='q':
        print("\n\nPlease select either a,v,s or q")
    choice=displayMenu()
