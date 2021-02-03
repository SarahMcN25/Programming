# This program inputs a person's height in cm and weight in kg
# Then outputs their bmi (weight divided by height) in meters squared.

weight = int(input("Enter weight(kg):"))
#print ('weight') to check code is working

height = int(input("Enter height(cm):"))
#print ('height') to check code is working

newHeight = int((height/100)*2)
#print (newHeight) This converts height from cm to m squared
# *** PROBLEM HERE TO FIX - not giving answer including decimal place. Gives answer as 3. Should be 3.6

bmi = weight/newHeight
#print (bmi) to check calculations are working

print ("BMI is: {}".format(bmi))
