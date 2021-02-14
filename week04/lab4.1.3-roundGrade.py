# this program reads in a students percentage mark 
# then prints out corresponding grade rounded 
# Author: Sarah McNelis

import math

percentage = float(input("Enter the percentage:"))
# print (percentage)

if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100") # checks if valid percentage
elif percentage < 39.5:
    print ("Fail")
elif percentage < 49.5:
    print ("Pass")
elif percentage < 59.5: 
    print ("Merit 2") 
elif percentage < 69.5:
    print ("Merit 1")
else:
    print ("Distinction")