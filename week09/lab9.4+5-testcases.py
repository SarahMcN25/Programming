# This program contains test cases that test that function called with the parmeters 7,11,0 and 1
# all return the correct values
# Author: Sarah McNelis

if __name__ == '__main__':
    return7 = [0,1,2,3,4,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
    assert Fibonacci(7) == return7, 'incorrect return for 7'
    assert Fibonacci(11) == return11, 'incorrect return for 11'
    assert Fibonacci(0) == [], 'incorrect return value for 0'
    assert Fibonacci(1) == [0], 'incorrect return value for 1'
    print("all good")

# will return error becasue body of function not written yet