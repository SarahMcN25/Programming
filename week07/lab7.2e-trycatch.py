# using try catch loop on the read
# Author: Sarah McNelis

def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        # this file will be created when we writebakc
        # no file assumes first time running
        # ie 0 previous runs
        return 0