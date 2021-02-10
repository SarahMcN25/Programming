# this program reads in two numbers, divides the first by the second 
# and gives the int result and remainder.
# author: Sarah McNelis

x = int(input("Enter first number:"))
y = int(input("Enter the number you want to divide by:"))
answer = int(x//y)
remainder = x%y 

print ("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))
