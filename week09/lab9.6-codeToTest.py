# This program containsthe code to test that the function will return a ValueError if 
# a number is less than 0 is passed in
# Author: Sarah McNelis

try:
    Fibonacci(-1)
except ValueError:
    # want this exception to be thrown
    # this is an eg of where we want to do nothing 
    pass
else:
    # if the exception was not thrown we should throw assertion error
    assert False, 'fibonacci missing ValueError'
    #or can use raise
    # raise AssertionError("fibonacci no ValueError")