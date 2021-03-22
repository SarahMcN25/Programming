# This program adds more code to actualcode.py
# This mades sure to throw an error if used enters 0 or a value less than 0
# Author: Sarah McNelis

def fibonacci(number):
    if number < 0: #throws error if ValueError is less than 0
        raise ValueError('number must be > 0')
    if number == 0: # throws error if user enters 0
        return []
    a = 0 
    b = 1
    fibonacciSequence = [0]
        fibonacciSequence.append(b)
        a , b = b, a + b
    logging.debug("%d :%s", number, fibonacciSequence)