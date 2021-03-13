# this program uses a function to read in a dict object from a file
# Author: Sarah McNelis

import json
filename = "testdict.json"

def readDict():
    # this will throw an error if the file does not exist
    # it should just return an empty dict
    with open(filename) as f:
        return json.load(f)

somedict = readDict() #test the function
print (somedict)