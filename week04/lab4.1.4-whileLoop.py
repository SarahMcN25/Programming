# this program asks the user to input a number 
# continues to prompt user until user enters -1
# Author: Sarah McNelis

number = -1
guessNumber = int(input("Please enter a number:"))

while guessNumber != number:
    print ("wrong number! Hint -1 to quit") 
    guessNumber = int(input("Please enter a number:"))
    # this will keep looping until answer is false then it will run else
else:
    print ("Yes the number is {}".format(number))
