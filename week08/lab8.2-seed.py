# this ensures that the random salaries are the same set of random numbers each time the program is run
# Author: Sarah McNelis

import numpy as np 

# set absolute values into variables at the beginning of prog - better practice
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # this keeps the random numbers the same each time prog is run
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)