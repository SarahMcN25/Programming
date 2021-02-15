# this program taakes in a float amount of dollars
# then returns that absolute amount in cent
# Author: Sarah McNelis

money = float(input("Please enter an amount:"))

absoluteValue = abs(money) 
#this gets the absolute value

centMoney = int(absoluteValue * 100)
# this converts the absoluteValue into cent

print ("That amount in cent is: {}".format(centMoney))