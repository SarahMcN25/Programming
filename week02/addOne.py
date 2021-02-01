# This program reads in a number and prints out one more than that number
# Author: Sarah McNelis

number = int(input("please enter a number:"))
newNumber = number + 1
print('{} plus one is {}'.format(number, newNumber))
# It thought number was a string which is why I needed to put int before my code