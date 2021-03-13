# this program makes the user create the file before they run the program
# Author: Sarah McNelis

import os.path
filename = "count.txt"
if not os.path.isfile(filename): #this function checks if the file exists
    print ("File does not exist")
    writeNumber(0)
# basically if the file doesn't exist print or else write the number 0 to the file
