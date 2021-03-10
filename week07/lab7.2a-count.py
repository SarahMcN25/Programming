# this program counts how many times a txt file was run using a function
# Author: Sarah McNelis

filename = "count.txt"

def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

num = readNumber()
print (num)