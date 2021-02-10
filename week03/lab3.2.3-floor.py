# this program takes in a float and output an int rounded down
# need to use math module math.floor()
# author: Sarah McNelis

import math

numberToFloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberToFloor)
print('{} floored is {}'.format(numberToFloor, flooredNumber))
