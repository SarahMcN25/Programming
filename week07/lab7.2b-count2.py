# this program takes in a number and overwrites a file with that number
# Author: Sarah McNelis

filename = "count.txt"

def writeNumber(number):
    with open (filename, "wt") as f:
        f.write(str(number)) # write takes a string so we need to convert

writeNumber(3)