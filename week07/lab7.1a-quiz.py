# Q1: assuming the file doesn't exist what will happen when the program runs?
# Answer: can't open file 'lab7.1-quiz.py': [Errno 2] No such file or directory
# default mode is r for read and therefore cannot read a file that doesn't exist
# Author: Sarah McNelis

with open ("test-a.txt") as f:
    data = f.read()
    print (data)
