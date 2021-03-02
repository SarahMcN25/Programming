# this program shows variables can be of type function which can be called variables
# Author: Sarah McNelis

def fun1():
    print("this is fun1")

def fun2():
    print("this is fun2")

whichFun = fun1
whichFun()
whichFun =fun2
whichFun()

# means list, tuples and dicts can have variables of type function in them