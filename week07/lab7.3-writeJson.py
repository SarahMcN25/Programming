# this program uses a function that will store a simple dict to a file as json
# Author: Sarah McNelis

# json has two functions
# 1- dump(obj,fp) which writes a dict or list to a file
# 2- load(fp) which loads a data structure(dict or list) from a file

import json 
filename = "testdict.json"
sample = dict(name='fred', age=31, grades=[1, 34, 55])

def writeDict(obj):
    with open (filename, 'wt') as f:
        json.dump(obj, f) #dumps to selected file

writeDict(sample) #test the function