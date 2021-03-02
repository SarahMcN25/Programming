# this program puts 10 random numbers in a list
# then outputs all values in the queue
# then prints each value one at a time while printing remainder of list
# Author: Sarah McNelis

import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(0,numberOfNumbers): # setting queue to 10 numbers
    queue.append(random.randint(0, rangeTo))
# using random.mandint to select random numbers from 0 to 100
# using append to add to queue
    
print ("queue is {}".format(queue))

while len(queue) !=0:
    currentNumber = queue.pop(0)
    print ("current Number is {} and the queue is {}".format(currentNumber, queue))
# when lenght of queue is not 0 then it will continue to print the above statement
print ("the queue is now empty")