# This program contains the code for the fibonacci function
# Author: Sarah McNelis

import logging
logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    a = 0
    b = 1
    fibonacciSequence = [0]
    # have one in the list already so no -1 times 
    for i in range(1, number):
        fibonacciSequence.apend(b)
        a, b = b, a+b 

    logging.debug("%d: %s", number, fibonacciSequence)