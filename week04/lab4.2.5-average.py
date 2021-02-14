# this program reads in numbers until user enters a 0
# it will print them back out again 
# and their average
# Author: Sarah McNelis

numbers = []

number = int(input("enter number (0 to quit):"))

while number != 0:
    numbers.append(number) #stores number to list
    number = int(input("enter another (0 to quit):"))

for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers) # want average to be a float hense float not int
print ("The average is", average)