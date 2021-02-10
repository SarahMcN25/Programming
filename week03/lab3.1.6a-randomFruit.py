# this program prints out a random fruit
# author: Sarah McNelis

import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear']
index = random.randint(0, len(fruits)-1) #creates random number between 0 and lenght -1

fruit = fruits[index]
print("A Random Fruit: {}".format(fruit))
