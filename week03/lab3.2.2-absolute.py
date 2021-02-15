# this program takes in a number and gives its absolute value
# Author: Sarah McNelis

number = float(input("Enter a number:"))
# because the number in question is ambiguous it implies that we should be dealing with floats hense float not int

absoluteValue = abs(number)
print ('The absolute value of {} is {}'.format(number, absoluteValue))
