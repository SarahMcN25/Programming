# this program takes in a float and outputs an int(rounded up or down)
# note it rounds to nearest number (eg 4.5 rounds to 4, 5.5 rounds to 6)
# Author: Sarah McNelis

numberToRound = float(input("Enter a float number:"))
roundedNumber = round(numberToRound)
print ('{} rounded is {}'.format(numberToRound, roundedNumber))